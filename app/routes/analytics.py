"""
Analytics Routes
Operational data dashboard and metrics visualization
"""

from flask import Blueprint, render_template, jsonify
from typing import Dict, Any

bp = Blueprint('analytics', __name__, url_prefix='/analytics')


@bp.route('/')
def analytics_dashboard() -> str:
    """Render analytics dashboard page."""
    return render_template('analytics.html')


@bp.route('/api/metrics')
def get_metrics() -> Dict[str, Any]:
    """Get operational metrics data."""
    return jsonify({
        "xiaohongshu_followers": 2900,
        "xiaohongshu_likes": 64000,
        "retention_rate": 88,
        "total_customers": 1250,
        "monthly_bookings": 156,
        "average_rating": 4.8,
        "products_sold": 3420,
        "revenue_growth": 23.5,
        "monthly_revenue": 18600,
        "avg_order_value": 36.5,
        "conversion_rate": 34,
        "campus_performance": {
            "main": {
                "bookings": 92,
                "revenue": 11800,
                "repeat_rate": 61
            },
            "sanshui": {
                "bookings": 64,
                "revenue": 6800,
                "repeat_rate": 54
            }
        }
    })


@bp.route('/api/chart-data')
def get_chart_data() -> Dict[str, Any]:
    """Get chart data for visualization."""
    return jsonify({
        "followers_growth": {
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "data": [2100, 2300, 2500, 2700, 2800, 2900]
        },
        "engagement_rate": {
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "data": [12.5, 13.2, 14.1, 15.3, 16.8, 18.2]
        },
        "retention_trend": {
            "labels": ["Q1", "Q2", "Q3", "Q4"],
            "data": [82, 85, 87, 88]
        },
        "campus_bookings": {
            "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
            "main": [18, 22, 25, 27],
            "sanshui": [12, 14, 18, 20]
        },
        "collection_mix": {
            "labels": ["Classic", "Trendy", "Minimalist", "Glamour"],
            "data": [28, 32, 18, 22]
        }
    })

