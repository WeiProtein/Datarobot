#!/usr/bin/env python

from flask import Flask, render_template, url_for, flash, redirect, request
from create_repo import app
from create_repo.forms import InfoForm
from create_repo.models import User

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    #return render_template('home.html')
    form = InfoForm()
    if form.validate_on_submit():
        flash('Repo has been created for %s!'% ({form.username.data}),'success')
    return render_template('info.html', title='GitHub Info', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

