# GFU Nail Website - Setup Instructions

## Quick Start Guide

### Step 1: Install Python Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

### Step 2: Start the Website

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

**Or manually:**
```bash
python app.py
```

### Step 3: Access the Website

Once the server starts, open your web browser and navigate to:

```
http://localhost:5000
```

## Deploying to Vercel

1. Install the Vercel CLI:
   ```bash
   npm i -g vercel
   ```
2. From the `dist/` directory run:
   ```bash
   vercel --prod
   ```
3. Vercel reads `vercel.json` and automatically serves `app.py`.

## Website Pages

- **Homepage**: http://localhost:5000/
- **Products**: http://localhost:5000/products/
- **Shopping Cart**: http://localhost:5000/cart/
- **Book Appointment**: http://localhost:5000/booking/
- **Analytics Dashboard**: http://localhost:5000/analytics/
- **About/Trust Section**: http://localhost:5000/trust/

## Features Available

✅ **Product Catalog** - Browse and filter press-on nails
✅ **Shopping Cart** - Add, remove, and update quantities
✅ **Booking System** - Schedule appointments
✅ **Analytics Dashboard** - View operational metrics
✅ **Social Links** - Direct links to Xiaohongshu and WeChat
✅ **Studio Gallery** - View offline operation photos

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, you can change it in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
```

### Missing Dependencies

If you get import errors, make sure all dependencies are installed:

```bash
pip install --upgrade -r requirements.txt
```

### Images Not Loading

The offline photos should be in `static/images/studio/`. If images don't load, check that the files were copied correctly.

## Production Deployment

For production deployment:

1. Set a secure `SECRET_KEY` in environment variables
2. Disable debug mode: `app.run(debug=False)`
3. Use a production WSGI server (e.g., Gunicorn)
4. Set up proper domain and SSL certificate

## Support

All features are functional and ready to use. The website includes:
- Real Xiaohongshu profile link
- Real WeChat article link
- Real operational data (2,900+ followers, 64,000+ likes, 88% retention)
- Offline studio photos
- Fully interactive features

Enjoy your GFU Nail website! 💅

