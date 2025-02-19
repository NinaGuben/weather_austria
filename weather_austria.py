import requests

main_url = "https://dataset.api.hub.geosphere.at/v1/station/current/tawes-v1-10min"

station_id = input("Please visit https://dataset.api.hub.geosphere.at/app/frontend/station/historical/synop-v1-1h \nfor finding station IDs in Austria.\nPlease enter a station ID e.g.11036 (for Vienna Schwechat airport)\n")
parameter = input("Please enter the abbreviation for the parameter you want to find out:\n"
                  "TL for Temperature \nP for air pressure \nFF for wind speed \nDD for wind direction\n")

params = {"parameters": parameter, "station_ids": station_id}
response = requests.get(main_url, params = params)

if response.status_code == 200:
    data = response.json()
    for feature in data["features"]:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})
    coordinates = geometry.get("coordinates")
    parameters = properties.get("parameters", {})
    data = parameters.get(parameter, {})
    data_param = data.get("data", {})
    unit = data.get("unit", {})
    station = properties.get("station", {})
    #location = properties.get("name",{})
    if parameter == "TL":
        print("The current temperature at station", station, "in Austria is", data_param[0],unit)
    elif parameter == "P":
        print("The current air pressure at station", station, "in Austria is", data_param[0],unit)
    elif parameter == "FF":
        print("The current wind speed at station", station, "in Austria is", data_param[0],unit)
    elif parameter == "DD":
        print("The current wind direction at station", station, "in Austria is", data_param[0],unit)
else:
    print("API not accessible")


