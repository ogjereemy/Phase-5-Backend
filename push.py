from flask import Flask, request, jsonify
from flask_cors import CORS
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
@app.route('/push/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.get_json()
        subscription_info = data.get('subscription_info')
        if not subscription_info:
            return jsonify({"msg": "Subscription information missing"}), 400

        # Add subscription to the list (replace with database logic in production)
        subscriptions.append(subscription_info)

        return jsonify({"msg": "Subscription successful"}), 200
    except Exception as e:
        print(f"Error subscribing user: {e}")
        return jsonify({"msg": "Subscription failed"}), 500

# Setup the scheduler to send reminders every day at 8 AM
scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_reminders, 'cron', hour=8)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
