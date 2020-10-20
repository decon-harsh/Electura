import requests
import secrets
import os,shutil
import json
from flask import render_template,url_for,flash,redirect,request
from WI import app,db,bcrypt,login_manager
from WI.forms import Registration,Login,Login_via_email,suggestion
from WI.models import User,load_user
from flask_login import login_user,current_user,logout_user,login_required




# routes

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=Login()
    if form.validate_on_submit():
        url='http://127.0.0.1:8000/api/v1/users/login_auth/'
        params= {"username":form.username.data,"password":form.password.data}
        r = requests.get(url,params=params).text
        if int(r) !=0:
            user=User.query.filter_by(username=form.username.data).first()
            if user:
                login_user(user,remember=form.remember.data)
                return redirect(url_for('home'))
            else:
                user=User(username=form.username.data)
                db.session.add(user)
                db.session.commit()
                flash(f"Login Unsuccessful.Please check email and Password",'danger')

        else:
            flash(f"You are not authorized!","danger")      
    return render_template('login.html',form=form)




@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=Registration()
    if form.validate_on_submit():
        Session=requests.Session()
        url='http://127.0.0.1:8000/api/v1/users/'
        data= {"username":form.username.data,
               "email":form.email.data,
               "password":form.password.data
               }
        r = Session.post(url,data=data)
        flash(r.status_code)
        if r.status_code == 201:
            return redirect(url_for('login'))
        else:
            flash(f"Username already taken")            
    return render_template("register.html",form=form,title="Registration Page") 



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        flash(f"You have to Login first",'warning')
        return redirect(url_for('login'))