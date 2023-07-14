"""
Generate Responses
"""

from performing_data_analytics import Calculations

class GenerateResponse:
    """
    Generate Responses based on calculations
    """
    def __init__(self):
        self.calculate = Calculations()
        
    def total_likes_response(self):
        return f"You liked {self.calculate.count_likes()} vidoes"
        
    def total_login_history_response(self):
        return f"You logged in {self.calculate.login_history()} times"
    
    def total_share_history_response(self):
        return f"You shared {self.calculate.share_history()} vidoes"
    
    def total_comments_response(self):
        return f"You commented {self.calculate.comments_list()} times"
    
    def total_watched_tiktok_live_response(self):
        return f"You watched {self.calculate.watch_tiktok_live_history()} \
            TikTok lives"
    
    def total_vidoes_you_made_response(self):
        return f"You made {self.calculate.count_videos_you_made()} vidoes"

