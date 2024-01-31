# Response example
response_example = {
    "cod": "200",
    "message": 0,
    "cnt": 4,
    "list": [
        {
            "dt": 1706659200,
            "main": {
                "temp": 290.97,
                "feels_like": 289.15,
                "temp_min": 290.97,
                "temp_max": 291.97,
                "pressure": 1025,
                "sea_level": 1025,
                "grnd_level": 786,
                "humidity": 13,
                "temp_kf": -1,
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                },
                {
                    "id": 808,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                },
            ],
            "clouds": {"all": 100},
            "wind": {"speed": 1.86, "deg": 30, "gust": 2.07},
            "visibility": 10000,
            "pop": 0,
            "sys": {"pod": "d"},
            "dt_txt": "2024-01-31 00:00:00",
        },
        {
            "dt": 1706670000,
            "main": {
                "temp": 290.64,
                "feels_like": 288.94,
                "temp_min": 289.98,
                "temp_max": 290.64,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 787,
                "humidity": 19,
                "temp_kf": 0.66,
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "clouds": {"all": 99},
            "wind": {"speed": 1.43, "deg": 27, "gust": 3.05},
            "visibility": 10000,
            "pop": 0,
            "sys": {"pod": "n"},
            "dt_txt": "2024-01-31 03:00:00",
        },
        {
            "dt": 1706680800,
            "main": {
                "temp": 289.88,
                "feels_like": 288.31,
                "temp_min": 289.34,
                "temp_max": 289.88,
                "pressure": 1021,
                "sea_level": 1021,
                "grnd_level": 787,
                "humidity": 27,
                "temp_kf": 0.54,
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "clouds": {"all": 99},
            "wind": {"speed": 0.58, "deg": 345, "gust": 1.06},
            "visibility": 10000,
            "pop": 0,
            "sys": {"pod": "n"},
            "dt_txt": "2024-01-31 06:00:00",
        },
        {
            "dt": 1706691600,
            "main": {
                "temp": 288.22,
                "feels_like": 286.83,
                "temp_min": 288.22,
                "temp_max": 288.22,
                "pressure": 1019,
                "sea_level": 1019,
                "grnd_level": 786,
                "humidity": 40,
                "temp_kf": 0,
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "clouds": {"all": 100},
            "wind": {"speed": 0.68, "deg": 1, "gust": 1.72},
            "visibility": 10000,
            "pop": 0,
            "sys": {"pod": "n"},
            "dt_txt": "2024-01-31 09:00:00",
        },
    ],
    "city": {
        "id": 3530597,
        "name": "Mexico City",
        "coord": {"lat": 19.4326, "lon": -99.1332},
        "country": "MX",
        "population": 15000,
        "timezone": -21600,
        "sunrise": 1706620312,
        "sunset": 1706660849,
    },
}

# Testing data for list comprehension
[
    [
        {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"},
        {"id": 805, "main": "Clouds", "description": "overcast clouds", "icon": "04n"},
    ],
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
]

[
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}],
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
    [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
]
