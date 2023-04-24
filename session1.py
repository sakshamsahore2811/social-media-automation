from instapy import InstaPy
from instapy.util import smart_run

pages = ['account1', 'account2', 'account3']

# Define your Instagram username and password
username = 'your_username'
password = 'yourpassword'

# Set up a new InstaPy session
session = InstaPy(username=username, password=password)

# Define the actions you want to perform using the smart_run decorator
with smart_run(session):
    # Log in to your Instagram account
    session.login()

    # Loop through each page and follow its followers
    for page in pages:
        session.set_quota_supervisor(enabled=True, peak_likes_hourly=10, peak_likes_daily=50)
        session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True, max_followers=100000, max_following=100000, min_followers=10, min_following=10)
        session.set_skip_users(skip_private=False, skip_no_profile_pic=True, skip_business=False, skip_non_business=False, business_percentage=100)

        # Follow the followers of the page
        session.follow_user_followers([page], amount=50, randomize=True, sleep_delay=600)

    # Log out of your Instagram account
    session.end()
print("Done !")
