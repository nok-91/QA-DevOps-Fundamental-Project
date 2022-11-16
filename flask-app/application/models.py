from application import db

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_title = db.Column(db.String(30), unique=True, nullable=False,)
    task = db.relationship('Task', backref='catbr')

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    