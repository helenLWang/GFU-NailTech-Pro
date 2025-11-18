"""
Product Routes
Product catalog, filtering, and detail pages
"""

from flask import Blueprint, render_template, jsonify, request
from typing import Dict, List, Any

bp = Blueprint('products', __name__, url_prefix='/products')


@bp.route('/')
def product_list() -> str:
    """Render product catalog page."""
    return render_template('products.html')


@bp.route('/<int:product_id>')
def product_detail(product_id: int) -> str:
    """Render product detail page."""
    return render_template('product-detail.html', product_id=product_id)


@bp.route('/api/list')
def api_product_list() -> Dict[str, Any]:
    """API endpoint for product list with filtering."""
    # Get filter parameters
    style = request.args.get('style', 'all')
    shape = request.args.get('shape', 'all')
    color = request.args.get('color', 'all')
    occasion = request.args.get('occasion', 'all')
    
    # Mock product data - in production, this would query a database
    products = get_mock_products()
    
    # Apply filters
    filtered_products = filter_products(products, style, shape, color, occasion)
    
    return jsonify({
        "products": filtered_products,
        "total": len(filtered_products),
        "filters": {
            "style": style,
            "shape": shape,
            "color": color,
            "occasion": occasion
        }
    })


def get_mock_products() -> List[Dict[str, Any]]:
    """Get mock product data."""
    return [
        {
            "id": 1,
            "name": "Rose Milk Cloud Set",
            "price": 35.00,
            "original_price": 44.00,
            "style": "classic",
            "shape": "almond",
            "color": "pink",
            "occasion": "wedding",
            "rating": 4.9,
            "reviews": 210,
            "stock": 14,
            "image": "/static/images/products/product-rose-milk.png",
            "description": "Milky pink gradients with 3D petals photographed in our Building A studio."
        },
        {
            "id": 2,
            "name": "MiuCute Storyboard",
            "price": 38.00,
            "original_price": 48.00,
            "style": "trendy",
            "shape": "stiletto",
            "color": "pink",
            "occasion": "party",
            "rating": 4.7,
            "reviews": 188,
            "stock": 12,
            "image": "/static/images/products/product-miucute.png",
            "description": "Editorial Miu Miu inspired set with character art and suede textures."
        },
        {
            "id": 3,
            "name": "Velvet Catwalk",
            "price": 34.50,
            "original_price": 44.50,
            "style": "minimalist",
            "shape": "almond",
            "color": "nude",
            "occasion": "office",
            "rating": 4.7,
            "reviews": 162,
            "stock": 18,
            "image": "/static/images/products/product-velvet-cat.png",
            "description": "Velvet overlays with sculpted cut-outs—perfect for internship presentations."
        },
        {
            "id": 4,
            "name": "Leopard Bow Atelier",
            "price": 35.99,
            "original_price": 46.99,
            "style": "trendy",
            "shape": "almond",
            "color": "brown",
            "occasion": "party",
            "rating": 4.9,
            "reviews": 198,
            "stock": 12,
            "image": "/static/images/products/product-leopard-bow.png",
            "description": "Leopard texture, 3D bows, and matte gradients shot in Qin Lake Room 203."
        },
        {
            "id": 5,
            "name": "Crystal Sugar Twist",
            "price": 32.00,
            "original_price": 40.00,
            "style": "glamour",
            "shape": "coffin",
            "color": "pink",
            "occasion": "party",
            "rating": 4.8,
            "reviews": 175,
            "stock": 15,
            "image": "/static/images/products/product-crystal-sugar.png",
            "description": "Crystal pink chrome with swirls that sparkle under dorm lighting."
        },
        {
            "id": 6,
            "name": "Mocha Dot Mochi",
            "price": 29.50,
            "original_price": 37.00,
            "style": "minimalist",
            "shape": "round",
            "color": "brown",
            "occasion": "everyday",
            "rating": 4.6,
            "reviews": 150,
            "stock": 20,
            "image": "/static/images/products/product-mocha-dot.png",
            "description": "Gradient latte base with playful dots—our best seller for casual outfits."
        },
        {
            "id": 7,
            "name": "Cozy Wool Pastels",
            "price": 28.00,
            "original_price": 35.00,
            "style": "minimalist",
            "shape": "round",
            "color": "pink",
            "occasion": "everyday",
            "rating": 4.5,
            "reviews": 132,
            "stock": 26,
            "image": "/static/images/products/product-cozy-wool.png",
            "description": "Soft-touch matte finish inspired by the incubator lounge mood board."
        },
        {
            "id": 8,
            "name": "Rose Bow Studio Set",
            "price": 36.00,
            "original_price": 45.00,
            "style": "glamour",
            "shape": "almond",
            "color": "pink",
            "occasion": "party",
            "rating": 4.9,
            "reviews": 210,
            "stock": 10,
            "image": "/static/images/products/product-rose-bow.jpg",
            "description": "Hand-sculpted bows with pearl centers inspired by our campus studio clients."
        },
        {
            "id": 9,
            "name": "Pearl Glaze Capsule",
            "price": 33.50,
            "original_price": 43.50,
            "style": "classic",
            "shape": "almond",
            "color": "nude",
            "occasion": "wedding",
            "rating": 4.8,
            "reviews": 188,
            "stock": 13,
            "image": "/static/images/products/product-pearl-glaze.jpg",
            "description": "High-gloss pink layers with floating pearls—our bestseller for graduation portraits."
        }
    ]


def filter_products(products: List[Dict[str, Any]], style: str, shape: str, color: str, occasion: str) -> List[Dict[str, Any]]:
    """Filter products based on criteria."""
    filtered = products
    
    if style != 'all':
        filtered = [p for p in filtered if p.get('style') == style]
    if shape != 'all':
        filtered = [p for p in filtered if p.get('shape') == shape]
    if color != 'all':
        filtered = [p for p in filtered if p.get('color') == color]
    if occasion != 'all':
        filtered = [p for p in filtered if p.get('occasion') == occasion]
    
    return filtered

