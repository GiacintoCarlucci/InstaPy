from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

def likeByTags(tags,_username,_password):
    # set workspace folder at desired location (default is at your home folder)
    set_workspace(path="/home/stranger/github/InstaPy/")

    # get an InstaPy session!
    session = InstaPy(username=_username, password=_password,headless_browser=False)

    with smart_run(session):
        # general settings
        session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')

        # activity
        session.like_by_tags(tags,amount=5,interact=True)

