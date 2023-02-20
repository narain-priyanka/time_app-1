from flask import Flask
import datetime
import pytz

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    NYC_time = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(NYC_time)
    current_time = now.strftime('%Y-%m-%d %H:%M:%S %Z')
    return "Current Time: " + current_time
    
if __name__== "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    
