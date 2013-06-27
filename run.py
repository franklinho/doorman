from flask import Flask
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.play("https://googledrive.com/host/0B0URKjV-4_aiUF9SZjlRRmk4RWM/6.mp3")
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')