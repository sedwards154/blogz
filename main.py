from flask import Flask, request, redirect, render_template

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://build-a-blog:seji1995@localhost:8889/build-a-blog'

app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)




class Blog(db.Model):



	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(120))

	body = db.Column(db.String(120))

	

	def __init__(self, name, body):

		self.name = name

		self.body = body

		

	def is_valid(self):

		if self.name and self.body:

			return True

		else:

			return False





@app.route('/', methods=['POST', 'GET'])

def index():


	

	posts = Blog.query.all()

	

	return render_template('main.html',title="Blog Posts", posts=posts)



			

@app.route('/blog', methods=['POST', 'GET'])

def new():

	if request.method == "GET":

		return render_template('newpost.html', title="Create A New Post")



@app.route('/newpost', methods=['POST','GET'])

def new_post():

	if request.method == "POST":

		new_blog_title = request.form['post-title']

		new_blog_body = request.form['message']

		if len(new_blog_title) <= 0 or len(new_blog_body) <= 0:

			return render_template('newpost.html', title="Create a New Post", error="Please fill out all fields")

		else:

			new_blog = Blog(new_blog_title, new_blog_body)

			db.session.add(new_blog)

			db.session.commit()

			return redirect('/single?id={0}'.format(new_blog.id))

		

@app.route('/single', methods=['POST', 'GET'])

def single():

	

	post_id = request.args.get('id')

	

	if post_id:

		post = Blog.query.get(post_id)

		return render_template('blog.html', title=str(post.name), post=post)

	

	





if __name__ == '__main__':
    
    app. run ()