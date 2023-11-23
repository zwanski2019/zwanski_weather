# Define the weather data
weather_data = {
    "Tonight": {"Description": "Partly Cloudy", "High": "--", "Low": "21°", "Precipitation": "0%", "Wind": "NE 15 km/h", "Humidity": "27%"},
    "Mon": {"Description": "Sunny", "High": "37°", "Low": "21°", "Precipitation": "0%", "Wind": "E 14 km/h", "Humidity": "19%"},
    "Tue": {"Description": "Sunny", "High": "37°", "Low": "20°", "Precipitation": "0%", "Wind": "E 15 km/h", "Humidity": "18%"},
    "Wed": {"Description": "Sunny", "High": "36°", "Low": "19°", "Precipitation": "0%", "Wind": "S 12 km/h", "Humidity": "18%"},
    "Thu": {"Description": "Sunny", "High": "35°", "Low": "19°", "Precipitation": "0%", "Wind": "SE 12 km/h", "Humidity": "30%"},
    "Fri": {"Description": "Mostly Sunny", "High": "35°", "Low": "20°", "Precipitation": "0%", "Wind": "SE 9 km/h", "Humidity": "36%"}
}


# Print the weather forecast
print("5-Day Weather Forecast for Abuja, Nigeria:")
print("{:<10} {:<15} {:<10} {:<15} {:<20} {:<10}".format("Day", "Description", "High/Low", "Precipitation", "Wind", "Humidity"))
for day, data in weather_data.items():
    print("{:<10} {:<15} {:<10} {:<15} {:<20} {:<10}".format(day, data["Description"], f"{data['High']}/{data['Low']}", data["Precipitation"], data["Wind"], data["Humidity"]))