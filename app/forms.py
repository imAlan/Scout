from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class scoutForm(Form):
    address = StringField('Address:', validators=[InputRequired(message="This field is required")])
    submit = SubmitField('Scout!')