from application import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    groupId = db.Column(db.Integer, db.ForeignKey('grp.id'), nullable=False)


    def __init__(self, name, count, groupId):
        self.name = name
        self.count = count
        self.groupId = groupId
