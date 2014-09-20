from app import app
from flask import render_template, redirect, url_for, session
from forms import scoutForm
from address import AddressParser
from models import db
from google_api import get_latlng

@app.route('/', methods=['GET', 'POST'])
def index():
    form = scoutForm()
    if form.validate_on_submit():
        address_input = form.address.data
        ap = AddressParser()
        address = ap.parse_address(address_input)
        lat, lng = get_latlng(address.full_address())
        session['lat'] = lat
        session['lng'] = lng
    return render_template('index.html', form=form)

@app.route('/scout')
def scout():
    return render_template('scout.html')

@app.route('/create')
def create():
    db.drop_all()
    db.create_all()
    return redirect(url_for('index'))

