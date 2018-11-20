from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2:build-a-blog2@localhost:8889/build-a-blog2'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    content = db.Column(db.Text)

    def __init__(self, title, author, content):
        self.title=title
        self.author=author
        self.content=content


@app.route('/')
def index():
    if request.method == 'POST':
        title = request.form['title']
        content= request.form['content']
        new_blogpost = Blogpost(title, 'author', content)
        db.session.add(new_blogpost)
        db.session.commit()

    blogposts = Blogpost.query.all()

    return render_template('index.html',title="Jay's Blog", blogposts=blogposts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content= request.form['content']
        new_blogpost = Blogpost(title, 'author', content)
        db.session.add(new_blogpost)
        db.session.commit()

    blogposts = Blogpost.query.all()

    return render_template('index.html',title="Jay's Blog", blogposts=blogposts)
    
    
    


if __name__=='__main__':
    app.run(debug=True)