# api4pin API(Heroku deployment)

This is a project that renders two endpoints for generating PIN & S/N, and also to validate the PIN & S/N when supplied.


## Starting the application
In order to run the application set the environment
variable below.
```
Windows
set FLASK_APP=run.py

Unix
export FLASK_APP=run.py
```
Then run the command below to start the application.
```
flask run
```

## API Documentation

The api documentation is hosted as the homepage
of the application.
The purpose of this project is to build two(2) API. 
This first endpoint ["/generate"] will return a PIN and a SERIAL_NO, while the second endpoint ["/validate"] will request for SERIAL_NO and PIN and validate if they are VALID [1] or NOT [0].
Feel free to consume the APIs.
