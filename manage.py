#import library and modules
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db, models
from app.models import PinGenerator
import os
import forgery_py as faker
from random import randint
from sqlalchemy.exc import IntegrityError

# Initializing the manager
manager = Manager(app)

# Initialize Flask Migrate
migrate = Migrate(app, db)

# Add the flask migrate
manager.add_command('db', MigrateCommand)


# Run the manager
if __name__ == '__main__':
    manager.run()
