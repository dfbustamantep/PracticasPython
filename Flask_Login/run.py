from app import creata_app,db
from app.auth.models import User


flask_scrapping_app = creata_app("prod")
with flask_scrapping_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name="test").first():
        User.create_user(
            user="test",
            email="test-testing@test.com",
            password="test**123"
        )
flask_scrapping_app.run() 