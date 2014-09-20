from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Precinct(db.Model):
    __tablename__ = 'precints'
    name = db.Column(db.String(64), primary_key=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(256))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    borough = db.Column(db.String(32))

    def __repr__(self):
        return '<Precinct %r>' % self.name

