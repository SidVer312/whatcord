from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST", "GET"])
def handle_message():
    # Get message details from Twilio request
    message = request.form.get("Body")
    sender = request.form.get("From")

    # Process the message as needed
    print(f"Received message: {message} from {sender}")

    # Create a response using TwiML
    response = MessagingResponse()
    # Replace with your desired response

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)


