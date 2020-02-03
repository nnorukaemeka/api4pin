from app import app, db


class PinGenerator(db.Model):
    """
    Table schema
    """
    __tablename__ = 'pinGenerator'

    pin = db.Column(db.String(15), primary_key=True, nullable=False, autoincrement=False, unique =True)
    serial_no = db.Column(db.String(12), nullable=False, unique =True)

    def __init__(self, pin, serial_no):
        self.pin = pin
        self.serial_no = serial_no

    def __repr__(self):
        return '<title {}'.format(self.serial_no)
