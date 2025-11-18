"""
Main Routes
Homepage and core navigation routes
"""

from flask import Blueprint, render_template, jsonify
from typing import Dict, Any

bp = Blueprint('main', __name__)


@bp.route('/')
def index() -> str:
    """Render homepage."""
    return render_template('index.html')


@bp.route('/about')
def about() -> str:
    """Render about page."""
    return render_template('about.html')


@bp.route('/api/health')
def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "GFU Nail"})

