# Frontend Documentation

## Overview

The Flask application now features a modern, responsive web interface that showcases the complete technology stack with beautiful visual elements and real-time monitoring.

## Features

### 🎨 Visual Design
- **Modern UI**: Clean, professional design with gradient backgrounds
- **Technology Cards**: Individual cards for Flask, PostgreSQL, Nginx, and Gunicorn
- **Icons**: Font Awesome icons representing each technology
- **Animations**: Smooth hover effects and loading animations
- **Responsive**: Mobile-friendly design that works on all screen sizes

### 📊 Real-time Monitoring
- **Status Indicators**: Live status updates for all services
- **Auto-refresh**: Status updates every 30 seconds
- **Health Checks**: Real-time connectivity testing
- **System Information**: Detailed version and configuration info

### 🔧 Technology Stack Display

#### Flask (Python)
- **Icon**: Python logo (fab fa-python)
- **Color**: Black (#000)
- **Status**: Shows running/stopped state
- **Info**: Framework version and status

#### PostgreSQL
- **Icon**: Database icon (fas fa-database)
- **Color**: PostgreSQL blue (#336791)
- **Status**: Connection status and version info
- **Info**: Database connectivity and version details

#### Nginx
- **Icon**: Globe icon (fas fa-globe)
- **Color**: Nginx green (#009639)
- **Status**: Proxy status
- **Info**: Web server status and configuration

#### Gunicorn
- **Icon**: Cogs icon (fas fa-cogs)
- **Color**: Green (#499848)
- **Status**: WSGI server status
- **Info**: Process manager status

## API Integration

### Endpoints Used by Frontend
- `GET /api/status` - Complete system status
- `GET /health` - Health check
- `GET /db` - Database connectivity

### JavaScript Functions
- `updateStatus()` - Fetches and updates all status indicators
- Auto-refresh every 30 seconds
- Error handling for failed requests

## File Structure

```
/opt/flaskapp/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Main HTML template
└── static/
    └── css/
        └── style.css     # CSS styling
```

## Customization

### Colors
- Primary gradient: `#667eea` to `#764ba2`
- Success status: `#d4edda` (light green)
- Error status: `#f8d7da` (light red)
- Card backgrounds: White with subtle shadows

### Animations
- Card hover effects with `translateY(-5px)`
- Pulse animation for status indicators
- Fade-in animations for page load
- Spinner animation for loading states

### Responsive Breakpoints
- Mobile: `max-width: 768px`
- Tablet: `768px - 1024px`
- Desktop: `1024px+`

## Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid and Flexbox support required
- Font Awesome 6.0+ for icons
- ES6+ JavaScript features

## Performance
- Lightweight CSS (no external frameworks)
- Minimal JavaScript footprint
- Efficient API calls with error handling
- Optimized for fast loading
