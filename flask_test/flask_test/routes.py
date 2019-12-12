from flask import render_template, url_for, flash, redirect
from flask_test import app, db
from flask_test.forms import ReviewForm



# dummy reviews
reviews = [
    
    {
        'business': 'Pizza Palace',
        'review_id': '1234',
        'content': 'Good, not great.',
        'date_posted': 'April 20, 2018'
    },
    {
        'business': 'Coffee House',
        'review_id': '5412',
        'content': 'The Best!',
        'date_posted': 'June 20, 2018'
    }
    
]


# define route for home page
# posts = posts give access to data within template
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', reviews=reviews)

# define route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# define route for manual review entry
# redirects to homepage (for now) if review entered successfully
@app.route("/review", methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        # add review to sqlite database
        review = ReviewForm(text=form.text.data, rating=form.rating.data)
        db.session.add(review)
        db.session.commit()
        flash(f'Review added to database!', 'success')
        return redirect(url_for('review'))
    return render_template('review.html', title='Write Your Own Review!', form=form)

# define route for businesses page
@app.route("/businesses")
def businesses():
    return render_template('businesses.html', title='Businesses')