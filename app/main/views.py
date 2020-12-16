from flask import render_template
from . import main
# Views
@main.route('/')
def footer():
    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('footer.html')