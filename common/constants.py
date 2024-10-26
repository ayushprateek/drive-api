class Constant:
    """Constants Values"""
    VERIFICATION_CODE_EXPIRE_TIME = 10  # Minutes

    # CATEGORIES
    # ATTRACTION = "Attractions"
    # FOOD = "Food"
    # WEIRDANDWACKY = "Weird and Wacky"
    # NATIONAL_PARK = "National Park"
    # FAMILY_FUN = "Family Fun"
    SITES = "Sites"
    # EXTREME_SPORTS = "Extreme Sports"
    # EVENT_CALENDAR = "Events Calendar"
    # CAMPING = "RV & Camping"
    HOTEL = "Hotels"

    # DOMAINS
    MIAMI_BEACH_SITE = 'www.miamiandbeaches.com'
    RESTAURANT_SITE = 'www.restaurantji.com'
    VISITORLANDO_SITE = 'www.visitorlando.com'
    FLORIDA_STATE_SITE = 'www.floridastateparks.org'
    FLORIDA_ATTRACTIONS_SITE = 'www.floridaattractions.com'
    VISITFLORIDA_SITE = "www.visitflorida.com"
    ATLASOBSCURA_SITE = "www.atlasobscura.com"
    BITLMOREHOTEL_SITE = "www.biltmorehotel.com"
    MYFISHERMANSCOVE_SITE = "myfishermanscove.com"
    VISITPANAMACITYBEACH_SITE = "www.visitpanamacitybeach.com"
    FLORIDADIVING_SITE = "floridadiving.wordpress.com"
    VISITTAMPABAY_SITE = "www.visittampabay.com"
    LEDGERNEWS_SITE = "www.theledger.com"
    HILTON_SITE = "www.hilton.com"
    CHOICE_HOTELS = "www.choicehotels.com"
    WYNDHAM_HOTELS = "www.wyndhamhotels.com"
    IHG_HOTELS = "www.ihg.com"
    MARRIOT_HOTELS = "www.marriott.com"
    OFFTHECHART = "offthechartsinn.com"
    DUNNELON_MOTELS = "www.dunnellonmotels.com"
    EVENT_BRITE = "www.eventbrite.com"
    WAKESURFTAMPABAY = "wakesurftampabay.com"
    THELIFTADVENTUREPARK_SITE = "theliftadventurepark.com"
    VISITLAUDERDALE = "www.visitlauderdale.com"
    STRANAHANHOUSE_SITE = "stranahanhouse.org"
    GROUPON_SITE = "www.groupon.com"
    MBTALLAHASSEE = "mbtallahassee.com"
    BESTWESTERN = "www.bestwestern.com"

    # GOOGLE MAPS - PLAN TRIP
    AVERAGE_SPEED = 60  # km/h
    DISCOUNT_TYPE_CHOICES = ["Hotels + Lodging", "Attractions", "Restaurants", "Cheap Gas", "ALL"]
    DISCOUNT_TYPE_SAVE_MODULE_CHOICES = ["Hotels", "Attractions", "Food", "Cheap Gas"]
    TRAVEL_TIME = ["4 Hours", "6 Hours", "8 Hours", "custom Hours"]


class ApplicationMessages:
    """Project wise generic response messages"""

    SUCCESS = "Success"
    WELCOME_NOTE = "Hello Welcome To"
    INVALID_REQUEST = "Invalid Request !"
    FILE_EXCEEDS_SIZE = "File should be less than "
    DELETED = "Data Deleted"
    EMAIL_REGISTERED = "Email Registered"
    EMAIL_SENT = "Email sent successfully"

    # USER Login and Signup
    USER_CREATED = "Account Created Successfully"
    USER_NOT_EXISTS = "User Does Not Exist"
    USER_N_EMAIL_EXISTS = "User with this Email Does not Exist"
    USER_NOT_ACTIVE = "User is not Active!"
    DOES_NOT_EXISTS = "{} not exists"
    EMAIL_PASSWORD_INCORRECT = "Email or Password is incorrect"
    LOGIN_FAIL = "Login Failed"
    INVALID_PASSWORD = "Invalid Password"
    USER_ALREADY_EXIST = "User with this email already Exist!"
    USER_PHONE_ALREADY_EXIST = "You're already registered with us, please login to continue!"
    USER_PROFILE_UPDATED = "Profile Updated Successfully!"

    SOMETHING_WENT_WRONG = "Something Went Wrong!"

    EMAIL_NOT_VERIFIED = (
        "Email is Not Verified, Please verify your email and then Login"
    )
    REST_PASSWORD_LINK_SENT = "Reset password link sent"
    RESET_EMAIL_SUBJECT = "Your Drive AI One-Time Password (OTP)"
    PASSWORD_SET = "Password Set"
    AUTHENTICATION_FAILED = "Incorrect Credentials"
    INVALID_AUTH_TOKEN = "This link is either invalid or got expired."
    PASSWORD_SHOULD_NOT_SAME = "Current Password and New password should not the same"
    CURRENT_NEW_PASSWORD_NOT_SAME = "Entered New & Retype pass are not same"
    PASSWORD_TOO_SHORT = "Minimum password length is 8 characters"
    PASSWORD_TOO_LONG = "Maximum password length is 25 characters"
    PASSWORD_VALIDATION = (
        "Minimum length of password is 8, Maximum length of password is 24 and contain "
        "one UpperCase, one LowerCase and a Special Character"
    )
    CURRENT_PASSWORD_INCORRECT = "Current password is incorrect"
    PASSWORD_CHANGED = "Password Changed Successfully"
    USER_AUTH_FAILED = "User Authentication Failed"
    LOGOUT_SUCCESSFULLY = "You've been successfully logged out!"
    LOGOUT_FAILED = "Logout Failed!"

    ATTEMPTS_EXHAUSTED = "You've exhausted your attempts. Try next week!"
    BAD_REQUEST = "Bad Request!"

    # FORGOT/RESET PASSWORD MESSAGES
    VERIFICATION_CODE_SENT = "The Verification code sent successfully!"
    VERIFICATION_CODE_EXPIRED = "The verification code has expired."
    INVALID_VERIFICATION_CODE = "Invalid verification code provided!"

    # LISTING MESSAGES
    CATEGORY_DOES_NOT_EXIST = "Category Does Not Exists"
    CITY_DOES_NOT_EXIST = "City Does Not Exists"
    CITY_UPDATE_SUCCESSFULLY = "City Updated Successfully."


common_descriptions = [
    "Discover the perfect blend of comfort and convenience at our hotel. Our well-appointed rooms, stunning views, and top-notch service ensure a memorable stay.",
    "Indulge in luxury and relaxation at our hotel, where every detail is designed to meet your needs. From upscale amenities to attentive service, we offer an exceptional experience.",
    "Immerse yourself in the heart of the city at our hotel, surrounded by iconic landmarks and vibrant culture. Our stylish rooms and prime location make us the ideal choice for your stay.",
    "Unwind and recharge in our modern, elegant hotel, offering a peaceful retreat from the bustling city. Enjoy first-class facilities and personalized service throughout your visit.",
    "Experience the epitome of hospitality at our hotel, where a warm welcome and a range of amenities await. Our dedication to your comfort ensures a delightful and relaxing stay.",
    "At our hotel, you'll find a harmonious balance of contemporary style and comfort. Take advantage of our world-class services and make the most of your time in this vibrant city.",
    "Discover a haven of luxury and tranquility with stunning views and exceptional service.",
    "Immerse yourself in elegance and comfort, offering a perfect blend of modern amenities and classic charm.",
    "Indulge in a delightful stay where convenience meets relaxation, providing a range of first-class services.",
    "Experience the ultimate in sophistication and style, offering a perfect retreat for leisure and business travelers.",
    "Unwind in a serene atmosphere, enjoying top-notch facilities and personalized hospitality.",
    "Elevate your travel experience in a contemporary setting designed for utmost comfort and convenience.",
    "Escape to a world of opulence and refinement, promising an unforgettable stay with every modern comfort.",
    "Savor the essence of luxury and convenience in a setting that reflects unparalleled warmth and elegance.",
    "Revel in a delightful stay characterized by modern amenities and a welcoming ambiance.",
    "Immerse yourself in a world of comfort and luxury, offering an oasis of relaxation in the heart of the city."
]


standard_question_patterns = "<h4> Here are some standard question patterns that you are thinking of ...!</h4>\
    <ul><li>Search a trip from Oklahoma to Miami</li> <li>Find events in California</li>\
    <li>Create a 5 days trip from Miami to Jacksonville</li>\
        <li> What would be the best attractions from miami to Oklahoma.</li>\
            <li> What's the most convenient way to travel from miami to Miami Beach.</li>\
                <li> What are some must-try local restaurant in Miami.</li>\
                    <li>Find me affordable hotels in New York City near Times Square for a weekend in August</li>\
                        <li>Suggest some events in Miami</li>\
                            <li>Suggest food in Lakecity</li>\
                                <li>Find restaurants in Miami</li>\
                                <li>Search a trip from Oklahoma to Miami</li></ul>\
                                    "
