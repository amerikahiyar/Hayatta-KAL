from app import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    complaint = db.Column(db.Text,nullable=False)
    age= db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.complaint}' '{self.age}')"
