from application import db


class User(db.Model):
    __tablename__ = "account"
    id = db.Column(db.integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=false)
    username = db.Column(db.String(144), nullable=false)
    password = db.Column(db.String(144), nullable=false)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def getId(self):
        return self.id

     def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
