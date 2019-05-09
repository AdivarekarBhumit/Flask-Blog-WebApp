from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '55035be74bb85d3b9f5b48a6a26eaf5d'

posts = [
    {
        'author': 'Bhumit',
        'title': 'First Post',
        'content': 'Blah Blah Blah....',
        'date_posted': 'April 16, 2019'
    },
    {
        'author': 'Adivarekar',
        'title': 'Second Post',
        'content': 'Blah Blah Blah....',
        'date_posted': 'April 15, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'abc@gmail.com' and form.password.data == 'abc123':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('LogIn Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)