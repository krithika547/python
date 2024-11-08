import requests
import smtplib

# Replace with your OpenWeatherMap API key
API_KEY = 'f82ad94ba6dd3ef08c2f2f032ef25bd3'
# Replace with your desired location
CITY = 'tamilnadu'
COUNTRY = 'india'

# Function to fetch weather data
def get_weather_data(api_key, city, country):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
    response = requests.get(url)
    return response.json()

# Function to send email
def send_email(subject, body):
    sender = 'weathernotification@gmail.com'
    receiver = 'receiver@gmail.com'
    password = 'bsaf bvyt jioe riro'

    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

# Main logic
weather_data = get_weather_data(API_KEY, CITY, COUNTRY)
weather_main = weather_data['weather'][0]['main']

if weather_main == 'Rain':
    send_email('Umbrella Reminder', 'It is going to rain today. Don\'t forget to take an umbrella!')
