# api4pin API(Heroku deployment)

This is a project that renders two endpoints for generating PIN & S/N, and also to validate the PIN & S/N when supplied.
The project is hosted on Heroku  <a href="https://api4pin.herokuapp.com">here.</a>


## Starting the application
In order to run the application,

* Recreate virtual enviroment:

	 # pip install -r requirements.txt

* Then, set the environment variable below:

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

## API4PIN Documentation

The api documentation is hosted as the homepage
of the application.
The purpose of this project is to build two(2) API. 
This first endpoint [/generate] returns a pin and a serial_no(s/n). The second endpoint [/validate/sn/...] validates pin or s/n when posted by returning [1] as VALID or [0] as NOT VALID.
Feel free to consume the APIs.
