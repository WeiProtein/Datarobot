from create_repo import db
from create_repo.models import User

db.drop_all()
db.create_all()

user_1 = User(username="Wei",password="home")
db.session.add(user_1)
db.session.commit()
print '===DID IT ADD?==='
User.query.all()
