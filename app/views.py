from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Arun Kumar'} #fake user
    posts = [ #fake array of posts
                {
                    'author': {'nickname': 'Arun'},
                    'body'  : 'Beautiful day today!'
                },
                {
                    'author': {'nickname': 'Anna'},
                    'body'  : 'The Avengers movie was so cool!'
                }
            ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
