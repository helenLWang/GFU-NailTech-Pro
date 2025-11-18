"""
GFU Nail - Flask Application Entry Point
Main application file for GFU Nail website
"""

from flask import Flask, render_template, jsonify, request, redirect, url_for
from app.routes import main, products, cart, booking, analytics, trust
from app.utils.link_handler import LinkHandler
import os

def create_app() -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(booking.bp)
    app.register_blueprint(analytics.bp)
    app.register_blueprint(trust.bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

