from instapy import InstaPy

session = InstaPy(username = "your_account", password = "yourpassword")

session.login()
session.like_by_tags(['tag1','tag2','tag3'],amount  =25)
session.end()

print("Liked 25 hashtag related posts")