from app import app

app.config['SECRET_KEY'] = "unhackathon"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost/scout"