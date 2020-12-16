from flask import render_template
from . import main
# Views
@main.route('/')
def footer():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('index.html', title = title)

from flask import render_template,request,url_for,redirect,flash,abort
from . import main
from .forms import UpdateProfile
from ..models import User
from flask_login import login_required, current_user
from .. import db, photos
import datetime


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)     

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))                   
