from flask import Flask, render_template, request, jsonify
import json
import random
import string
from datetime import datetime, timedelta

app = Flask(__name__)

# Hardcoded train data
TRAINS_DATA = [
    {
        'id': 1,
        'name': 'Rajdhani Express',
        'number': '12953',
        'source': 'Delhi',
        'destination': 'Mumbai',
        'departure': '08:00 AM',
        'arrival': '08:30 PM',
        'duration': '12h 30m',
        'fare': 2500,
        'seats_available': 45
    },
    {
        'id': 2,
        'name': 'Shatabdi Express',
        'number': '12009',
        'source': 'Delhi',
        'destination': 'Agra',
        'departure': '06:30 AM',
        'arrival': '08:20 AM',
        'duration': '1h 50m',
        'fare': 550,
        'seats_available': 62
    },
    {
        'id': 3,
        'name': 'Intercity Express',
        'number': '12211',
        'source': 'Mumbai',
        'destination': 'Pune',
        'departure': '10:15 AM',
        'arrival': '03:45 PM',
        'duration': '5h 30m',
        'fare': 450,
        'seats_available': 78
    },
    {
        'id': 4,
        'name': 'Duronto Express',
        'number': '12217',
        'source': 'Delhi',
        'destination': 'Kolkata',
        'departure': '04:00 PM',
        'arrival': '12:15 PM (Next Day)',
        'duration': '20h 15m',
        'fare': 1800,
        'seats_available': 35
    },
    {
        'id': 5,
        'name': 'Garib Rath',
        'number': '12571',
        'source': 'Mumbai',
        'destination': 'Delhi',
        'departure': '11:30 AM',
        'arrival': '08:00 AM (Next Day)',
        'duration': '20h 30m',
        'fare': 1200,
        'seats_available': 55
    },
    {
        'id': 6,
        'name': 'Premium Express',
        'number': '12314',
        'source': 'Agra',
        'destination': 'Pune',
        'departure': '02:30 PM',
        'arrival': '11:45 PM',
        'duration': '9h 15m',
        'fare': 1500,
        'seats_available': 40
    },
    {
        'id': 7,
        'name': 'Local Fast',
        'number': '11011',
        'source': 'Delhi',
        'destination': 'Pune',
        'departure': '06:00 PM',
        'arrival': '04:30 AM (Next Day)',
        'duration': '22h 30m',
        'fare': 950,
        'seats_available': 88
    },
    {
        'id': 8,
        'name': 'Nonstop Express',
        'number': '12408',
        'source': 'Kolkata',
        'destination': 'Mumbai',
        'departure': '09:45 AM',
        'arrival': '07:20 AM (Next Day)',
        'duration': '21h 35m',
        'fare': 1400,
        'seats_available': 51
    }
]

# Dictionary to store bookings (temporary storage)
BOOKINGS = {}


def generate_pnr():
    """Generate a random 10-digit PNR number"""
    return ''.join(random.choices(string.digits, k=10))


def get_sources_destinations():
    """Get unique sources and destinations"""
    sources = set()
    destinations = set()
    for train in TRAINS_DATA:
        sources.add(train['source'])
        destinations.add(train['destination'])
    return sorted(list(sources)), sorted(list(destinations))


@app.route('/')
def index():
    """Home page with search bar"""
    sources, destinations = get_sources_destinations()
    return render_template('index.html', sources=sources, destinations=destinations)


@app.route('/search', methods=['POST'])
def search_trains():
    """Search trains based on source and destination"""
    data = request.get_json()
    source = data.get('source', '').strip()
    destination = data.get('destination', '').strip()

    if not source or not destination:
        return jsonify({'error': 'Please select both source and destination'}), 400

    if source == destination:
        return jsonify({'error': 'Source and destination cannot be the same'}), 400

    # Filter trains
    matched_trains = [
        train for train in TRAINS_DATA
        if train['source'].lower() == source.lower() and 
           train['destination'].lower() == destination.lower()
    ]

    if not matched_trains:
        return jsonify({'error': f'No trains found from {source} to {destination}'}), 404

    return jsonify({
        'success': True,
        'trains': matched_trains,
        'count': len(matched_trains)
    })


@app.route('/trains')
def trains():
    """Train listing page"""
    sources, destinations = get_sources_destinations()
    return render_template('trains.html', sources=sources, destinations=destinations)


@app.route('/booking/<int:train_id>')
def booking(train_id):
    """Booking form page"""
    train = next((t for t in TRAINS_DATA if t['id'] == train_id), None)
    if not train:
        return "Train not found", 404

    return render_template('booking.html', train=train)


@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    """Submit booking and generate ticket"""
    data = request.get_json()

    # Validate input
    required_fields = ['name', 'email', 'phone', 'age', 'gender', 'train_id', 'passengers']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Generate PNR and booking reference
    pnr = generate_pnr()
    booking_id = pnr
    booking_date = datetime.now().strftime('%d-%m-%Y %H:%M')

    # Find train details
    train = next((t for t in TRAINS_DATA if t['id'] == int(data['train_id'])), None)
    if not train:
        return jsonify({'error': 'Train not found'}), 404

    # Store booking
    booking_info = {
        'pnr': pnr,
        'booking_date': booking_date,
        'passenger': {
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'age': data['age'],
            'gender': data['gender']
        },
        'train': {
            'id': train['id'],
            'name': train['name'],
            'number': train['number'],
            'source': train['source'],
            'destination': train['destination'],
            'departure': train['departure'],
            'arrival': train['arrival'],
            'fare': train['fare'],
            'passengers_count': len(data['passengers'])
        },
        'passengers': data['passengers'],
        'total_fare': train['fare'] * len(data['passengers']),
        'seat_numbers': [f"S{random.randint(1, 120)}" for _ in data['passengers']]
    }

    BOOKINGS[pnr] = booking_info

    return jsonify({
        'success': True,
        'pnr': pnr,
        'booking': booking_info
    })


@app.route('/ticket/<pnr>')
def ticket(pnr):
    """Display ticket for a booking"""
    if pnr not in BOOKINGS:
        return "Ticket not found", 404

    booking = BOOKINGS[pnr]
    return render_template('ticket.html', booking=booking)


@app.route('/api/bookings')
def get_bookings():
    """API endpoint to get all bookings (for admin view)"""
    return jsonify(list(BOOKINGS.values()))


if __name__ == '__main__':
    app.run(debug=True)
