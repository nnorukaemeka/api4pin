from app import app, db


class PinGenerator(db.Model):
    """
    Table schema
    """
    __tablename__ = 'pinGenerator'

    serial_no = db.Column(db.String(length=12, value=000000000000), primary_key=True, nullable=False, autoincrement=True, unique =True)
    pin = db.Column(db.String(length=15), nullable=False, unique =True)

    def __init__(self, pin):
        # self.serial_no = serial_no
        self.pin = pin
        

    def __repr__(self):
        return '<title {}'.format(self.pin)


