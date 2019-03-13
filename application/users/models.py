from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

def __init__(self, username, password):
    self.username = username
    self.password = password
