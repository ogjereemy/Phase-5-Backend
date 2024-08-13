from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pywebpush import webpush, WebPushException
from apscheduler.schedulers.background import BackgroundScheduler
import json

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# In-memory storage for demo purposes; replace with a persistent database in production
subscriptions = []

VAPID_PUBLIC_KEY = "BFGaoiHTu_EEsa3a5YpPSksJcGl11E_2kjnpqo_KW7RVXtcK4uSjrE4uxlrjWPXhN-K5uM16duDXiCcMCFNkPH4"
VAPID_PRIVATE_KEY = "tdpYckEtBuZSn1qnZ22BLoNv_wjhY76E79b4V47V7Bk"
VAPID_CLAIMS = {"sub": "mailto:jeremy044@gmail.com"}

# Function to build CORS preflight response
def _build_cors_prelight_response():
    response = jsonify({'message': 'CORS preflight response'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    return response

# Function to send push notifications
def send_notification(subscription_info, message_title, message_body):
    try:
        webpush(
            subscription_info=subscription_info,
            data=json.dumps({"title": message_title, "body": message_body}),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS
        )
    except WebPushException as ex:
        print(f"WebPush failed: {repr(ex)}")

# Scheduled task to send daily workout reminders
def send_daily_reminders():
    for subscription in subscriptions:
        send_notification(subscription, "Workout Reminder", "Don't forget to complete your workout today!")

# Endpoint to subscribe for push notifications
@app.route('/subscribe', methods=['POST', 'OPTIONS'])
@cross_origin()  # Allow CORS for this route
def subscribe():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    subscription_info = request.json.get('subscription_info')
    subscriptions.append(subscription_info)  # Store subscription info
    return jsonify({"message": "Subscription successful"}), 201

# Setup the scheduler to send reminders every day at 8 AM
scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_reminders, 'cron', hour=8)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
