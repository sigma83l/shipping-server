
from flask import Flask, request, jsonify, session
from datetime import timedelta
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import random
from dotenv import load_dotenv
import os
import bcrypt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from urllib.parse import quote_plus
import certifi
from flask_mail import Mail, Message  
import time

username = quote_plus('hamedsedaghatgit83')
password = quote_plus('Hitlerwashero2050')
# Load env variables
load_dotenv()
MONGO_URI =  'mongodb+srv://' + username + ':' + password + "@cluster0.kpry90i.mongodb.net/?retryWrites=true&w=majority"

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://lexfleetlogisticsservices.com"])

# Setup MongoDB client
client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True, tlsCAFile=certifi.where())
db = client['sp-shipping']
users_col = db['users']
tracking_col = db['tracking']

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER') or 'smtp.gmail.com'
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT') or 465)
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') != 'False'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.secret_key = os.getenv('SECRET_KEY', 'a_very_secret_key')  # Make sure to set a real secret key

mail = Mail(app)

app.permanent_session_lifetime = timedelta(minutes=30)

def send_email(subject, body, recipient_email):
    try:
        msg = Message(subject, recipients=[recipient_email])
        msg.body = body
        mail.send(msg)
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    email = data.get('email')
    otp = data.get('otp')

    # Check if OTP exists and is still valid
    stored_otp = session.get('otp')
    otp_expiry = session.get('otp_expiry')

    if not stored_otp or time.time() > otp_expiry:
        return jsonify({"error": "OTP has expired or doesn't exist"}), 400

    if int(otp) != stored_otp:
        return jsonify({"error": "Invalid OTP"}), 400

    # OTP is correct, now log the user in by storing their ID in the session
    user = users_col.find_one({'email': email})
    session['user_id'] = str(user['_id'])  # Store user ID in the session
    session.permanent = True  # Make session permanent

    # Clear OTP from session after verification
    session.pop('otp', None)
    session.pop('otp_expiry', None)

    return jsonify({"message": "Email verified successfully, you are now logged in"}), 200
        
# def send_email(to_email, template_path, context):
#     with open(template_path, "r", encoding="utf-8") as file:
#         template = Template(file.read())
#     body = template.render(context)
#     msg = Message('Payment Confirmation', sender=app.config['MAIL_USERNAME'], recipients=[to_email])
#     msg.html = body
#     mail.send(msg)
#     print(f"Sending email to {to_email} with body:\n{body}")

tracking_data = {    
    "H2SsJ93dM2": {
        "merchant": "Senoc Point of Sale Marketing",
        "first_name": "Mercel",
        "last_name": "Foucault",
        "email": "marcelfoucault@gmail.com",
        "product": "2020 Kubota BX23 Backhoe Loader (KBUC1DHRTLGK45022)",
        "merchant_address": "Terelay Industrial Estate, Bo. Pittland, Provincial Rd, Cabuyao, Laguna, Philippines",
        "merchant_phone_number": "+63 (961) 479 1394 / +63 (920) 142 7892",
        "merchant_email": "info@senocmarketing.com",
        "phone_number": "+1 (705) 822-8992",
        "shipping_address": "1763 Kathleen Street, Val Caron, Greater Sudbury, Ontario, P3N 1M6, Canada",
        "city": "Greater Sudbury",
        "departure_date": "20 March 2025",
        "country": "Canada",
        "scheduled_arrival": "27 April 2025",
        "transit_time": "38 days 13 hours",
        "pick_up_date": "19 March 2025",
        "service_type": "Standard",
        "Total_Freight": 1680.00,
        "parcel_type": "Container",
        "weight": " 1,074 Kg",
        "mode": "Sea Transportation",
        "quantity": 1,
        "current_status": "In Transit",
        "tracking": [
            {
                "id": 1,
                "port_name": "Port of Manila (PHMNL)",
                "country": "Philippines",
                "scheduled_departure": "20 March 2025",
                "scheduled_arrival": "28 March 2025 ",
                "transit_duration": "8 days 12 hours",
                "arrival_port": "Port of Shanghai (CNSHG)",
                "vessel_name": "EVER BLISS",
                "vessel_imo": "9786932",
                "is_checked": False
            },
            {
                "id": 2,
                "port_name": "Port of Shanghai (CNSHG)",
                "country": "China",
                "scheduled_departure": "01 April 2025",
                "scheduled_arrival": "27 April 2025 ",
                "transit_duration": "26 days 22 hours",
                "arrival_port": "Port of New York (USNYC)",
                "vessel_name": "OOCL BERLIN",
                "vessel_imo": "9622605",
                "is_checked": False
            },
            {   
                "id": 3,
                "port_name": "---",
                "country": "USA",
                "scheduled_departure": "---",
                "scheduled_arrival": "---",
                "transit_duration": "12 hours 55 minutes",
                "vessel_name": "---",
                "vessel_imo": "---",
                "is_checked": False
            }
        ],
        "tracking_additional_info": "From Port of New York (USNYC) to 1763 Kathleen Street, Val Caron, ON, Canada by Truck it will take 12 hours 55 minutes",
        "description": "Electronics - Mobile Phone",
        "additional_information": "The Designated Ship Has Arrived. The Loaded 20ft Container Is Loaded On The Ship As Per The Cargo Plan. The Ship Will Now Depart For The Next Assigned Port. Final Destination Port Is New York, USA And The Estimated Arrival Time Is 27/04/2025 Subject To Delay Especially Under Unexpected Severe Weather Condition. ------------------------------------ Your cargo has arrived at Port of Shanghai (CNSHG) aboard EVER BLISS (IMO: 9786932) and is scheduled for transshipment to OOCL BERLIN (IMO: 9622605), with a scheduled departure on April 1, 2025, and an estimated arrival at Port of New York (USNYC) on April 27, 2025.",
    },
    "KOf34Ws69d": {
        "merchant": "Senoc Point of Sale Marketing",
        "first_name": "Greg",
        "last_name": "Mahurin",
        "email": "mahuringreg@gmail.com",
        "product": "2018 Bobcat E85 Crawler Excavator (B48411753)",
        "merchant_address": "Terelay Industrial Estate, Bo. Pittland, Provincial Rd, Cabuyao, Laguna, Philippines",
        "merchant_phone_number": "+63 (961) 479 1394 / +63 (920) 142 7892",
        "merchant_email": "info@senocmarketing.com",
        "phone_number": "+1 (573) 280-7273 ",
        "shipping_address": "488 Hwy W, Rocky Mount, Missouri, 65072, USA ",
        "city": "Rocky Mount ",
        "departure_date": "25 March 2025 ",
        "country": "USA",
        "scheduled_arrival": "28 April 2025",
        "transit_time": "33 Days",
        "pick_up_date": "24 March 2025",
        "service_type": "Standard",
        "Total_Freight": 2125.00,
        "parcel_type": "Container",
        "weight": " 8600 Kg",
        "mode": "Sea Transportation",
        "quantity": 1,
        "current_status": "In Transit",
        "tracking": [
            {
                "id": 1,
                "port_name": "Port of Manila (PHMNL)",
                "country": "Philippines",
                "scheduled_departure": "25 March 2025",
                "scheduled_arrival": "28 March 2025 ",
                "transit_duration": "3 days 17 hours",
                "arrival_port": "Port of Busan (KRPUS)",
                "vessel_name": "NAVIOS UTMOST",
                "vessel_imo": "9972787",
                "is_checked": False
            },
            {
                "id": 2,
                "port_name": "Port of Busan (KRPUS)",
                "country": "South Korea",
                "scheduled_departure": "02 April 2025",
                "scheduled_arrival": "28 April 2025 ",
                "transit_duration": "26 days 18 hours",
                "arrival_port": "Port of New Orleans (USMSY)",
                "vessel_name": "CMA CGM ALMAVIVA",
                "vessel_imo": "9450648",
                "is_checked": False
            }
        ],
        "tracking_additional_info": "From Port of New Orleans (USMSY) to 488 Hwy W, Rocky Mount, Missouri, 65072, USA by Truck it will take 15 hours.",
        "description": "Electronics - Mobile Phone",
        "additional_information": "The Designated Ship Has Arrived. The Loaded 20ft Container Is Loaded On The Ship As Per The Cargo Plan. The Ship Will Now Depart For The Next Assigned Port. Final Destination Port Is New Orleans, USA And The Estimated Arrival Time Is 28/04/2025 Subject To Delay Especially Under Unexpected Severe Weather Condition. ----------------------------------------------------------- Your cargo has arrived at Port of Busan (KRPUS) aboard NAVIOS UTMOST (IMO: 9972787) and is scheduled for transshipment to CMA CGM ALMAVIVA (IMO: 9450648), with a scheduled departure on April 2, 2025, and an estimated arrival at Port of New Orleans (USMSY) on April 28, 2025. ----------------------------------------------------------- The designated vessel, CMA CGM ALMAVIVA, has departed from the Port of Busan (KRPUS) today, April 2, 2025, en route to its final destination at the Port of New Orleans (USMSY), USA. The estimated transit duration is 26 days and 18 hours, with an expected arrival date of April 28, 2025. Please note that the arrival timeline is subject to possible delays due to weather or other unforeseen circumstances.",
    },

}

# ---------------- USER ROUTES ---------------- #

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if user already exists
    if users_col.find_one({'email': email}):
        return jsonify({"error": "User already exists"}), 409

    # Hash the password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert user into the database
    user = users_col.insert_one({'email': email, 'password': hashed_pw})

    # Get user data (including ObjectId)
    new_user = users_col.find_one({'_id': user.inserted_id})

    # Log the user in by storing user ID in session
    session['user_id'] = str(new_user['_id'])  # Store user ID in the session
    session.permanent = True  # Make session permanent

    return jsonify({"message": "Registration successful, you are now logged in"}), 201

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Check if user is logged in (i.e., if session['user_id'] exists)
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    # Fetch user data from DB
    user_id = session['user_id']
    user = users_col.find_one({'_id': ObjectId(user_id)})

    return jsonify({"message": f"Welcome, {user['email']}!"}), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find user in the database by email
    user = users_col.find_one({'email': email})
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    # Check password
    if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    # Store user info in session after successful login
    session['user_id'] = str(user['_id'])  # You can store other details like email if needed
    session.permanent = True  # Make the session permanent

    return jsonify({"message": "Login successful"}), 200


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    return jsonify({"message": "Logged out successfully"}), 200

# ---------------- TRACKING ROUTES ---------------- #

# @app.route('/get-all-trackings', methods=['GET'])
# def get_all_trackings():
#     try:
#         trackings = list(tracking_col.find({}, {'_id': False}))
#         return jsonify(trackings), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
@app.route('/track', methods=['GET'])
def get_tracking():
    tracking_number = request.args.get('number')
    record = tracking_col.find_one({'tracking_number': tracking_number})
    if not record:
        return jsonify({'error': 'Tracking number not found'}), 404

    record['_id'] = str(record['_id'])
    return jsonify(record)


@app.route('/add-tracking', methods=['POST'])
def add_tracking():
    # Check if user is logged in (i.e., if session['user_id'] exists)
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized, please log in first"}), 401

    data = request.json
    if 'tracking_number' not in data:
        return jsonify({'error': 'Tracking number is required'}), 400

    if tracking_col.find_one({'tracking_number': data['tracking_number']}):
        return jsonify({'error': 'Tracking number already exists'}), 409

    tracking_col.insert_one(data)

    # Prepare the email body
    tracking_details = f"""
    Tracking Number: {data['tracking_number']}
    First Name: {data['first_name']}
    Last Name: {data['last_name']}
    Email: {data['email']}
    Product: {data['product']}
    Merchant Address: {data['merchant_address']}
    Shipping Address: {data['shipping_address']}
    Departure Date: {data['departure_date']}
    Scheduled Arrival: {data['scheduled_arrival']}
    Transit Time: {data['transit_time']}
    Current Status: {data['current_status']}
    Price: {data['price']}

    Additional Information:
    {data['additional_information']}
    """

    # Send the email with the tracking details
    send_email(
        subject=f"New Tracking Data: {data['tracking_number']}",
        body=tracking_details,
        recipient_email="hamedsedaghatcrt83@gmail.com"
    )

    return jsonify({'message': 'Tracking data added successfully'}), 201


@app.route('/update-tracking/<tracking_number>', methods=['PUT'])
def update_tracking(tracking_number):
    # Check if user is logged in (i.e., if session['user_id'] exists)
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized, please log in first"}), 401

    update_data = request.json
    result = tracking_col.update_one(
        {'tracking_number': tracking_number},
        {'$set': update_data}
    )
    if result.matched_count == 0:
        return jsonify({'error': 'Tracking number not found'}), 404
    return jsonify({'message': 'Tracking data updated'})


@app.route('/delete-tracking/<tracking_number>', methods=['DELETE'])
def delete_tracking(tracking_number):
    # Check if user is logged in (i.e., if session['user_id'] exists)
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized, please log in first"}), 401

    result = tracking_col.delete_one({'tracking_number': tracking_number})
    if result.deleted_count == 0:
        return jsonify({'error': 'Tracking number not found'}), 404
    return jsonify({'message': 'Tracking data deleted'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
