from flask import render_template,request,redirect,url_for
from . import main
from app.models import Products
from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import Products,User
from .forms import UpdateProfile,ProductForm
from .. import db,photos
# from flask_login import login_required, current_user
# Views

@main.route('/')
# @login_required
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('index.html', title = title)

@main.route('/all')
# @login_required
def index2():
    '''
    View root page function that returns the index page and its data
    '''
    products = Products.query.all()
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('products.html', title = title, products=products)

@main.route('/phones')
def phone():
    '''
    View root page function that returns the index page and its data
    '''
    phones = Products.query.filter_by(category=phone).all()
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('phones.html', title = title, phones=phones)

@main.route('/television')
def television():
    '''
    View root page function that returns the index page and its data
    '''
    televisions = Products.query.filter_by(category=television).all()
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('television.html', title = title, televisions=televisions)

@main.route('/watches')
def watch():
    '''
    View root page function that returns the index page and its data
    '''
    watches = Products.query.filter_by(category=twatches).all()
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('watches.html', title = title, watches=watches)

@main.route('/dolls')
def doll():
    '''
    View root page function that returns the index page and its data
    '''
    dolls = Products.query.filter_by(category=dolls).all()
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('dolls.html', title = title, dolls=dolls)

@main.route('/bicycles')
def bicycle():
    '''
    View root page function that returns the index page and its data
    '''
    bicycles = Products.query.filter_by(category=bicycles).all()
    title = 'Home - Jumia online website '
    images = 'img1.jpeg'
    return render_template('bicycles.html', title = title, bicycles=bicycles)






@main.route('/footer')
def footer():
    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html')

@main.route('/about')
def about():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('about.html')
 

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

@main.route('/search/<category_name>')
def search(category_name):
    '''
    View function to display the search results
    '''
    category_list = category.split(" category_name")
    category_format = "+".join(category_list)
    searched_category = search_category(category_format)
    title = f'search results for {category_name}'
    return render_template('search.html', category= searched_category)  


          
@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        description = form.description.data
        price= form.price.data
        category = form.category.data
        image_pic_path = form.image.data
        name = form.name.data
        new_product_object = Product(description=description,name=name,category=category,price=price,image_pic_path=image)
        new_product_object.save_p()
        return redirect(url_for('main.index'))
    return render_template('create_product.html', form = form)          
