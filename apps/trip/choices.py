
class ChoicesFields():
    ATTRACTIONS_CHOICE = (
        ("museums", "Museums"),
        ("sightseeing", "Sightseeing"),
        ("themeparks", "Theme Parks"),
        ("zoosaquarium", "Zoos & Aquarium"),
        ("others", "Others"))

    EVENT_CHOICE = (
        ("music", "Music"),
        ("festivals", "Festivals"),
        ("sports", "Sports"),
        ("holidays", "Holidays"),
        ("others", "Others"))

    category_to_field = {
        "Hotels": "liked_hotels",
        "Extreme Sports": "liked_extremesports",
        "Historical Sites": "liked_historicalsites",
        "Events Calendar": "liked_events",
        "Weird and Wacky": "liked_wierdandwacky",
        "National Park": "liked_parks",
        "Attractions": "liked_attractions",
    }
