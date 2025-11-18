"""
Diagnostic and Fix Script for GFU Nail Website
This script will check for issues and help you start the server
"""
import sys
import os

print("=" * 60)
print("GFU Nail Website - Diagnostic Tool")
print("=" * 60)
print()

# Check Python version
print("1. Checking Python version...")
print(f"   Python version: {sys.version}")
if sys.version_info < (3, 8):
    print("   ⚠️  Warning: Python 3.8+ recommended")
else:
    print("   ✅ Python version OK")
print()

# Check Flask installation
print("2. Checking Flask installation...")
try:
    import flask
    print(f"   ✅ Flask {flask.__version__} is installed")
except ImportError:
    print("   ❌ Flask is NOT installed")
    print("   Installing Flask...")
    os.system("pip install -r requirements.txt")
    try:
        import flask
        print(f"   ✅ Flask {flask.__version__} installed successfully")
    except ImportError:
        print("   ❌ Failed to install Flask. Please run: pip install -r requirements.txt")
        sys.exit(1)
print()

# Check if app.py exists
print("3. Checking application files...")
if os.path.exists("app.py"):
    print("   ✅ app.py found")
else:
    print("   ❌ app.py not found!")
    sys.exit(1)

if os.path.exists("app"):
    print("   ✅ app/ directory found")
else:
    print("   ❌ app/ directory not found!")
    sys.exit(1)

if os.path.exists("templates"):
    print("   ✅ templates/ directory found")
else:
    print("   ❌ templates/ directory not found!")
    sys.exit(1)
print()

# Try to import and create app
print("4. Testing application import...")
try:
    # Import from app.py directly
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from app import create_app
    app = create_app()
    print("   ✅ Application created successfully!")
    print("   ✅ All routes registered!")
except Exception as e:
    print(f"   ❌ Error creating application: {e}")
    import traceback
    traceback.print_exc()
    print()
    print("   Trying alternative import method...")
    try:
        # Try importing app.py as module
        import importlib.util
        spec = importlib.util.spec_from_file_location("app_module", "app.py")
        app_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_module)
        app = app_module.app
        print("   ✅ Application loaded via alternative method!")
    except Exception as e2:
        print(f"   ❌ Alternative method also failed: {e2}")
        sys.exit(1)
print()

# Check port availability
print("5. Checking port 5000...")
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1', 5000))
sock.close()
if result == 0:
    print("   ⚠️  Port 5000 is already in use!")
    print("   💡 Try closing other applications or use a different port")
else:
    print("   ✅ Port 5000 is available")
print()

# Start server
print("=" * 60)
print("🚀 Starting GFU Nail Website Server...")
print("=" * 60)
print()
print("📝 Open your browser and visit:")
print("   http://localhost:5000")
print()
print("📝 Or try:")
print("   http://127.0.0.1:5000")
print()
print("⚠️  Press Ctrl+C to stop the server")
print("=" * 60)
print()

try:
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
except KeyboardInterrupt:
    print("\n\n👋 Server stopped by user")
except Exception as e:
    print(f"\n\n❌ Server error: {e}")
    import traceback
    traceback.print_exc()

