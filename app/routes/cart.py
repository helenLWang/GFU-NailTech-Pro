"""
Shopping Cart Routes
Cart management and checkout
"""

from flask import Blueprint, render_template, jsonify, request, session
from typing import Dict, List, Any

bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/')
def cart_page() -> str:
    """Render shopping cart page."""
    return render_template('cart.html')


@bp.route('/api/add', methods=['POST'])
def add_to_cart() -> Dict[str, Any]:
    """Add product to cart."""
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    # Initialize cart in session if not exists
    if 'cart' not in session:
        session['cart'] = []
    
    # Check if product already in cart
    cart = session['cart']
    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            session['cart'] = cart
            return jsonify({"success": True, "message": "Quantity updated"})
    
    # Add new item
    cart.append({
        "product_id": product_id,
        "quantity": quantity
    })
    session['cart'] = cart
    
    return jsonify({"success": True, "message": "Added to cart", "cart_count": len(cart)})


@bp.route('/api/remove', methods=['POST'])
def remove_from_cart() -> Dict[str, Any]:
    """Remove product from cart."""
    data = request.get_json()
    product_id = data.get('product_id')
    
    if 'cart' not in session:
        return jsonify({"success": False, "message": "Cart is empty"})
    
    cart = session['cart']
    cart = [item for item in cart if item['product_id'] != product_id]
    session['cart'] = cart
    
    return jsonify({"success": True, "message": "Removed from cart", "cart_count": len(cart)})


@bp.route('/api/update', methods=['POST'])
def update_cart() -> Dict[str, Any]:
    """Update product quantity in cart."""
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    if 'cart' not in session:
        return jsonify({"success": False, "message": "Cart is empty"})
    
    cart = session['cart']
    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] = max(1, quantity)  # Minimum quantity is 1
            session['cart'] = cart
            return jsonify({"success": True, "message": "Quantity updated"})
    
    return jsonify({"success": False, "message": "Product not found in cart"})


@bp.route('/api/items')
def get_cart_items() -> Dict[str, Any]:
    """Get all cart items."""
    cart = session.get('cart', [])
    return jsonify({"cart": cart, "count": len(cart)})

