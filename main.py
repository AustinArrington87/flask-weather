from flask import Flask, render_template
from darksky import forecast

apikey = "4220aeb6ebb11c7abd00a31ae35cab06"


def weather(latitude, longitude):
    LOCATION = latitude, longitude
    with forecast(apikey, *LOCATION) as location:
        return(location['hourly']['data'][0])

midtown = weather(40.754932, -73.984016)
brooklyn = weather(40.650002, -73.949997)
queens = weather(40.742054, -73.769417)
statenisland = weather(40.579021, -74.151535)
bronx = weather(40.837048, -73.865433)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/weather")
def weather():
    return render_template("weather.html",midtown=midtown, 
    brooklyn=brooklyn, queens=queens, statenisland=statenisland, bronx=bronx)
    
if __name__ == "__main__":
    app.run(debug=True)