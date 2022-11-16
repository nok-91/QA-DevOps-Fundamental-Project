from application import db
from application.models import Category, Task

db.drop_all()
db.create_all()


# for cat in ['Education','Lifestyle','Work']:
#     category = Category(category_title=cat)
#     db.session.add(category)
#     db.session.commit()


# # print some stuff from the db
# for i in db.session.query(Category):
#     print(i.category_id, i.category_title)