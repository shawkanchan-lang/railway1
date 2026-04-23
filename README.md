# Railway Ticket Booking System

A modern, full-stack web application for railway ticket booking built with Flask, HTML5, CSS3, and JavaScript. Perfect for school exhibitions and projects at the Class 12th level.

## 🌟 Features

- **Modern UI**: Contemporary railway-themed design with blue/white/gray color scheme
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Train Search**: Filter trains by source and destination
- **Booking System**: Interactive booking form with multi-passenger support
- **Digital Ticket**: Generate and display digital tickets with PNR numbers
- **Animations**: Smooth CSS transitions for enhanced user experience
- **No Database Required**: Uses Python dictionaries for temporary data storage
- **Print & Download**: Users can print or download their tickets

## 📋 Project Structure

```
railway/
├── app.py                    # Flask backend application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/                # HTML templates
│   ├── index.html           # Home page with search bar
│   ├── trains.html          # Train listing page
│   ├── booking.html         # Booking form page
│   └── ticket.html          # Digital ticket page
└── static/                   # Static files
    └── style.css            # Complete styling with animations
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd railway
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   - Navigate to `http://127.0.0.1:5000/`
   - Or `http://localhost:5000/`

## 🎨 UI/UX Highlights

### Pages

1. **Home Page (index.html)**
   - Hero section with search train bar
   - Feature highlights
   - Quick access to all sections

2. **Train Listing (trains.html)**
   - Search interface
   - Beautiful train cards
   - Train details: departure, arrival, duration, fare
   - One-click booking button

3. **Booking Form (booking.html)**
   - Passenger information section
   - Co-passenger support (up to 6 passengers)
   - Real-time fare calculation
   - Form validation

4. **Digital Ticket (ticket.html)**
   - Stylized ticket design
   - PNR number (randomly generated)
   - Passenger and train details
   - Seat allocation
   - Print and download options

### Design Elements

- **Color Scheme**: Blue (#0066cc), White, Gray (#f5f5f5)
- **Animations**: 
  - Slide-in effects
  - Hover transitions
  - Modal pop-ups
  - Floating elements

## 🔧 Backend Features

### Routes

- `GET /` - Home page
- `POST /search` - Search trains (returns JSON)
- `GET /trains` - Train listing page
- `GET /booking/<train_id>` - Booking form
- `POST /submit-booking` - Process booking
- `GET /ticket/<pnr>` - Display ticket
- `GET /api/bookings` - Get all bookings (API)

### Data Storage

- **Trains Data**: Hardcoded list of 8 sample trains
- **Bookings**: Stored in Python dictionary (temporary)
- **PNR Generation**: Random 10-digit number

### Sample Trains

Includes 8 pre-configured trains with various routes:
- Rajdhani Express (Delhi ↔ Mumbai)
- Shatabdi Express (Delhi ↔ Agra)
- Intercity Express (Mumbai ↔ Pune)
- And 5 more...

## 📝 Sample Bookings

When a user completes a booking:
1. A random 10-digit PNR is generated
2. Booking information is stored in the application
3. User is redirected to ticket page
4. Ticket can be printed or downloaded

Example booking structure:
```json
{
  "pnr": "1234567890",
  "booking_date": "23-04-2026 14:30",
  "passenger": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "age": 25,
    "gender": "Male"
  },
  "train": {
    "name": "Rajdhani Express",
    "number": "12953",
    "source": "Delhi",
    "destination": "Mumbai",
    "departure": "08:00 AM",
    "arrival": "08:30 PM",
    "fare": 2500
  },
  "passengers": [
    {"name": "John Doe", "gender": "Male", "age": 25},
    {"name": "Jane Doe", "gender": "Female", "age": 23}
  ],
  "total_fare": 5000,
  "seat_numbers": ["S45", "S46"]
}
```

## 🎯 Customization Guide

### Adding More Trains

Edit `TRAINS_DATA` in `app.py`:
```python
{
    'id': 9,
    'name': 'Your Train Name',
    'number': '12345',
    'source': 'City A',
    'destination': 'City B',
    'departure': '10:00 AM',
    'arrival': '06:00 PM',
    'duration': '8h',
    'fare': 1000,
    'seats_available': 80
}
```

### Changing Colors

Edit CSS variables in `static/style.css`:
```css
:root {
    --primary-blue: #0066cc;      /* Change primary color */
    --secondary-blue: #0052a3;    /* Change secondary color */
    --success-green: #5cb85c;     /* Change success color */
    /* ... more colors */
}
```

### Making Database Persistent

To save bookings permanently, replace the dictionary storage in `app.py` with:
- JSON file storage
- SQLite database
- Any other persistent storage

## 🖥️ Technical Stack

- **Backend**: Python 3 with Flask framework
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: CSS3 with animations and transitions
- **Storage**: Python dictionaries (in-memory)
- **Deployment**: Flask development server

## ⚙️ Debug Mode

The application runs in debug mode by default (`debug=True`). This means:
- Changes are automatically reloaded
- You'll get detailed error pages
- The server restarts on file changes

To disable debug mode (for production):
```python
app.run(debug=False)
```

## 📱 Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🎓 Learning Objectives

This project demonstrates:
- Full-stack web development
- Flask framework basics
- RESTful API design
- Responsive web design
- JavaScript DOM manipulation
- CSS animations and transitions
- Form handling and validation
- State management (Python dictionaries)

## 📚 Possible Enhancements

1. **Database Integration**: Add SQLite/PostgreSQL for persistent storage
2. **User Authentication**: Add login/registration system
3. **Payment Integration**: Add payment gateway (Stripe/PayPal)
4. **Email Notifications**: Send booking confirmation emails
5. **PDF Export**: Generate PDF tickets instead of text
6. **Admin Panel**: Manage trains and bookings
7. **Real-time Updates**: Use WebSockets for live seat availability
8. **Multiple Languages**: Add i18n support

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is in use, change it in `app.py`:
```python
app.run(debug=True, port=5001)
```

### ModuleNotFoundError
Make sure Flask is installed:
```bash
pip install -r requirements.txt
```

### Static Files Not Loading
Ensure the `static/` folder exists and contains `style.css`

### Forms Not Submitting
Check browser console for JavaScript errors
Verify Flask is running in debug mode

## 📄 License

This project is created for educational purposes. Feel free to use and modify for school exhibitions and learning.

## 👨‍💻 Author

Created for Class 12th School Fest Exhibition

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Test with sample data provided
4. Verify all files are in correct folders

---

**Happy Coding!** 🚂✨

Visit `http://localhost:5000` to start using the Railway Ticket Booking System!
