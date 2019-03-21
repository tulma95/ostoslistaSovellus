from application import db


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    groupCreator = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='group', lazy=True)

    def __init__(self, name, groupCreator):
        self.name = name
        self.groupCreator = groupCreator

    def get_id(self):
        return self.id
