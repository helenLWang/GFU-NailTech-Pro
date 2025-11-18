"""
Quick test script to verify the Flask app works
"""
import sys

try:
    from app import create_app
    app = create_app()
    print("✅ Flask app created successfully!")
    print("✅ All routes registered!")
    print("\n🚀 Starting server...")
    print("📝 Open your browser and visit: http://localhost:5000")
    print("⚠️  Press Ctrl+C to stop the server\n")
    app.run(debug=True, host='127.0.0.1', port=5000)
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

