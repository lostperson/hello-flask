# -*- coding:utf-8 -*-
import random

from flask import Flask,render_template,flash,redirect,url_for,session
from flask_wtf import Form
from wtforms import IntegerField, SubmitField 
from wtforms.validators import Required, NumberRange 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session['number'] = random.randint(0,1)
    return render_template('index.html')


@app.route('/guess',methods=['GET','POST'])
def guess():
    result = session.get('number')
    form = GuessNumberForm()
    if form.validate_on_submit():
        answer = form.number.data
        if answer != result:
            flash(u'Sorry')
            return redirect(url_for('.index'))
        else:
            flash(u'Win')
            return redirect(url_for('.index'))
    return render_template('guess.html',form=form)

class GuessNumberForm(Form):
    number = IntegerField(u'enter 0 0r 1:',validators=[
        Required(u'enter a legal number'),
        NumberRange(0,1,u'enter 0 0r 1 (0)')])
    submit = SubmitField(u'push')

if __name__=='__main__':
    app.run(debug=False,host="0.0.0.0")
