from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

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
