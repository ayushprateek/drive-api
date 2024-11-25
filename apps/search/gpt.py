import re
from common import constants
import openai
import json

from apps.trip import helper
from drive_ai import settings


class TravelAssistant:
    def __init__(self):
        """
        Initializes the TravelAssistant with the OpenAI API key.
        """
        openai.api_key = settings.GPT_SECRET_KEY

    def generate_chatgpt_response(self, user_query):
        """
        Generates a response from the OpenAI GPT-3.5-turbo model.

        Args:
        - user_query (str): The user's input/query.

        Returns:
        - str: The assistant's reply.
        """
        # Set parameters for the OpenAI GPT-3 API
        print('generate_chatgpt_response called')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                      {'role': 'user', 'content': user_query}],
            temperature=0.2
        )
        print('True response = ',response)
        # Extract and return the assistant's reply
        assistant_reply = response['choices'][0]["message"]["content"]
        return assistant_reply

    def is_travel_related(self, query, context):
        """
        Determines if a given query is related to travel based on various criteria.

        Args:
        - query (str): The user's input/query.
        - context (dict): The context information, including previous queries.

        Returns:
        - bool: True if the query is related to travel, False otherwise.
        """
        # Step 1: Keyword Matching
        travel_keywords = ["deals", "best", "deal", "travel", "hotel", "discount", "stay", "accommodation", "plan", "trip", "journey",
                           "hotels", "attractions", "restaurants", "station", "electric", "fuel", "restaurant",
                           "fastest", "shortest", "nearest", "cheapest", "mexican",
                           "italian", "sea", "sushi", "tapas", "hotdog", "fast", "highest","tinerary"]

        if any(keyword in query.lower() for keyword in travel_keywords):
            return True

        # Step 2: Pattern Matching
        travel_patterns = ["plan a trip", "find hotels in", "find attractions", "find restaurants in", "restaurants in",
                           "attractions in", "attraction in", "Can you suggest", "the cheapest", "how long", "how many"]
        if any(pattern in query.lower() for pattern in travel_patterns):
            return True

        # Step 3: Use Regular Expressions for more complex patterns
        destination_pattern = re.compile(r'\bin\b\s+\w+')
        if destination_pattern.search(query.lower()):
            return True

        date_pattern = re.compile(r'\bfor\b\s+\w+')
        if date_pattern.search(query.lower()):
            return True

        # Step 4: Context-Based Approach
        if context.get("previous_query") and "travel" in context["previous_query"].lower():
            return True

        return False

    def is_city_related(self, query, context):
        """
        Determines if a given query is related to travel based on various criteria.

        Args:
        - query (str): The user's input/query.
        - context (dict): The context information, including previous queries.

        Returns:
        - bool: True if the query is related to travel, False otherwise.
        """
        # Step 1: Keyword Matching
        city_keywords = ["known", "famous", "interesting", "facts", "people", "tips", "family", "ways"]

        if any(keyword in query.lower() for keyword in city_keywords):
            return True
        return False



    def convert_to_json(self, gpt_text):
        """
        """
        # Extract JSON data from the string
        start_index = gpt_text.find("{")  # Find the starting index of the JSON data
        json_data_string = gpt_text[start_index:]

        # Parse the JSON data into a Python dictionary
        json_data = json.loads(json_data_string)
        return json_data

    def format_response(self, formatted_response):
        """
        Formats the GPT response with trip details, attractions, hotels, and food information.

        Args:
        - formatted_response (dict): Response data from OpenAI GPT.

        Returns:
        - str: Formatted reply.
        """
        trip_data = {
            'from': formatted_response['locations'][0]['city_name'],
            'to': formatted_response['locations'][-1]['city_name'],
            'days': formatted_response['number_of_days'],
            'day_details': {key: value for key, value in formatted_response.items() if key.startswith('day')}
        }

        # Format the response
        formatted_reply = f"<h5>Trip From: {trip_data['from']} Trip To: {trip_data['to']}</h5>"

        for day_key, day_data in trip_data['day_details'].items():
            if day_key.startswith('day'):
                day_number = int(day_key[3:])  # Extract day number from the key (assuming key starts with 'day')
                formatted_reply += f"<br> <p> Day {day_number}:\n"
                formatted_reply += f"{day_data['text']}</p>"

                attractions_list = self.format_category_list(day_data.get('attractions', []), 'Attraction',
                                                             'Best Attractions')
                if attractions_list:
                    formatted_reply += 'Best Attractions:'
                    formatted_reply += f"<ul> {attractions_list} </ul>"

                hotels_list = self.format_category_list(day_data.get('hotels', []), 'Hotel', 'Best Stays')
                if hotels_list:
                    formatted_reply += 'Best Hotels:'
                    formatted_reply += f"<ul> {hotels_list} </ul>"

                food_list = self.format_category_list(day_data.get('food', []), 'Restaurant', 'Top Restaurants')
                if food_list:
                    formatted_reply += 'Top Restaurants:'
                    formatted_reply += f"<ul> {food_list} </ul>"

        return formatted_reply
        
    def format_events_response(self, formatted_response, category=None):
            """
            Formats the GPT response with trip details, attractions, hotels, and food information.
            Args:
            - formatted_response (dict): Response data from OpenAI GPT.
            Returns:
            - str: Formatted reply.
            """
            location = {"lat":formatted_response["city_coordinates"][0], "lng":formatted_response["city_coordinates"][1]}
            args_list = ("Events Calendar", location, settings.GOOGLE_API_KEY, set(), [], True)
            data = helper.fetch_pois_for_smart_search(args=args_list)
            if data:
                formatted_reply = f"<h5>Here is the list of {helper.get_key_from_value(target_value=category)} near {formatted_response['city_name']}</h5>"
                if location:
                    for item in data:
                        formatted_reply += "<li>"+ item["name"] +"</li>"
                return formatted_reply
            return f"We apologize, but there are currently no {helper.get_key_from_value(target_value=category)} available in {formatted_response['city_name']}. Please check again later or try a different location."

    def format_fuel_station_response(self, formatted_response, category):
        """
        Formats the GPT response with trip details, attractions, hotels, and food information.
        Args:
        - formatted_response (dict): Response data from OpenAI GPT.
        Returns:
        - str: Formatted reply.
        """
        formatted_reply = f"<h5>Here is the list of {helper.get_key_from_value(target_value=category)} near {formatted_response['city_name']}</h5>"

        location = {"lat":formatted_response["city_coordinates"][0], "lng":formatted_response["city_coordinates"][1]}               
        if location:
            pois = helper.get_pois_around_location(location, api_key=settings.GOOGLE_API_KEY, type_of_place=category)
            for item in pois:
                formatted_reply += "<li>"+ item["name"] +"</li>"
        return formatted_reply


    def format_food_response(self, formatted_response, category):
        """
        Formats the GPT response with trip details, attractions, hotels, and food information.
        Args:
        - formatted_response (dict): Response data from OpenAI GPT.
        Returns:
        - str: Formatted reply.
        """
        location = {"lat":formatted_response["city_coordinates"][0], "lng":formatted_response["city_coordinates"][1]}
        flag = False if category in ["tourist_attraction"] else True
        args_list = (helper.get_key_from_value(target_value=category), location, settings.GOOGLE_API_KEY, set(), [], flag)
        data = helper.fetch_pois_for_smart_search(args=args_list)
        if data:
            formatted_reply = f"<h5>Here is the list of {helper.get_key_from_value(target_value=category)} near {formatted_response['city_name']}</h5>"
            if location:
                for item in data:
                    formatted_reply += "<li>"+ item["name"] +"</li>"
            return formatted_reply
        return f"We apologize, but there are currently no {helper.get_key_from_value(target_value=category)} available in {formatted_response['city_name']}. Please check again later or try a different location."


    def format_category_list(self, items, category_name, best_title):
        """
        Formats a list of items in a category.

        Args:
        - items (list): List of items in the category.
        - category_name (str): Name of the category.
        - best_title (str): Suggested best title for the category.

        Returns:
        - str: Formatted list of items.
        """
        formatted_list = [item for item in items if not item.lower().startswith(category_name.lower())]
        if formatted_list:
            formatted_list = [f"<li> {item} </li>" for item in formatted_list]
            return ''.join(formatted_list)
        else:
            return []

    def process_user_query(self, user_query, context):
        """
        Processes the user's query and generates a response if it is travel-related.

        Args:
        - user_query (str): The user's input/query.
        - context (dict): The context information, including previous queries.

        Returns:
        - str: The assistant's reply or a message indicating that only travel-related queries are supported.
        """


        if self.is_city_related(user_query, context):
            user_query += (
                '? .Provide me brief information on question')
            response = self.generate_chatgpt_response(user_query)
            return response

        trip_keywords = ["travel", "plan", "trip", "journey", "solo"]

        hotel_keywords = ["deals", "deal"]

        attractions_keywords = ["enticements", "allurements", "charms", "appeals", "lures", "temptations",
                                "fascinations", "drawings", "pleasures", "delights", "distractions", 
                                "allures", "magnetisms", "charisma", "amusements", "attractions", "attraction"]

        events_keywords = ["occasions", "happenings", "occurrences", "incidents", "episodes", "instances",
                           "circumstances", "situations", "developments", "proceedings", "events", "event"]

        food_keywords = ["food", "foods", "cuisine", "cuisines", "dish", "dishes", "recipe", "recipes",
                         "ingredients", "cooking", "nutrition","nutritions", "flavor","flavors", "taste",
                         "gourmet","gourmets", "culinary", "menu", "appetizer", "maincourse", "maincourses",
                         "dessert", "desserts", "beverage","beverages", "spice", "fresh", "organic", "foodie",
                         "eatery", "chef", "dining", "savor", "tasty", "savory", "sour"]
        
        charging_station = ["gas", "station", "service", "illing", "petrol", "fuel", "gasoline", "petrol", "pump", "fueling", 
                            "gas", "garage", "gas", "charging", "point", "charging", "electric", "vehicle", 
                            "hub", "power", "plug-in"]
        
        weird_and_wacky_keywords = ["eccentric", "quirky", "zany", "offbeat", "whimsical", "unconventional", "oddball", 
                                    "kooky", "outlandish", "far-out", "freaky", "bizarre", "out-of-the-ordinary", 
                                    "peculiar", "off-the-wall", "off-kilter", "singular", "whacky", "surreal",
                                    "nutty", "weird", "wacky"]

        if self.is_travel_related(user_query, context):
            # if any(keyword in user_query.lower() for keyword in trip_keywords):
            #     user_query += (
            #         "Provide me with a travel plan. Include information like the number of days, "
            #         "'stay': 'Recommend suitable night halts along the route. If the number of days required to travel is more than one, the coordinates of the stay should be the final_destination_of_day', "
            #         "daily plans, final destinations, attractions, route information, and activities in the response JSON format. For example, "
            #         '{"number_of_days": 2, "day1": {"text": "On Day 1, visit local attractions and enjoy outdoor activities. Explore nearby attractions like [Attraction1], [Attraction2], and [Attraction3].", '
            #         '"final_destination_of_day": ["17.3850", "78.4867"], "attractions": ["Attraction1", "Attraction2", "Attraction3"], "hotels": ["Hotel1", "Hotel2", "Hotel3"], "food": ["Restaurant1", "Restaurant2", "Restaurant3"]}, '
            #         '"day2": {"text": "On Day 2, take a scenic route to [Destination]. Visit [Landmark] and try local cuisine at [Restaurant1], [Restaurant2], and [Restaurant3].", '
            #         '"final_destination_of_day": ["17.3850", "78.4867"], "attractions": ["Attraction1", "Attraction2", "Attraction3"], "hotels": ["Hotel1", "Hotel2", "Hotel3"], "food": ["Restaurant1", "Restaurant2", "Restaurant3"]}, '
            #         '"locations": [{"city_name": "city_name", "coordinates": ["17.3850", "78.4867"]}, {"city_name": "city_name", "coordinates": ["17.3850", "78.4867"]}]}'
            #     )

            #     response = self.generate_chatgpt_response(user_query)
            #     response = self.convert_to_json(response)
            #     formatted_response = self.format_response(response)
            #     return formatted_response

            # elif any(keyword in user_query.lower() for keyword in charging_station):
            #     user_query += (
            #         '"find the location name from the above sentence and return answer in below format for example ''{"city_name":"name", city_coordinates:[]}''"'
            #         )
            #     response = self.generate_chatgpt_response(user_query)
            #     parsed_data = json.loads(response)
            #     if len(parsed_data["city_coordinates"]) == 0:
            #         lat, long = helper.get_coordinates(parsed_data.get("city_name"))
            #         parsed_data.update({"city_coordinates":[lat, long]})
            #     formatted_response = self.format_fuel_station_response(parsed_data,category="electric_vehicle_station")
            #     return formatted_response

            # if any(keyword in user_query.lower() for keyword in hotel_keywords):
            #     user_query += (
            #         '"find the location name from the above sentense and return answer in below format for example ''{"city_name":"name", city_coordinates:[]}''"'
            #         )
            #     response = self.generate_chatgpt_response(user_query)
            #     parsed_data = json.loads(response)
            #     if len(parsed_data["city_coordinates"]) == 0:
            #         lat, long = helper.get_coordinates(parsed_data.get("city_name"))
            #         parsed_data.update({"city_coordinates":[lat, long]})
            #     formatted_response = self.format_food_response(parsed_data, category="lodging")
            #     return formatted_response
                        
            # elif any(keyword in user_query.lower() for keyword in events_keywords):
            #     user_query += (
            #         '"find the location name from the above sentence and return answer in below format for example ''{"city_name":"name", city_coordinates:[]}''"'
            #         )
            #     response = self.generate_chatgpt_response(user_query)
            #     parsed_data = json.loads(response)
            #     if len(parsed_data["city_coordinates"]) == 0:
            #         lat, long = helper.get_coordinates(parsed_data.get("city_name"))
            #         parsed_data.update({"city_coordinates":[lat, long]})
            #     formatted_response = self.format_events_response(parsed_data,category="events")
            #     return formatted_response

            # elif any(keyword in user_query.lower() for keyword in food_keywords):
            #     user_query += (
            #         '"find the location name from the above sentence and return answer in below format for example ''{"city_name":"name", city_coordinates:[]}''"'
            #         )
            #     response = self.generate_chatgpt_response(user_query)
            #     parsed_data = json.loads(response)
            #     if len(parsed_data["city_coordinates"]) == 0:
            #         lat, long = helper.get_coordinates(parsed_data.get("city_name"))
            #         parsed_data.update({"city_coordinates":[lat, long]})
            #     formatted_response = self.format_food_response(parsed_data,category="restaurant")
            #     return formatted_response

            # elif any(keyword in user_query.lower() for keyword in attractions_keywords):
            #     user_query += (
            #         '"find the location name from the above sentence and return answer in below format for example ''{"city_name":"name", city_coordinates:[]}''"'
            #         )
            #     response = self.generate_chatgpt_response(user_query)
            #     parsed_data = json.loads(response)
            #     if len(parsed_data["city_coordinates"]) == 0:
            #         lat, long = helper.get_coordinates(parsed_data.get("city_name"))
            #         parsed_data.update({"city_coordinates":[lat, long]})
            #     formatted_response = self.format_food_response(parsed_data,category="tourist_attraction")
            #     return formatted_response

            # elif any(keyword in user_query.lower() for keyword in weird_and_wacky_keywords):
            #     user_query += (
            #         '"find the location name from the above sentence and return answer in below format for example ''{"city_name":"name", city_coordinates:[]}''"'
            #         )
            #     response = self.generate_chatgpt_response(user_query)
            #     parsed_data = json.loads(response)
            #     if len(parsed_data["city_coordinates"]) == 0:
            #         lat, long = helper.get_coordinates(parsed_data.get("city_name"))
            #         parsed_data.update({"city_coordinates":[lat, long]})
            #     formatted_response = self.format_food_response(parsed_data,category="point_of_interest")
            #     return formatted_response
            # else:
            response = self.generate_chatgpt_response(user_query)
            # if "sorry" in response:
            #     user_query += "Provide me with a travel plan for this question, "
            #     response = self.generate_chatgpt_response(user_query)
            return response
        else:
            return constants.standard_question_patterns
