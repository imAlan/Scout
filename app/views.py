from app import app
from flask import render_template
from forms import scoutForm
from address import AddressParser, Address

@app.route('/', methods=['GET', 'POST'])
def index():
    form = scoutForm()
    if form.validate_on_submit():
        address_input = form.address.data
        ap = AddressParser()
        address = ap.parse_address(address_input)
        print address.house_number
    return render_template('index.html', form=form)

@app.route('/scout')
def scout():
    return render_template('scout.html')