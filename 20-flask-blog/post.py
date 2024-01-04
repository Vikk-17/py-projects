import requests

class Post:
    def __init__(self, blog_id):
        self.id = blog_id

    def get_post(self):
        url = " https://api.npoint.io/c790b4d5cab58020d391"
        res = requests.get(url)
        all_post = res.json()
        for post in all_post:
            if (post["id"] == self.id):
                return post
