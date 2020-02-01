from flask import render_template, request, flash, url_for, redirect, session
from app import app, db, api
from app.models import PinGenerator
from flask_restful import Resource, Api
from sqlalchemy import exc
from sqlalchemy.exc import IntegrityError
import uuid


def random_pin(length):
    stringLength = length
    randomString = str(uuid.uuid4().int) # get a random string in a UUID fromat
    randomString  = randomString[0:stringLength] # trim to stringLength.
    return randomString


class Generate(Resource):
    def get(self):
        try:
            #generate a random uuid 15 digits
            epin = random_pin(15)
            #generate a random uuid 25 digits
            eserial_no = random_pin(25)
            #make an object of the database class
            new_pin = PinGenerator(pin = epin, serial_no = eserial_no)

            #compare the generated digits with database, if any exists, generate again
            if PinGenerator.query.get(epin) or PinGenerator.query.filter_by(serial_no= eserial_no).first():
                db.session.rollback()
                return redirect(url_for('generate'))
            # if they don't exist in db, add to database and return the generated digits
            db.session.add(new_pin)
            db.session.commit()
            return {"pin": epin, "s/n": eserial_no}, 200
        except exc.IntegrityError: #for any other exception, flag error message
            db.session.rollback()
            return {"message": " Oops! try again later"}, 404

api.add_resource(Generate, '/generate')  


class Validate(Resource):
    def post(self):
        #get serial_no and pin from user, and convert to string
        request_data = request.get_json()
        eserial_no = str(request_data["s/n"])
        epin = str(request_data["pin"])
        #check if both serial_no and pin exist in the database
        chkpin = PinGenerator.query.filter_by(pin=epin, serial_no=eserial_no).first()
        if chkpin: # if they exist, return 1 connoting valid
            return {"message":"1"},200
        else: # if they don't exist, return 0 connoting invalid
            return {"message":"0"}, 200

api.add_resource(Validate, '/validate')


class AllPin(Resource):
    def get(self):
        database1 = []
        records = db.session.query(PinGenerator).all()
        for record in records:
            recordObject = {"pin": record.pin,
                    "s/n": record.serial_no}
            database1.append(recordObject)
        
        return {'Records': database1}, 200

api.add_resource(AllPin, '/database')


class Home(Resource):
    def get(self):
        return {
            'message': '''Welcome, my name is Emeka Nnoruka. The purpose of this project is to build two(2) API. This first endpoint [/generate] returns a pin and a serial_no(s/n). The second endpoint [/validate] validates pin and s/n when posted by returning [1] as VALID or [0] as NOT VALID. I added additional endpoint [/database] for accessing the whole data in the database. Feel free to consume the APIs.'''}
api.add_resource(Home, '/')