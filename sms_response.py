from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from weather import Weather, Unit
weather = Weather(unit=Unit.FAHRENHEIT)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    number = request.form['From']
    message_body = request.form['Body']
    resp = MessagingResponse()
    
    location = weather.lookup_by_location(str(message_body))
    condition = location.condition
    forecasts = location.forecast
    resp.message("Hey! Looks like it's " + str(condition.text).lower() + " there. The high is " + forecasts[1].high + "F and the low is " + forecasts[2].low + "F. Goodbye!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


