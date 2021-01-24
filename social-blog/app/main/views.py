from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session['name']
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['SBLOG_ADMIN']:
                    send_email(current_app.config['SBLOG_ADMIN'], 'New User',
                                'mail/new_user', user=user)
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                            known=session.get('known', False),
                            current_time=datetime.utcnow())