import requests

def get_weather(api_key, city):
    # OpenWeatherMap API endpoint
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
    
    # Make a request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        city_name = data['location']['name']
        temperature = data['current']['temp_c']
        # weather_description = data['weather'][0]['description']
        
        # Print the weather information
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        # print(f"Weather: {weather_description.capitalize()}")
    else:
        print("City not found or API request failed.")

def main():
    api_key = "577da78ef0bb4935a13112456252403"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()