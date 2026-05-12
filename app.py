from flask import Flask, request, jsonify, render_template
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- FRONTEND PAGES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tracking")
def tracking():
    return render_template("tracking.html")


# ---------------- AI PREDICTION API ----------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    crop = data.get("crop", "").lower()
    quantity = data.get("quantity") or 0
    pickup = data.get("pickup", "Unknown")
    destination = data.get("destination", "Unknown")
    distance = data.get("distance", 10)

    # ---------------- VEHICLE LOGIC ----------------
    if crop == "tomato":
        vehicle = "Refrigerated Truck"
    elif quantity > 1000:
        vehicle = "Large Truck"
    else:
        vehicle = "Mini Truck"

    # ---------------- WEATHER LOGIC ----------------
    if distance > 150:
        weather = "Rain Expected"
        weather_status = "Risky"
    else:
        weather = "Clear Weather"
        weather_status = "Safe"

    # ---------------- SPOILAGE LOGIC ----------------
    if crop == "tomato" and distance > 100:
        spoilage = "High"
        urgency = "Dispatch within 12 hrs"
    elif crop == "rice":
        spoilage = "Low"
        urgency = "No Immediate Risk"
    else:
        spoilage = "Medium"
        urgency = "Dispatch Soon"

    # ---------------- ROUTE ----------------
    route = f"{pickup} → {destination}"

    # ---------------- ETA ----------------
    eta = f"{max(1, int(distance / 30))} hrs approx"

    # ---------------- COST ----------------
    estimated_cost = distance * 12 + quantity * 2

    # ---------------- TRANSPORTER MATCH ----------------
    transporters = ["Rajesh Trucks", "Karnataka Cargo", "GreenWay Logistics"]
    transporter = random.choice(transporters)

    match_score = f"{random.randint(85, 98)}%"
    driver_status = "Available"

    # ---------------- TRACKING ----------------
    order_id = "AG-" + str(random.randint(1000, 9999))
    tracking_status = "In Transit"

    return jsonify({
        "order_id": order_id,
        "crop": crop,
        "quantity": quantity,
        "pickup": pickup,
        "destination": destination,
        "route": route,

        "recommended_vehicle": vehicle,

        "weather": weather,
        "weather_status": weather_status,

        "spoilage_risk": spoilage,
        "urgency": urgency,

        "eta": eta,
        "estimated_cost": estimated_cost,

        "transporter": transporter,
        "match_score": match_score,
        "driver_status": driver_status,

        "tracking_status": tracking_status,
        "status": "success"
    })


if __name__ == "__main__":
    app.run(debug=True)