from drf_yasg import openapi

search_api_response = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 200,
    "data": {
        "result": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta "
                  "http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" "
                  "content=\"width=device-width, initial-scale=1.0\">\n    <title>Response</title>\n    <style>\n     "
                  "   body {\n            font-family: Arial, sans-serif;\n        }\n    </style>\n</head>\n<body>\n "
                  "   <div>\n        Here are some highly-rated hotels in Miami, FL:1. The Setai Miami Beach - A "
                  "luxurious beachfront hotel with elegant rooms, multiple pools, and a spa.2. Four Seasons Hotel "
                  "Miami - A five-star hotel offering spacious rooms, a rooftop pool, and a full-service spa.3. Faena "
                  "Hotel Miami Beach - A stylish hotel featuring art deco-inspired rooms, a private beach, "
                  "and multiple dining options.4. Mandarin Oriental, Miami - A waterfront hotel with stunning views, "
                  "a spa, and a rooftop pool.5. The Biltmore Hotel - A historic hotel with a championship golf "
                  "course, a spa, and multiple dining options.6. The Ritz-Carlton, South Beach - A beachfront hotel "
                  "with luxurious rooms, a spa, and a rooftop pool.7. Fontainebleau Miami Beach - A renowned hotel "
                  "offering spacious rooms, multiple pools, and a vibrant nightlife scene.8. JW Marriott Miami "
                  "Turnberry Resort & Spa - A resort with a golf course, a spa, and multiple dining options.9. The "
                  "Miami Beach EDITION - A trendy hotel with stylish rooms, a beach club, and multiple dining "
                  "options.10. W South Beach - A modern hotel with oceanfront rooms, a rooftop pool, and a vibrant "
                  "nightlife.Please note that availability and prices may vary, so it's recommended to check with "
                  "each hotel directly for the most up-to-date information.\n    </div>\n</body>\n</html>\n"
        }
    }
})
