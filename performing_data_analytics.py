"""
Data Analytics
"""

from json import load


class Calculations:
    """
    Methods used to find the calculations.
    """
    def __init__(self):
        f = open("user_data.json")
        data = load(f)
        self.like_list = data["Activity"]["Like List"]["ItemFavoriteList"]
        self.login_history = data["Activity"]["Login History"]["LoginHistoryList"]
        self.share_history = data["Activity"]["Share History"]["ShareHistoryList"]
        self.comments_list = data["Comment"]["Comments"]["CommentsList"]
        self.watch_tiktok_live_history = data["Tiktok Live"]["Watch Live History"]["WatchLiveMap"]
        self.your_videos = data["Video"]["Videos"]["VideoList"]
        
    def count_likes(self):
        return len(self.like_list)
    
    def count_login_history(self):
        return len(self.login_history)
    
    def count_share_history(self):
        return len(self.share_history)
    
    def count_comments(self):
        return len(self.comments_list)
    
    def count_watched_tiktok_live(self):
        return len(self.watch_tiktok_live_history)
    
    def count_your_videos(self):
        return len(self.your_videos)
        

