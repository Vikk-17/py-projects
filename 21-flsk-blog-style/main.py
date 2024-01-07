from flask import Flask, render_template
import requests


all_posts = requests.get("https://api.npoint.io/7027b07da924cc1b15de").json()


app = Flask(__name__)


@app.route("/")
def get_all_post():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for post in all_posts:
        if (post["id"] == index):
            requested_post=post
    return render_template("post.html", post=requested_post)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
