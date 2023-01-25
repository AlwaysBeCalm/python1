from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///user.db"
    db.app = app
    db.init_app(app)
    db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(500))

    def __repr__(self):
        return f"<{self.id}: {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserToken(db.Model):
    user_email = db.Column(db.String(50), primary_key=True)
    token = db.Column(db.String(500))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
