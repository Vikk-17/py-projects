from flask import Flask, render_template
import requests
from post import Post

# initialize the app
app = Flask(__name__)



@app.route("/")
@app.route("/index.html")
def index():
    url_post = "https://api.npoint.io/095a01a3e91429b526c1"
    res = requests.get(url_post)
    all_posts = res.json()
    return render_template("index.html", posts=all_posts)

# @app.route("/post.html")
# def sample_post():
#     return render_template("post.html")

@app.route("/post.html/<int:id>")
def get_blog(id):
    p = Post(id)
    specific_post = p.get_post()
    return render_template("post.html", post=specific_post)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
