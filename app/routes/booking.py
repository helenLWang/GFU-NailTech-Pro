"""
Booking Routes
Appointment booking system aligned with offline SOPs
"""

from flask import Blueprint, render_template, jsonify, request
from typing import Dict, List, Any
from datetime import datetime, timedelta

bp = Blueprint('booking', __name__, url_prefix='/booking')


@bp.route('/')
def booking_page() -> str:
    """Render booking page."""
    return render_template('booking.html')


@bp.route('/api/available-slots', methods=['GET'])
def get_available_slots() -> Dict[str, Any]:
    """Get available time slots for selected date."""
    date_str = request.args.get('date')
    
    if not date_str:
        return jsonify({"error": "Date parameter required"}), 400
    
    try:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    
    # Generate available time slots (9 AM to 6 PM, hourly)
    slots = []
    start_time = selected_date.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = selected_date.replace(hour=18, minute=0, second=0, microsecond=0)
    
    current_time = start_time
    while current_time < end_time:
        # Check if slot is in the past
        if current_time > datetime.now():
            slots.append({
                "time": current_time.strftime('%H:%M'),
                "available": True
            })
        current_time += timedelta(hours=1)
    
    return jsonify({
        "date": date_str,
        "slots": slots
    })


@bp.route('/api/book', methods=['POST'])
def create_booking() -> Dict[str, Any]:
    """Create a new booking."""
    data = request.get_json()
    
    required_fields = ['date', 'time', 'service_type', 'name', 'email', 'phone']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    # In production, save to database
    booking = {
        "id": len(get_mock_bookings()) + 1,
        "date": data['date'],
        "time": data['time'],
        "service_type": data['service_type'],
        "name": data['name'],
        "email": data['email'],
        "phone": data['phone'],
        "status": "confirmed",
        "created_at": datetime.now().isoformat()
    }
    
    return jsonify({
        "success": True,
        "message": "Booking confirmed",
        "booking": booking
    })


def get_mock_bookings() -> List[Dict[str, Any]]:
    """Get mock booking data (for development)."""
    return []

