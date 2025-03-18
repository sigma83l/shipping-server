from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

tracking_data = {    
    "H2SsJ93dM2": {
        "merchant": "SENOC POINT OF SALE MARKETING",
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
        "pick_up_date": "18 March 2025",
        "service_type": "Express",
        "Total_Freight": 1680.00,
        "parcel_type": "container",
        "weight": " 1,074 Kg",
        "mode": "Sea Transportation",
        "quantity": 1,
        "current_status": "Picked Up",
        "tracking": [
            {
                "id": 1,
                "port_name": "Port of Manila (PHMNL)",
                "country": "Philippines",
                "scheduled_departure": "20 March 2025",
                "scheduled_arrival": "28 March 2025 ",
                "transit_duration": "8 days 12 hours",
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
        "description": "Electronics - Mobile Phone",
        "additional_information": "Handle with care",
    },
    "KOf34Ws69d": {
        "merchant": "SENOC POINT OF SALE MARKETING",
        "first_name": "Mercel",
        "last_name": "Foucault",
        "email": "marcelfoucault@gmail.com",
        "product": "2020 Kubota BX23 Backhoe Loader (KBUC1DHRTLGK45022)",
        "merchant_address": "Terelay Industrial Estate, Bo. Pittland, Provincial Rd, Cabuyao, Laguna, Philippines",
        "merchant_phone_number": "+63 (961) 479 1394 / +63 (920) 142 7892",
        "merchant_email": "info@senocmarketing.com",
        "phone_number": "+1 (705) 822-8992",
        "shipping_address": "1763 Kathleen Street, Val Caron, Greater Sudbury, Ontario, P3N 1M6, Canada",
        "city": "New York",
        "departure_date": "20 March 2025",
        "country": "USA",
        "scheduled_arrival": "27 April 2025",
        "transit_time": "38 days 13 hours",
        "pick_up_date": "19 March 2025",
        "service_type": "Express",
        "Total_Freight": 1680.00,
        "parcel_type": "container",
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
                "vessel_name": "EVER BLISS",
                "vessel_imo": "9786932",
                "is_checked": True
            },
            {
                "id": 2,
                "port_name": "Port of Shanghai (CNSHG)",
                "country": "China",
                "scheduled_departure": "01 April 2025",
                "scheduled_arrival": "27 April 2025 ",
                "transit_duration": "26 days 22 hours",
                "vessel_name": "OOCL BERLIN",
                "vessel_imo": "9622605",
                "is_checked": True
            },
            {   
                "id": 3,
                "port_name": "Port of Rotterdam",
                "country": "Netherlands",
                "scheduled_departure": "2024-03-20 07:30:00",
                "scheduled_arrival": "2024-03-28 14:45:00",
                "transit_duration": "8 days",
                "vessel_name": "MSC Zoe",
                "vessel_imo": "9703318",
                "is_checked": False
            }
        ],
        "description": "Electronics - Mobile Phone",
        "additional_information": "Handle with care",
    },

}


@app.route('/track', methods=['GET'])
def track():
    tracking_number = request.args.get('number')
    
    if tracking_number in tracking_data:
        # print(tracking_data[tracking_number])
        return jsonify(tracking_data[tracking_number])
    else:
        return jsonify({"error": "Tracking number not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
