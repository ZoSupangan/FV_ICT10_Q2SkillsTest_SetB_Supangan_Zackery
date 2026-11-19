from pyscript import document

instruments = {
    "Thermometer": {
        "name": "Thermometer",
        "measures": "Air Temperature",
        "unit": "Degrees Celsius (°C)",
        "purpose": "Measures how hot or cold the air is."
    },
    "Barometer": {
        "name": "Barometer",
        "measures": "Atmospheric Pressure",
        "unit": "Hectopascals (hPa)",
        "purpose": "Measures air pressure to help monitor weather changes."
    },
    "Anemometer": {
        "name": "Anemometer",
        "measures": "Wind Speed",
        "unit": "Kilometers per hour (km/h)",
        "purpose": "Measures how fast the wind is blowing."
    },
    "Hygrometer": {
        "name": "Hygrometer",
        "measures": "Relative Humidity",
        "unit": "Percent (%)",
        "purpose": "Measures the amount of moisture in the air."
    },
    "Rain Gauge": {
        "name": "Rain Gauge",
        "measures": "Rainfall",
        "unit": "Millimeters (mm)",
        "purpose": "Measures the amount of rainfall in an area."
    },
    "Wind Vane": {
        "name": "Wind Vane",
        "measures": "Wind Direction",
        "unit": "Cardinal Directions",
        "purpose": "Identifies the direction from which the wind is blowing."
    },
    "Weather Balloon": {
        "name": "Weather Balloon",
        "measures": "Atmospheric Conditions",
        "unit": "Varies",
        "purpose": "Collects atmospheric data at different altitudes."
    },
    "Pyranometer": {
        "name": "Pyranometer",
        "measures": "Solar Radiation",
        "unit": "Watts per square meter (W/m²)",
        "purpose": "Measures incoming solar radiation."
    }
}

not_found = {
    "name": "Not Found",
    "measures": "Not Found",
    "unit": "Not Found",
    "purpose": "This instrument is not included in the dataset."
}

def find_instrument(event):
    user_input = document.getElementById("instrument").value.strip().title()
    data = instruments.get(user_input, not_found)

    document.getElementById("name").innerText = data.get("name")
    document.getElementById("measures").innerText = data.get("measures")
    document.getElementById("unit").innerText = data.get("unit")
    document.getElementById("purpose").innerText = data.get("purpose")