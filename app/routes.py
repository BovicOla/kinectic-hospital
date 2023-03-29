
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db
from app.forms import RecordForm, RegistrationForm

from app.models import User


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = RecordForm()
    if form.validate_on_submit():
        user = User.query.get(int(form.card_no.data))
        if user is None:
            flash('Invalid Record Number')
        else:
            return render_template('landingPage.html', title='Sign In',
                                   form=form, patient=user)
    return render_template('landingPage.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        kw = {}
        if (_gender := form.gender.data) != 'null':
            kw['gender'] = _gender
        if (_employment := form.employment.data) != 'null':
            kw['employment'] = _employment
        user = User(
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            phone_number=form.phone_number.data,
            address=form.address.data,
            age=form.age.data,
            **kw
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user')
        return redirect(url_for('index'))
    return render_template('registrationpage.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
