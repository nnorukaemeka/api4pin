#import library and modules
from flask import render_template, request, flash, url_for, redirect, session
from app import app, db, api
from app.models import PinGenerator
from flask_restful import Resource, Api
from sqlalchemy import exc
from sqlalchemy.exc import IntegrityError
import uuid


#UUID function that generate random codes
def random_pin(length):
    stringLength = length
    randomString = str(uuid.uuid4().int) # get a random string in a UUID fromat
    randomString  = randomString[0:stringLength] # trim to stringLength.
    return randomString


#api route for generating and returning pin and s/n
class Generate(Resource):
    def get(self):
        epin = random_pin(15)   #generate a random uuid 15 digits
        new_pin = PinGenerator(pin = epin) #post to table
        db.session.add(new_pin) #add to database
        db.session.commit() #commit to database
        record = PinGenerator.query.filter_by(pin=epin).first()
        return {"pin": record.pin, "s/n": record.serial_no}, 200
api.add_resource(Generate, '/generate')  


#api route for validating pin and s/n
class ValidateSn(Resource):
    def get(self,sn):
        #get pin from user, and convert to string
        eserial = str(sn) 
        #check if  serial_no exist in the database
        checkpin = PinGenerator.query.filter_by(serial_no=eserial).first() 
        # return 1 if valid else, return 0  
        return {"message":"1"} if checkpin, else return {"message":"0"} 
api.add_resource(ValidatePin, '/validate/sn/<string:sn>')


# class ValidateSn(Resource):
#     def get(self,sn):
#         #get serial_no  from user, and convert to string
#         eserial = str(sn)
#         #check if serial_no  exist in the database
#         chkpin = PinGenerator.query.filter_by(serial_no=eserial).first()
#         if chkpin: # if it exists, return 1 connoting valid
#             return {"message":"1"},200
#         else: # if it doesn't exist, return 0 connoting invalid
#             return {"message":"0"}, 200

# api.add_resource(ValidateSn, '/validate/sn/<string:sn>')


# #api route for returning all data in database
# class AllPin(Resource):
#     def get(self):
#         database1 = []
#         records = db.session.query(PinGenerator).all()
#         for record in records:
#             recordObject = {"pin": record.pin,
#                     "s/n": record.serial_no}
#             database1.append(recordObject)
        
#         return {'Records': database1}, 200

# api.add_resource(AllPin, '/database')


#api route for the homepage
class Home(Resource):
    def get(self):
        return {
            'message': '''Welcome, my name is Emeka Nnoruka. The purpose of this project is to build two(2) API. This first endpoint [/generate] returns a pin and a serial_no(s/n). The second endpoint [/validate/pin/...  or /validate/sn/...] validates pin or s/n when posted by returning [1] as VALID or [0] as NOT VALID. I added additional endpoint [/database] for accessing the whole data in the database. Feel free to consume the APIs.'''}
api.add_resource(Home, '/')