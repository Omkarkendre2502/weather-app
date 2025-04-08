from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    city = request.args.get('city')  # Get city from the input form
    error = None
    weather_data = None

    if city:
        api_key = "455d9243f6a91b61261f840570537cc8"  # Replace with your actual API key
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found. Please try again."
    else:
        error = "City parameter is required. Please enter a city."

    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



