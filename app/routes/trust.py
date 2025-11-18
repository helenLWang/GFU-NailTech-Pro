"""
Trust Section Routes
Brand trust, social proof, and authentic link integration
"""

from flask import Blueprint, render_template, jsonify, redirect
from app.utils.link_handler import LinkHandler
from typing import Dict, Any

bp = Blueprint('trust', __name__, url_prefix='/trust')


@bp.route('/')
def trust_section() -> str:
    """Render brand trust section page."""
    links = LinkHandler.get_all_links()
    return render_template('trust.html', links=links)


@bp.route('/xiaohongshu')
def redirect_xiaohongshu() -> redirect:
    """Redirect to Xiaohongshu profile."""
    return redirect(LinkHandler.get_xiaohongshu_profile())


@bp.route('/wechat-article/<article_id>')
def redirect_wechat_article(article_id: str) -> redirect:
    """Redirect to WeChat article."""
    article_url = LinkHandler.get_wechat_article(article_id)
    return redirect(article_url)


@bp.route('/api/links')
def get_trust_links() -> Dict[str, Any]:
    """Get all trust section links."""
    links = LinkHandler.get_all_links()
    return jsonify({
        "links": links,
        "descriptions": {
            "xiaohongshu": "Follow us on Xiaohongshu",
            "wechat_article_1": "Read our service updates",
            "wechat_article_2": "Read more service updates"
        }
    })

