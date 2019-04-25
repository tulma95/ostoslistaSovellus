from application import db
from application.groups.models import Group, group_users


class User(db.Model):

    __tablename__ = "account"
    # __table_args__ = (db.UniqueConstraint('username'), )
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    groups = db.relationship('Group',
                             secondary=group_users,
                             backref=db.backref('groupUsers',
                                                lazy='dynamic',
                                                cascade='all,delete-orphan',
                                                single_parent=True))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
