"""
Link Handler Utility Class
Manages authentic redirect links for WeChat articles, Xiaohongshu profile, and studio resources
"""

from typing import Dict, Optional


class LinkHandler:
    """Handles all external link redirects for GFU Nail website."""
    
    # Authentic links provided by user
    XIAOHONGSHU_PROFILE: str = "https://www.xiaohongshu.com/user/profile/6178fcfc000000001f03e6ef"
    WECHAT_ARTICLE_1: str = "https://mp.weixin.qq.com/s/YEMatSm_00WPCWdT9l2Gig"
    WECHAT_ARTICLE_2: Optional[str] = None  # Awaiting user-provided second article link
    
    @staticmethod
    def get_xiaohongshu_profile() -> str:
        """
        Returns URL to Xiaohongshu account profile.
        
        Returns:
            str: Xiaohongshu profile URL with English label "Follow us on Xiaohongshu"
        """
        return LinkHandler.XIAOHONGSHU_PROFILE
    
    @staticmethod
    def get_wechat_article(article_id: str = "1") -> str:
        """
        Returns URL to specified WeChat article.
        
        Args:
            article_id: Article identifier ("1" or "2")
            
        Returns:
            str: WeChat article URL with English description "Read our service updates"
        """
        if article_id == "1":
            return LinkHandler.WECHAT_ARTICLE_1
        elif article_id == "2" and LinkHandler.WECHAT_ARTICLE_2:
            return LinkHandler.WECHAT_ARTICLE_2
        else:
            return LinkHandler.WECHAT_ARTICLE_1
    
    @staticmethod
    def get_studio_poster() -> str:
        """
        Returns URL to offline studio poster.
        
        Returns:
            str: Studio poster image URL with English caption
        """
        # Return static path - will be resolved in templates using url_for
        return '/static/images/studio/poster.jpg'
    
    @staticmethod
    def get_all_links() -> Dict[str, str]:
        """
        Returns dictionary of all available links.
        
        Returns:
            Dict[str, str]: Dictionary mapping link types to URLs
        """
        links = {
            "xiaohongshu": LinkHandler.get_xiaohongshu_profile(),
            "wechat_article_1": LinkHandler.get_wechat_article("1"),
        }
        
        if LinkHandler.WECHAT_ARTICLE_2:
            links["wechat_article_2"] = LinkHandler.get_wechat_article("2")
        
        return links

