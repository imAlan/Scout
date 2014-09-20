from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Precinct(db.Model):
    __tablename__ = 'Precinct'
    name = db.Column(db.String(128), primary_key=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(256))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    borough = db.Column(db.String(32))

    def __repr__(self):
        return '<Precinct %r>' % self.name


class PrecinctData(db.Model):
    __tablename__ = 'PrecintData'
    name = db.Column(db.String(128), db.ForeignKey('Precinct.name'), primary_key=True)
    crime = db.Column(db.Enum('Burglary', 'Robbery', 'Forcible rape', 'Grand larceny', 'Grand larceny auto', 'Major felony crime', 'Felonious assault', 'Murder and non-negligent manslaughter'))
    total = db.Column(db.Integer)