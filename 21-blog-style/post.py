import requests

class Post:
    def __init__(self, id):
        self.blog_id = id
    

    def get_post(self):
        url = "https://api.npoint.io/095a01a3e91429b526c1"
        res = requests.get(url)
        all_posts = res.json()

        for post in all_posts:
            if (post["id"] == self.blog_id):
                return post