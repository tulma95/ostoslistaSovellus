from application import db

group_users = db.Table('group_users',
                       db.Column('account_id', db.Integer,
                                 db.ForeignKey('account.id', ondelete='cascade')),
                       db.Column('group_id', db.Integer,
                                 db.ForeignKey('grp.id', ondelete='cascade')))


class Group(db.Model):

    __tablename__ = "grp"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    groupCreator = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='grp', lazy=True)
    users = db.relationship('User',
                            secondary=group_users,
                            backref=db.backref('groupUsers',
                                               lazy='dynamic'))

    def __init__(self, name, groupCreator):
        self.name = name
        self.groupCreator = groupCreator

    def get_id(self):
        return self.id
