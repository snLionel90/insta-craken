
import instaloader
import sys

print("sn.lionel90")

def picture_download(username):
    parser = instaloader.Instaloader()
    """Creates a new folder for insta downloads"""
    with settings(warn_only=True):
        run('mkdir /home/InstaDonloads')
        return parser.download_profile(username,profile_pic= True)

if __name__ =="__main__":
    #win_crack.mainloop()
    user = input ("Enter Instagram Account: ")
    picture_download(user)
        
