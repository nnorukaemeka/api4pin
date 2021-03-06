#import library and modules
from flask import render_template, request, flash, url_for, redirect, session
from app import app, db, api
from app.models import PinGenerator
from flask_restful import Resource, Api
from sqlalchemy import exc
from sqlalchemy.exc import IntegrityError

from hashFunc import HashTable, GetKeyValue

hashed = HashTable() #instance of HashTable 
generate = GetKeyValue()    #Instance of GetKeyValue that generates pin and serial no
 



#api route for generating and returning pin and s/n
class Generate(Resource):
    def get(self):
        epin = generate.getValue()   #generate a random uuid 15 digits
        eserial = generate.getKey() #generate a 12 digit serial number
        hashed[eserial] = epin  #store the key-value in the hash table
        return {"pin": epin, "s/n": eserial}, 200
api.add_resource(Generate, '/generate')  


#api route for validating pin and s/n
class ValidateSn(Resource):
    def get(self,sn):
        if (hashed[sn]) == None: #check if serial no is in hash table, 
            return {"message":"0"}  # return 0 if invalid 
        return {"message":"1"} #else, return 1 
api.add_resource(ValidateSn, '/validate/<string:sn>')



#api route for the homepage
class Home(Resource):
    def get(self):
        return {
            'message': '''Welcome, my name is Emeka Nnoruka. The purpose of this project is to build two(2) API. This first endpoint [/generate] returns a pin and a serial_no(s/n). The second endpoint [/validate/<paste s/n>] validates s/n when posted by returning [1] as VALID or [0] as NOT VALID. Feel free to consume the APIs.'''}
api.add_resource(Home, '/')