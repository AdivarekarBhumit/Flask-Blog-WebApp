from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def index():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)