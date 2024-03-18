import pyowm

# Initialize OpenWeatherMap API key
owm_api_key = 'your_api_key'  # Replace 'your_api_key' with your actual API key

# Initialize OpenWeatherMap client
owm = pyowm.OWM(owm_api_key)

# Function to get weather information
def get_weather(location):
    try:
        observation = owm.weather_at_place(location)
        weather = observation.get_weather()
        temperature = weather.get_temperature('celsius')['temp']
        status = weather.get_status()
        return f"The weather in {location} is {status} with a temperature of {temperature}°C."
    except pyowm.exceptions.api_response_error.NotFoundError:
        return "Location not found. Please enter a valid location."

# Main function
def main():
    location = input("Enter your location: ")
    print(get_weather(location))

if __name__ == "__main__":
    main()
