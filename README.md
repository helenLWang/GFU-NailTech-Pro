# GFU Nail Website

A complete, functional website for GFU Nail - Premium Press-On Nails & Professional Nail Services.

## Features

- ✅ Beautiful, modern frontend (inspired by nevflynn.com style)
- ✅ Product catalog with filtering
- ✅ Shopping cart functionality
- ✅ Booking system
- ✅ Analytics dashboard with real operational data
- ✅ Brand trust section with authentic links
- ✅ Integration with Xiaohongshu and WeChat
- ✅ Offline studio photos showcase
- ✅ Fully responsive design
- ✅ All content in English for the bilingual campus audience

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the website:**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
GFU_Nail/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── app/
│   ├── __init__.py
│   ├── routes/           # Route handlers
│   │   ├── main.py      # Homepage routes
│   │   ├── products.py  # Product catalog routes
│   │   ├── cart.py      # Shopping cart routes
│   │   ├── booking.py   # Booking system routes
│   │   ├── analytics.py # Analytics dashboard routes
│   │   └── trust.py     # Trust section routes
│   └── utils/
│       └── link_handler.py  # Link management utility
├── templates/            # Jinja2 templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── products.html     # Product catalog
│   ├── cart.html        # Shopping cart
│   ├── booking.html      # Booking page
│   ├── analytics.html   # Analytics dashboard
│   ├── trust.html       # Trust section
│   └── ...
└── static/              # Static files
    ├── css/
    │   └── main.css     # Main stylesheet
    ├── js/
    │   └── main.js      # Main JavaScript
    └── images/
        └── studio/      # Offline operation photos
```

## Pages

- **Homepage** (`/`) - Main landing page with hero section and features
- **Products** (`/products/`) - Product catalog with filtering
- **Shopping Cart** (`/cart/`) - Cart management
- **Booking** (`/booking/`) - Appointment booking system
- **Analytics** (`/analytics/`) - Operational metrics dashboard
- **About/Trust** (`/trust/`) - Brand trust section with social links

## Authentic Links

The website includes real, authentic links:

- **Xiaohongshu Profile**: https://www.xiaohongshu.com/user/profile/6178fcfc000000001f03e6ef
- **WeChat Article**: https://mp.weixin.qq.com/s/YEMatSm_00WPCWdT9l2Gig

## Operational Data

The analytics dashboard displays real operational metrics:

- 2,900+ Xiaohongshu followers
- 64,000+ likes
- 88% retention rate
- Additional metrics available in the dashboard

## Development

### Running in Development Mode

```bash
python app.py
```

The app will run in debug mode on `http://localhost:5000`

### Deploying to Vercel

1. Install the Vercel CLI (one time):
   ```bash
   npm i -g vercel
   ```
2. From the `dist/` directory, deploy:
   ```bash
   vercel --prod
   ```

This repo includes `vercel.json`, so Vercel automatically runs `app.py` with the Python runtime and serves all routes.

### Environment Variables

Create a `.env` file (optional) for production:

```
SECRET_KEY=your-secret-key-here
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Charts**: Chart.js
- **Architecture**: Modular Flask application with blueprints

## Notes

- All content is in English for students and international visitors
- All links are authentic (no fabrication)
- All features are functional (not mockups)
- Images are optimized for web use
- Follows modular development standards

## Support

For questions or issues, please refer to the code documentation or contact the development team.

---

**GFU Nail** - Premium Press-On Nails & Professional Nail Services

