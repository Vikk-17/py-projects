from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/blog/<int:id>")
def get_blog(id):
    p = Post(id)
    particular_post = p.get_post()
    return render_template("post.html", post=particular_post)

if __name__ == "__main__":
    app.run(debug=True)
