from application import db
from application.groups.models import Group, group_users
from sqlalchemy.sql import text


class User(db.Model):

    __tablename__ = "account"
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

    @staticmethod
    def remove_user(userId):
        stmt = text('''
        DELETE FROM group_users WHERE account_id = :accountId;'''
                    ).params(accountId=userId)

        res = db.engine.execute(stmt)
        User.query.filter_by(id=userId).delete()
        db.session().commit()
