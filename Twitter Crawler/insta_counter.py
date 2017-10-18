from time import sleep  
from instagram.client import InstagramAPI


access_token="407414984.e5af07d.825e02a23338476eac59d44958c1f4e0"
client_secret="30dc27f2fa2d4bad8a2dc316ded545a1"

api = InstagramAPI(access_token=access_token,  
                    client_secret=client_secret)
recent_media, url = api.tag_recent_media(tag_name="coding", count=5) # 1

for media in recent_media:  
    # Where the media is
    id_ = media.id
    # List of users that like the image
    users = [user.username for user in media.likes]
    # If you have already like the picture, do nothing
    if "YOUR USERNAME" in users:
        print("IN PHOTO")

    # If you haven't liked the photo then do it
    else:
        print("LIKING PICTURE")
        api.like_media(media_id=id_)

    # Sleep to make instagram stop complaining
    sleep(2)