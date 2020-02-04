import uuid

class HashTable:
    #initialize variables
    def __init__(self):
        self.size = 255
        self.hashmap = [[] for _ in range(0, self.size)]
    
    #define hashing Function
    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    #Function that set the key-value into the hash table
    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break
        
        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))
    
    #Function that get the value of a given key from the hash table
    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('does not exist.')

    
    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


#class for generating 12 digit serial number and 15 digit random pin
class GetKeyValue:

    #initialize the variables
    def __init__(self) :
        self.seq = '000000000000'

    #generates the key(serial number)
    def getKey(self) :
        self.seq = '%012d' % (int(self.seq) + 1)
        return self.seq
    
    #UUID function that generate the random value (pin)
    def getValue(self):
        stringLength = 15
        randomString = str(uuid.uuid4().int) # get a random string in a UUID fromat
        randomString  = randomString[0:stringLength] # trim to stringLength.
        return randomString

    def __getvalue__(self):
        return self.getValue()

    def __getkey__(self):
        return self.getKey()

# h = HashTable()

# #get
# h['key1'] = 'value1'
# print(h['key1'])

# h.set('key2', 'value2')
# h.set(20, 'value3')
# h.set('key4', 'value4')


# print(h.get(15))
# print(h.hashmap)