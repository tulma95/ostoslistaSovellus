from application import db
from sqlalchemy.sql import text
from application.products.models import Product

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
    products = db.relationship('Product',
                               backref='grp',
                               lazy=True)
    users = db.relationship('User',
                            secondary=group_users,
                            backref=db.backref('groupUsers',
                                               lazy='dynamic'))

    def __init__(self, name, groupCreator):
        self.name = name
        self.groupCreator = groupCreator

    def get_id(self):
        return self.id

    @staticmethod
    def delete_group(groupId):
        stmt = text('''
        DELETE FROM group_users WHERE group_id = :groupId;'''
                    ).params(groupId=groupId)
        res = db.engine.execute(stmt)
        Group.query.filter_by(id=groupId).delete()
        Product.query.filter_by(groupid=groupId).delete()
        db.session().commit()

    @staticmethod
    def find_users_not_in_group(groupId):
        stmt = text('''
            SELECT * FROM account WHERE account.id 
            NOT IN(SELECT account.id 
            FROM account 
            JOIN group_users ON account.id = group_users.account_id
            JOIN grp ON group_users.group_id = grp.id
            WHERE grp.id = :groupId)
            ''').params(groupId=groupId)

        res = db.engine.execute(stmt)
        usersNotInGroup = []
        for row in res:
            usersNotInGroup.append(row)
        return usersNotInGroup

    @staticmethod
    def find_user_groups_and_item_count(userId):
        stmt = text('''
            SELECT grp.id AS id, grp.name AS name, 
            (SELECT COUNT(id) FROM product 
            WHERE product.groupId = grp.id) 
            AS groupitemcount 
            FROM grp
            LEFT JOIN product on product.id = grp.id
            JOIN group_users ON grp.id = group_users.group_id
	    	JOIN account ON account.id = group_users.account_id
            WHERE account.Id = :userId
            ''').params(userId=userId)
        res = db.engine.execute(stmt)
        groups = []
        for row in res:
            groups.append(row)
        return groups
