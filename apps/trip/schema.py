from drf_yasg import openapi

category_data_list_response = openapi.Response(
    description="Success",
    examples={
        "application/json": {
            "success": True,
            "code": 200,
            "data": {
                "count": 30,
                "next": "http://127.0.0.1:8000/trip/list/?category=Food&page=2&page_size=3",
                "pages": 10,
                "previous": None,
                "results": [
                    {
                        "id": "6e29384d-6168-4542-a2b3-528c95ba62ad",
                        "name": "Aguacate Sanctuary of Love",
                        "city_name": "Miami",
                        "latitude": "25.727836",
                        "longitude": "-80.390912",
                        "description": "It felt so serene to be here. While it was very hot outside, they tried to accommodate with fans. There was a space for yoga, chickens to roam around and try to eat your food, vegan foods in multiple trucks, cute nooks to read or eat at, and lots of vibrant decor/ colors. I had the yogo berry smoothie & the aguacate garden toast. Good kick to my morning start!",
                        "images": [],
                        "meta_data": {
                            "address": {
                                "latitude": "25.727836",
                                "longitude": "-80.390912",
                                "postalCode": "33175",
                                "addressRegion": "Florida",
                                "streetAddress": "12100 SW 43rd St",
                                "addressCountry": "US",
                                "addressLocality": "Miami",
                            },
                            "scraped_from": "https://www.restaurantji.com/fl/miami/aguacate-sanctuary-of-love-/",
                        },
                    },
                    {
                        "id": "ac6f04f5-bcf2-41d5-a83c-84b22985fa78",
                        "name": "MOFONGO RESTAURANT CALLE 8",
                        "city_name": "Miami",
                        "latitude": "25.765514",
                        "longitude": "-80.221498",
                        "description": "Need a little Havana in your life?  Then this is the place for you!Large food portions. Plenty of flavor and ambiance, all packed in a small Cafe style restaurant.Located in the heart of Little Havana.",
                        "images": [],
                        "meta_data": {
                            "address": {
                                "latitude": "25.7655136",
                                "longitude": "-80.2214984",
                                "postalCode": "33135",
                                "addressRegion": "Florida",
                                "streetAddress": "1644 SW 8th St",
                                "addressCountry": "US",
                                "addressLocality": "Miami",
                            },
                            "scraped_from": "https://www.restaurantji.com/fl/miami/mofongos-restaurant-/",
                        },
                    },
                    {
                        "id": "3faa8dc3-aa13-4b5d-8266-d7bfff5c24b0",
                        "name": "R House Wynwood",
                        "city_name": "Miami",
                        "latitude": "25.802684",
                        "longitude": "-80.198995",
                        "description": "Our Waiter ANTHONY was AMAZING!!  I LOVE HIM! He kept things moving and I was impressed with his dancing skills in the half time show. So cute…and a great server!!",
                        "images": [],
                        "meta_data": {
                            "address": {
                                "latitude": "25.8026844",
                                "longitude": "-80.1989946",
                                "postalCode": "33127",
                                "addressRegion": "Florida",
                                "streetAddress": "2727 NW 2nd Ave",
                                "addressCountry": "US",
                                "addressLocality": "Miami",
                            },
                            "scraped_from": "https://www.restaurantji.com/fl/miami/r-house-wynwood-/",
                        },
                    },
                ],
            },
        }
    },
)

category_data_list_params = [
    openapi.Parameter(
        "category",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_STRING,
        description="Category Choice",
        required=True,
    )
]

category_list_response = openapi.Response(
    description="Success",
    examples={
        "application/json": {
            "success": True,
            "code": 200,
            "data": {
                "count": 11,
                "next": None,
                "pages": 1,
                "previous": None,
                "results": [
                    {"name": "Attractions", "image_url": "https://"},
                    {"name": "Food", "image_url": "https://"},
                    {"name": "Family Fun", "image_url": "https://"},
                    {"name": "National Park", "image_url": "https://"},
                    {"name": "RV & Camping", "image_url": "https://"},
                    {"name": "Weird and Wacky", "image_url": "https://"},
                    {"name": "Events Calendar", "image_url": "https://"},
                    {"name": "Historical Sites", "image_url": "https://"},
                    {"name": "Extreme Sports", "image_url": "https://"},
                    {"name": "City", "image_url": "https://"},
                    {"name": "Hotels", "image_url": "https://"},
                ],
            },
        }
    },
)

city_list_response = openapi.Response(
    description="Success",
    examples={
        "application/json": {
            "success": True,
            "code": 200,
            "data": {
                "count": 6,
                "next": "http://127.0.0.1:8000/trip/city/list/?page=2&page_size=3",
                "pages": 2,
                "previous": None,
                "results": [
                    {
                        "name": "Destin",
                        "latitude": None,
                        "longitude": None,
                        "images": [],
                        "attraction": {},
                        "camp": {
                            "name": "Tallahassee RV Park",
                            "description": "ABOUT Located in the rolling hills just east of Tallahassee. The park is very quiet, covered with a large variety of flowering plants and shrubs. Giant pines, magnolia, dogwood and other native trees dot the landscape. A country setting convenient to all of Tallahassee's dining and entertainment. Enjoy the long pull-thru sites with full hook-ups. Big rigs are welcome. Relax in the large recreation room or sparkling swimming pool. You can e-mail using Wi-Fi while you do your laundry.",
                            "images": [
                                "https://s3.amazonaws.com/nfx-drive-ai/image/49332_l6s7up1wnb02ljyvhfpu9j59sfar6bmf_96da9135-5056-a36a-0bfe34f5db3a05e1.jpg"
                            ],
                        },
                        "event": {
                            "name": "God Owl",
                            "description": "Awesome",
                            "images": ['["https://"]'],
                        },
                        "extreme_sport": {},
                        "family_fun": {},
                        "food": {},
                        "historical_site": {},
                        "hotel": {
                            "name": "Welcome to Fairfield Inn & Suites Destin",
                            "description": "                        Relax on some of the Florida Panhandle's most picturesque beaches during your stay at Fairfield Inn and Suites Destin. Enjoy easy access to the gulf, directly across the street from the hotel, or venture out and discover Destin's many shops, restaurants and attractions. Feel at home at our Destin, FL, lodging near the beach with family-friendly amenities including free Wi-Fi, complimentary hot breakfast and free onsite parking. Keep in shape while staying in the heart of Destin with a visit to our hotel fitness center with cardio equipment and free weights. Then cool off with a dip in our indoor/outdoor pools. Kick back at the end of the day in spacious hotel rooms and suites, featuring plush bedding, mini-fridges, microwaves and beautiful Florida views in select rooms. At Fairfield Inn and Suites Destin, you are our number 1 priority. That is why our friendly Panhandle staff offers the Fairfield 100 percent Guarantee, where we promise you will be satisfied or we will make it right.                    ",
                            "images": [
                                "hotel-images/fi-vpsdf-double-queen-room-57047-10089:Square",
                                "hotel-images/fi-vpsdf-front-entrance-94148-10110:Square",
                                "hotel-images/fi-vpsdf-lobby-02655-09218:Square",
                                "hotel-images/fi-vpsdf-double-queen-room-57047-10089:Classic-Hor",
                                "hotel-images/fi-vpsdf-lobby-02655-09218:Classic-Hor",
                                "hotel-images/fi-vpsdf-front-entrance-94148-10110:Classic-Hor",
                            ],
                        },
                        "park": {},
                        "weirdandwacky": {},
                    },
                    {
                        "name": "Ocala",
                        "latitude": None,
                        "longitude": None,
                        "images": [],
                        "attraction": {},
                        "camp": {},
                        "event": {},
                        "extreme_sport": {},
                        "family_fun": {},
                        "food": {},
                        "historical_site": {},
                        "hotel": {},
                        "park": {},
                        "weirdandwacky": {},
                    },
                    {
                        "name": "Tallahassee",
                        "latitude": "30.438260",
                        "longitude": "-84.280730",
                        "images": [
                            "https://s3.amazonaws.com/nfx-drive-ai/image/273px-Downtown_Tallahassee_2023.png"
                        ],
                        "attraction": {},
                        "camp": {},
                        "event": {},
                        "extreme_sport": {},
                        "family_fun": {},
                        "food": {
                            "name": "DEEP Brewing Company",
                            "description": "Stopped at this little joint aftet traveling from the Pacific NW, and let me tell you coming from a state that specializes in Beer this place absolutely blew my mind. Everything they had was fantastic from hazy IPA's to stouts. Definitely recommend, and definitely returning ?",
                            "images": [
                                "https://s3.amazonaws.com/nfx-drive-ai/image/BRwjbL61VR.jpg"
                            ],
                        },
                        "historical_site": {},
                        "hotel": {},
                        "park": {
                            "name": "Madison Blue Spring State Park",
                            "description": " Welcome to Madison Blue Spring State Park This crystal-clear, first-magnitude spring is a popular spot for swimming and cave diving.    About 82 feet wide and 25 feet deep, the spring bubbles up into a limestone basin along the west bank of the Withlacoochee River. Scenic woodlands of mixed hardwoods and pines create a picturesque setting for picnicking, paddling and wildlife viewing. Voted the No. 1 swimming hole in the country by USA Today, Madison Blue Spring is a family favorite destination and a fantastic place to spend the day. ",
                            "images": [
                                "https://s3.amazonaws.com/nfx-drive-ai/image/MBSP_Hero_IMG_3654.jpg"
                            ],
                        },
                        "weirdandwacky": {},
                    },
                ],
            },
        }
    },
)

trip_list_response = openapi.Response(
    description="Success",
    examples={
        "application/json": {
            "success": True,
            "code": 200,
            "data": {
                "count": 2,
                "next": None,
                "pages": 1,
                "previous": None,
                "results": [
                    {
                        "type": "food",
                        "data": [
                            {
                                "name": "Bird's Aphrodisiac Oyster Shack",
                                "description": "Had a very nice time there. It's been about 10 years since we've visited Birds (moved out of state) and it's nice to know that they've only changed for better. Food is great too. We love their oysters and variety of the menu. If you're in the area I def recommend giving them a try.",
                                "images": [
                                    "https://s3.amazonaws.com/nfx-drive-ai/image/aqcZcajnp1.jpg"
                                ],
                            },
                            {
                                "name": "Hummingbird Wine Bar",
                                "description": "Lovely place, great selection (even by the glass) very knowledgeable and attentive staff. Good selection of accomplishments too, local produce, high quality deli products.",
                                "images": [
                                    "https://s3.amazonaws.com/nfx-drive-ai/image/E9Zx2gCMab.jpg"
                                ],
                            },
                        ],
                    }
                ],
            },
        }
    },
)

plan_trip_response = openapi.Response(
    description="Success",
    examples={"application/json": {
        "success": True,
        "code": 200,
        "data": {"route": {
            "geocoded_waypoints": [
                {
                    "geocoder_status": "OK",
                    "place_id": "ChIJEcHIDqKw2YgRZU-t3XHylv8",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "geocoder_status": "OK",
                    "place_id": "ChIJ66_O8Ra35YgR4sf8ljh9zcQ",
                    "types": [
                        "locality",
                        "political"
                    ]
                }
            ],
            "routes": [
                {
                    "bounds": {
                        "northeast": {
                            "lat": 30.3330064,
                            "lng": -80.1287327
                        },
                        "southwest": {
                            "lat": 25.7525792,
                            "lng": -81.6590157
                        }
                    },
                    "copyrights": "Map data ©2023 Google, INEGI",
                    "legs": [
                        {
                            "distance": {
                                "text": "347 mi",
                                "value": 558649
                            },
                            "duration": {
                                "text": "4 hours 59 mins",
                                "value": 17965
                            },
                            "end_address": "Jacksonville, FL, USA",
                            "end_location": {
                                "lat": 30.332119,
                                "lng": -81.65562849999999
                            },
                            "start_address": "Miami, FL, USA",
                            "start_location": {
                                "lat": 25.7617059,
                                "lng": -80.1918211
                            },
                            "steps": [
                                {
                                    "distance": {
                                        "text": "492 ft",
                                        "value": 150
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 40
                                    },
                                    "end_location": {
                                        "lat": 25.7630117,
                                        "lng": -80.1914355
                                    },
                                    "html_instructions": "Head <b>north</b> on <b>Brickell Ave</b> toward <b>SE 12th St</b>",
                                    "polyline": {
                                        "points": "uqf|CzmmhN_@IEAWEKCc@KwBa@SEIA"
                                    },
                                    "start_location": {
                                        "lat": 25.7617059,
                                        "lng": -80.1918211
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.1 mi",
                                        "value": 173
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 51
                                    },
                                    "end_location": {
                                        "lat": 25.7616832,
                                        "lng": -80.1919705
                                    },
                                    "html_instructions": "Make a <b>U-turn</b> at <b>SE 11th St</b>",
                                    "maneuver": "uturn-left",
                                    "polyline": {
                                        "points": "yyf|CnkmhNG^r@LXDd@D\\Ff@Jp@Nd@J"
                                    },
                                    "start_location": {
                                        "lat": 25.7630117,
                                        "lng": -80.1914355
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "423 ft",
                                        "value": 129
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 32
                                    },
                                    "end_location": {
                                        "lat": 25.761603,
                                        "lng": -80.19325040000001
                                    },
                                    "html_instructions": "Turn <b>right</b> onto <b>SE 13th St</b>",
                                    "maneuver": "turn-right",
                                    "polyline": {
                                        "points": "oqf|CxnmhNBh@@LBpA@j@BhA"
                                    },
                                    "start_location": {
                                        "lat": 25.7616832,
                                        "lng": -80.1919705
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.2 mi",
                                        "value": 321
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 64
                                    },
                                    "end_location": {
                                        "lat": 25.7588092,
                                        "lng": -80.1940642
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>S Miami Ave</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "_qf|CxvmhNp@P\\FnB\\b@F\\FdBZXHnAV~@PZH"
                                    },
                                    "start_location": {
                                        "lat": 25.761603,
                                        "lng": -80.19325040000001
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.8 mi",
                                        "value": 1242
                                    },
                                    "duration": {
                                        "text": "2 mins",
                                        "value": 110
                                    },
                                    "end_location": {
                                        "lat": 25.7520564,
                                        "lng": -80.2038467
                                    },
                                    "html_instructions": "At the traffic circle, take the <b>2nd</b> exit and stay on <b>S Miami Ave</b>",
                                    "maneuver": "roundabout-right",
                                    "polyline": {
                                        "points": "q_f|Cz{mhN?@?@A??@?@?@?@?@?@?@?@?@@??@?@@@?@@@@@@??@@??@@?@?@@@?@?@?@?@?@A@?FFNVR\\|BxDrBdDtBjDJPh@z@r@hAPRhBzCNVlBdDrBbDpBdDnBfDpB`DfBzC"
                                    },
                                    "start_location": {
                                        "lat": 25.7588092,
                                        "lng": -80.1940642
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "377 ft",
                                        "value": 115
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 24
                                    },
                                    "end_location": {
                                        "lat": 25.7528756,
                                        "lng": -80.20454769999999
                                    },
                                    "html_instructions": "Turn <b>right</b> onto <b>SW 25th Rd</b>",
                                    "maneuver": "turn-right",
                                    "polyline": {
                                        "points": "kud|C`yohNmAbAuAfA"
                                    },
                                    "start_location": {
                                        "lat": 25.7520564,
                                        "lng": -80.2038467
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "3.7 mi",
                                        "value": 5980
                                    },
                                    "duration": {
                                        "text": "4 mins",
                                        "value": 269
                                    },
                                    "end_location": {
                                        "lat": 25.8034526,
                                        "lng": -80.2055907
                                    },
                                    "html_instructions": "Turn <b>right</b> to merge onto <b>I-95 N</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "ozd|Cl}ohNi@w@m@y@c@o@w@eAa@i@KMu@cA[c@u@cAACU]IEQWAAQAEIMQKSQWIOAAKSU]EGKSCCKMMSKKCEGGGIOMMKCCKKECCCMIKIEAWQYOECMEECMEECOECAKE[IC?QGUCEAICKCSCQCOA_@CU?W?UAW?m@Ai@AU?W?]Aa@?e@AC?a@Ae@?m@AY?i@A_AA}BC[AE?O?WAS?[?U?MAM?U@U?Q@W@U@[@WBU@mAJm@DQBC?U@i@DqBN}ALYBWB_BJA@_AFg@DW@W@U@W?G?K?U?G?OAU?SAUCUAUCA?e@G]GSCWGWEQEUEQEWGQEQGKCOEc@Mq@UWIQGSGSGSGUIUI_@MyAe@}@WQGMCICMEEAQCWESCOAOAUAa@CS?[?O@O?K@G?K@S@G@O@SBOBE@SBSDUFQDUFSFSHQFSHA?SHSFWJODUHSHSFQDWFQDYDQDUBI@I@W@SBU@[@y@@o@@w@@sBBY?S@aCBq@@]@eA@o@?g@@e@BaAFs@HM@S@SBiC\\a@Hk@L}@Te@NQFE@UHg@RUJa@PIB[P{@Zy@ZgBt@MFeAb@iAd@UJg@RMFm@VOFm@V_@NyAn@G@m@VaA`@o@XGBs@X[N[LQHw@Z[LC@C@A@C@A?IDMFyAn@aCbAkBt@kA`@WHcAXo@Lq@Jm@LQBa@HE?SBSB{@HuAFW@_@@a@@cA@oB?_B@y@@S?aA@iB@i@?A?a@?cC@wD@{@@gA@}CDeABcA@wBDcAB_ADs@@{EFgA@"
                                    },
                                    "start_location": {
                                        "lat": 25.7528756,
                                        "lng": -80.20454769999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "7.4 mi",
                                        "value": 11936
                                    },
                                    "duration": {
                                        "text": "7 mins",
                                        "value": 401
                                    },
                                    "end_location": {
                                        "lat": 25.9104018,
                                        "lng": -80.2100117
                                    },
                                    "html_instructions": "Keep <b>left</b> at the fork to continue on <b>I-95 Express</b>, follow signs for <b>Express Lanes</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "fork-left",
                                    "polyline": {
                                        "points": "qvn|C|cphNEDEBEBIBI@e@?_@@W?aA@o@@W@s@?uAB}CBW@W?O?U@wA@yCDC?g@@mBB}@@k@@m@?e@@U?I@S?_A@e@@[?w@@g@@u@@cA@k@?k@@i@?A?_@@A?C?A?Q?S?M?i@@Q?W?U@U?Y?e@@qA@Q?m@?U@g@?m@@_@?_A@k@@U?kA@A?gB@_@@g@@o@?K@K?W?W@U?c@@G?m@?{ABY?gABS?E?S@_BBk@@a@@M?u@@i@@a@@sABc@@k@Bs@@A?kADe@@g@BaABkABC?u@Bi@@C?g@@a@@u@B]@c@@c@@Q?a@@aAB[?O@K?U?Y?e@?Y?OAK?[Ac@Ae@Ce@E[C]CIAWCi@IM?w@MoAUw@Os@Ko@Im@Ga@Ec@Ec@EiAEs@ASAU?[?S?W?g@?k@Bo@@G?C@c@@gBBO?oCF{BBI?w@@q@BcEFmA@C?y@BgA?eC@Q?wA?qAAyCAm@?k@?Y?aA?Q@S?K?y@@Q@}@AE?S?Q@A?S?k@@k@Bk@D}@Hc@F}@PC?YFq@N]Ls@TiBr@C@]Lm@TUJ_@LA?MDQFWF{@TSDK@YDYF_@Da@D[Bw@DO@W?kAD_BBiBFs@@kADkGNQ@C?oCFm@BW?k@@Y@c@?W@gAB_A@mKJg@?yABqBBwGFyABo@?eDDs@@uA@qCBa@@oCBU?Y@Y?K?M@q@?cCB{FF{CBcCB_HHuA@_DBQ?iCBq@@q@@sCBG?O@_@?i@@m@B{@BgAFA?g@BcAFk@De@DK?I@A?]BI?k@Bw@Bs@BW?iABcA@_@@G?Q?]@i@@Y?I?S?M?E?W@S?W@Q?W@U?S@q@@O?Q?O@Q?S?U@U?U@U?U@S?W@U?U@U?W@E?K?W@U?U@U?S?S@[?Q@W?U@U?S@S?W@U?U?U@S?U@U?W?[?Q?U?S?UAA?U?U?UASA[?OASAS?UAUAU?SASAU?SAS?S?U?S?U?S?U?c@?{@Bc@@e@@U?U@W?S@W?k@@]@M?i@@k@Bi@@i@@cA@S@U?Y@i@@k@@U?i@Bk@@W?i@@]@y@@[@e@@c@@}@@c@@U?i@Bm@@k@@i@@A?k@@k@@m@@i@@}@Bk@@U?m@@k@@{@Bc@@I?wCFS?k@@i@@i@@e@@U@g@@k@@g@@c@@eBBC@gBBA?q@BW?e@@A?{DFa@@S@c@@sBFeAFi@Bc@B_BJG?c@@?@a@@Q@y@Bm@BgBFa@@e@@g@@K?S?e@@c@?e@@Q?S?yC@K?OAO?_B?c@AiA?[?GAe@?iLAI?y@AcB?_BAqC@cA?"
                                    },
                                    "start_location": {
                                        "lat": 25.8034526,
                                        "lng": -80.2055907
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "387 ft",
                                        "value": 118
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 4
                                    },
                                    "end_location": {
                                        "lat": 25.9114363,
                                        "lng": -80.2099051
                                    },
                                    "html_instructions": "Take the exit toward <b>Florida Turnpike</b>/<wbr/><b>FL-826</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "_sc}Cp_qhNUE]?e@@w@?O@MAOECAIEAA"
                                    },
                                    "start_location": {
                                        "lat": 25.9104018,
                                        "lng": -80.2100117
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.5 mi",
                                        "value": 802
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 32
                                    },
                                    "end_location": {
                                        "lat": 25.9186414,
                                        "lng": -80.21019249999999
                                    },
                                    "html_instructions": "Merge onto <b>I-95 N</b>",
                                    "maneuver": "merge",
                                    "polyline": {
                                        "points": "oyc}C|~phNeB?[?oDBGAK?A??@{@?yHHoBDc@@g@@qEJs@B_HN"
                                    },
                                    "start_location": {
                                        "lat": 25.9114363,
                                        "lng": -80.2099051
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "1.2 mi",
                                        "value": 1954
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 81
                                    },
                                    "end_location": {
                                        "lat": 25.9348563,
                                        "lng": -80.2155609
                                    },
                                    "html_instructions": "Take exit <b>12 A</b> on the <b>left</b> for <b>Florida's Turnpike</b> toward <b>Turnpike</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "ramp-left",
                                    "polyline": {
                                        "points": "ofe}Ct`qhNQLI@k@Dm@Fu@HeANc@H}@N_@HI@q@JYFWDYDMB_@FOBm@JA?I@A?SD]D_@FA?I@YDa@HI@I@s@HuAPe@FA?i@Fc@FU@o@Fe@F]@g@D{@FUBi@DO@E?WBE?M@k@DWBg@DW@i@DaAFSBWBU@O@E@S@WBS@c@BWBK@c@BM@UB]BiAJG?[BgAH}@Fo@Dy@FC?G@[@UBC?o@Fm@DQ@y@FS@UBG?MBU@IBI@KBG@QDIBKBQHIBIFULMHSNOLGFMNMNEFEFMRg@x@SZY`@GHW^SXOR]d@EDUZa@f@k@l@]`@EV"
                                    },
                                    "start_location": {
                                        "lat": 25.9186414,
                                        "lng": -80.21019249999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "108 mi",
                                        "value": 174478
                                    },
                                    "duration": {
                                        "text": "1 hour 33 mins",
                                        "value": 5560
                                    },
                                    "end_location": {
                                        "lat": 27.4049094,
                                        "lng": -80.3988579
                                    },
                                    "html_instructions": "Merge onto <b>Florida's Tpke</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "merge",
                                    "polyline": {
                                        "points": "{kh}CfbrhNaB`B[Z}A~A{@z@k@l@KJOP]Zc@b@STUVe@d@g@h@IH_@^[\\_@^A@]^i@h@ONYZw@x@UV]\\]\\QPYZGFmBpBi@h@[\\UTEDSTIHON_@^YXg@h@QRiAhASROPYXMLYV_@^GD[X_@\\e@`@s@j@a@\\c@\\c@Z[Vk@`@c@Ze@Zw@d@y@h@e@XQJA@oAp@KFk@ZSHmAl@e@Tk@Tc@RoChAcBn@i@RSHSFi@P_AXi@NSFi@Nu@PeB`@OBu@N]FUDYF_ALg@He@FE@WBk@Hg@Fo@FSBWBUBSBW@SBU@m@DaAFU@w@BA?gADY@{@@}AB{@@{@@oCDeABE?Y@{CDwA@gCDy@@]?gABO@cBBiEFqB@sC@w@?Q?i@@oB@}CDwABsDFaB@i@BqAB_A@q@@i@@wABA?mA@s@@a@@qABU?yBBu@@u@B[@]?eABeA@A?G@i@@sA@U@gA@c@@k@@O?]@k@?i@@U@uHJc@@_HJq@@sABO?[@k@@uABqBBaCDU?S?U@k@?gA?iBAW?kBGUAU?UAMAK?g@EUAWAWAUCUAGAOASAWCMAk@GUCk@Gm@IQCC?UCQCk@IuASUEUESEUEUEMCWGk@Ks@Qu@Q_AUOEi@Mc@MMEGAECGAEACCaAYg@QCAMEaA]aBm@uB}@y@_@SKWMe@U{@c@MIGCm@]OI]Ue@Wa@Ye@YSMQMOIc@[QMQMUOQMi@a@u@k@SOYWQMOOa@]QOcA_AaA_AKKc@c@UU_@_@OO[]MMs@s@OOc@c@KMSQOQc@c@y@y@YY_DaDgCkCeAeAq@q@_AaAOOWU[[[_@QOa@c@_@_@MMWW[[SSi@i@YYYWOOQOEEKISOQQ_@[WSs@k@IGOKQMQO]UQM_@W_@Wm@a@i@[YQQKy@e@m@[aAg@iAk@QIICWMmAg@e@QcAa@OGOG[KOEKEe@O}Ac@SGCASESGi@OWGk@Mm@MUGKAUGUESEg@ISC{@O{@MmAQ_AIq@I[Ck@Ga@Ca@EaAGI?e@CSASA[AC?y@Cy@AI?QAq@?O?_@?[?Q?M?U?g@@_@?I?]@U?i@@U@Q?m@@aCDC?y@@}ABgABC?Q?{@@eCDoBBkDFk@@_BBo@@O?}@@_AB_DDqDDoDFkABU?aBB_EFmEFyCFkBBqBBW@yA@uABk@@kIL[?S@e@?yCDwBDO?iBDm@@m@@g@@E?i@BU@k@@U@U@S@U?U@m@B]Bi@BQ?S@cAFG?mAF_BHaBJmCLA?eDPcDPcBH{BLiCN_I^]BE?{DP{BJS?m@Bc@@aAB_AB_BBO?gABE?M@c@?eCBuABiKLcDDmCDU?gCDk@?aCDuUXyFHyABeA@s@@_B@eABiBB{BB]?iFFiBBmBBy@@c@@cA@i@@[?{@?[@}@@Y@U?Y?Y@c@@i@?k@@y@@E?m@@e@?sBBoCDs@@gCDkDD}HJ_GFaCDeCBi@@W@i@?m@@sABo@?_ABU?W?U@E?O?k@@_@@mCDsDDi@@o@?}@BuA@yABmBBaA@uA@m@@W?S?U@U?M?G?Y?A?S?s@@K@Q?o@@W?i@@m@@k@@i@B[?g@?c@@aABg@@}AHmAFw@@S@c@BU@}AJk@Bc@Bc@BK@}BPO@[@a@@g@BU@]BW@aADqAD}AFeADo@Bw@BaCJA?S@gAD_BF]Be@Ba@@yAHG@iBJ{AJaBJkCTK@sAJu@Dm@FyAJcAJ}@Fw@FaAFq@Fm@DQ@e@D_AF_AFkBJq@DqAF}@Bk@BS@e@@O@c@@G?uADS@aA@o@Bm@?_ABaDDW?_ABsBBi@?}@B[?e@@o@@u@@O?o@@O?S?C@w@?S@K@G@G?K@O@M?S@_A@A?qABQ?O?Q@W?{@@gBBs@@g@@qA@}CDs@@{ABmA@s@@oA@a@?aAA_A?m@CmACKAaBGe@Cq@Eo@Eu@I{@Ga@EKAWCm@GWEKAUCMAWCi@EMAa@Em@IQA_@Em@Gw@Ie@Ec@Ge@EIA_@Ek@Ee@GWCs@EMAm@Eg@EUAm@CiAEs@C{ACi@?kB?g@AQ?W?o@@S@_@@g@@sADk@Bo@Di@BW@SBaAFg@Fk@Do@HkBRaANu@HyARy@JWH}@Js@JYD_@DaALi@Hk@Fe@Hk@Fk@Hk@H{@JUBi@Fk@FWBUBS@i@Dg@DYBg@BU@W@U@g@BY@S@i@@U@U?U@_@?u@@}@@m@@_A?g@@]?cB@o@@uA?Q@W?S?W?S?U@S?Q?S?W@]?s@?o@@cA@U?W?S?i@@W?W?_A@]?eDBsA@aDBuA@yA@_A?Y@aA?m@@wCBk@?i@@yGDmLFS@i@?o@@S?k@?aA@A?[?]@]?S?Y@S?c@?G?U?U@U?Y?S?S@Y?}@@{A?S@}@?E?]@_A?Y@c@?k@?aA@y@@_@?m@?i@@k@@U?eC@U?oBBk@?i@@U?}@@[?K?Y?sB@U?W?aA@aA@W?U?U?W@S?i@@Y?oC@m@@_@?k@?U@U?U?U?U?U@U?U?U?W@U?aA@yA@k@?U?U?S@W?K?K?S?W@k@?W?U@U?U?S?U@S?W?U?S?m@@k@?cA@Q?cA@kGDU?gDBaB?S?W?W?wA@S?U@S?[?U?U?SAW?UAk@AWAaACm@EUAk@Cg@EQAo@EsAMeBQa@Gi@Gm@IqASYEk@Kw@O]GQEk@Mk@M[Ge@Mu@QQGOEUGkBk@_A[c@Oa@MoAe@_@OwAm@WKa@Si@UmBaAsBgA]Uq@_@g@]YOaAq@s@g@c@]WQ[Wm@e@a@[a@]aAy@qAgAyAmAKKYW]Ys@k@i@e@oAcA_Aw@k@e@oAaAEE}@u@eAw@c@]{AkAs@k@]WUQgBuAs@i@]WWSGEQOMKOKCCYUIESQk@c@IIQMYUa@[e@_@w@m@]WQOUQUQSQQOGE[W[UWSKKWSUQOMWSOKOMi@c@CAUSSQUQMKYU_@[WSWSKIk@c@AA[YKIUOu@o@e@]MMYSQOQOSOKI]Yc@_@WSECWU]WIGEECAIIMKSOWSIGGGWSUSWQWUYUYSKKIGOMCCYUCASQ]WMKEEMKk@e@YSwAkAcBsAEEGGGEYUGGUOc@_@OKKKc@]sAgAOMc@[eGuEiDgCoB{AwBcBAAOKKKA?wBgBo@i@eByAyE_EcAy@eByAa@[c@_@OMQM_@[CAa@]OMOMQOQMOMQOOKOOQMa@]SMMMQMu@m@QOy@o@USGECCMIwAkAa@[GGk@e@QMQOQMs@k@QOu@k@sC}BeDiCgCsBs@k@s@k@c@]EEa@[a@[MKKKUOi@c@g@c@MIYUe@a@m@e@q@i@gCqB{@s@a@]QOQMaAw@WS_@[QOWQQOSO_@[WQQMSOQMIGEEAAe@a@QMMIEE_@Yu@o@}AmAu@m@UQYUGEIIEEUQOMSMa@]QMQOUS]WCCa@]QOGEECWUOMUQAAIG?AMIEECCA?EEQOMIUS]Wc@_@OMYUy@m@sAgAk@e@_Au@c@]_@[{@q@o@i@IGMKkAaAA?OMUQUS[U]YyAkAIISOy@o@]Y]YOKCCEEIGQOUQaAw@OKOM_@Ye@a@s@k@OMWS[UEEIG_@Yk@g@q@i@_@Y}@s@QO]Yc@][UCCSQKIMKWSQOOKa@]KGOMIIIGWS]YGGKGWUMKKG[WOMEEMKk@c@YSKIECqA_AYS[Sa@WKIQKQKKIWOmAq@UMSKQKOIo@]KEYOOIe@SAAOGSKi@WYKOGa@QECOGOGu@WECUIGCGCEAGCKEGCUIICWIe@OWIGCEA[Ie@OA?EAg@OGAEAsA]ICMCICKCOCUGSEMCs@Oe@Ky@MAAQCk@ISEe@IgAMYEg@GcAKiAKs@GA?s@EaBIEAUAK?w@COAm@AI?c@Ai@AU?w@AU?S?Q?iC@W?g@@}@@g@@gA@a@?w@@[?U@]?[@gA@cBBY?[@o@BK@C?Q@kAFU@YBa@BK@{@FK@k@FWBc@D}@JI@QBw@JMBSBe@HgAPa@F[F]Fc@Hc@HG@[HMBWDkATc@Ho@LODmB\\IBOBm@LWDmATWDE@WDm@J_BRq@Jc@DQBQBc@BI@K@c@DG@I@k@DU@C?QBM?QB_@@[BY@a@B[@c@@Q?S@o@@U?Y@kA@[?S?S?c@?U@M?a@?o@?K?S?g@@c@?O?M?K?eD@e@@}GBc@?_B@cC@sA?w@@E?oA?W?_@@kB@oA?e@@{A@yC@{@@oA?g@?[?oGBu@@u@?eD@c@?gA@mB@qD@u@@yA?a@@s@?M?kIDi@?eD@mA@A?O?a@?a@?o@@iC@{B@Q?aC@cA@A?iD@w@?wC@}@@Y?[?k@@a@?]?qB@O?o@@U?i@?eA?yA@kB@k@?e@@aE@s@@oA?{C@kB@_A@{ABa@?c@@M?{CDg@@E?qABe@@W?W?sBD_CDSAuAByCFU?m@@aA@g@@S@W?U@e@@mABQ?Q?O@sABK@aBFK?uDHy@@cCDaA@uCDQ?oABgABqHJeMTuJPcA@cCBY@u@@Q?m@@]?k@@I?{A?S?U@[?G?e@?k@@{@?m@@W?w@?W?s@?yB@e@@Y?k@?]?a@?I?{B@S?i@@W?]?c@?U@Y?O?m@?S?U?k@@A?SAgA@k@?_@?M?{A@K?m@?Y?G?{@B{@?a@?]?m@?K?O@M?C?mB@C?O?m@?U@_A?M?]?e@?G?k@@Y?_@?e@@[?eB?oA@[?c@?q@@C?e@?_A?C?i@@i@?_A?U?i@?[@s@?aA@C?g@?_@?o@@S?M?G?_A?k@@Y?A?i@?m@@A?g@?k@?_@?K?e@@G?y@?]?aA?i@@W?i@?Y?S@q@?m@@K?W?Y?Y?g@@m@?_C@U?k@?e@@_@?wA?yEBqA?cB@S?a@?G?yD@cA@E?}GBoA?_C@uA@{A?k@@M?W?O@gA?wA@w@?]?e@?wB@i@?oB@e@?U?aA@Y?sB@Y?cA@cA?cB@iA?{A@o@@gA?wA@e@?gA?}D@i@@eA?_@@_@?W?E?K?U?yA@cA@[?]?iA@u@?aA@E?m@?c@?c@@U?M?mB@k@@Y?U?G@K?Q?Q?a@@{A@o@@u@@G?S@Y?Q?G?I?I@O?c@?]?a@@mD@K?qCBk@?A?gB?U?{C@oC?]?u@?gD@E?O?c@?y@?eC@k@?{A?U?E?gD?_@?qA?{A@i@?S?i@?cC@A?}B@m@@Y?kB@kC?_A@G?o@?}A?O@q@?gE@gB@oB@a@?iC@wB@{A@aA?Q?o@?S?s@@wB@O?iA@iB?}JDQ?sA@g@?W?wA@yB@aB?U@uB@sB?W?]@_@?W?[?C?S@K?k@?K?q@@]?}@?k@@C?S?Q?o@?C?]@iA?G?w@@_@?m@?Y@]?cB@{GBA?yB@mA?oA@K?mA@gB@sA@m@?I?i@?a@@c@?[?a@?i@@S?U?Y?cA@O?_B@c@?A?a@?gCBA?_@?}B@_@?_@?c@@Q?Y?M?Y?w@@_B?g@@c@?c@@_@?c@?{@@_A?U?W?i@@_@?]?y@@C?]?I?W@G?a@?e@?c@?oCBc@?cA@g@?[?O?uB@_@?w@@e@?c@?iA@uB@]?}EBeLDo@@wC@w@@U?q@?}A@K?w@@w@?S@k@?o@?c@?c@@G?g@?o@@A?wE@m@@A?_C@U@O?S?gADQ?W@S@S@O?]Be@@a@Bk@Du@D[@qBNgBNG@s@FE?e@D_@DOBSBYBOBYDg@FK@OBWBUDSBG@UBu@JK@g@F]FYDQBe@F]DuAPo@HQBcFp@k@HgALeANg@FUDe@FWBMBWDc@FUB{C`@[DYBA?y@JSBWB[BK@qALQ@uALs@Dk@DQ@W@YBC?O@O@q@BU@Q@A?u@BK?s@Ba@@[@e@@G?w@@c@@yA@e@?[@O?{@?{B@K@m@?E?eA@gA@O?K?E?Q?K?S?S?Q@M?k@?[@cA?[@W?O?C?gA@Q?Q?U@Q?Q?Y?U?U@Q?A?kB@_@?k@?o@?[@Y?a@?W?_B@G?O@oFB{CBK?gA?aDBE?a@@iA?_A@c@?i@@e@?]?a@@q@?iCB]?o@@W?m@?o@@c@?i@@I?Q?kEB_C@wA@cCB}B@k@@}A@W?uA@y@?mCBmA@m@?_B?C?_@@c@@kC@iA@c@?{@@q@?wDB_@?eA?c@?i@?Y?i@?o@A}@AW?a@AwDIy@EkBI]Cm@CcAKgAGmBS]Ce@E_@EYEmAOo@I_D]yAO]EUESCQAMCQA_AKu@IKAA?aBUq@Iy@KyAQqAMw@Kq@IWCSEWCm@Ii@Ek@GMCQCc@EQAWAMCoAIsCSsBK[CkAC[AeBEC?q@Am@AO?m@?[AuA?wA?sA?G?a@?uD?c@?o@?W?c@?kB?_@?C?yF?c@?sN?cU?W?[?kA?yE?mD?yC?iD?iN?cF?q@?{@?w@?q@?iA?E@O?iE?yA?sB?s@?aB?mD?]?A?U?kK?cD?_@?iA?S?_A?{@?gA?[?[?{I?Q?mC?I?gA?Q?Q?Q?aB?Y?A?K?C?]?gE?aG?s@?a@?y@?O?E?M?I?eA?cB@M?iA?eB?_D?sCAcA?E?E?gMAwA?qAAoC@o@?kA@i@?]?k@?u@@e@?S?yA@{B@eB@{A@S?s@@k@?[?Y@aA?s@?c@@Y?c@?q@?kGBeB@y@?i@@_A?U?Q?]?o@@S?c@?_@?a@@W?oE@}@@oA?M?q@@m@?U?k@?aA@_A?wA@W?i@?a@?_@@g@?e@?_@?C?o@@u@?iB?aFBsA?wA@W?K?kA@S?W?Q?oA@_@?e@?mD@y@?yHFeD@G?cA?Y?cA@E?u@?K?cHBoE@}@@]?{C@c@?k@@A?_A?c@?gA@gB?qABuA@Y?cABs@@uABcABa@@[?aABi@@_@?mBBw@@cA?k@?k@@_B?a@?U?U?g@?U@C?k@?o@A{@?I?_CAiAAW?s@Ay@A[?S?U?k@?g@?O?[?y@AY@aA?q@?k@?U@a@?aC@m@?I?S?Y?I?c@@S?U?U?O?Y?m@?i@@k@?C?c@?G?Q?k@@U?k@?kB@aA?W?o@@gB?k@@Q?_A@eC?m@@i@?k@?aA@yA?[?O?u@@ePDeE@eC@iRFsD@mC@iA?g@@u@?mC@mA@s@?M?_@?g@?{A?wCBi@?u@?mA@u@?sD@]?cA@k@?_B@}@?}@?q@@u@?sB@mB@eA?yEBgB?cC@qB@oC@W?K?c@?c@?Y@sB?mA@kC?]@m@?iA?s@@M?{A?iD@C?gA@wG@sPF_C@gA?_IBa@?uEBsMDaG@i@@gA?s@@y@?g@?sD@c@?wGBoA?k@?i@@k@?o@?k@?Q?k@@k@?c@?}@@eC@}@?K@K?K?W?}@?U?k@?k@?qB@O?W@W?S?A?_B?{A@c@?aA?}DB{E@wA@qB?{@@eA@e@?Q?U?U?U?U?W?S@W?S?U?uA?m@@U?U?U?U?U?U@U?S?Y?S?U?k@@U?U?U?U?g@?C?S?W?U?k@@G?M?i@?W?S@U?U?U?M?G?U?U@U?U?U?U?W?Q?U?U@M?G?U?U?W?S?O?]?U?U@U?W?U?U?U?U@U?U?U?s@?}@@Q?U?[?O?U?U?U?U?U@U?U?U?U?U?U@U?U?U?S?U?U?S@K?K?W?U?W?U@m@?U?S?_@?y@?W@G?G?U?U?oD@g@?eA@_A?aB?w@@qB@uA@qA?gA@o@?e@?wA@Q?eC@E?u@?_B@S?y@?]?i@?W?k@@U?U?S?cA?aA@o@?O?W?U@W?U?U?U?k@?W@U?W?k@?gA@S?W?k@@U?U?U?S?W?aA@k@?cA?W@S?gA?U?K?K?i@@O?G?W?U?U?W?Q?uB@W?C?Q?Q@[?m@?S?gA@U?W?a@?K?U?m@?W@W?O?G?Q?eA?WAQ?c@Ac@?OAk@Aa@AIAK?M?E?e@AK?SCWAYASA_@CKASCs@Gi@Gi@E_@I[Ee@Gi@Gc@EOCUCICOCi@IIASEe@IYGm@Me@I_@IKCg@MYGUGOEYISEUI_@KYIc@M{@WUIu@Wo@Us@W_@O]MIEaAa@]OkAi@UM_@QOIsAs@OGQK}@g@MIe@YUMOK{@i@WO_@UQM{@g@gAs@[QKIc@WGEc@Wy@i@k@[e@[UOc@Wc@YOIcAo@a@W}@k@[QKGw@g@c@YgAs@c@WkBkAcAm@i@[e@[c@WQKUO_@UoAu@[S_Ak@c@WSMQIe@YWQq@a@QMSMUMSM_@UWOs@c@KIa@Ue@Y_@Us@c@a@WSOSK{@i@a@WKGWQEC{@g@[SWQaAo@SOYQm@c@ECaAq@WScBqAQMQOQMcAy@c@_@OMq@o@QMQOOOOOQOq@m@OOsBoBc@c@]]KICCQQ[[k@i@USOQQO_@]QQMMUUSSGGUS[Y_@a@q@o@oBkBOMa@_@OOCCKKq@o@o@o@a@_@IIIIo@m@KKCCCAACyBsBCCo@o@EEKKKImCkCIKa@_@a@_@a@a@MMq@m@a@a@_@_@q@o@QOOOUUKKKIUWECIIOOWUII_@_@uAoAe@e@y@w@cAaA_@]SSKKQOOOOOOOa@_@k@k@US_@_@sAoAOOOOQQ_@]OOQOSSKKOOQOOOOOa@_@OOOOQOOOOOOOQOOOOQa@]_@_@q@q@QMGGWWaAaAOOa@_@a@_@o@o@OOWW{@w@YWYYo@o@q@o@OOQOQOq@o@y@w@i@c@USeBuAcAw@UOc@[c@[c@[[Um@_@UOUMkAs@m@_@c@USKSKw@c@OGi@YUKSKUKOG}@a@u@[k@WUICAMGUIWKc@OQISGCAQGg@QUIYKMCSIUGSGOECASGSGUGUG}@WSGYGc@KUGQEUEUGSESEKCICo@MQCSESEUEQCWEUCAAOCIAMCk@ISCWESCUCWCQCUCQCYC[E]CKAe@EUAUCSCYAUCe@Ce@CK?k@CSCU?UASAWAUAU?SAU?WAQ?WAm@AuACWAa@?IAU?UAS?U?aACU?SA]AQ?U?UAS?WAU?SAU?QAY?eEImBCi@AUAk@AeEGUAU?k@Ao@Ac@AW?UAaACS?m@AE?O?e@AWAY?A?UAS?SAW?UAS?UAS?Y?g@Ai@AK?_@AEA]?K?i@AWAq@AM?A?UAk@AU?UAi@Ai@?YAU?UA_AA_BCOAcAA_ACk@AS?k@Ak@Ak@AwACmBEk@AW?g@AaAAwAEw@AkAAk@AUAk@Ai@AU?UAU?UAU?k@Aa@AI?k@Ak@Aa@AM?]AM?U?GAM?U?UAk@AI?a@AQAC?O?y@AK?UAU?UAe@AE?k@AU?k@AaACU?UA{@Ak@AK?uEIS?}@Co@AU?mBEk@AS?WAuACE?e@?k@Aw@AIAU?UAk@AI?KAS?WAs@AO?}@AUAU?UAU?WAC?e@AQ?]AQ?UAUAU?UAaAAY?QAaAA{@CY?wACaACU?UAo@AW?k@A]Ak@A_@A_BCwCEg@AMA{ACS?UA[?A?UASAwACk@AqAE{CIUAUAU?UAUAWAUAU?UAUAUAUAk@AUAc@A]Am@CUAcCGUAG?IAU?QASASAQ?SAQAS?u@CEAcBEeBGqBGS?gBGI?wDMeAC]AqCIqHUeBG]AO?o@C[Ak@Aq@C{@EaAC_ACgBG_ACE?i@COA{CI]AOAS?{@EuDKmBGaBEsDM_DImBGo@CeDKoACo@Cm@Ao@CUAUAUAUAk@A}AE{@EcCGUAUAUAUAU?UAk@CU?UAi@CUAa@AWAQ?w@Ck@CU?UASAUAU?UAUAU?UAWAS?WAU?UAU?UAU?k@CU?m@Ak@AU?UAU?UAU?U?UAW?UAS?A?UAU?UAU?U?UAU?UAU?UAU?M?G?UAU?W?UAU?UAU?UAU?k@AQ?YAU?UAU?UAW?U?UAU?k@AC?QAU?UAU?U?UAU?_AAKAY?]A_@?w@Cs@Aa@?s@AmBCUAI?I?W?UAI?e@AQ?E?e@AU?YAcAAS?c@AC?yAAWAeAC[?c@AgBC[?UAU?sACe@AC?_BCU?O?GAaAAUAU?qBCa@AA?uDESAS?U?uACm@Ak@AyACU?WAS?W?k@ASAU?QAE?i@?k@AUA_@AS?Y?WAc@AiAAoAAcACSA[?a@?IAeFGsEGQAiBCaAAm@Ao@Ai@AqBCM?U?UAU?UAU?k@AUAg@?k@Am@AaACS?k@Ag@AU?S?E?OAS?G?S?g@Ae@AC?A?O?E?sACmBCQAk@?UAU?SAU?aAAUAU?UAk@?UAS?WAg@AyAAO?o@AUAU?WAo@Ac@?QAM?K?wACU?UAU?UAW?wACk@Ac@?E?QAU?k@AO?E?UAU?KAC?u@AC?E?O?UAcCCE?UAO?E?O?EAU?O?E?EAK?C?Q?OA_@?OAE?O?]AK?U?IAK?S?_@AM?U?OAY?SAE?O?g@A]?KA_@?UAS?U?GAM?O?E?A?UAI?I?G?OAI?O?QAE?U?K?I?IAA?M?I?S?QAK?I?YAU?E?e@AS?A?_@AA?G?SAI?Q?QAO?G?SAA?U?]AK?W?GAc@?UAM?G?U?SAU?K?IAU?M?I?QAm@AK?G?WAU?C?O?QAE?S?E?QAC?O?UAU?UAQ?G?K?YAW?SAU?U?EAM?W?IAE?[?SA]?MAU?S?UAK?W?_@AG?M?SAW?OAE?wAAKAI?U?G?MAS?E?OAO?E?o@AO?[AW?c@AU?EAU?]?GAe@?WAY?SAK?_@?A?UAS?WAS?UAY?Q?C?UAS?WAS?o@ASAU?]?C?QAU?k@AUA_AA[?WAW?UAE?Q?m@AU?UAW?QAC?U?UAA?U?E?YAG?S?K?KAK?K?M?IAK?M?Q?UAU?]AU?C?_ACm@?E?OAU?WAW?O?o@AYAU?S?MAU?UAS?U?EAO?U?G?MAU?S?UAU?C?SAU?G?KAU?Q?k@Ag@Ak@A_AAaAAcAAkBEwAAaAAwACkBC_ACiAAy@AaAA_ACU?m@A}@AWAaAAaAAk@A[?OA_AAaAAa@AkAAaAC_AAkBCcAA_ACwAAUAk@A_AAaAAm@Ak@Ai@AU?k@A_AAwACk@AU?k@AsACo@Ai@?SAW?i@Am@A_AAwACW?k@A_ACk@?UAk@?k@AUAi@?m@Ai@AUAk@AU?U?k@AUAU?i@Ak@AU?k@?Q?{A?i@?m@?_A@aA@aABaABuAFS@W@]@yAH_AFWBa@BC?_@BA?QB_AHaAH_AJk@F_AJw@JeANu@JUDkAP_ANg@Je@Ho@LUDSDi@LWDk@LGBMBQDg@Jm@Ne@LSF]H[HYHi@NkA\\}@XkBj@c@NA?g@PyBt@C@SFoAb@[JoBp@UF}CdAKDUF_@NE@eBl@[HMFSFy@X}@Xq@Ta@N{JdDgDhAMDaAZ}Bv@}Bt@OFwBr@mDjASHeA\\g@PWHSFMF_@JA@eBj@_@LQFKD[Ji@Pg@Pe@Pk@P_@LGBWHqAb@E@_A\\a@LA@SFQFOFE@SFIDKBSHQDC@QFSFCBQDSFGBIBSHKDIBQFUFg@PUHQFUHGBMBQHWHODUHMDGBQFIBKDSFE@KDOFE@SFUHQFKBGDG@KDSFA?SHSFMDEBUFQHUFQFGBKDWHg@PSFSFUHUHOFUHSFA?QFSHODE@SHSFSHi@PQFQFWHSFGBKDSFUHIBIDSFE@OFSFC@OFSFUHSF}@ZQFSFMDGBUHMDC@SFSHSFA?SHSFQFi@PQFWHSHSFA?SHQFUHUHODWHKDGBSFQFC@UHQFIB]LKDw@VG@WJg@NGBKDi@PSHODC@UFQFC@MFIBIBWHSFSHSFMDE@SHWHE@KDQFC@QFSFC@QFe@NA@UHSFSFC@MDSHODGBQFSFSHMDG@SHGBIBUFSHA?SHKD[JC@MDUFQHKBGBUFMFC@YHQFYJODQFMDq@TQFSHSFGBKDSFKDIBSFOFC@UFQFUHSFSHE@ODIDIBSFKDIBQFUHQFUHMDE@UHQFSFIDIBSFUHIBIBUHSFSHSFQFUHA@QFODE@SHG@KDQFUHQFE@SFQHSFSHA?QFSFKDIBSHSFSHQFA?UHSFUHQFWHQFMDGBUHMDSHSFo@Tg@NYJc@N{@Xk@Re@P}@X}@Xg@Pi@P_Bh@{@XWHg@P{@XmC|@{@Zi@PSFE@wAf@iA^]J_A\\c@Ne@Nm@Rg@N}Ah@C@SFMFgA\\c@NUHSFSHE@e@NoAb@g@P{Bt@}@Ze@Nk@Re@N{@XsC`Aa@N}@Xi@P[Ju@VaA\\c@N{@Xi@PSHqDlAuAb@]LSFWHe@PaBj@g@Ng@Pe@PSFk@PKDQHSFSFSHi@RWJe@PODEBQFIDIBSHKDIBQHSHg@RWLg@Ta@Pk@Va@RSHMFEBSJQHSJQJSJQHQHk@Zy@b@e@VOJg@Xc@Vc@VC@_@VC@a@VC@gAr@c@Zm@^[Pk@^oAz@]R]TMJQJ_J~FoAv@wA~@_Al@{@j@q@b@]R}E`DqAz@cDzBQJOJIDIHSJOJSLQLOJMHSLQJSNc@Xc@XgAr@SJs@d@mBnAyA~@SNMJIDuA|@oChBe@XgAr@gAr@mBnASNoBnAyA~@yAbA{A`AmBnA{AbAyA~@}BzA_C|AiEpCm@`@cBfA{E~CgInFiIlFkBnA{@j@_@Ve@Xc@Zs@d@]TUL]T{@h@]VgAr@w@f@cAp@oCfBeBhAWPa@V{@j@qA|@o@^q@d@k@\\s@f@k@\\{@l@u@d@g@\\]V[Rc@Xm@`@i@\\i@\\_@Vm@`@a@V_An@YPkAv@a@VYPk@^q@b@YPe@Zq@b@qAz@u@d@e@\\kAr@eAt@k@\\o@b@qAx@w@h@aHpEw@h@iBlAiAr@mAv@kAx@}B|AcBjAyAhA}BjBkA`AYXoAdAgAdAiAhA_A~@}@`Aw@z@c@d@cAjA{BlC{BjCoElFWXm@t@cDzDcCtCoCdDkAtAs@x@s@|@aAfAwAbBgEbF_BnBm@r@aCrCeAlA{@dAo@t@kAvAkBxB{BlCqCdDkAtAu@z@wAdBoAzAyAbBmB|BgEbFiBvBy@`AkC~CyCnDoAzAkBzB{BjC}BlCyBjCc@h@i@n@yAdB{AhBoB|BwAbBsGzH}AhBcGfHiGpHm@r@g@l@[^[^sEpFkAvAm@r@UToCbD{CrD_EzESTSRMNSRm@n@eB`BsApAa@^OLq@l@yBdBgAx@m@`@YR[Te@ZUPkAr@c@XMFyC`B}DnBoAj@u@Xg@RoAf@}@ZcBj@}@VuA`@iAZ[HiB`@uAZuAVuAT{@NE@uARmBTuALoBPyAJsAHyAFwADmBByA@mB?uA?yA?M?_@?{AAcA?aCAo@?yC?o@?s@?g@?M?u@?i@?k@Ag@?s@?Q@S?k@?c@?_@?W?g@?M?Y?W?W@U?W?Q?U@Q?K?W@Y@q@@U?U@U?W@Q@U?W@E?M@Q@Y@i@@UBO@[@k@DI?I@U@WBS@E@_@BYBWBU@i@Fi@Dk@Fk@Fe@DUDYBq@JuBXm@HcANm@Jq@JeARm@Jw@PSD[FKBMBy@Rm@Lk@NWFG@KBC@QDQDSFe@LWHg@Lg@Ni@Pe@NcBh@g@PWH]Li@POFsAd@}Br@]L]JGBUH_@L_@LOFeA\\y@XgA^yAf@_Bj@mA`@YJqBt@mBr@}@ZUHSHUFSHSHSFSHUHSF[LWHOFQFQFWJODSHSHSFg@PSHSHSFSHUHQFSHc@NWHA@g@PUHa@Lg@Pm@TE@[Ji@RIBe@Ne@PWHe@NE@WJwC`Am@To@R[JYJ]L]LUHq@TWHQFC@k@R_@Le@NUH]Lk@RSFOFc@Na@Lc@Ng@PWHMDm@Rk@Re@Pi@PSFUHa@NSFWJSFSFSHUHQFUFSHSHUHQDSHSHSFUHQFSHSFUHSFSHQFSHUHSFSHUHQFUFSHSFSHSHSFSHSFSHSFSHUHSFSHWHe@PGBSFa@Ne@Ng@PSHi@P{@Zg@PSFOFg@PC@SFSH}@Xc@Pk@Re@NWHSHg@P{@XiBp@w@VoAb@{@Xg@Pw@Xm@Re@PWH[Lq@Tc@Nc@NyAf@k@Rk@RGBi@Pa@NGBg@Pg@P}@Z{@Xe@PSHKB_@NODYJSHiAb@YJ_@NYLSHSHSHSHQHSJSHSHMFQJUHQHSJSHQJSHe@VSJQHSJSJSJc@TSJQJSLYN]RQJQJSJQLQJQJSLQJQJQLQJSLQJSNOJc@XQLQLQJQLQLc@ZOLc@\\QLQLOLQLu@j@OL_@ZUPMLc@\\OLa@\\QP_@\\QNOLONONQP_@^QNOLQPMLa@^_@^QNOLONONONQNONONQNONONOLONa@^OL_@`@QLONONMJc@b@ONONQL{@x@OPURQNONONMLA?QPOLONQN_@\\QNONOLOLQPOLQNQNm@f@WT_@XSPMJGFKHMJQNMJSNEDKFONQLQLQLOLQLQLQLQLQLOLQLQLQLQLQLQLQJQLQLQLQLQJQLQL_@T[R{BrAyBrAcFzCA?KFWNIF[PQJQLQJQJSJc@Xe@VWP{@f@_@Ti@\\KFIDULEBSLi@\\s@`@[RaAj@eBdAs@`@_@TGDKF}@f@e@Za@Tk@\\oAt@m@^g@XYPMHYP}BtA{A|@QJIDC@}@j@GBIF_@TWPQJOJQLQJQLQJSNOHSNQLOJQJOLC@OJQLOJSLSNQLSLOJQJQLMFCBSLQJOJSLQJSLgAn@A@QJQJiAp@EBKFiAr@QJe@Vu@d@e@Xw@d@QJQJe@XKFEBe@XQJQJMHC@QJGDIFKDGDC@MHaCxAKDEDQHA@c@VOJC@OJe@XQJw@b@kC~A_Aj@iAp@QJQJgAp@ULQJQJQJa@Vi@ZKFEBe@XMHC@MHC@QJOJw@d@SJmBjAkAp@QJQLSJQLQJSJQJQL{D|BIFYNQJg@XUNQJiF|Cw@f@aB`Ao@^QJQJu@d@QJQJOJSJQJQJQLc@ViAn@QLSJa@VSLQJQJQJQJQJQJQJSLOHy@f@g@XCBGDSLuBpAQHSLOHA@SLMFQJWNEBKHMFCBSJOHA@QJSLQJMHE@GDIDKHk@ZQLSJQJ]RGDQJSLMHWLQLQJy@d@]TC@]Ts@`@]Ry@d@e@XQJGDgAn@KHGBmAt@IDQJSLQJQL}A|@}BtAy@d@_B`AYPuAx@uCdBKFGBa@VULQJe@XMHC@OJQJC@QLQJSJQLQJOHSLC@MHSLQJw@d@OJyAz@c@Vm@^QJA@c@V]REBA@QJULGDWPi@XOJmAt@MFA@WPULwBpAe@XSLC@KFMHWNOJA@SJA@EBKFQJe@XC@OHc@VMHYPw@b@QJMHMHKFQJOHC@MJKD?@OHMFQLQJSJQJSLQJc@Ve@XQJ?@m@\\GDULSLe@VOJQJA@A@MFMHC@UNQJQJSLQJc@Ve@XQJSLc@VSLQHSLQLOHSLIDA@KFMFSLQJQJQLIDKFOHQLQJULg@ZKDABKDGDQJKFEBe@XA@MHSLQJSJID]TIDEBSLQJQJQLSJGDSLa@T{@f@YRQJKDYRQJSJQJ?@QJSLc@Ve@XSJw@d@QLQJQJQJSJSLQJQLQJSJQLSJA@OJQJSJQLc@VSJSLOJWNMH[Po@^WN}@h@GDc@VQJQLOHSJWPOHGDaAj@WNe@Xo@`@QJQJSLMHULEBMHQJm@\\cBdAQJOHULSLQJQLA?QJQLQJ_@RYPYP]Rc@V?@QJm@\\]RQJQLSJQJQLSJQJSLQJSJQLQJQJSLQJQJQJSLQJQLSJSJQLQJQJSLQJQJQJSLSJOJSLQJSLSJOJQJSLQJe@XA@QHOJg@XSNOHkAp@OJSLQJSJQLQJSJQJQLSJc@XMFEBQJQLSJQJQJSLQJQLSJQJe@XQJSLQJQJSLQJSJQLQJe@XQJQJSLQJQJeAp@_@VYNs@b@m@\\KFe@Xg@XMHSLSLQJSJQLSJMJSJQJk@\\u@b@WNIFe@XC@MFc@XiAp@SLQJOHQJULOHGDKFSJy@b@g@XGBOHc@TA?A@KFSJSHSJg@TSJQHSJSHSHSHSJSHSHQHSHSHQHSHSHSHSHMDEBUHSFSHSHSHSHSHSFSHUHSHUHw@ZUHQHSFSHc@PUHQHSHUFSHSHSHSHSFSHSHSHSFSHg@RUHUHSHSHSHg@RSFs@XGBUHcC~@i@RYJ{@ZSHSHIBIDSHSHSFSHSHSHSHUHSFSHSHSHSHg@Pg@R]L]Ng@Pi@RcBn@g@RSFKF[Jg@RUFSHSHg@R[LKBIDSHSHSHKD[JSHy@Z_A\\w@Xw@ZA?SHSHg@ReBn@SHg@Rg@Pg@ROFC@qAd@SHQF}@\\A@q@V]LuAh@MDSHi@R_Bj@UJUHUHSHWJUHYJo@Vi@RmCbASHSHiE~AeBp@SHg@PyBx@e@RUHSHUHKDGBSHSHSFSHQFC@SHSHSHSFSHSHSHSHSHSHUFSHSHSHQFEBOFUHQFA@QFUHQHC@QFSHSHKBIDSHSFQHUHSHSFSHSHSHUHQHUHSHSFUJQFSHUHSHSHSFSHSHSHSHUHSHSFEBKDUHSHSHSFSHUHQHUHSHSHQFUHSHSFUHSHMDEBUFSHSFUHSFSFSFSHUFSFUFSFSFSFWHUFQDSFUFUFSDSFUFKBG@UFSDUFUDSFUDSDUFUDSDUDUDSDUDUDUDSDUDUDUDSDUBSDA?UDSDSBQDC?SDWDG@MBSDUBSDUDSDWDSBWDSDSDUDUBSDUDUDUDSBUDUDSDUDSDUBG@MBUDMBG@SDWDSBUDUDSDUDUBIBI@UDUDUBUDKBG@UDUDSDE?ODUBQDC?UDSDSBSDA?WFSBeAPYDmATsB\\oBZ}B`@m@HsEv@aANm@Jk@JqDl@w@Li@Ji@Hc@Hk@Jm@JOD_ANs@LMB{@Ns@LA?k@JsAT]F{@NE?KBa@Hk@Jm@Jm@Jk@Hi@Ji@JA?WDs@Li@H_@HmBZgARm@Jk@Jk@JI@K@_BXYDuAT{B`@[DWD_@F_@Hc@HSBg@H]FIBI@_ANuCf@aC`@mARYFu@LK@_@HYDOBSDmARG@_@HMB]FMBSDUDq@Li@Lc@H[HWFQD_@JUFQD]HaATKBo@Pi@P_@J{@Vg@Nc@Ni@Ne@Pi@PSHi@P}@Zg@RSHg@Rm@VKD_@NYLg@RUJc@REBOF]Ni@VWLUHQJUJOFQHgBx@YLQHQHSJUJUJQHSHm@X}@`@{@`@a@RYLmAj@YL_@P_@POFoAl@yAp@{BbAsDdBe@Tk@Vg@Tg@Tg@TSJSJSHg@Vy@^i@Te@Tg@TSJe@R{@`@g@Tg@TQJ[L{Ar@w@^g@Te@Ti@V{Ar@g@Ty@`@KD]Ne@Ti@Vg@TSHSJUJe@TUJSHe@TULg@Tg@Tg@TQHULSHSJSJYJMHg@Tg@TSJSHe@Te@Rg@TMFCBUJg@TUJg@TUJWL_@P[La@Rg@VMF_A`@k@XSHqAl@SJQHWLUJOFk@Xg@Tg@TUJg@Tg@Vi@Te@Ti@TSJg@V]NKDe@TUJSJSHSJg@Tg@Tg@Te@TULi@Te@Tg@Ti@Vi@VQHUJg@TSJa@PQHA@y@^UJQJQHUJQHSJSHSJSHSJEBMFSHQHSJSHSJOHUJC@QHQHSJSHQHSJSJSHQHSJSHQJUJQHQHUJQHSJSHSJUJQHC@QHQHUJSJSHSJSHUJQHIBKDSJSHSHMDGBSHSFSHSHC@QFSFUHUHSFUHSFUFSFUHWFUFUFUFUFSFUDUFUFSDSDUFSDWDSDA@c@Hm@JG@MBUDOBYDUDC@E@K@WDMBE@WDWDSDSBUDIBK@UDSDUB?@UBUDSDUDUDSBIBK@G@MBUDSDA?UDUDWDSBWFSBE@KBSBWDSDSDSBE@g@HWDQDUDWDUDUDM@E@YFQB[FUDG@OBQDYDUDUDUDUDSBSDC?UDUDSDWDSBSDC@UBUDSDC?QDWDUDUDUDWDQBUDUDC@QBUDSDG@C?MBUDSDUBUDUDWDSDWDG@OBUDUDUDUDUDOBC?SDUDOBE@SBODE?WDC@OBUDA?QDUDMBG@UDUBUDA@SBSDUDSDWDaANSDUBWDO@G@SBUDUBUBI@K@WBQBA?UBS@YBWBSBC?i@DWBU@U@WBU@W@W@O@U@Y@Q?K@M?Y@U?S@W?W@U?W?W@W?U?SAI?M?U?S?W?S?W?U?U?U?U?U?U?U?Y?U?U?W?U?A?S?U?U?U?S?A?U?W?m@?U?Y?}@AY?k@?q@?c@?u@?k@?o@?U?A?Q?W?U?U?W?Q?W?W?S?S?W?A?k@?U?U?UAW@IAM?U?W?U?Q?C?U?S?U?U?W?S?U?W?U?U?i@?W?G?M?U?S?a@?M?i@?U?A?U?U?WAW?I?K?U?W?S?Y?U?W?W?W?S?W?U?O?Y?K?I?U?U?[?O?I?M?G?M?W?Q?W?Q?U?U?S?S?W?SAW?S?W@OAC?S?aA?oB?W?C?Q?{@?o@?W?o@?uA?U?e@?q@Ak@?U?W?O?C?uB?cC?]?g@?u@?S?e@?g@?e@?i@@}@?Q?aA?U?Y?{@?k@?k@?W?S?U?k@AM?]?k@?U?k@?U?S?A?W?S?k@?U?W?U?U?S?k@?aA?i@?W?S?W?U?U?M?G?U?SAo@?U?k@?k@?i@?W?k@?I?a@?U?i@?k@?S?k@?i@?S?a@?G?SAk@?U?U?S?U?S?U?U?U?O?E?i@?S?S?W?S?U?Q?C?U?I?c@?i@?yA?sA?Y?o@?}@AU?i@?E?O?k@?S?k@?S?S?A?W?i@?i@?S?S?m@?U?g@?W?S?W?U?C?Q?W?U?U?U@m@?W@S@U?S@A?U@U@M?G@W@S@A?U@U@U@U@UBU@WBUBU@SBWBUBUBUBUBUBUBUBUDUBWDSBk@HSDUDUDUDUDUBGBKBUDUDUDSFUDSD[HQDSDIBKBUFSFSDSFWHSFUFUHSFWHQFUFSHSHA?SFUHIDIBSHUHQHUHSHSHk@REBKDUHQHUHSHMFG@SHSHSHSHSHSHUHSHSHSHSHUHSHSHQHSHQFC?SJYJSHUHUJSHUHWJUJA?QFUJWJSHUHUHUJSHOFE@SHi@RUJSHUHSHUJSFUJOFC@a@Nu@Zg@P_@NWJ]NUHUJUHSFSJUHUHSHUJQFYLUHUHUJSHUHSHUHSJWHUJSHUHUHSJSHUHSHUHSHSHKDE@k@TUJUHUHUJYJWJYL[JUJ[Lq@V[LWJWJYJWJ[LGBQFqAf@WJWJYLYJ[LSHSHUHSHQFWLe@PUHA@QHSHSHSFA@QHg@Pi@TSHUHg@RYJOFSFSHIDIBSHQFSHGDKBSHSHSHSHe@ROFk@Rg@Ra@NEBg@Pe@Ri@Rg@Rg@R[LMFi@Ri@Rg@RWJQFEBw@XSHUJSHSFg@Ti@Rm@To@VWJWJUHk@Tk@Tw@ZoDtA{@\\WJUHYLUHUJWHSHCBUHWHUJUJSFeAb@SHWHo@Vk@TWJSHWJg@RG@SHYLUHUJA?UHSHWJUJSHWHWJIDMDUJWJWJYJWJWJWJWJWJWHgAb@YLWJSHC@SHGBSFWJUJYJWJo@VYLUH[LWHo@XOD]No@VIBQFUJo@VWJE@QHWJUHA@WHGBMDUJQFOFQHSFgAb@QHQFQHSFSHOHUHg@RSF?@QFSHSFSHSHQHSFA@SHUHSHUJQFUHk@TYJUJUHYLKDIBWJWJo@VWJSHC@WJUHYLYJUJWHC@UJWJUHUJMDaFnBkAb@UJE@OFWJGBIBWJSHWJWJC@SHWJWJWJWJUHWJE@OHYJWJSHYJGBg@RC@MFg@PCBQFSHQFE@SJUHGBKDSHWJQFUHSHA@QFSHKDIBSFSHUHYJ"
                                    },
                                    "start_location": {
                                        "lat": 25.9348563,
                                        "lng": -80.2155609
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.5 mi",
                                        "value": 885
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 64
                                    },
                                    "end_location": {
                                        "lat": 27.4126653,
                                        "lng": -80.3986628
                                    },
                                    "html_instructions": "Take exit <b>152</b> toward <b>Ft Pierce</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "uogfDz{uiNQCc@HSDM@QDO@i@FiAHY@{@Au@CUA_@Eq@IaASk@MwAYu@Og@Iq@E[AE?Q?Y?Q?A?K@I@E@QJ{@J_BL}@JaBJWBi@B{@Fu@HICEAGAGCICGEIGECECGGGK"
                                    },
                                    "start_location": {
                                        "lat": 27.4049094,
                                        "lng": -80.3988579
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "367 ft",
                                        "value": 112
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 14
                                    },
                                    "end_location": {
                                        "lat": 27.4129125,
                                        "lng": -80.3975674
                                    },
                                    "html_instructions": "Merge onto <b>FL-70</b>",
                                    "maneuver": "merge",
                                    "polyline": {
                                        "points": "e`ifDrzuiNOsAE]YgB"
                                    },
                                    "start_location": {
                                        "lat": 27.4126653,
                                        "lng": -80.3986628
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.4 mi",
                                        "value": 572
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 57
                                    },
                                    "end_location": {
                                        "lat": 27.4146674,
                                        "lng": -80.3921191
                                    },
                                    "html_instructions": "Continue straight to stay on <b>FL-70</b><div style=\"font-size:0.9em\">Pass by Wendy's (on the right)</div>",
                                    "maneuver": "straight",
                                    "polyline": {
                                        "points": "uaifDxsuiNUkAY}Ag@yB]wAKe@S_AiA{EK_@SaA_BaH"
                                    },
                                    "start_location": {
                                        "lat": 27.4129125,
                                        "lng": -80.3975674
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "221 mi",
                                        "value": 355025
                                    },
                                    "duration": {
                                        "text": "3 hours 0 mins",
                                        "value": 10816
                                    },
                                    "end_location": {
                                        "lat": 30.3026826,
                                        "lng": -81.641262
                                    },
                                    "html_instructions": "Slight <b>right</b> to merge onto <b>I-95 N</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "ulifDvqtiNBQ@MAMG[WiAAIG[CIEQQy@EIOo@Ow@Ke@WeA_@aB_@cBs@_DAQCWAMAG?O@O@K@K@I@IDMDQHMFMFIFGHIJGJGJGBCFAFA@AHAFAHADAB?H?F@H?F@F@F?D@JDH@BBFBDB@?BBFDFDDFFHDJDHBF@FBF?B@D@F@L?J?@?H?J?HADCLCFCJEHCFEFCDEDCDEDEBEDC@C@EDGBGBCBC?CBYFOBE?]@U@[?[@U@A?]Pu@?SAoB?a@A}AAc@?c@?iA@_@@iABcCCwA?U?O?uA?eAAk@?{@?q@AK?Y?Q?}@?gB?_A?_@AI?m@?cA?yBBuB?U?aAAcA?m@?aA?i@?[?g@?{@?_D?k@?W?U?k@?M?I?Q?a@?kA?i@?i@?Y?a@?G?aD?S?Y@SAi@?i@@e@?g@@w@@gADY@i@Bi@Bi@DqALuALu@Ji@Hc@Fq@Lo@Lc@H{@PUFo@Nm@Na@LG@e@NSFUHUFc@NYJUHoA`@eA\\a@NgBj@SHi@Pi@Pg@PmA^uAd@k@Ri@PSFQFUHKBa@NKBC@i@Ps@Vq@R]Lc@NaF`BQFk@P}@Xk@R_@LA?YJi@PsAb@QFcBj@YJC@SFc@NUHQFw@VC@c@N{Ad@cBj@a@NE@i@Pg@PgA\\y@Xa@Ng@Ne@N]LA@_@LODo@Te@N_AZA?[LKDSHc@Rq@\\MFQJMFYPOJWPSJWRi@`@i@b@EBMLONOLEFON_@^KJMNKJCDQRIJi@r@QVKLADGFGJMTGJEFCFAD[j@Yj@A@Sd@Sd@O\\a@~@Uj@Sf@O\\i@nAc@fAg@fAGRa@~@Uh@Qb@OZ{@tBKVSf@mArCcB`E[r@Yt@KTm@xAyAjDUh@KTu@jBa@|@aA~Bi@rAWl@i@lAYn@Qb@?@O\\]x@KT_@|@c@dAGL]x@_@|@GPq@~A]v@uAdDm@xAYr@y@nBUj@Sb@Wn@KTa@~@KRc@bAYn@k@lAw@`Bk@lAc@|@Yl@S`@GLKP[n@g@`Ag@~@[l@m@jAq@nAEHc@t@Wd@Yf@a@r@q@lAqAvB?@OTi@|@qAtB{@tACFg@v@A@MR]f@s@`AEFe@n@GJWZGFe@l@e@j@Y^c@d@IHSVQR[^QPc@b@c@d@YVYXk@j@a@^_@\\]ZQNa@\\SPOJi@d@A?YTe@^_@Xe@\\QLi@^]Tq@d@w@f@UNq@`@g@Xo@^c@Tm@\\_Ad@gAh@]No@Z_@Pe@P_@PG@c@PgAb@{Ah@s@V[HC@m@RqA`@sAb@g@N}@X[JmCx@gA\\aAX{@XuBn@cAZa@LcBh@wAb@oA`@{Ad@qA`@qA^iCx@a@Lc@LgA\\eA\\u@TyBp@oA`@uA`@m@R_@LmA^c@Ni@NUHeAZeAZSHy@VsA`@}Ad@sAb@w@TWHiA^i@Nc@N_Cr@_AX_@LgA\\sA`@y@Vq@R?@iA\\q@RaBh@{Ad@wBp@mA^mA\\aA\\cBf@eBh@i@Pe@NeAZ_Bf@g@Nw@Vs@TMDSF_AX{@XuA`@SFmA`@kBj@YHsBn@]JgA\\{Br@qA`@k@PQFUFsAb@w@Xi@Ng@Pa@Ji@Pi@PODWHgBj@i@Pu@T[J{@VE@y@Vu@Vo@Pg@Pm@PG@]JSFSFi@Pg@NUFC@q@R]JE@a@Lk@PSF{@T]JUHIBoBl@[Jq@RMDQFgBj@WJa@Lm@TODaA\\e@R[Ju@XkAf@UHUJg@RYLMF_@No@Xa@RUJQHk@XC@kAj@SHIDsAr@]PaB|@y@d@WNSLs@`@]Rq@`@GDu@f@a@Vo@`@m@`@OJOLi@^c@XYRIFc@Zs@h@QL_Ar@c@\\qA~@c@Zg@`@UPy@p@ONMJC@a@\\IDGFQLQNSNIHEBQLOLQLQLOLQLA@OLQLQNQLA@MJQNQLQLA@a@ZOLSNOLQLA?OLQLOLSNCBKHgAz@OLQLOJABa@ZQLQLOLA@QLQLQNOLQLQLQLEDKHOLQLOJSNOLOLC@YTIFOLQLOJQNIFGFQLQLQLQNQLQNQLOLQLOLQNGDIFQLc@ZOLEDKHQLSNo@f@C@QNQLOLOLQNQLQLQLa@\\OJe@^QNOJQNQLQLQNOLQLQNOLGBIHQLQLu@j@a@Z?@QLQNQLQLOLC@MJQNQLQNGDIFQLQNOLQJQNQLQNQLQNUPIHSLOLQLQNQLQLONKHEBc@ZQNQLk@b@IFQNOLSLONQJOLA@QLQNOLQLOJOLQNSNQLQNOJQLQNQNQLOLu@j@SNOLQLQLOLQLOLQLA@a@Zc@\\QLOLQLA@OLu@j@s@h@QLONQLc@\\QLOLSNa@ZA@_@XQLQNQLQLOLQNQLQNQLQLOLQL?@QLQLQNQLOLSNOLQLQNMJC@QLQNOLQLQLQLONQLQLQLOLA@OLQLQLQLONSLONKFi@`@QNOLQLQLQNQLOLMJiAz@u@j@s@j@UP_@ZQLQLQLKHuAdAGF]X}@n@g@`@{AjAKJIFMHc@\\OLg@^c@\\a@Zc@\\WP[Vu@j@a@\\c@ZWRKHQLOLc@\\c@\\c@ZOLQNc@Zs@j@c@\\a@Zc@\\gAx@s@j@c@Za@\\c@Zc@\\OLc@\\QLQLa@\\c@Zc@\\c@\\a@Zc@\\WRm@d@c@\\c@Za@\\c@\\c@Zs@j@u@j@a@Zc@\\c@Za@\\c@ZQNc@\\c@Za@\\c@\\c@Za@\\c@Zc@\\a@ZWR]Va@\\c@\\c@ZOLc@\\c@\\a@Zc@\\c@Zc@\\c@\\a@Zc@\\c@\\c@\\a@Zc@Za@\\c@Zc@\\c@\\a@ZUPcAv@a@Zc@\\c@\\a@Zc@\\c@Zc@Zc@ZSLQJMHUNi@Z_@Te@VYNa@RIFQHYLWNSHe@Rk@Ve@RSHQHi@RA@{@^e@RMDWLg@Rg@Tg@R[LyCnAyD~AaIfDoCjAqDzAoDzAsGnCgBt@mBx@_Bp@gCfA_CbA{B~@oEjBkChAaGdC_DrA}D`BwB~@{CpA{IrDaBr@oAh@_Bp@{QzHiCdAUJy@^YN{@^iAd@w@\\oAh@[LSHSHoAh@oAh@g@Re@RYJa@LUJe@Rg@RUJ[LSJs@Z{@\\y@^UHSHqBz@y@^_A^SJUHc@Ri@TGB_Ab@YLSHy@^UJC@sB|@w@\\wB~@CBOFuB~@{@`@c@Pa@Pq@VSHSJSH]NSHu@\\]NOFu@Zu@Zc@POH]NmAf@[LUJKDs@XiAb@kAd@GBs@Xi@RSHQHA?i@RQFUHuAb@KBSHYFg@NIBc@JODi@LUFSDUFUD_@Hs@Lm@JUD[D]FYDg@FK@I@o@FQBE?}@Hg@DS@M@O@c@BC?U@[@{@BoA@E?q@@s@AQ?I?o@?wCAA?U?Q?o@?U?w@?[?U?WAS?m@?g@?m@?s@AqA?_A?k@?i@AcA?S?U?U?gCAS?S?k@?a@?[?sDAeAAuC?yAAaA@A?}@@G?a@@cABaAFU@_AFw@FI@SBa@BK@UBWD_@D_@Di@Ho@JUDc@H_@H_@Fa@J]HIBs@P}@TYHMBe@L_Cn@oA\\WF[H}@VQFSDUFcBd@mAZkBf@w@Tu@R{Bl@_@Jq@PWF{@TiBd@o@NyBj@A?qCr@UFODQDg@LsA\\i@N[FWH[Fe@LoA\\UHaAV{@TIBaAVm@NQDoA\\yFzAkI|BG@]JUFa@JYHe@Lq@RmAZWHw@RODi@NWHg@LG@{A`@eAXs@RC@{@Te@Ly@Tq@PYHa@J_Cn@]JsA\\KDKB}@T[HC@e@LWFMDsA^g@LKBIBoA\\UFSFWFQFc@JcAXqA\\A@}@T}@VWFk@NQFg@LUFKD]HSFi@No@Ri@NEBa@Jw@VUHg@Pq@Ts@V[LYJq@Vs@XUHQHk@Tc@RyAp@gAf@QHg@VWLKDQHWLUJmAl@{@`@QHcAb@MFw@ZCBc@Pq@Vg@Ry@Xe@P{@Z{@XGBWH}@Xm@RUFIB_AXa@J[H{@Tg@LaCj@oAXi@LUDg@JUFqAV_ARkB`@UDqAXcATg@J}Bf@cATyBd@C?ODWDSDSFUDSDWFYFe@JUDSDQDe@J}A\\kCj@sBb@mAVqAVkB`@}Cp@UDUDSFeB^G?KBKB[HG@QDiB^q@NsIhBu@NUFwDx@SDSDSDuCn@w@N}RfEmCj@{Bd@cB^cB^A?k@LqDv@mATi@Le@J]FaDp@wDx@mB`@}Bf@iDr@oBb@mFhA{@P_Dp@gDp@aBZs@L_@He@HaC`@cC^w@N{@Lk@Fy@LgANsOvBsAPe@F{@LgC\\_ALuARcALuAPUDi@H{ARe@FoAPw@Jc@H]D]DkFt@_@DaBTE?eANk@Jew@lKqc@bG_H~@}BZaBVaPvBmC\\c@DeALoFj@cBPgAJYBI?UBgAJM@_@Dg@FoBP[B_@DUBo@Fo@F[BQBq@Fo@Fi@DC@S@UDk@FWB}BTC?g@Dg@Fk@Fo@FM@[Dm@Dk@FE@o@Fo@Fm@FSBC?WBWBYBm@FM@I@YBWBaAJA@o@Fe@BI@iAJQBG@O@WBYBc@FO@YB]DaAHMBYB_@Bg@DWBUBWBWBUBU@I@M@S@UBm@DE@Q@UBW@k@BO@_@BW@W@U@c@@[@]@o@@o@@k@@Y@cA@o@@K?a@?k@?A?aA?cAAi@?m@Am@As@?_@AW?i@AiBEmGI_CC}CEaAAoBC}@Ce@?aACkBCE?I?]Ak@AS?UAQ?E?S?UAU?WAS?OAm@AW?SAU?WA[AKAeACk@AU?UA_ACWAi@Ac@Aa@CU?SA[AQAWAUAc@AQAK?YAWAUAUAUAU?WAUAUAg@Cs@AUA{@ES?GAO?WAwAE_BGoBGW?UAWAUAUAWAYA]AK?WAA?a@A_@AWAk@CUAUAW?m@CWAW?SAYASAWAi@AWASASAW?[AOASASAW?UAS?UAE?g@AcACo@C_ACU?WA}CIWAU?UAW?SAUAC?wAEaACq@AkBEo@C_DGaACWAqBEWAaACU?A?oDIa@AsAEg@Am@AUAk@AU?UAw@A}EMe@AgAC}AEeBG]AqACUAwEKI?o@CU?c@A}AEoAEuACeACs@C_BC_@AmDKY?G?eACgCG}AEC?[Ai@ASAm@Ao@AKAo@Au@Cq@AA?e@AsAEcDGg@AsAEuBEUAkACk@CY?uBKi@EUASASCWAGAOAg@EUCi@Ee@GUCKAy@KmDc@kAO_@Ek@Ig@G}@MqAOc@Gs@I]Ee@Gk@Ew@IM?WCa@A{@Ca@AYAK?[?I?a@?O@W@E?u@@e@Bi@B]BG?c@Dk@Fg@FWDi@Fg@JMBaAPaATg@LyBr@iAb@y@\\m@XwAt@c@Vc@Vq@d@{@p@i@`@a@\\e@b@iA`Aq@l@UPyBlBWXKJc@^cBxAeCzBsHxG}AtAcA|@{@t@mBdBqAhAy@r@ONwCjCu@n@u@p@CBYVmAfAyBlBe@`@IHGFURgDxCiA`Au@r@A?sAlAaCvBwBjByClCq@l@cA|@a@\\yDjDuBjBs@l@qDdDGFMLQLQNIFm@h@oAhAk@f@i@d@QNWTcA~@QLi@f@OLq@l@SPeCzBeB|AQNo@j@QPOLYVm@f@QPMJg@b@iAbAKJOLKJo@j@s@n@a@ZQP_@\\OLyBnByDhDyBpBSNs@n@g@b@a@^OL_@Zw@r@sAjAc@`@m@j@wBlBcA|@a@^[XmC~Ba@^aA|@GDu@n@{AtAwDfD_CrBaEpDg@d@KHyClCeDvCYVy@t@WTc@^kAdAsAjAa@^eFpEgPxN}BrBYVe@`@sAlAo@h@CBWROL]XSN[RYPSLe@XQJy@`@]PODOHq@Ve@PSFq@Ta@JA?aATw@Nc@HI@a@Di@HUBg@DY@i@DY@i@@U?C?Q@S?W?o@AU?uAAk@AS?wA?uJImCAaEEeDA_@?w@AuAAkEEU?oECmDCmECsDC}@A{LIm@?uAAm@@A?g@?]@gABs@DE?uBL_AFs@HqANm@HM@_@HWDuATaANsATiBZuCd@}@NwAT}@NyAVoARWDOBkARa@FQDE@kIrAmB\\gAPcAPa@F_ANsQvC{B^wAVwAT_C^s@LmBZaAP]DgBZiBXgCb@yAVsB\\s@JiOdCoATqARQBu@LsCd@aAN}@NYFOBuARuEv@iAP{@NaBV}@Nk@JsEv@{AVwATk@HyDn@kEt@{GfAuGfAYDkCb@a@HA?a@Fu@L_MrB{QzCQB}B^MBYDi@HcEr@yCf@{HpAiBXaC`@QBe@HiARaBVwAToShD_BVe@HUDqCd@qKdBYFcDh@]D}@PsItAgMtBsy@bNyATqDl@[DE@a@Hk@He@H_APiAPuB^mANi@JUBOD[D}@NUDsB\\k@Js@Jq@LeAPg@Hi@Hg@Hi@Jm@Ji@Hq@J_@HYDYDg@HUDSDo@JUDI@sATo@J}@P_ANm@Jy@LaAPu@Lg@Hu@LMBOBc@Fm@Ji@Jc@Fo@Lm@Jm@Hq@LI@u@LqAToARu@LUD[DUDm@Jy@NK@gBZq@Ju@LgARaAN_@F_@Fa@Hm@J{@LaAPaAPq@J_AN}@Ni@Ji@H_APWDSBo@Jk@JUDa@Hi@HOBE@WFmB^KBKBa@HC@kAZ_AX[JA?g@P}@ZaA\\]Ni@Tc@P[Nc@RULk@XWLe@Vs@`@SL_@Ti@\\YPq@b@i@Zw@f@g@Zu@f@q@`@YP_@Va@VUNQJA?[Ri@\\WPa@Ve@Zc@Vk@^k@^e@Xm@^_@TQLa@Va@Ve@ZYPe@XEBe@Zm@^[RWPw@f@wBrAi@\\oAx@o@`@QJWN_@Ve@Zy@f@a@VUNIFi@\\c@VCBm@^c@XQLSJIFSLKFQLQJKFq@d@MFWPUN]Rc@XOJo@`@[RoAv@]T]RWPoAv@m@`@_@TSLs@b@s@d@q@b@_@TC@_@Vs@b@a@Xc@Xk@\\aAn@QJe@Xu@f@gAp@WP_@Tk@\\s@b@SNSLYR{A~@a@VQJu@f@u@d@c@XYPUNi@\\_@Tw@f@[RQJOJcBfA{@h@YP_@Vi@\\QJy@h@MHq@b@QJ]RQNg@ZKHC@_@TEBIDo@b@k@\\[RIFgEjCy@h@{A`Ae@XgAr@aAl@u@f@]R]Ts@b@KFwBtAmKxGuD`CmAt@aAn@y@f@iAr@qBpAe@X?@QJqAx@wAz@s@d@iAt@_@TKFKFSL[R_@VaAl@cAn@_Al@]T]TA?oAx@g@ZIDOJiAr@mAv@KF{@j@]RGDKFaBdAa@VKFaBdAyBvAOHi@\\_BbAWP[Rw@f@KFE@c@Xa@V_@VQJwDbC}DdCCB}@j@cAn@[Re@Z}@j@cAn@m@^EBYRe@Vm@`@i@Zc@Xk@^uCfBs@d@iDvB_Al@gAt@k@\\yA|@{A`AULiFfDA@A?cF`DgAr@gAp@c@XGDa@V]T_@TA@o@`@yDbCIFq@b@qBnA}AbAGBg@ZYRKFSLULsA|@oAv@QJ]TsBpAYRk@^s@b@QJ[RGDk@^_An@]V]X[Vc@^QNk@j@c@b@i@l@EDGHQPCDQRKNa@h@KLU\\CDGHA@W`@SZGJS\\GJGJKRkBdDs@pAA@s@lAYj@ILKPe@v@[j@GL[h@wBxDc@v@KP}@~Ae@z@a@r@iBdDo@hAg@x@s@rAKP{@zACFm@bAWd@qFtJyBzDMT_AbBw@vAqA|BQZe@x@mAxBCDkAtBu@pA_@n@S`@k@bAgB|C?@MR[j@Yf@m@fAA@k@bAo@jAu@pAINYf@S\\S\\A@Ub@ABKPSZOXw@tAwCjF]j@e@|@Yd@gB`DS^KRmCxEc@x@a@r@GJKP]l@mAxBy@xAq@jAs@nA_@p@c@v@]l@k@`AMTa@t@MTGHMTMToBlDk@bAMTi@~@_BvC{D`HU^e@z@e@x@Wd@QZc@t@_EjHk@bAw@tAiApBk@dAGJU^MT_A~AMVYf@KNe@r@EHQXW^OP]`@a@f@KL]\\IHEFUTOL_@\\SPOJ]VWRYRc@Xo@`@k@XMFi@XEBMDQJYJYLUHe@PODC@o@PWFKD_@HMBKBMBe@Js@JUBa@FC?MBO@i@DK@M@Q@i@Bs@@I@U?y@@wEAE?u@?Q?[?mE?e@?Q?w@?cA?_B?A?cCAI?gA?wE?eA?iA?iA?iB?w@?eF?g@?G?w@?o@A{A@cB?wB?eAAk@?iD?qA?_@?sB?mC?aBAuB?}D?_B?[?A?kC?kB?qAAA?uF?kB?aA?q@?gA?}A?_A?c@?{B?I?gB?I?wB?sC?U?kA?{F?iFA}C?uF?e\\A{A?mF?iA?eA?eEAkE?wC?qC?aA?U?mA?W?I?K@K?]?eBAcC?Q?K?E?yA?S?_A?g@?E?aA?iC?iCA}A?uB?C?C?M?M?C?a@?oA?yA?_D?sC?eA?_A?e@?sA?gA?W?o@?c@?_B?mA?kAAmF?mC?c@?uB?{A?}B?oA?[?}@?a@?iA?I?Y?I?sDAkB?Q?Q?{@?wN?kK?_H?m@?g@?w@?o@?A?iE?c@?K?c@?oC?_AA_A?cB?o@?S?k@?cA?yA?q@?c@?c@?u@A[@Y?c@?iA?eB?mBAy@?k@?gA?gF?eC?_f@AmC?wA?sP?aFAwJ?iA?}A?aB?sB?sA?iB?u@?_A?K?c@?E?]?c@?aA?Q?Y?_A?i@?{A?C?iA?_@?U?]?IAg@?k@?S?a@?Q?i@?oA?Q?q@?I?_A?G?I?O?s@?s@?i@?u@?k@?q@?G?sA?c@?qA?gA?i@?sA?cA?M?gC?G?kA?C?y@?eBAS?W?}@?iC?a@@S?e@?O?o@@i@?oABiABQ@M@}@BS@aBH[@Q@i@D_@@YBs@Fy@FM@iAJC@a@DkAJWDUBkALG@wARI@e@HOBy@LcAPs@L_@FUFgBZMBm@LaARoATG@_AR[FWF]Fg@Hg@JaAPaB\\{Bb@uFdAUDuBb@a@Fs@NcLxBaF~@aARg@JiCf@kHtAoCh@_F`A{@NG@kI~AG@_BZc@H_AR_HpA_BZiDp@{Cj@aBZcEx@_Ev@qS|DUDe@Jc@HMBGB_@F]HmATy@N]HwAXe@HWF}@PiATqAVw@NqAVc@HyAXk@L{AX_@FeB\\mB^{Bb@eBZIBiB\\_@Hs@Nw@NsAVQBaDl@wAXeATo@LyAXg@JmATg@JqATqAV}AZi@Ji@Js@Nc@Hi@Ja@HMDeAPi@LM@_BZe@H}@P_BZcAR_Dl@QDwAVyAZ{@NiAR}@RC?aARUDw@NIB{@Pm@LmATmATo@Lo@Ly@N_APm@LqAVsE|@QBQDWDUFk@Jk@JUFUDUDUDWFUDi@JSDOB[FmATmATk@J}@RWDe@HUDi@J_ARUDSDk@LSDc@HoB^k@JwAXg@HODWDk@LSDi@JUDUDC@c@HUDUDsAVUDi@LUDSDUDSDUDUD_APSFUDSDUDSDUDSDUDUDSDUDUDSDUFSDUDUDSDUDSDUDi@JMBG@SDUFUDSDUDUDSDUDi@JUDi@JC@g@HSDSFSBWFSDUD_APSDMDG@UDiB\\UDSDSDk@JSDUFk@JSDSDUDUDSDUDSDUDUDSDUDUDSDk@LUD}@PSDWDSDm@Lg@JSDUDSDUDWD_F`A_BZk@JKBIBA?m@JsB`@qAVuAVk@LaDl@GB_APg@JqB^oATi@J]H[FMBI@KBQDgARq@Li@L}@PmB^e@Hq@NC?w@Na@Hu@N[FKBQBsB`@w@Nq@NaAP{AZg@HaAPk@Lu@Nu@NSDWD{@Pk@JUDi@L}@NWFSD{@PYDuAXgB\\KBs@LIBYFe@H_APUDUFUDYDYFSDWFu@NiB^cAT}@Py@P_@Hy@P]H_@HOFYHKBm@Pm@RWH[Ja@NODKFu@V_A`@YLULA?WLo@ZKDEBg@Vg@X}@f@q@b@_@Vi@\\WPu@h@k@b@_@X[XKFEFyApAIHo@n@k@j@u@x@{@`AIJy@dA_@f@c@l@QVc@n@INYb@W`@OTUb@a@r@KRMTgApBk@dAIPi@`AiBhDs@tAS^a@t@Yh@OXOXi@bAINi@`AKP]p@cCrEg@~@qChFk@fAi@bAw@xAGHaAjB]j@CFk@~@y@rA_AzACBU^A@U\\iA`Bm@z@y@fACBeC`D_@d@uA|Ay@~@g@h@u@x@k@l@o@n@sAnAe@d@i@d@KJ{BlBABmBzAgAz@m@d@GD_@Vq@f@w@h@e@ZIDkAv@_@TeCzAUNo@\\sDtB}@f@mAr@{@f@IDoAr@i@ZaB~@KHaCrAuAx@OH}DzB_DhBmDrBkBdAg@Xy@d@i@ZMF_@RaB~@_CvAo@^q@\\OJo@^wAx@oAr@y@d@u@b@{@d@w@d@iAp@iAn@y@d@{@f@w@b@qBjAy@d@iAn@YN]Tg@XiAn@y@f@}Az@MHMFaAj@y@f@kAp@sAt@MH]Ri@ZkAp@{@d@gAn@y@d@m@\\[Py@d@e@Xw@b@}@f@u@d@MF_@TMFc@V{@f@uAv@q@^_Aj@WNy@b@iAp@mAp@o@^EBWNaAj@oAr@cAl@sAv@kAn@y@f@{@d@{Az@w@d@cB`Ae@Xw@`@eAn@oAr@_B~@s@`@SLo@\\_CtA}Az@_B|@cCvAqBjA}A|@cCvAcCtAc@Tc@VmAr@mAr@uDvBuAv@iAn@_B~@kAp@kAp@a@TaB~@qBjA{Az@wAx@OHOHwAz@_Ah@qBhAk@\\o@\\]RUL_@RaE~B_@TsBjA]R_GfDoAr@e@XmAp@WNSLy@d@c@TgEbC_Aj@MFKFuAv@GD[R]R}@h@y@d@OJm@ZSJA@_CrAOHkBdA[Py@f@c@Va@V}@d@GD_@Ri@Za@TOJmC|AgAn@{@f@qC~Ai@XiAp@qAt@MHiAn@e@ViAn@g@Ze@V_B~@w@b@e@X{Az@QJ{@f@iAn@i@Zc@VgBbA]RMH{@f@s@`@}@f@}D|B[PyCdBkAp@YPoC|AMHC@i@ZoAr@qAt@qAt@QJiCxAMHw@b@a@Ti@Ze@XSJgAn@SJSLWNOHULu@b@_B|@mBhAcCtAe@Xc@V_@RgGnDQJk@Z}A|@yCdBmAr@QHKFyAz@oAt@aAh@kAp@KFyAz@gAn@c@V}@f@KF]RA?o@^k@\\a@TsBjAmBfAq@Zi@VoCjAC@gA`@eA\\sA`@u@RaG~AgD|@aCn@gW`HgJdCq@Pc@LaB`@wCv@w@RaDz@i@N_AViAZaHjBo@NQFUFUDc@HK@UDSDc@FK@k@FOBC?[DkAFm@BM@K?[?i@@i@?i@?aC@aA?a@?i@?O?mA?q@?kB?eB?_@?_A?[?A?_@@}@?o@AwA@aA?cA?[?iE?}D?c@?eE?wA?}B?uC@qB?kC?s@?y@@aG?qB?eB?Q?W?[?iC?S?mE?sD?m@?m@?U?S?S?S?G?e@@W?yA?U?m@?k@?k@?U?cA?U?m@?qB?qB?U?y@?a@?k@?aA?u@?c@@o@Aw@?qC@o@?qA?o@@i@?S?yA@eA@{A@u@@qDFs@@iLRm\\j@mJPsCDI?cDF]@_@@cEFU@sABE?{GLsCDcBBq@@]@}ABg@BmDD{ADeGFiCBU@Y?U?U?A?W@U?U?S?A?U?W?e@@q@?W?U?Y?W?U?e@AC?U?I?a@?A?UAU?U?U?Y?S?O?yEAe@?mBAw@?e@AcKCk@AeA?e@?eAAW?S?G?w@AW?S?W?U?a@?_@AS?W?S?U?U?UAW?U?U?U?U?UAS?W?k@?S?S?U?UAS?U?U?W?S?U?W?S?UAU?U?U?U?U?U?W?UAU?U?U?U?U?S?UAW?U?U?U?U?U?WAU?S?U?U?U?S?WAS?U?U?W?QAS?I?K?U?aA?_AAU?S?U?U?U?U?UAU?U?U?U?U?U?U?UAY?S?S?W?Y?Q?S?W?S?U?Y?S@U@U@W@C?O@Y@WBA?SBWBS@UDWBUBUDWBUDUDUBUDWFSDWDq@PIB[HGB[Ha@Js@V}@\\QHSHi@Te@VSHIDIFg@VQJSLg@ZA?OJQNQJYRKHSNOJu@j@gLrIqBzAaHfFsFbEe@^eChBkDhCsB|AuB|Ao@d@GFsHvFgAz@y@l@c@ZkAz@]VkEbDYTsBzAaE|CuAbAi@`@MJ{AfAiDfCe@^cAt@q@f@{C|B}AjAe@^k@`@_@VaCfBSNgDdCe@\\QLs@h@QNkBtAQLs@h@e@\\QLaBlAeBpAmBvA{AjAaCfBy@l@iAz@}AhAw@l@SNuEhDoEfDQLc@\\w@j@u@j@u@j@u@j@mBvAc@Z_CfBc@Zw@j@s@h@w@l@eAv@c@\\QLQLe@ZYRg@Za@TYLa@TUJe@RYJc@PMDKDUHOD[JUFA?MD[Fg@LYFUDQB[FQB[DSBQB[BUBY@UBQ@Y@S@[@S?S?Y@[?M?Y?SAQ?sA?k@?i@?Y?a@?W?aAAsA?Y?w@?mBA_A?o@?y@?q@?_A?o@AuA?k@?i@?aA?k@?_AAcB@ka@G_@?_A?aA?uCAU?Q?yA?iB?U?k@?aBAiD?mFAwXEmJAsEAiB?eF?i@A]?}A?o@?O?A?C?eIAS?k@?uAAc@?yB?oCAg@?sB?O?y@?sAAi@?{@?Q?q@?_EAk@?o@?gD?kFA}@?Y?q@?_B?W?cAAm@?uDA}@?c@?aC?k@AoD?yCAqA?c@?[?yA?oA?[?c@AyE?cEAu@?wGAyUEyIAyC?s@?_PCcA?q@?kGA_FA{F?aBAyB?{B?kBAyA?qA?Y?y@?aAAmA?g@?kCAY?a@?iB?uB?yBAmC?cJCiB?kE?iEAuC?k@?[?uAAcA?g@?uA?I?m@Ae@?U?Y?Q?}A?S?a@A[?w@?gA?uAAwD?[?e@?E?aA?aDAuDAI?mA?A?]?k@?_A?i@?cC?qCAA?cC?cAAO?mC?O?U?oA?qDAuA?Y?eBAaE?u@?y@AeA?g@?kE?]?U?gA?a@Ag@?{@?]?i@?k@?]?kAAcA?qB?qBAeA?u@?wA?m@@K?W@O?Q@sBLUBk@Fm@HgARm@Ls@Po@PcAZa@LSFi@PKDWHq@ReBf@eCv@_AXy@TYJwDjAq@RyAb@yAb@m@Rc@Lg@NuAb@y@VWHK@c@LG@kA^SH[Ho@RIBa@LiBj@w@TSH}Ad@k@PoA^q@Rm@Re@NeAZkBj@m@PuBp@q@Ro@RgBh@q@RsA`@IDuA`@wBp@k@PgAZg@P}Ad@}@X_AXyAb@wBp@k@Pi@PgAZs@TcDbAmF~Ac@N]Jy@VeBh@oA^_Cr@kA^]J]JwAd@qA^}Ad@_GhBsIjCyAb@WHy@Vc@LQD_Bh@[HiDdAiBj@}FfBwBn@mBl@mBl@sBp@mBl@sBn@iBj@cAZg@NMDSFC@aAZIBe@NmDfAMBu@TkBl@UHWFQHgAZgA\\a@LUFwExAa@La@LKDUFMDkBj@o@R]HQD]Jq@RIDSFg@NeCt@OHuC~@q@RoBl@}@Ti@P}@X}Af@w@Te@N}@Xs@Ty@ViBj@m@P}@VcA\\u@TuA`@WHWH_@LA?}C`AyAb@iCt@yAb@kCv@[JqA^_D`AsBn@a@No@Py@VUHcBf@cBh@kDdAg@NQD[JeCv@}DlAcBh@kA\\OF_@JwBp@aBf@mCx@KDs@R}Af@s@ReA\\gAZm@Rg@NmDfAaFzAy@X_FzAcAXyAd@oBl@wDjA}Br@qA`@gBh@}Ad@oA`@kA\\eA\\gBh@iCv@q@TqDfA{DlASFs@REBk@PgDbAi@PcAZwFdB}ExA{C~@{Af@]JYHy@Ve@NgA\\o@RiBj@YF?@}Ad@w@TUHkA\\ODSHMBsAb@wBn@WHg@NkBl@sBn@}Bp@}Br@aAZcAZwA`@o@TYHYHa@Jc@Jc@HE@o@JSBa@Fy@Hs@Fc@Be@BcA@w@@{@AQ?{@EyAIA?UCg@G]E}@Mi@KeCk@sAYc@Kg@KWG_@I_AS_AUqBc@oAYeAUWI}@QqBe@A?eCk@y@QkAYq@MyA]y@So@Oi@KUGSEa@KaB]mBc@qBc@gAUoAYm@MuA[s@QeAUu@Qm@M_AUmCk@g@Mw@QYG{@S}@SuBe@kAWu@Oa@Ic@Ig@GSCSCw@Im@E[A{@E_AAYAo@@O?U@]?c@Be@B]BUBG@e@Dk@Fg@HSBUDk@JaARQBg@JaAPk@JQDYDKBq@LuAVe@H}AZu@Lq@Lk@J}@PuAV_APuCj@QBy@Nc@HaBZaCd@{B`@eAPKBkB\\]Fg@JWFe@HWDuAVk@LA?SDuAVk@J{B`@wCj@SBoB^g@JUDc@H[FiB\\UDw@NyAVmB^]FMBi@JUDi@J_APaAP_APi@Ji@Ji@JOB]Hg@HUDUDi@J_APi@Jk@Ji@Jk@J}@Pk@JuAVg@J]HuEx@{@P{E|@cHpAi@Ja@Fs@NcHnAuDr@oB^A?o@LsAV_APUDE@yDr@_AP_APoDp@UD}@PuAVi@JUDMBG@UDSDUDSDWDgF`Ai@HwB`@{AXaDl@q@Lg@HC@g@JG@w@Ni@JwAVs@LgCd@gGjA[F_@FaAPwB`@gB\\kCd@QDe@HOBODSDo@JE@s@LSDSDi@Jk@Jc@HYFg@Hi@J{@PSBUDUDSDi@Jg@Jg@Jm@JOBQDiARwE|@kCf@aCb@{@NsAVy@NuHvAc@HiEv@}GnAiATu@LmCh@UB_Cb@wGnAa@HgB\\yB`@cF|@A@WDI@{AXwOvC_Cb@sB^[FG@w@N}@PqAVwBb@u@NSDSDUFSDSDa@HYFUD_@H]Fg@LUDQDa@HG@SDSD{@Rk@JSFSDSDWDUF}@P{A\\u@NyAZ_@HWDg@LUDSDUDg@Lk@JSDUFQBC@g@Jg@La@HYFa@Ha@HC@c@Ha@HIBSDa@J[FSDUDUFUDIB]Fi@Li@JSDUFa@Ha@Jc@HUFQDSDSDWDi@Lg@JUDSFUDUDSDSFUDUDWFo@LUDODa@Hg@JUFC?QDg@JWF[FKBw@Pq@LSDUFSDUDSDSFUDSDUDUFSDUDQDUFSDi@JUDi@LSDUDSFSDUDaARYFKBi@LSDi@Jg@JUFk@JSDSF{@PaARa@H]HC?c@Jk@LOBQDG@SDUFSDSDWFWD_@Hk@L_@Hi@JYF[HyAZa@HyAZk@LI@q@Na@Jm@JWFSDC@m@LC@WDi@LOBw@N_@He@Jk@Le@Je@Jg@JSD[FIB{@Pe@Ji@Jc@J{@PSDSDg@Je@JQDA@g@Jg@Jg@JQDUDi@Lg@Jg@JQDSDSDe@JOBUFSDQBSFi@Jy@Pg@Jg@Je@Ji@JQD{@Pe@Ji@LOBUFi@LiARI@UDg@Jk@HSDSBUDi@Hi@Hi@HUBi@Hi@HUBO@YDi@FS@WD}@H_AHWBS@i@Fi@DUBi@Dk@Fi@DUBU@i@FU@SBUBU@UBSBU@UBSBi@DUBi@DE@e@DUBS@i@FU@k@FUBS@k@FS@UBUBSBW@QBE@O@UBU@SBUBA?S@UBSBU@UBQBA?UBU@SBUBi@DUBUBU@SBA?SBU@SBUBU@SBUBUBi@DUBUBS@UBSBW@SBUBS@UBUBS@UBUBU@UBSBI@iAJg@DSBeBLoFf@qE^k@FyD\\}@HaAHA?k@FiAHkALk@DE?c@Dm@Fy@Hi@Do@DcAJuALaAHu@HM@m@DcBNgAJsALeBNw@F}@HeAJcAHM@UBoBPy@Hg@DcAJi@DK@w@HC?y@Li@HaAN{@Nm@JWF]HE@]Hu@Rc@Jy@TgAZaAXqA^}Ad@YH}@Ve@LWHe@Ng@Le@NYHODk@PWHw@TgAZo@P]J}@Vu@TQDQFm@PgAZYHSFUHOBe@Ni@NwBn@_AVaBd@aCr@mA\\iA\\mA\\mA\\w@V{Ab@kBf@q@Rg@NmCv@_AXuBl@kBh@cAZoA\\YJUF_Cp@oCv@u@T_AVeAZkA\\aAXaAXA?oA^_AXMDE?_AXyAb@{@V{@VsBj@iA\\eAZmA\\_AVQF_AXUFMDOD]JaAX_AVcBf@sA^s@TmA\\uA`@kBh@iA\\mA^mAZgCt@iAX}Bn@oBd@QDSDSFSDUFUDQDi@J}@RUDi@JSFUDSDSDUDSFUDSDSDUDUDSFi@Ji@Jg@Ji@LUDSFUDSDSDSDi@J}@Rk@Jg@Li@Ji@Ji@Jg@LUDi@JSDUFg@JUD}@Ri@JSDUFMBE@i@Ji@Ji@LSDUDSDSDUFUDQDUDUDi@LSDi@JSDUDg@Ji@Li@Ji@Ji@LSDUDSFUDSDi@Ji@Lg@Jk@Jg@JUFg@Ji@JUDSFSDUDUDSFUDSDSDSDUDSDUFg@JWDQDUDUFSDi@Jg@Ji@Li@Ji@Ji@Jg@Li@JSDk@Lg@J_ARi@Ji@LSDSDUDSDSDUDUFSDSDOB[FSFSDUDSDSDSDUFSDWDQDUDQDWFSDSDUDSFSDUDSDUFSDSDUDSFi@LUFQDUFSFSFUFSFSFg@NUFOFE@UHC@ODSFOFa@NqAb@eBn@i@PoIzCqUnIuHhCg@RSF_@N_@L_@Na@Na@NWHc@Nc@P_@L]Lg@PMDQH{@ZC@YJWH]Li@Ro@Tk@Rs@VWJ[J_@LEBYJ_@LC@YJa@Nk@Rg@Pg@Ro@TSH_@Lg@Pi@Rc@Nw@Xi@Rq@Ta@Nq@VSFMDSHQFa@N_@Le@P_@Ng@Rg@Pk@R]Lc@Na@Ng@RWHi@PqAd@QH_A\\MDwAf@e@P[Lm@RsCdAID_@LOFSFm@TIB_@Na@NWH[Lg@P_@LWJKDG@WJ_@Na@NMDu@XUHk@Re@POFWHYJGBOF]LUHODMFa@L?@e@Ne@PSF]LYJg@PUHSHWHA@MDQFWHKDWJQFUHqAb@k@RQHUHQFSFQFKDq@VYHMFg@Pa@Na@NQFMDUHUJMDSH[JIBUJIBOF_@L]LKDm@Rg@Rg@Pk@Rc@Ng@PQHSFGBEBWHYJUJMDQFMD]LQFOFa@Ng@PQHMD[Jg@RKBMFWHSHSFSHSHOFWHQFIDYJUHSFIDODEBMDUHKDWJ_@Lg@Pa@Ng@P]LYLa@LWJSHWHQFWJYJODUJMDi@P]NSFQFa@Ni@R_@N_@LGB]LODi@RWJIB[Le@PSHG@GBSHUHSHSJWJe@P]NWLUJSJKD[NOFWNUJIFIBWN[NMFYPe@VGDSJg@X_@Te@VGBEB_@Rg@ZIDSLg@X_@Rw@b@_@T]Pa@TQJUNUJWPa@ROJULiAn@QJGBA@SLWLMHEBQJSJULCBQJa@T[Nc@Vq@^a@Vu@`@YP_@R[PQHEDmAr@]Rc@Ve@Ze@Xg@XeAn@ULu@b@QJSLUJ[PQJ]Rc@Ts@^YNSLm@\\y@d@WLw@d@_Ah@_Ah@_Af@o@^SLULa@Ty@d@iAn@CB_B|@y@d@w@b@EBw@d@q@^oAr@EB{@f@oAr@ULQJu@b@y@b@]RsAt@ULKFWN_B~@[Pc@To@^EBWNWNSLWLGBUNa@Tg@X_Ah@kBdA]Re@VYPm@\\y@d@mAp@q@`@q@^iBdAi@Zc@T]ReCvAEBa@T]Po@^]R]Ra@Te@X_@RQJA?c@VmAp@c@VQJ{@f@eB`Ag@Xk@\\WNm@\\_@R_B|@q@`@ULIDWNYPC@GBkEdCA?eH~DmC|Ai@ZYNo@^{EnCw@b@gAn@e@Vw@b@w@b@e@X}A|@s@`@_B|@mBfAOHCBu@`@qAt@q@^i@ZULOJGB[PGDa@TKFo@^_@RQJe@VYPMH]R]PeAl@g@XoC|Ac@VeAl@WNe@Xc@TKHgBbAOHA@OHUL?@IDYNwAx@uAv@]PA@}@h@}@f@{CdB]RGDk@Z_B|@_Aj@OHSJq@^q@`@ULy@d@k@Zm@\\qAv@]PWNWNEBi@XQJgAn@[NQJgBbAw@d@}@f@u@`@s@b@w@b@y@b@EDeAj@gAn@_Ah@{BnAwC`BUNgAl@uAv@WNs@`@IF_@Ri@ZWNYPYNc@VUNqAr@{BpAA@QJWN}@f@q@`@YN_Aj@yA|@OFuAz@OH}@h@GDu@d@MHuAx@E@kAp@u@`@s@^aAh@}BnA_Af@IDq@^MH]RULuAv@wAz@QJ}@f@}D~Bo@\\c@TKFQJg@Vc@VC@k@Zy@b@KDaAd@eAf@m@Tg@TcA`@IBs@ViA`@k@PEBe@Lu@T_@JcAVw@RYF]Hu@P}@PA@e@HOBMBYFYDSBgBVYDk@F]DK@UBK@_@DaAJ[Bi@Bk@DS@g@Bi@Bg@B_ADY@m@Ba@@I?k@BU@Q@e@@]Ba@@mADU@}@DaADg@BM?O@M?W@k@Bc@BI?g@Bg@Bq@Bi@Bk@@k@Ba@Bq@Bc@@aDLk@Bo@B{AFK@Q@S?e@Bs@B[BcADcADG?K@g@@[Bk@BaADi@@c@BkADmBHU@i@BS@Q@cBHA?a@@i@Bi@BE?oAFm@BiADW@C?u@Di@BQ@e@@_@BQ@i@@a@BW@k@BK@sAFi@Ba@@m@DK@]@O@o@FWBYBq@HG@g@Fg@Fm@J}@N_@Fc@J[F[FGBg@JQFa@HIBYHg@Lk@Pe@Nm@RQHc@NaA^eA`@gAb@gA`@s@XiBr@A@A?_@NA?aA^a@PWJy@Zo@VaA^YJs@X{Aj@gAd@s@Xk@RUJmAd@i@ROHUHaA^A@oBt@gAb@]Nk@RiAd@i@TE@KD[LOFi@TwBx@g@RcA`@}@\\sAh@cA`@c@PC@c@Pk@Tg@Pi@TuChA{@\\q@XYJeAb@g@Ri@Ro@VUH{@\\C@w@XkAd@[LA@yAj@e@Pq@VWLC@q@VMDOFSHa@NOFk@Tc@PeA`@u@Ze@Pk@T_@No@VGB]LYLSHg@Pq@XYJu@Xu@XsAh@[J_A^a@NA?UJoBx@iAb@w@\\{Al@k@Tk@Te@PcA^MDsAf@UJm@T]LSHa@P_@NSHmAd@o@TA@k@TcA^u@ZeA`@g@R_@N_@N}B|@s@XgAb@[Lo@Vm@TYLwAj@yAl@aAb@IBgAd@YNu@Xe@Tm@Vm@XC@eDvAa@PIDa@NIDy@Zi@TaA^SHQFe@RsAh@C@kBt@}@\\KDe@Pa@NuAh@MDIDIBWJ_@Ni@RsAf@k@VQFA@g@Pu@Xm@VYJKDq@VSH_@Nq@Vs@XUHGD]JUJwBz@}@\\g@Rg@R_@RYNo@\\[P_@V_@TWPSL{@n@MLGDUR_@ZWVMLC@OPML]\\c@f@QTaAlAm@|@?@i@x@MTKPOVEHYj@g@|@o@pA{AtCcApB}@bBk@hAy@~AqAdCS`@cCzE_@r@KRYh@KRq@pAKTaAjBaDjG]r@yArCYj@_BzCm@lAe@|@k@hAq@pAcBbDKTKR[j@a@z@MRc@z@KTYh@oBvDKTILGNS\\Wh@Yh@Wf@]p@GJKRKTKRKRWd@S`@yBhEw@zAoBxDGNqBzDoAdCQ\\EHa@t@MXU`@c@x@a@r@Yd@[h@i@z@QVU^KN]d@{@lAe@l@e@n@MN_@b@]`@]`@MLST_@`@c@f@KJa@^QPUTIJy@v@URGFEDWRa@\\i@d@KHa@Za@\\u@j@UPOJMJo@`@m@^SLQJe@Xe@XSLQJQJSJQJQJSJw@`@[PMFUJiAh@eBx@kAj@ULQHg@TQHSJg@TSJg@TIDkB|@qAl@A@qB~@_Bv@}FpCy@^c@R_@P?@_@PID_Ab@]NC@q@\\QHiAj@SHSJe@TSJe@Tw@^y@^s@\\eAf@c@R[Nw@^qB`AeBx@oAl@IDSJ{Ar@w@^aDzA_ChA]PSHQHe@Tg@VSHmAl@kHjDgBx@cBx@wBbA_@R_F|Bc@TSJy@^g@Te@VQHSJg@TSJe@TSJSHSJEB_@PSHYN_@Pe@TSJQHi@VOFULKDYLSLSHe@TQHUJKFsAn@SJe@Tg@Te@TGB_@P_Ad@}@`@[P{@^q@\\o@Z_Bt@c@Tu@\\m@Xe@TSJMFaDzAmAj@g@Vg@Te@TQHUJ]PYNy@^g@Tm@VUJ]N{@Zg@Rg@Pi@R{@Vi@PSFUFy@Tk@Ps@PGBsA^k@Pe@Lw@VYJSHUHSFk@TUHSHg@RYNYLa@PuAp@_Af@QJ_@RMH]R]VQJYPCBQLSLa@XQLu@h@QN{@n@C@YRA@MHSNg@^}@n@SNSNi@\\YPg@XSLULULWLUJULUJSJWJUJWJUHWJSHo@To@RC@i@NWFUHWF_AT_@JUDm@Nu@Rs@Pm@L_@Ja@JYFUF_ATgBb@UFo@Nq@PeAVsCr@s@PSDA@g@Le@JWHsA\\SDgAXu@PqBf@WFo@NUFeBb@QDo@N{@TcB`@eBb@u@PiHdBQDg@LiBd@UD}A`@kCn@WHYFgAXk@LGBuA\\QDqAZe@L{@ReAVg@Lq@PiAX]HcBb@o@Ng@LyA^gAVu@R_AT{Bh@mBd@oAZ_B^}Bj@[HiBb@}@TqAZaDx@uA\\iBb@}A^ODODkCn@GB}D`A{[~HoEfA}@TaAT]Ha@Jm@N}Bl@sA\\}A\\g@LcAVcBb@sCr@UFUDi@NkBb@WHKB}A^]J]Hc@JE@G@ODSDYD[HYHE@mAZYFQDWFg@LUFSDoBf@g@Li@NODMDmAXe@LoBf@gAVmBd@]J}Ct@kAXsA\\a@JoAZsAZ{@Pu@PiAXUFUDUFgDz@_@Hs@PeAVo@P[H{A\\oBf@cBb@oCn@cAXq@NoHhB{Bj@wBh@eB`@uA\\cEbA{@R_B`@aAVoBd@}A^{@TuA\\wD~@sAZ_ATsBh@u@PUFiDx@aEbAaFnAaAT_Cj@MBMDYHMBa@J_ATk@NkAXcB`@a@JkBd@SDqAZmBd@kAXE@[HmAXmA^QDk@NUFSDQD[JWFIBe@LUDuA\\}A^A?oBf@kBb@c@LQDODu@RE@kAVgBb@iAXQDy@R{@TyBh@OD{@TA?A?E@aAVA?cAV_ATMDcATODk@NeAVkAXgDv@cCl@}Bj@A@qAZaATcB`@A@qAZeBb@e@Li@LoAZeAVkAXYHoBd@w@RcEbAo@Nc@L}@Ri@NUFUD{@Tk@LaAV{@RMBEBgDx@aATKBi@NcAVuAZm@Ny@Ru@PEBk@LkAXq@Pk@L[HQDcAVG@a@JcB\\iAVYFgATYFmATeAR_BZgB^g@JwAZ]Hs@NeB`@q@P}A^c@LiAX}A`@[Jm@P]HUHQDaAXWHuBn@[HQF]JiCr@a@JA@eAZcHjB}q@vPiP~D{DbAyD|@mCf@q@L}ARcBP}AL{AJyBF_@@qB@uRMgBAwAAk@?aAAk@Ai@?k@?k@A_AAcA?aAA_AAi@?aAAaAAaA?wAAuAAaAA_AAk@A_A?cAA_AAaA?_AAaAAaAAaA?k@AaA?_AA_AAaAAm@?}@AcAA_AAk@?i@Ak@?aAAm@?aAAg@?c@AI?Y?Q?aAAk@?i@AW?}@AcA?_AAaAAuAAaA?uAAaAA_AAo@?[?a@AA?}@?o@Aa@?G?k@Ak@?_AA_AAk@?aAAaAA_@?a@AA?c@?Y?m@AS?O?[Ak@?i@AaA?c@AK@C?G?W?aAAw@AU?M?sBAU?SAcA?KA_@?[?E?{@AA?u@AK?_A?A?A?MCS?YAO?a@?OAwBAS?aAA]BS?k@Aw@?S?I?YAg@?C?O?_AAE?eAA{AAoBA_AAY?y@Au@CoBA}@A]?k@A_AAcA?m@Ag@?O@O?Q?k@?SAm@?o@AA?i@?[?O?_@AU?S?QAW?i@?YAW?S?m@?_@?I?W@U?U@U?O@G?U@U@SB[@UBQ@UBWBUBSDQ@QBMBQBOBQBIB[F]FWFUDWFUFUFSFUFUHSFk@PSHSFUHE@OFk@Pk@Rm@Ru@Vi@Pi@Pg@Pg@Nk@Ri@Pi@PuAd@sAb@uAd@uAb@u@VKBGBo@Rg@Pi@Pg@P{@X}@X}@Z{@Xi@P{@X}@ZA?_@Lq@T}@XoA`@qAb@g@PWHYH_@Li@Pg@P{@X}@ZoAb@i@Pi@P}@X{@X}@Z{@Xi@PSFg@Pi@P}@Z{@X}@Z{@X_AXIB]L}@X{@ZeBh@sAb@oAb@qAb@k@Re@N{@X{@X_AZ{@XqAb@]Ls@T}@X{@X}@Zg@N}@Z}@Xy@XUHi@Pi@Pg@PSFcM`EsL|DmExAoA`@kA`@}@XuAd@uAd@mA`@uAb@kA`@iA^oA`@aAZ}@Z}@Z}@X_AZsAb@sAb@qAb@sAb@uAd@mBn@{Bt@}Af@{Af@y@XuAd@uAb@sC~@e@Pu@Ta@NIB]La@LQFKBo@TE@]LqAb@UFg@PUHUFi@Ri@Pi@PUHg@PUFGBa@Le@PC?u@VEBg@PE?C@OBk@PsAd@sAb@}@Zi@PSFKFEB[Je@Ni@PSHYJMBQHA?WHUHi@Pi@P[Jg@PUHc@L}@Z_AX}@Z_AZaAZ{@X}@Zi@Pi@Pk@Rg@NMDWHSF}Ab@IBSFODUHaBh@{@Z_@J_@LyBt@SFG@cBj@}@Z{@X]La@Lo@T{@Z_@Le@No@To@Tg@Ng@Pi@Ps@T]Ly@XsAb@m@RKBEBC?C@K@o@Tc@NC?e@PE@QFg@Pi@P]NG@iA^}@ZmAb@g@Ni@Ri@PMDMHIBi@Pw@XUHSFi@P}@ZcBj@}@Z_AZ{@XmA`@sAb@y@XUHyBt@eBj@qA`@y@X}@Z}@Xs@TqAb@oAb@sAb@cBj@eBj@oA`@}@Z_AZ{@X}@XcAZC?EB]JoBl@gBf@{C|@k@Po@P]JC?_Bb@c@LOD[J{@TcAXy@Tm@PGBu@Ra@LgAZkAZC?SFMDSFsCv@oA\\kAZiAZA@eD|@G@cD|@o@PuA`@_EfAyBn@iAZiAZ}@VeD|@_AVwLfDcD|@qCv@uA`@kOdEcBd@e@LqDbAeCp@WHcAXgL`DiBf@UHa@JwEpAuCx@_FrAkLbDeCp@cD~@_FrAyQbFgL`DaEhA{ErAyA`@k@PaAT{DhAyQbFm@Pe@L[JoCt@a@LIBoElAy@TqBj@gAZk@Nu@Rq@RqCt@YHwBl@IB_@JqEnAUFIBaHlBaFtAMDYHgBd@MFC?SFq@RwA^_AXeAXmD`AmA\\aBd@_@J_@Ja@J_@Lk@Ni@NUFa@LaBd@aBb@{Cz@}Cz@IBc@LuBj@]HMDa@LMBuDdAe@Lm@PuA^QDgD~@KBoCv@mA\\o@PIBcAXe@L]Ju@Ru@TcBd@wA`@KBa@LA@ODo@Ng@N]Jc@Ja@JaAXcAXWHiBf@_AVKBwA`@{Bl@sA^qA^gBf@WFOF_Bb@o@PUHi@NeD|@iAZs@RQDUHWF}@Vy@Ta@LKBa@LiBf@_Dz@eD~@gAZe@L]JgBf@eBd@wA`@}Bn@sBj@IBWFSFOD_Cp@i@N[H}HxB{@V}@TUHMB]JODSFsCv@eAZ[Hk@NE@_@Lg@LUFODs@Rw@TKBc@L[JE@_AVYHQFgBd@w@TqBj@qA^uA^]JIBQDEBKBIBODkAZsA^{@VWHUFSDUHYHKBUFWHSDSFSFSFSF_AVSFSFUFi@NSDSFWHe@LSFg@LA@qA\\UFSFSFIBG@WHQDUFSFODYHIBa@LSDUHSDSFYHa@J_@LMBa@LE@SFKBKBQFQDk@NSHUDQFUFWHg@LMD[HSFUFSFUFUHQDSFSFYFOFSDUFSFUFe@N[HG@YHUHUFSDWHSFSFgBf@QDk@NSFUFSFA@IBm@NUHg@LWHQFm@RGBKBGBKDSFSHQFUJg@RUHe@RSJe@Ra@RSJ[NQJa@R[Na@TOJOHk@Ze@VQLc@Tg@X?@_@RWLSLc@Ve@Xg@Xe@VSLw@b@e@VQLc@Tg@Xy@f@s@^QJGDULWNgBbAeBbAcAj@_Ah@{@f@}@f@cB`AgBbA]Ri@ZaFpCsAv@s@`@EBoDrBIDSJQLSJUN{@f@KDQL]NgBdASLg@VSNOFUNULYNm@\\SLe@XiAn@g@XOHe@VULMHKFm@Z}@h@a@Ta@TYPe@VKHeFtCQJYN_Ah@oBfAQJi@Zc@VsAt@g@Z{GxDMHKF]Pe@XYNo@^iDnBiBdAYNKFg@X]PQLEB_@Ri@ZUL}BrAaCrAu@b@y@d@]RMHMHULQJULSJ_@Te@Xq@^gCvAo@^WNw@b@kDpBoAr@u@b@ULQJk@\\eB`AwCbBSJYPQHMJOFKFQJSLKFIDA@SJMHg@ZQHwBlAQLWLIFSJOHQJQJw@b@c@XGDKDGBq@`@QJIFg@XULo@^GBIDEBSLSJc@VSLQJSJy@f@SJ[PWN_@TUL_@ROJUL_@Rg@XQLg@VSLa@Tc@Vq@^_@RSLYPm@ZiAp@YPe@VQJQJQJQJQHCBOHQJQJQJA?u@b@c@Vw@b@QJOJe@Vc@VQJSJQJQJQJQJw@b@QJQJOJA?OHe@XQJMFEBQJQJQJQJIFGBQJQJQHSLQJQJQJSJQJQJQJQJw@b@QJQJQJiAn@QJQJiBdAC@QLw@b@QJc@TQLQH?@SJOHSLc@Va@TQJkAp@e@VQJQJSLSJ_@Ta@Ty@d@SJQJQJc@VSLa@TQH_@Re@Xc@VSJUNKFQJSJQJQJSLQJOHOHCBQHSJQJu@b@u@b@SJQLULMFIDqC~A]ROHOH?@SJc@VGBKFSL]RMFeAn@u@`@u@`@_B|@qAn@A@{BhAiAh@MHg@TYLUJu@\\eBv@g@Tk@TQHWLs@ZmBz@GBsJhESHq@ZSHoD~AcBt@oAj@g@TuCnAOHQHc@RiAf@o@XwIzDu@\\oAj@UJSHsB|@A@_@Nw@^IBC@KFi@TWJq@ZUJYLMFUJSHQJSHSHwB`AIDWJIDID[Lm@XMD_Ab@QHSHSHu@\\WLKDGBUJUJ{@^OFQHi@VUJ[N[LmAh@UJUJe@TOFaAb@IDIBSJQFSJUJQHUJSHSHULe@RUJ_@PWJSJWJOFSJYL]NWLIDgAd@s@ZkAh@A?_@PIB]PSHSJSHg@Tg@TSHWLOFQHSHc@RaAb@y@^e@RUJYLQHOH_DtAiAf@aAb@SHg@TWLa@PQHSJSHSHUJSHSJQHWJQHg@TaBt@YLOFSJQHIB]Pi@R{@`@QH{@^wB`AKDGBiCjAUHSJSHSJSHSJ}@`@q@XE@ULSHSJSHg@TSHg@TSJq@ZG@QJk@TSJg@TOFWJkCjACBw@\\y@^UHe@RQJSHUJQHi@TcAd@A?IDIBIDSJGBIBSJUJg@TMDEBSJOFWJSJSHSJSHSJSHyB`AWLKDSJYLMDWLOFIDIDUJSH[NuAl@YL[NSHc@RA?c@RSHUJQHQH]Nu@\\SHSJUHCBMDOHMDIDYN]Lm@XOFQHIDa@PQHWLQFy@^SJQHi@Ty@^MF[LSHSJSHQH_@PGBID]NYLa@Ro@V_@RWJQHQHA?c@RUJSHUJy@^i@TIDWLqAj@i@Tq@Z[LC@iAh@C@_@N[NE@s@\\SHUJi@Vc@PkAh@c@RmD|AuB~@{@`@g@T{@^i@TmAj@qAj@{@^uB~@}@`@o@XIDuCpAq@XUJQHUJe@T[LQHa@PSJGBIDULUJWLC@YNMFSJWLGDs@`@QJIFIDMHc@Xe@XQLCB[RWRYR[TCBKHQLMJUPa@^MJSPYVKHWVSRMJCD]\\[\\WX]\\WZONORQRUZ]b@ORk@t@W`@GJSZi@x@KNKPe@v@CFS^QZKRa@x@c@x@CFqAlCe@bAoAlCSd@OXWj@O\\gAzBABQ\\mAhCq@xACFSb@c@|@m@rA]r@[r@Ud@Wj@CBSb@?@S^ABKVQ\\IPMVCDO^QZGNIPYl@yA|CKRKT[p@GNQ\\EJOZYl@MVSb@MVEJO\\]t@_@t@[p@y@dBIPKTSb@Ud@GLMXUd@Wh@KVABOXS`@MX]v@Sb@OZOZKTQ^S`@Q^Q\\?@KROZIRMVQ\\Qb@c@z@Q`@OZ[n@MXSd@CBS`@MZSb@]p@Sb@[p@Wh@Ud@m@tAQ\\o@pA]v@GLINKTWh@MV]v@Yj@Uf@IRMVMTKTKTUf@Wf@?BKRUd@Wj@Wh@KTWh@Q^CFWh@MVWh@IRMVIPKR[p@[r@a@x@O\\Wh@Wh@]v@QZSd@m@nAABIPMVWj@Q\\Q`@Ub@GN]p@o@tA_@x@e@~@Yh@KRe@z@ABWb@MTKPMRWd@MROR_@n@KN[d@Yb@IJCDMPMP[`@MROPOROPY\\_@d@QRY\\GFk@n@MNUTi@l@_@^MLw@t@SR]ZMJ]Zc@^]ZWREDUP[Ta@ZKHIH_@VSNSNUNSLYRQLUNMHSLULOJ_@TWNQJSJQHWNOH[PMFSJa@RULQHC@UJSJi@TKD[N]NSHe@PC@OFWJi@Py@X[L_@LQD]L_@JUHUFSFSFe@NODMBOFSF}@VeBh@UFQD]Je@NUFe@NWHg@LUHe@LUHOD_AXgKzCeAZoA^kA^g@Ne@Lk@Py@VwA`@qA`@UF}@Xi@N}@XQDQF{@Vo@R{@Vi@NiBh@{EvAiBh@{@Xg@NaAXy@VqA^g@N{@Vk@Nc@Nm@Pi@Ng@N}@XQDOD_@Lw@T_@J_@Ls@Rm@Re@Lk@PSFe@LwAb@aAXUHy@Tg@NgBh@cD`AMD{Ad@cElAc@L_@Lg@Nc@Lk@P{Ab@[H[JgBh@iBh@u@TcAXA@}Ad@_OlEG@gEpAc@JuGnBYHSFkA\\}@X_AVi@P}@VYJMDa@LyAb@[HOF{Ab@}DjAg@NsK`D]Lc@LODoErAsF`B}Ab@oJtCeD`AmBj@}M~DcCr@_@Ls@Rq@R[H]Jg@NKDMBw@Ve@LIBcLhDqCx@o@Ra@LG@sBl@eDbAkA\\eI`Cw@Tg@NSFWFa@NWH{@ViA\\SFm@P}@VgCv@aCr@YHMD}@V_AVe@NGBMBa@LmA^k@No@Rc@LaAZgCt@gA\\g@NqIfCa@LoA^g@NQDa@Ly@VmA\\{Ad@eFzAUHqErAaFxAQF}Bp@gGhBQFcFzAuBl@{H~BsCz@oZ~I}@XeD`A_ZxI]JqErA{DjAaAXMDkA\\qOrEaD`A}@VMDuP`FoErAaElA_GdB{FdBSFMDSDe@NeBh@a@J]La@LqA\\mA^gDdAaWrHeAZ_D~@iAZsTvGWH{@Tm[jJmErAQDeBh@yBp@[JQFKBQDWHIBGBUHSDSHWHe@LUHWHOFi@Pg@Pg@PSHUHaA\\MFc@NA@YJk@Ra@NEB]LaA^UJsDvAq@X_@NQFUHe@Ri@RmAf@qAf@i@R{@\\UHw@\\YJOFSH[LiAb@GB[LsAh@m@Tc@P{B|@ODYLoBt@m@Vk@TcBp@QFa@Na@NgAb@q@XuAh@WJy@Ze@PMDUJOFkCdAC@c@Ng@TuAd@}EnBeE`Bq@XkAd@IBw@ZaBp@A?_@NcC~@cC`AsBx@a@NgFpBeAb@KBC@EBUHKD]NC@[LODg@To@Va@N_@Nk@RoAf@i@RQHq@Vc@PaC~@_A^y@ZyBz@s@XoHvC_C~@QFaBp@e@RuAf@c@Rk@RoAf@MFs@VkCdAgBp@QHSHe@PYJiAd@o@Vy@ZqHvCc@P]LSHQFUJA?SHcBp@A?SHSHUJSFSJQFWJu@XiBr@cA`@MFQFKDC@OFMFOFUH{@\\g@Ri@Te@PWJ[LQFMF_@NWJMDOFGBi@RQFk@RQHi@P[JKD_@Le@NKDc@Lq@RUFUHSFcAXa@JYHSDSFg@LWFq@Nk@LSFe@HWFc@JgARKBaB\\ODm@LUDi@JC@QDUDUDSFK@IBUDi@Jk@LSDWDWFg@Ji@Lk@Jk@Lg@Jm@LSDi@JUFi@Jk@Li@Jk@Li@JYFm@Lw@NaARsAXi@LUDE@e@J}@PaARiB^k@Ji@LUDi@JYFg@J_ARWDk@Lg@Jk@L}@Pa@H]HiDr@aARi@JuCl@y@P[FUDk@L}@R_APk@Li@JWFQDk@JwAZo@LMBuAXSDk@LiATs@LaARk@Li@Ji@Lm@Li@JUDi@LsAXkATuBb@k@L_AP_ARUDw@P]F_ARwAZQDk@Ji@LkAT}A\\uAXUDuAX}@PuAXWFMB]Hi@JSDMBcATkATa@Ji@Jm@L}Bd@g@J_AR_BZc@Jk@J}@Pk@JC@iB\\g@Jk@Lk@JSDQDeATe@HYFSDWFSDSDi@LUDk@LQBSFQBq@Na@HOBe@JqAXkB`@G@mAVi@JA?i@LgB\\ODI@sBb@QBa@JmFfASDUD[FMBUF[Fc@JUD}@PG@k@LeB\\g@Lg@JE@i@JSDk@L]F]HQDOBMBa@HE@A@[FE@G@i@J{AZsDv@gFdAmHxAsDt@_ARk@Lm@LiB^_Cd@YFa@Hg@J]HsAV_ARa@HKBgB^e@JKBaB\\A?_ARKBmATqAXMBwAXwCn@aAPE@mCj@QDUDoB`@}Bd@QDgATUDQDWDg@JoB`@wBb@A@]Hm@L_@FE@oDt@KBs@NMB}@PWFy@P}@P}@Ro@Jk@L]HuAXKBA?a@Hu@Nq@NGBeATKBMBIBQD_@Ji@N]JWHa@LA?KBq@VWHOF{@Za@PKFUJi@TYLKFWJGDKFULk@XKF]RYN]TIDe@XYRo@b@EB[TGDWRKFMJQLA@IFWTMJMJSPi@d@e@b@KHo@j@IFGFOLiAdAQLa@`@GDUTWR_@\\[ZA?w@r@a@^WR[ZIFq@l@a@^KHED[XOLu@p@OLc@`@ONKHA@URo@j@GFi@d@QNIHMJQPIFYVm@h@k@h@i@d@a@^c@^QNs@n@ONURo@j@cA|@c@`@_@\\ED[VIHGDONEBUTEBw@r@y@t@_@ZIHQPm@h@a@\\i@f@QNe@`@]Z[Xi@d@A@QPMJm@h@]ZaAz@{@t@}AvAMLi@d@]ZURYVc@`@a@\\yApAe@b@YVIFq@l@k@h@gA`AUTo@h@CBcA|@ONA?o@l@wAnAe@b@KHs@n@k@f@k@f@eA`AaAz@CBsAlAc@^a@^IH[XqAjAOLA@q@l@OLs@n@C@q@n@a@\\QPSPKJ[XIFa@^KHm@h@MLkB`Bm@h@ONcBzAA@mBbBMLOLABoAfAURKHSR_@\\SPQNQPk@f@YVKH_Ax@_@\\IJy@r@g@d@i@b@a@^IFGHa@\\]XQPEDSPSNQNIFSPQLOLOLUP_@XKHgAx@YRe@\\c@XABm@`@YR]T[PSLQLa@VWPu@b@YPGBy@f@MFk@\\_@Pk@Zk@ZUJSJkAl@y@b@A?a@R{BjASJkAl@u@^sAp@SJiAl@gB|@gCpAQH}@d@oAn@sBdAqBdAWLgB|@wAt@CBeCnA_@RGBmAn@e@Tk@XqBdAmAl@sAr@OHmAl@w@`@CBe@Tg@VkAl@g@VoAn@uBfASJQHOHe@VE@u@^ULg@VEB_@ROF_Ad@iAl@C@{@b@g@Xe@Te@VcAf@]PMFsAp@e@VUJQJUJmAp@cAf@q@\\QHq@\\q@\\yDnBs@^mB`AkAl@kAl@iB~@g@VOHSL}@b@e@VSJm@ZiB~@qAn@oAp@{At@YPi@V_Bx@kAl@mCtAaHlDiAl@mAn@w@^i@ZYLCBC@]Pu@`@mCtAwAr@UJsBdAcCnAgCpAUJmGbDiB|@EBm@ZmE|BiB`AwCxAKF_JrE{BhAu@`@k@XUL[NOHo@Zo@\\C@s@^KDA@QHQHa@TA@{@b@MFIDQJ{@b@m@XOHa@TOH[NSJIDg@VMFk@XULKFSHQJo@\\_@PQJy@`@mAn@sAp@MFkAl@qAp@w@`@m@Zu@^g@V[PsAp@WLOHs@^i@Xw@^CBcBz@OHuAr@eAh@QHWLyAv@_@PMHIDqAn@GDwAr@ULwAt@MFeAh@q@\\s@^_@RiAj@{@b@OHEBqBbAOFoAp@o@ZeB|@sAr@]PQHiAj@EDc@R{Av@}Av@y@`@OHkAn@u@\\a@TYLu@`@uAt@yAt@}@b@y@b@A?c@Tc@T}@d@UJi@Xo@\\}Av@oAn@KF_ClAKFqAn@GDgAh@SJ?@c@TSJQHGBGDUJ]Ru@^QHKFg@Vi@XID_Af@UJe@V]NMFeAj@c@RaAf@OH}Av@{@b@QJKDIDu@`@mAl@y@b@g@VA@iDdBoAn@o@Zm@ZULa@RoAp@SHmAn@c@TeB|@IFqAn@c@TSJoAn@QHQJMFeAj@MFw@`@{@b@w@`@SJy@`@IFm@ZMFk@XSJOH[Ps@\\C@gB~@eAh@OH[NMFUL_@ROHWLSJm@ZOHWLk@Zu@^m@ZeAh@[PYL]Ro@Z{@b@o@ZE@YNE@k@Xc@P[N[L_@NWHk@Rg@Py@Vs@TuA\\_ATwAX_@H]FeANUDa@DSB[DWBK@k@Fi@DO@m@DI@a@B[@I@s@B[@i@@E?[@c@@M@K?O@[@a@@U?m@Bq@@w@BU@aABq@BM?Y@e@@M@[@Q?K@c@@W@m@@I@_@@_AB{@BG?uADG?c@@I@_@@W?m@BK?aCFeBFQ?mAD]@W?Y@O@{AD{@Bi@@U@_ABG?y@Bk@BU?]@a@B_ABS?Y@Q@m@@m@BS?k@BU@W@gBDeADU?s@BI@a@@i@@qADC?cBFaADM?]@a@@]@M@qADI?{@BK@k@@uBFu@Bu@BiABm@B}@BO?q@BaABO?q@Bw@BU@s@B{@BS?A?g@@_@Bk@@S@k@@y@Bm@B_ABe@@M@s@@W@gABG@c@@aELs@@e@@u@@w@@}@@o@?uA?UA_A?s@A_@A[?s@C_@Am@A_@Ag@Cc@Ak@C_BEc@CgAEe@AuAEsAEk@CqBGoEOcAEo@CkDKkFQgL_@oFQeAEmACe@CiCImAEK?eACUAKAaAA}@AcAAU?k@?i@@g@@g@?W@O@[@_@@S@U@U@U@U@Y@K@Y@Q@WBS@YBUBS@SBWBUBUBQ@WDSBWBUBSDUBUBUDMBK@c@HSBWDUDODUDWDSDUDQDWFQDWFUDKBIBSFQDUFSDQFq@Pi@Pk@Pu@VKBeA^OFm@TSHa@N_A`@OFUJSHSJQHIDKDQHULSHSJSLYN]Pe@XQHSLSJQJQLSLOHSNQJQLQJA@OJQJIFEBQNSLOJSNc@\\a@ZSNOLQNQNCBUPA@UPSR_@ZQPOLg@f@EBSRSROLQPOLONGFg@d@QPCBMLQNUT{@x@QPc@`@MLQNOPONC@qCnCqApAYXKHOP_@^}BzBQNq@p@]^_@^aA~@a@`@a@^a@`@YXOL_@`@YVKLSPONiChCi@f@QRc@`@sApAaA`A_@^a@`@OLOP]\\[Z]Z[Zq@n@a@`@]^SPON_@^a@^ONONONSTkBfBOPSRsEnEONwCtCqInIoBlBYXqApAoAlAq@p@k@h@}@|@KJe@b@MNON{@x@e@d@eAdA}AzAKJa@`@oAlAm@l@gAdAkAjAYVg@f@w@v@gAfAcAbAu@t@a@b@uAvAA@cBdBaB`BcAbAaI~Hy@v@ONwCrCwAvAi@h@OP]Zq@n@c@d@IHQP[ZiAfAc@d@a@^WVa@`@]Z_@^_@`@e@`@c@f@qAnAu@t@eBbBsBpBUTgAdA{@z@{@x@g@f@YXEDgDbDq@r@YVCBq@p@wAvAg@f@IFYXwAvAe@d@}@x@YX{@z@yAnAy@r@MJ{@r@s@j@w@l@y@n@SL[VMHC@q@d@a@XYPcAp@}@j@KFk@^y@d@CBu@`@e@Vg@Xu@`@c@Tg@V]Pg@T_@Ru@\\]N_@PYLqCjAkAf@SHC@WJGDa@N[Lq@XOFC@cAb@_Bn@}CpAm@VkEfBmBx@_@Nq@XeEdBo@VYLoAh@i@RoAh@qDzAUHg@R{@^A?_A`@o@Xk@TGBi@R}Ap@y@\\gBr@gAb@]PoBx@A?w@\\e@P{@^cA`@A@yAl@g@Re@R{@\\eBt@IBkCfAu@Zq@XMFeBr@]NeAb@i@Tq@XaA`@y@ZaAb@_A^_Bp@aBp@WJ}An@{B~@_C`AaBp@oAh@u@ZMDw@\\q@V_@LoAb@}@VoA\\m@Nw@P[FYF_BXOBSDw@JkANUBe@DaBLw@FeBFS@o@@Q?s@@q@?_A?u@Ao@AA?UAi@CYAOAA?I?WCI?y@GC?_@E_@CWC]EiAK_CWC?c@EeAKs@I_AK_AI?AA?C?GAa@EWC}@KI?A?AAE?a@ESCOCq@Ge@Gq@G]EUCw@GSCeAM_AI_@EKAOCo@Ii@EWCUCm@G_@EcBQ{AOgCW[Cu@Iy@Iy@IkAMUCUCWCUCUCUCUCWCUCUCUCUCSAUC[ESC]Ca@E[EQASCWCUCSCWCUCUCWCSCWCWCUCUCSCWC]CQAQCUAUAUAEAM?UAW?UAU?O?E?U@M?m@DQ?W@SB[BQ@MBG?G@Q@UDa@FYD[DUDSDQDQDSFUFSDQFQFQFSFUHMDKDSJOFQH_@PWLULUJQLWLMHQJOHCBOH[POHMH_@RMFSLQJQJQJg@XQJQJSLSJSJQJWNQJMH[NKHSJSJSLQJQJSJSLQJOHGDs@^w@b@YPMHkBdAIDc@Vo@^gGjDyAz@q@^e@V[PSLWLYPw@b@k@Z}@h@wDvBqBfAkLtGeBbAcAj@gGlDOHs@`@aAj@aAh@m@\\s@`@q@`@cDjBo@\\iAn@a@Tw@d@sAt@_@Rc@VwAv@g@XeAl@c@VKF_@RIF_Ah@QH?@A?ULKFC@WNKFA@_@R_@TmBdAa@TMHA@SJmCzAcAl@C@WNGDy@b@KH}@d@}BrAoC|AoC`BMFSLyCbBmC|AqAt@uAv@}EnCkBdA_DhB_Ah@{Az@c@VIDc@VQJ_@RgCxAk@ZoAr@m@\\SLe@Ve@Ve@Xg@XQJe@VSLQJSJQJSLQJSJQJSJQLQJSLSLQJQJUPKBC@QJQLQLSLQLQLQLOLQLSNQLCDMHQLQNOLQNQNQNOLQNQNQNONQPONQNQPMLQNOPONOPONONUTKLQPa@b@ONOPON[\\SRQPONOPONOPONONOPMNa@b@ONQP]^OPQNOPONOPONKLWV_@`@_AbAq@p@ONa@b@k@n@WV}@~@[\\KLaAbAONOPONONSROPONOPONOPMJQROPONKLA@OLQROPKHABSRONONOPONMNQPKJSTOPONONQRMJQTSRiAlAu@t@m@n@m@p@IHONIJONKLURMPONQN?@ONKLUR_@b@QPQPIJQPOPONQPSTKJc@d@KL_B`BSVWVQROLOPONQRA@KH_@b@k@l@QP_@`@OPONQPONOPONOPONCB]^ONONOPON_@`@IHWVOP_@`@SROPONOPONOPQNOPON_@`@OPiAjAGFOPOPa@`@ONOP_@`@ONOPONONOPONOPMLSRKJOPONONOPONOPONOPONSRGFGHONOPEDWXIHYZUV_@\\OPWTONKJQNs@p@}@x@YRe@`@a@Za@ZYV}@t@MHg@^[ToA~@KFMHsA~@UNq@d@QJy@f@C@{A`Ak@^]TA?OJOJ_B`A[TGD{@h@eBdAMHEBIFeBfAq@b@ULoAx@KFGDUNq@`@SLUNGDWNWPA@eC|AA@s@d@q@`@MHEBe@Xg@ZoAv@s@d@IDYRgAp@kAv@kAr@aAn@OHOJc@VKH]TGBQLSJSLq@b@i@\\aAl@_Al@{@j@_BbAqAx@e@Zo@^aJzFqAx@o@^y@h@gHpEe@ZWNg@Zo@`@a@VYPmAv@y@h@SLA@mAx@iAx@YRIF{@n@oA`AGDGFq@j@aAv@SPQNA@}@x@ON[XA@YVcA`A[XCDu@v@A@s@r@_@`@IJeAhACD_@`@MNYZuAzAkApAeAjAq@t@yA`BQRIHkApA{@|@MNqAxAq@r@uAzAMNOPSRGFOPc@f@uB|BiBpBgAlAe@h@IHu@v@Y\\e@f@qAvAu@x@i@l@oAtAOPONOP_@`@WVMNIH[\\k@n@{@z@KLEBOPMNKLUTKJu@z@[\\OPqCzCa@b@e@h@m@n@WZcAfAy@|@{@~@g@f@IHKHSP[VQLQNo@b@_@TYPULWLQJy@b@[N}@f@]POHiAj@yAv@"
                                    },
                                    "start_location": {
                                        "lat": 27.4146674,
                                        "lng": -80.3921191
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.1 mi",
                                        "value": 235
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 9
                                    },
                                    "end_location": {
                                        "lat": 30.3045678,
                                        "lng": -81.64229069999999
                                    },
                                    "html_instructions": "Take exit <b>348</b> toward <b>Interstate 95 service Rd</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "wn}wDzphqNUEUHUJE@UJ_@NIDOFMFIDSJSJSJUJKFSLULOJq@b@"
                                    },
                                    "start_location": {
                                        "lat": 30.3026826,
                                        "lng": -81.641262
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.5 mi",
                                        "value": 816
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 31
                                    },
                                    "end_location": {
                                        "lat": 30.3103446,
                                        "lng": -81.64747589999999
                                    },
                                    "html_instructions": "Take the ramp to <b>Downtown</b>/<wbr/><b>Main St Bridge</b>/<wbr/><b>Acosta Brg</b>",
                                    "polyline": {
                                        "points": "qz}wDhwhqNMHIFUPED]Va@\\QP[XCBMLQNONMNmBtBIHGFOPu@x@k@l@GH]\\WXEJ[ZOL[\\OLe@`@EDEDSNOLURQLQL_@VOH}A`Ay@b@c@TUNSLOLIHGDGF]XONEDEBEF"
                                    },
                                    "start_location": {
                                        "lat": 30.3045678,
                                        "lng": -81.64229069999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.7 mi",
                                        "value": 1144
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 45
                                    },
                                    "end_location": {
                                        "lat": 30.31433729999999,
                                        "lng": -81.6576734
                                    },
                                    "html_instructions": "Continue onto <b>Interstate 95 service Rd</b>",
                                    "polyline": {
                                        "points": "s~~wDvwiqNOLOPOPQPMNIJCFOPMRKRMP[j@[f@KRYd@MTMRGLEDMTGHCFORKNOTQTKLGHILOPOPONOPMNMNONQRQPOPGFUVOROPKNORKPMRS^KTITKTADABEJADGPIXGRGVEVGXEVCVADCXARCX?X?@AV?V@V?J?f@?L?d@@Z@~B?Z@P?Z?V?Z@n@@X?Z?B?R@V?X?F@fA@T?V"
                                    },
                                    "start_location": {
                                        "lat": 30.3103446,
                                        "lng": -81.64747589999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "299 ft",
                                        "value": 91
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 5
                                    },
                                    "end_location": {
                                        "lat": 30.3146852,
                                        "lng": -81.6585151
                                    },
                                    "html_instructions": "Take the <b>FL-10</b>/<wbr/><b>US-1</b>/<wbr/><b>Prudential Dr</b> exit toward <b>Main St Bridge</b>/<wbr/><b>Ocean St</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "sw_xDlwkqNGPCHAJALAHAJA@CLGPADIPCDKRGH"
                                    },
                                    "start_location": {
                                        "lat": 30.31433729999999,
                                        "lng": -81.6576734
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "1.2 mi",
                                        "value": 1938
                                    },
                                    "duration": {
                                        "text": "3 mins",
                                        "value": 176
                                    },
                                    "end_location": {
                                        "lat": 30.3312381,
                                        "lng": -81.6552402
                                    },
                                    "html_instructions": "Continue onto <b>FL-10 W</b>",
                                    "polyline": {
                                        "points": "yy_xDv|kqN]\\QLWNA?UHMBQDKBM@WBMBKBK?]@k@?g@?}@CeAC}@Co@C_@CE?G?A?A?[A]Ac@A_@AC?I?K?A?C?GAE?u@AkBEiAEyBIy@CQAA?OAq@EmBIiCMgAGeAEgAGsBKG?Q?YAEAC?GAEACAICCACAACCACACCCCECCECCCEEGEKYe@Wg@We@MYMSMQIKIGUOIECAaAWMGg@MeAS[GyCm@y@QwAWeASSEy@O]Gc@KYGYEa@IqCg@}@Q[GMCq@M"
                                    },
                                    "start_location": {
                                        "lat": 30.3146852,
                                        "lng": -81.6585151
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.1 mi",
                                        "value": 171
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 27
                                    },
                                    "end_location": {
                                        "lat": 30.33273359999999,
                                        "lng": -81.654819
                                    },
                                    "html_instructions": "Continue onto <b>N Ocean St</b>",
                                    "polyline": {
                                        "points": "gacxDfhkqNi@KmAU]GkB]g@K"
                                    },
                                    "start_location": {
                                        "lat": 30.3312381,
                                        "lng": -81.6552402
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "384 ft",
                                        "value": 117
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 16
                                    },
                                    "end_location": {
                                        "lat": 30.3330064,
                                        "lng": -81.6559944
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>E State St</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "qjcxDrekqNUzAIh@Kx@Kh@"
                                    },
                                    "start_location": {
                                        "lat": 30.33273359999999,
                                        "lng": -81.654819
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "285 ft",
                                        "value": 87
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 21
                                    },
                                    "end_location": {
                                        "lat": 30.332246,
                                        "lng": -81.656216
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>N Main St</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "ilcxD|lkqNf@LB?TDtAX"
                                    },
                                    "start_location": {
                                        "lat": 30.3330064,
                                        "lng": -81.6559944
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "190 ft",
                                        "value": 58
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 16
                                    },
                                    "end_location": {
                                        "lat": 30.332119,
                                        "lng": -81.65562849999999
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>E Union St</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "qgcxDjnkqNVgB@M"
                                    },
                                    "start_location": {
                                        "lat": 30.332246,
                                        "lng": -81.656216
                                    },
                                    "travel_mode": "DRIVING"
                                }
                            ],
                            "traffic_speed_entry": [],
                            "via_waypoint": []
                        }
                    ],
                    "overview_polyline": {
                        "points": "uqf|CzmmhNcGkAhGhB|PbLNd@jHzKxMpTfMrSeBnF_IsKu@aAqDaFaLoEe]U}v@uDor@lEumAz`@swD`FslAkAcxAdJigEjGulCdEiqBvDsy@dH}l@vi@mgAnu@ozExH{~@_b@_cAsz@geAoIi}ClHs_HvKgjBlJcyASokD`GilDxAyl@aMiq@of@ar@ui@ytCy}B}~AapA{j@iW_jAaBo}@hKouCfA{eF~E}gL|DsjEtEiyCbMenHiKooGr@siP~Ee_Cr@cw@Mo`Ao\\ieCglBis@qq@s}@}i@ioB_JwrCqE{_IgQmeEwFicByBk~AuBwvArRk|B~u@acAx\\mfBll@kiAxa@iiBpkAekC~dBszAftAqaBfoByxAhbBifAx]aqAhA_nCtv@svBhu@kpAnbAqrBzoAsvE`qCuhD`rBeqEvgB{wFtkA}nCpoAcpA|d@shAfRixArAqvBGw|AxHk~D`}Aw|Abm@kw@pBqQc{@bAqOyBjIgeBNgxAb_@yr@x^ky@znBuy@~nAsqBpu@cxBfq@_iAvb@kn@|d@_dAxw@yxA~hAadA~w@qoBbbAazCjpAu|@~VsxAbBenBpg@mcDj`AowD~v@csFzr@onChDgsDgJstAwGy|@`i@mhAdbAofBx}A_hAr_A{o@dDu|AnAccBvXyeI`sAi_BvWsrAf_@cgCt_BggFzcD}bAb}AgmA`xBec@pt@gX|LknCXilKQeaCEqsBnWm~GfrAa{B~b@uyAhYcd@xOg`@~e@wi@t`A_y@~p@_}B~qAy{FjeDwwBpnAymBlj@qm@n@qsCZqhDbDo|Ab@atFtyDk}JPimDa@}gAMwu@zOioCbz@}`Cpt@clD|eAogAx\\{u@tMytBka@ahBb[sxGfnAatCrk@q}Brd@srCpVq`F`rA{rBfb@odGfuBkmHh`Ey`B|~@eyArr@krCxPeqDlvAywApk@q^`Xgn@|lAq}@|{AwlAfo@ctDtbBabAr`@ogCln@kfHveBgyHpiB}oE}BgbAGoiAr]ojFjeBc|QnnFccEziAolBfv@yxGzwDi|Gh~Co`CleAel@`r@ci@viAmpAt_C__DhgAkcLtgDqlIhoCynD|pAo~Dzx@{jEz|@sp@f^cq@dm@}_CnrBkqFtqCgwDfnB{oAzo@aeAz[ggDjIsrBwCen@tRcpCfkCanBtlBeeB`z@avBbt@{|@sGux@sGmf@pRwsEfjC{mA`nAmyAdvAsaBxdAcmAxiA_pBvcBkXfc@?`ZoKdHst@mFyg@qOwH`DpDgA"
                    },
                    "summary": "Florida's Tpke and I-95 N",
                    "warnings": [],
                    "waypoint_order": []
                }
            ],
            "status": "OK"
        }, "places": [
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7665181,
                    "lng": -80.2019991
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Calle Ocho Plaza",
                "place_id": "ChIJw3-9-Y622YgRYWXCmMaNMek",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7789389,
                    "lng": -80.1878931
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Themidnightclubrentals",
                "place_id": "ChIJ30KwmJq32YgRoLPKAjeAzgk",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7896077,
                    "lng": -80.2172372
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Whateverforever09",
                "place_id": "ChIJW3Dmjri32YgRmXArI-EokJE",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.92864149999999,
                    "lng": -80.1955076
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Claroma Shops",
                "place_id": "ChIJAfgMFWmv2YgR4C3_ELSt4j8",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.740819,
                    "lng": -80.278453
                },
                "icon": None,
                "name": "the-biltmore-hotel-miami---coral-gables",
                "place_id": None,
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Camping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7623624,
                    "lng": -80.19407199999999
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Hampton Inn & Suites by Hilton Miami Brickell Downtown",
                "place_id": "ChIJn-2Oo4a22YgR-fOW2Yuryjo",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7588046,
                    "lng": -80.1922639
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Four Seasons Hotel Miami",
                "place_id": "ChIJB4u6yIC22YgRSudXSqzWT0k",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.77052149999999,
                    "lng": -80.18933919999999
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Kimpton EPIC Hotel",
                "place_id": "ChIJlWF1Gp222YgRkg_v_MAt_Sc",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7709263,
                    "lng": -80.1910809
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Hyatt Regency Miami",
                "place_id": "ChIJlZUqA5222YgRzjtasuQFBNg",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7754416,
                    "lng": -80.18836689999999
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Dump Hotel",
                "place_id": "ChIJEZE3EZ622YgRsVmaEQPx0Pk",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            }]
        }
    }}
)


save_trip_response = openapi.Response(
    description="Success",
    examples={"application/json": {
        "success": True,
        "code": 200,
        "data": {"route": {
            "geocoded_waypoints": [
                {
                    "geocoder_status": "OK",
                    "place_id": "ChIJEcHIDqKw2YgRZU-t3XHylv8",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "geocoder_status": "OK",
                    "place_id": "ChIJ66_O8Ra35YgR4sf8ljh9zcQ",
                    "types": [
                        "locality",
                        "political"
                    ]
                }
            ],
            "routes": [
                {
                    "bounds": {
                        "northeast": {
                            "lat": 30.3330064,
                            "lng": -80.1287327
                        },
                        "southwest": {
                            "lat": 25.7525792,
                            "lng": -81.6590157
                        }
                    },
                    "copyrights": "Map data ©2023 Google, INEGI",
                    "legs": [
                        {
                            "distance": {
                                "text": "347 mi",
                                "value": 558649
                            },
                            "duration": {
                                "text": "4 hours 59 mins",
                                "value": 17965
                            },
                            "end_address": "Jacksonville, FL, USA",
                            "end_location": {
                                "lat": 30.332119,
                                "lng": -81.65562849999999
                            },
                            "start_address": "Miami, FL, USA",
                            "start_location": {
                                "lat": 25.7617059,
                                "lng": -80.1918211
                            },
                            "steps": [
                                {
                                    "distance": {
                                        "text": "492 ft",
                                        "value": 150
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 40
                                    },
                                    "end_location": {
                                        "lat": 25.7630117,
                                        "lng": -80.1914355
                                    },
                                    "html_instructions": "Head <b>north</b> on <b>Brickell Ave</b> toward <b>SE 12th St</b>",
                                    "polyline": {
                                        "points": "uqf|CzmmhN_@IEAWEKCc@KwBa@SEIA"
                                    },
                                    "start_location": {
                                        "lat": 25.7617059,
                                        "lng": -80.1918211
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.1 mi",
                                        "value": 173
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 51
                                    },
                                    "end_location": {
                                        "lat": 25.7616832,
                                        "lng": -80.1919705
                                    },
                                    "html_instructions": "Make a <b>U-turn</b> at <b>SE 11th St</b>",
                                    "maneuver": "uturn-left",
                                    "polyline": {
                                        "points": "yyf|CnkmhNG^r@LXDd@D\\Ff@Jp@Nd@J"
                                    },
                                    "start_location": {
                                        "lat": 25.7630117,
                                        "lng": -80.1914355
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "423 ft",
                                        "value": 129
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 32
                                    },
                                    "end_location": {
                                        "lat": 25.761603,
                                        "lng": -80.19325040000001
                                    },
                                    "html_instructions": "Turn <b>right</b> onto <b>SE 13th St</b>",
                                    "maneuver": "turn-right",
                                    "polyline": {
                                        "points": "oqf|CxnmhNBh@@LBpA@j@BhA"
                                    },
                                    "start_location": {
                                        "lat": 25.7616832,
                                        "lng": -80.1919705
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.2 mi",
                                        "value": 321
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 64
                                    },
                                    "end_location": {
                                        "lat": 25.7588092,
                                        "lng": -80.1940642
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>S Miami Ave</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "_qf|CxvmhNp@P\\FnB\\b@F\\FdBZXHnAV~@PZH"
                                    },
                                    "start_location": {
                                        "lat": 25.761603,
                                        "lng": -80.19325040000001
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.8 mi",
                                        "value": 1242
                                    },
                                    "duration": {
                                        "text": "2 mins",
                                        "value": 110
                                    },
                                    "end_location": {
                                        "lat": 25.7520564,
                                        "lng": -80.2038467
                                    },
                                    "html_instructions": "At the traffic circle, take the <b>2nd</b> exit and stay on <b>S Miami Ave</b>",
                                    "maneuver": "roundabout-right",
                                    "polyline": {
                                        "points": "q_f|Cz{mhN?@?@A??@?@?@?@?@?@?@?@?@@??@?@@@?@@@@@@??@@??@@?@?@@@?@?@?@?@?@A@?FFNVR\\|BxDrBdDtBjDJPh@z@r@hAPRhBzCNVlBdDrBbDpBdDnBfDpB`DfBzC"
                                    },
                                    "start_location": {
                                        "lat": 25.7588092,
                                        "lng": -80.1940642
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "377 ft",
                                        "value": 115
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 24
                                    },
                                    "end_location": {
                                        "lat": 25.7528756,
                                        "lng": -80.20454769999999
                                    },
                                    "html_instructions": "Turn <b>right</b> onto <b>SW 25th Rd</b>",
                                    "maneuver": "turn-right",
                                    "polyline": {
                                        "points": "kud|C`yohNmAbAuAfA"
                                    },
                                    "start_location": {
                                        "lat": 25.7520564,
                                        "lng": -80.2038467
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "3.7 mi",
                                        "value": 5980
                                    },
                                    "duration": {
                                        "text": "4 mins",
                                        "value": 269
                                    },
                                    "end_location": {
                                        "lat": 25.8034526,
                                        "lng": -80.2055907
                                    },
                                    "html_instructions": "Turn <b>right</b> to merge onto <b>I-95 N</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "ozd|Cl}ohNi@w@m@y@c@o@w@eAa@i@KMu@cA[c@u@cAACU]IEQWAAQAEIMQKSQWIOAAKSU]EGKSCCKMMSKKCEGGGIOMMKCCKKECCCMIKIEAWQYOECMEECMEECOECAKE[IC?QGUCEAICKCSCQCOA_@CU?W?UAW?m@Ai@AU?W?]Aa@?e@AC?a@Ae@?m@AY?i@A_AA}BC[AE?O?WAS?[?U?MAM?U@U?Q@W@U@[@WBU@mAJm@DQBC?U@i@DqBN}ALYBWB_BJA@_AFg@DW@W@U@W?G?K?U?G?OAU?SAUCUAUCA?e@G]GSCWGWEQEUEQEWGQEQGKCOEc@Mq@UWIQGSGSGSGUIUI_@MyAe@}@WQGMCICMEEAQCWESCOAOAUAa@CS?[?O@O?K@G?K@S@G@O@SBOBE@SBSDUFQDUFSFSHQFSHA?SHSFWJODUHSHSFQDWFQDYDQDUBI@I@W@SBU@[@y@@o@@w@@sBBY?S@aCBq@@]@eA@o@?g@@e@BaAFs@HM@S@SBiC\\a@Hk@L}@Te@NQFE@UHg@RUJa@PIB[P{@Zy@ZgBt@MFeAb@iAd@UJg@RMFm@VOFm@V_@NyAn@G@m@VaA`@o@XGBs@X[N[LQHw@Z[LC@C@A@C@A?IDMFyAn@aCbAkBt@kA`@WHcAXo@Lq@Jm@LQBa@HE?SBSB{@HuAFW@_@@a@@cA@oB?_B@y@@S?aA@iB@i@?A?a@?cC@wD@{@@gA@}CDeABcA@wBDcAB_ADs@@{EFgA@"
                                    },
                                    "start_location": {
                                        "lat": 25.7528756,
                                        "lng": -80.20454769999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "7.4 mi",
                                        "value": 11936
                                    },
                                    "duration": {
                                        "text": "7 mins",
                                        "value": 401
                                    },
                                    "end_location": {
                                        "lat": 25.9104018,
                                        "lng": -80.2100117
                                    },
                                    "html_instructions": "Keep <b>left</b> at the fork to continue on <b>I-95 Express</b>, follow signs for <b>Express Lanes</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "fork-left",
                                    "polyline": {
                                        "points": "qvn|C|cphNEDEBEBIBI@e@?_@@W?aA@o@@W@s@?uAB}CBW@W?O?U@wA@yCDC?g@@mBB}@@k@@m@?e@@U?I@S?_A@e@@[?w@@g@@u@@cA@k@?k@@i@?A?_@@A?C?A?Q?S?M?i@@Q?W?U@U?Y?e@@qA@Q?m@?U@g@?m@@_@?_A@k@@U?kA@A?gB@_@@g@@o@?K@K?W?W@U?c@@G?m@?{ABY?gABS?E?S@_BBk@@a@@M?u@@i@@a@@sABc@@k@Bs@@A?kADe@@g@BaABkABC?u@Bi@@C?g@@a@@u@B]@c@@c@@Q?a@@aAB[?O@K?U?Y?e@?Y?OAK?[Ac@Ae@Ce@E[C]CIAWCi@IM?w@MoAUw@Os@Ko@Im@Ga@Ec@Ec@EiAEs@ASAU?[?S?W?g@?k@Bo@@G?C@c@@gBBO?oCF{BBI?w@@q@BcEFmA@C?y@BgA?eC@Q?wA?qAAyCAm@?k@?Y?aA?Q@S?K?y@@Q@}@AE?S?Q@A?S?k@@k@Bk@D}@Hc@F}@PC?YFq@N]Ls@TiBr@C@]Lm@TUJ_@LA?MDQFWF{@TSDK@YDYF_@Da@D[Bw@DO@W?kAD_BBiBFs@@kADkGNQ@C?oCFm@BW?k@@Y@c@?W@gAB_A@mKJg@?yABqBBwGFyABo@?eDDs@@uA@qCBa@@oCBU?Y@Y?K?M@q@?cCB{FF{CBcCB_HHuA@_DBQ?iCBq@@q@@sCBG?O@_@?i@@m@B{@BgAFA?g@BcAFk@De@DK?I@A?]BI?k@Bw@Bs@BW?iABcA@_@@G?Q?]@i@@Y?I?S?M?E?W@S?W@Q?W@U?S@q@@O?Q?O@Q?S?U@U?U@U?U@S?W@U?U@U?W@E?K?W@U?U@U?S?S@[?Q@W?U@U?S@S?W@U?U?U@S?U@U?W?[?Q?U?S?UAA?U?U?UASA[?OASAS?UAUAU?SASAU?SAS?S?U?S?U?S?U?c@?{@Bc@@e@@U?U@W?S@W?k@@]@M?i@@k@Bi@@i@@cA@S@U?Y@i@@k@@U?i@Bk@@W?i@@]@y@@[@e@@c@@}@@c@@U?i@Bm@@k@@i@@A?k@@k@@m@@i@@}@Bk@@U?m@@k@@{@Bc@@I?wCFS?k@@i@@i@@e@@U@g@@k@@g@@c@@eBBC@gBBA?q@BW?e@@A?{DFa@@S@c@@sBFeAFi@Bc@B_BJG?c@@?@a@@Q@y@Bm@BgBFa@@e@@g@@K?S?e@@c@?e@@Q?S?yC@K?OAO?_B?c@AiA?[?GAe@?iLAI?y@AcB?_BAqC@cA?"
                                    },
                                    "start_location": {
                                        "lat": 25.8034526,
                                        "lng": -80.2055907
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "387 ft",
                                        "value": 118
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 4
                                    },
                                    "end_location": {
                                        "lat": 25.9114363,
                                        "lng": -80.2099051
                                    },
                                    "html_instructions": "Take the exit toward <b>Florida Turnpike</b>/<wbr/><b>FL-826</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "_sc}Cp_qhNUE]?e@@w@?O@MAOECAIEAA"
                                    },
                                    "start_location": {
                                        "lat": 25.9104018,
                                        "lng": -80.2100117
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.5 mi",
                                        "value": 802
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 32
                                    },
                                    "end_location": {
                                        "lat": 25.9186414,
                                        "lng": -80.21019249999999
                                    },
                                    "html_instructions": "Merge onto <b>I-95 N</b>",
                                    "maneuver": "merge",
                                    "polyline": {
                                        "points": "oyc}C|~phNeB?[?oDBGAK?A??@{@?yHHoBDc@@g@@qEJs@B_HN"
                                    },
                                    "start_location": {
                                        "lat": 25.9114363,
                                        "lng": -80.2099051
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "1.2 mi",
                                        "value": 1954
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 81
                                    },
                                    "end_location": {
                                        "lat": 25.9348563,
                                        "lng": -80.2155609
                                    },
                                    "html_instructions": "Take exit <b>12 A</b> on the <b>left</b> for <b>Florida's Turnpike</b> toward <b>Turnpike</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "ramp-left",
                                    "polyline": {
                                        "points": "ofe}Ct`qhNQLI@k@Dm@Fu@HeANc@H}@N_@HI@q@JYFWDYDMB_@FOBm@JA?I@A?SD]D_@FA?I@YDa@HI@I@s@HuAPe@FA?i@Fc@FU@o@Fe@F]@g@D{@FUBi@DO@E?WBE?M@k@DWBg@DW@i@DaAFSBWBU@O@E@S@WBS@c@BWBK@c@BM@UB]BiAJG?[BgAH}@Fo@Dy@FC?G@[@UBC?o@Fm@DQ@y@FS@UBG?MBU@IBI@KBG@QDIBKBQHIBIFULMHSNOLGFMNMNEFEFMRg@x@SZY`@GHW^SXOR]d@EDUZa@f@k@l@]`@EV"
                                    },
                                    "start_location": {
                                        "lat": 25.9186414,
                                        "lng": -80.21019249999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "108 mi",
                                        "value": 174478
                                    },
                                    "duration": {
                                        "text": "1 hour 33 mins",
                                        "value": 5560
                                    },
                                    "end_location": {
                                        "lat": 27.4049094,
                                        "lng": -80.3988579
                                    },
                                    "html_instructions": "Merge onto <b>Florida's Tpke</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "merge",
                                    "polyline": {
                                        "points": "{kh}CfbrhNaB`B[Z}A~A{@z@k@l@KJOP]Zc@b@STUVe@d@g@h@IH_@^[\\_@^A@]^i@h@ONYZw@x@UV]\\]\\QPYZGFmBpBi@h@[\\UTEDSTIHON_@^YXg@h@QRiAhASROPYXMLYV_@^GD[X_@\\e@`@s@j@a@\\c@\\c@Z[Vk@`@c@Ze@Zw@d@y@h@e@XQJA@oAp@KFk@ZSHmAl@e@Tk@Tc@RoChAcBn@i@RSHSFi@P_AXi@NSFi@Nu@PeB`@OBu@N]FUDYF_ALg@He@FE@WBk@Hg@Fo@FSBWBUBSBW@SBU@m@DaAFU@w@BA?gADY@{@@}AB{@@{@@oCDeABE?Y@{CDwA@gCDy@@]?gABO@cBBiEFqB@sC@w@?Q?i@@oB@}CDwABsDFaB@i@BqAB_A@q@@i@@wABA?mA@s@@a@@qABU?yBBu@@u@B[@]?eABeA@A?G@i@@sA@U@gA@c@@k@@O?]@k@?i@@U@uHJc@@_HJq@@sABO?[@k@@uABqBBaCDU?S?U@k@?gA?iBAW?kBGUAU?UAMAK?g@EUAWAWAUCUAGAOASAWCMAk@GUCk@Gm@IQCC?UCQCk@IuASUEUESEUEUEMCWGk@Ks@Qu@Q_AUOEi@Mc@MMEGAECGAEACCaAYg@QCAMEaA]aBm@uB}@y@_@SKWMe@U{@c@MIGCm@]OI]Ue@Wa@Ye@YSMQMOIc@[QMQMUOQMi@a@u@k@SOYWQMOOa@]QOcA_AaA_AKKc@c@UU_@_@OO[]MMs@s@OOc@c@KMSQOQc@c@y@y@YY_DaDgCkCeAeAq@q@_AaAOOWU[[[_@QOa@c@_@_@MMWW[[SSi@i@YYYWOOQOEEKISOQQ_@[WSs@k@IGOKQMQO]UQM_@W_@Wm@a@i@[YQQKy@e@m@[aAg@iAk@QIICWMmAg@e@QcAa@OGOG[KOEKEe@O}Ac@SGCASESGi@OWGk@Mm@MUGKAUGUESEg@ISC{@O{@MmAQ_AIq@I[Ck@Ga@Ca@EaAGI?e@CSASA[AC?y@Cy@AI?QAq@?O?_@?[?Q?M?U?g@@_@?I?]@U?i@@U@Q?m@@aCDC?y@@}ABgABC?Q?{@@eCDoBBkDFk@@_BBo@@O?}@@_AB_DDqDDoDFkABU?aBB_EFmEFyCFkBBqBBW@yA@uABk@@kIL[?S@e@?yCDwBDO?iBDm@@m@@g@@E?i@BU@k@@U@U@S@U?U@m@B]Bi@BQ?S@cAFG?mAF_BHaBJmCLA?eDPcDPcBH{BLiCN_I^]BE?{DP{BJS?m@Bc@@aAB_AB_BBO?gABE?M@c@?eCBuABiKLcDDmCDU?gCDk@?aCDuUXyFHyABeA@s@@_B@eABiBB{BB]?iFFiBBmBBy@@c@@cA@i@@[?{@?[@}@@Y@U?Y?Y@c@@i@?k@@y@@E?m@@e@?sBBoCDs@@gCDkDD}HJ_GFaCDeCBi@@W@i@?m@@sABo@?_ABU?W?U@E?O?k@@_@@mCDsDDi@@o@?}@BuA@yABmBBaA@uA@m@@W?S?U@U?M?G?Y?A?S?s@@K@Q?o@@W?i@@m@@k@@i@B[?g@?c@@aABg@@}AHmAFw@@S@c@BU@}AJk@Bc@Bc@BK@}BPO@[@a@@g@BU@]BW@aADqAD}AFeADo@Bw@BaCJA?S@gAD_BF]Be@Ba@@yAHG@iBJ{AJaBJkCTK@sAJu@Dm@FyAJcAJ}@Fw@FaAFq@Fm@DQ@e@D_AF_AFkBJq@DqAF}@Bk@BS@e@@O@c@@G?uADS@aA@o@Bm@?_ABaDDW?_ABsBBi@?}@B[?e@@o@@u@@O?o@@O?S?C@w@?S@K@G@G?K@O@M?S@_A@A?qABQ?O?Q@W?{@@gBBs@@g@@qA@}CDs@@{ABmA@s@@oA@a@?aAA_A?m@CmACKAaBGe@Cq@Eo@Eu@I{@Ga@EKAWCm@GWEKAUCMAWCi@EMAa@Em@IQA_@Em@Gw@Ie@Ec@Ge@EIA_@Ek@Ee@GWCs@EMAm@Eg@EUAm@CiAEs@C{ACi@?kB?g@AQ?W?o@@S@_@@g@@sADk@Bo@Di@BW@SBaAFg@Fk@Do@HkBRaANu@HyARy@JWH}@Js@JYD_@DaALi@Hk@Fe@Hk@Fk@Hk@H{@JUBi@Fk@FWBUBS@i@Dg@DYBg@BU@W@U@g@BY@S@i@@U@U?U@_@?u@@}@@m@@_A?g@@]?cB@o@@uA?Q@W?S?W?S?U@S?Q?S?W@]?s@?o@@cA@U?W?S?i@@W?W?_A@]?eDBsA@aDBuA@yA@_A?Y@aA?m@@wCBk@?i@@yGDmLFS@i@?o@@S?k@?aA@A?[?]@]?S?Y@S?c@?G?U?U@U?Y?S?S@Y?}@@{A?S@}@?E?]@_A?Y@c@?k@?aA@y@@_@?m@?i@@k@@U?eC@U?oBBk@?i@@U?}@@[?K?Y?sB@U?W?aA@aA@W?U?U?W@S?i@@Y?oC@m@@_@?k@?U@U?U?U?U?U@U?U?U?W@U?aA@yA@k@?U?U?S@W?K?K?S?W@k@?W?U@U?U?S?U@S?W?U?S?m@@k@?cA@Q?cA@kGDU?gDBaB?S?W?W?wA@S?U@S?[?U?U?SAW?UAk@AWAaACm@EUAk@Cg@EQAo@EsAMeBQa@Gi@Gm@IqASYEk@Kw@O]GQEk@Mk@M[Ge@Mu@QQGOEUGkBk@_A[c@Oa@MoAe@_@OwAm@WKa@Si@UmBaAsBgA]Uq@_@g@]YOaAq@s@g@c@]WQ[Wm@e@a@[a@]aAy@qAgAyAmAKKYW]Ys@k@i@e@oAcA_Aw@k@e@oAaAEE}@u@eAw@c@]{AkAs@k@]WUQgBuAs@i@]WWSGEQOMKOKCCYUIESQk@c@IIQMYUa@[e@_@w@m@]WQOUQUQSQQOGE[W[UWSKKWSUQOMWSOKOMi@c@CAUSSQUQMKYU_@[WSWSKIk@c@AA[YKIUOu@o@e@]MMYSQOQOSOKI]Yc@_@WSECWU]WIGEECAIIMKSOWSIGGGWSUSWQWUYUYSKKIGOMCCYUCASQ]WMKEEMKk@e@YSwAkAcBsAEEGGGEYUGGUOc@_@OKKKc@]sAgAOMc@[eGuEiDgCoB{AwBcBAAOKKKA?wBgBo@i@eByAyE_EcAy@eByAa@[c@_@OMQM_@[CAa@]OMOMQOQMOMQOOKOOQMa@]SMMMQMu@m@QOy@o@USGECCMIwAkAa@[GGk@e@QMQOQMs@k@QOu@k@sC}BeDiCgCsBs@k@s@k@c@]EEa@[a@[MKKKUOi@c@g@c@MIYUe@a@m@e@q@i@gCqB{@s@a@]QOQMaAw@WS_@[QOWQQOSO_@[WQQMSOQMIGEEAAe@a@QMMIEE_@Yu@o@}AmAu@m@UQYUGEIIEEUQOMSMa@]QMQOUS]WCCa@]QOGEECWUOMUQAAIG?AMIEECCA?EEQOMIUS]Wc@_@OMYUy@m@sAgAk@e@_Au@c@]_@[{@q@o@i@IGMKkAaAA?OMUQUS[U]YyAkAIISOy@o@]Y]YOKCCEEIGQOUQaAw@OKOM_@Ye@a@s@k@OMWS[UEEIG_@Yk@g@q@i@_@Y}@s@QO]Yc@][UCCSQKIMKWSQOOKa@]KGOMIIIGWS]YGGKGWUMKKG[WOMEEMKk@c@YSKIECqA_AYS[Sa@WKIQKQKKIWOmAq@UMSKQKOIo@]KEYOOIe@SAAOGSKi@WYKOGa@QECOGOGu@WECUIGCGCEAGCKEGCUIICWIe@OWIGCEA[Ie@OA?EAg@OGAEAsA]ICMCICKCOCUGSEMCs@Oe@Ky@MAAQCk@ISEe@IgAMYEg@GcAKiAKs@GA?s@EaBIEAUAK?w@COAm@AI?c@Ai@AU?w@AU?S?Q?iC@W?g@@}@@g@@gA@a@?w@@[?U@]?[@gA@cBBY?[@o@BK@C?Q@kAFU@YBa@BK@{@FK@k@FWBc@D}@JI@QBw@JMBSBe@HgAPa@F[F]Fc@Hc@HG@[HMBWDkATc@Ho@LODmB\\IBOBm@LWDmATWDE@WDm@J_BRq@Jc@DQBQBc@BI@K@c@DG@I@k@DU@C?QBM?QB_@@[BY@a@B[@c@@Q?S@o@@U?Y@kA@[?S?S?c@?U@M?a@?o@?K?S?g@@c@?O?M?K?eD@e@@}GBc@?_B@cC@sA?w@@E?oA?W?_@@kB@oA?e@@{A@yC@{@@oA?g@?[?oGBu@@u@?eD@c@?gA@mB@qD@u@@yA?a@@s@?M?kIDi@?eD@mA@A?O?a@?a@?o@@iC@{B@Q?aC@cA@A?iD@w@?wC@}@@Y?[?k@@a@?]?qB@O?o@@U?i@?eA?yA@kB@k@?e@@aE@s@@oA?{C@kB@_A@{ABa@?c@@M?{CDg@@E?qABe@@W?W?sBD_CDSAuAByCFU?m@@aA@g@@S@W?U@e@@mABQ?Q?O@sABK@aBFK?uDHy@@cCDaA@uCDQ?oABgABqHJeMTuJPcA@cCBY@u@@Q?m@@]?k@@I?{A?S?U@[?G?e@?k@@{@?m@@W?w@?W?s@?yB@e@@Y?k@?]?a@?I?{B@S?i@@W?]?c@?U@Y?O?m@?S?U?k@@A?SAgA@k@?_@?M?{A@K?m@?Y?G?{@B{@?a@?]?m@?K?O@M?C?mB@C?O?m@?U@_A?M?]?e@?G?k@@Y?_@?e@@[?eB?oA@[?c@?q@@C?e@?_A?C?i@@i@?_A?U?i@?[@s@?aA@C?g@?_@?o@@S?M?G?_A?k@@Y?A?i@?m@@A?g@?k@?_@?K?e@@G?y@?]?aA?i@@W?i@?Y?S@q@?m@@K?W?Y?Y?g@@m@?_C@U?k@?e@@_@?wA?yEBqA?cB@S?a@?G?yD@cA@E?}GBoA?_C@uA@{A?k@@M?W?O@gA?wA@w@?]?e@?wB@i@?oB@e@?U?aA@Y?sB@Y?cA@cA?cB@iA?{A@o@@gA?wA@e@?gA?}D@i@@eA?_@@_@?W?E?K?U?yA@cA@[?]?iA@u@?aA@E?m@?c@?c@@U?M?mB@k@@Y?U?G@K?Q?Q?a@@{A@o@@u@@G?S@Y?Q?G?I?I@O?c@?]?a@@mD@K?qCBk@?A?gB?U?{C@oC?]?u@?gD@E?O?c@?y@?eC@k@?{A?U?E?gD?_@?qA?{A@i@?S?i@?cC@A?}B@m@@Y?kB@kC?_A@G?o@?}A?O@q@?gE@gB@oB@a@?iC@wB@{A@aA?Q?o@?S?s@@wB@O?iA@iB?}JDQ?sA@g@?W?wA@yB@aB?U@uB@sB?W?]@_@?W?[?C?S@K?k@?K?q@@]?}@?k@@C?S?Q?o@?C?]@iA?G?w@@_@?m@?Y@]?cB@{GBA?yB@mA?oA@K?mA@gB@sA@m@?I?i@?a@@c@?[?a@?i@@S?U?Y?cA@O?_B@c@?A?a@?gCBA?_@?}B@_@?_@?c@@Q?Y?M?Y?w@@_B?g@@c@?c@@_@?c@?{@@_A?U?W?i@@_@?]?y@@C?]?I?W@G?a@?e@?c@?oCBc@?cA@g@?[?O?uB@_@?w@@e@?c@?iA@uB@]?}EBeLDo@@wC@w@@U?q@?}A@K?w@@w@?S@k@?o@?c@?c@@G?g@?o@@A?wE@m@@A?_C@U@O?S?gADQ?W@S@S@O?]Be@@a@Bk@Du@D[@qBNgBNG@s@FE?e@D_@DOBSBYBOBYDg@FK@OBWBUDSBG@UBu@JK@g@F]FYDQBe@F]DuAPo@HQBcFp@k@HgALeANg@FUDe@FWBMBWDc@FUB{C`@[DYBA?y@JSBWB[BK@qALQ@uALs@Dk@DQ@W@YBC?O@O@q@BU@Q@A?u@BK?s@Ba@@[@e@@G?w@@c@@yA@e@?[@O?{@?{B@K@m@?E?eA@gA@O?K?E?Q?K?S?S?Q@M?k@?[@cA?[@W?O?C?gA@Q?Q?U@Q?Q?Y?U?U@Q?A?kB@_@?k@?o@?[@Y?a@?W?_B@G?O@oFB{CBK?gA?aDBE?a@@iA?_A@c@?i@@e@?]?a@@q@?iCB]?o@@W?m@?o@@c@?i@@I?Q?kEB_C@wA@cCB}B@k@@}A@W?uA@y@?mCBmA@m@?_B?C?_@@c@@kC@iA@c@?{@@q@?wDB_@?eA?c@?i@?Y?i@?o@A}@AW?a@AwDIy@EkBI]Cm@CcAKgAGmBS]Ce@E_@EYEmAOo@I_D]yAO]EUESCQAMCQA_AKu@IKAA?aBUq@Iy@KyAQqAMw@Kq@IWCSEWCm@Ii@Ek@GMCQCc@EQAWAMCoAIsCSsBK[CkAC[AeBEC?q@Am@AO?m@?[AuA?wA?sA?G?a@?uD?c@?o@?W?c@?kB?_@?C?yF?c@?sN?cU?W?[?kA?yE?mD?yC?iD?iN?cF?q@?{@?w@?q@?iA?E@O?iE?yA?sB?s@?aB?mD?]?A?U?kK?cD?_@?iA?S?_A?{@?gA?[?[?{I?Q?mC?I?gA?Q?Q?Q?aB?Y?A?K?C?]?gE?aG?s@?a@?y@?O?E?M?I?eA?cB@M?iA?eB?_D?sCAcA?E?E?gMAwA?qAAoC@o@?kA@i@?]?k@?u@@e@?S?yA@{B@eB@{A@S?s@@k@?[?Y@aA?s@?c@@Y?c@?q@?kGBeB@y@?i@@_A?U?Q?]?o@@S?c@?_@?a@@W?oE@}@@oA?M?q@@m@?U?k@?aA@_A?wA@W?i@?a@?_@@g@?e@?_@?C?o@@u@?iB?aFBsA?wA@W?K?kA@S?W?Q?oA@_@?e@?mD@y@?yHFeD@G?cA?Y?cA@E?u@?K?cHBoE@}@@]?{C@c@?k@@A?_A?c@?gA@gB?qABuA@Y?cABs@@uABcABa@@[?aABi@@_@?mBBw@@cA?k@?k@@_B?a@?U?U?g@?U@C?k@?o@A{@?I?_CAiAAW?s@Ay@A[?S?U?k@?g@?O?[?y@AY@aA?q@?k@?U@a@?aC@m@?I?S?Y?I?c@@S?U?U?O?Y?m@?i@@k@?C?c@?G?Q?k@@U?k@?kB@aA?W?o@@gB?k@@Q?_A@eC?m@@i@?k@?aA@yA?[?O?u@@ePDeE@eC@iRFsD@mC@iA?g@@u@?mC@mA@s@?M?_@?g@?{A?wCBi@?u@?mA@u@?sD@]?cA@k@?_B@}@?}@?q@@u@?sB@mB@eA?yEBgB?cC@qB@oC@W?K?c@?c@?Y@sB?mA@kC?]@m@?iA?s@@M?{A?iD@C?gA@wG@sPF_C@gA?_IBa@?uEBsMDaG@i@@gA?s@@y@?g@?sD@c@?wGBoA?k@?i@@k@?o@?k@?Q?k@@k@?c@?}@@eC@}@?K@K?K?W?}@?U?k@?k@?qB@O?W@W?S?A?_B?{A@c@?aA?}DB{E@wA@qB?{@@eA@e@?Q?U?U?U?U?W?S@W?S?U?uA?m@@U?U?U?U?U?U@U?S?Y?S?U?k@@U?U?U?U?g@?C?S?W?U?k@@G?M?i@?W?S@U?U?U?M?G?U?U@U?U?U?U?W?Q?U?U@M?G?U?U?W?S?O?]?U?U@U?W?U?U?U?U@U?U?U?s@?}@@Q?U?[?O?U?U?U?U?U@U?U?U?U?U?U@U?U?U?S?U?U?S@K?K?W?U?W?U@m@?U?S?_@?y@?W@G?G?U?U?oD@g@?eA@_A?aB?w@@qB@uA@qA?gA@o@?e@?wA@Q?eC@E?u@?_B@S?y@?]?i@?W?k@@U?U?S?cA?aA@o@?O?W?U@W?U?U?U?k@?W@U?W?k@?gA@S?W?k@@U?U?U?S?W?aA@k@?cA?W@S?gA?U?K?K?i@@O?G?W?U?U?W?Q?uB@W?C?Q?Q@[?m@?S?gA@U?W?a@?K?U?m@?W@W?O?G?Q?eA?WAQ?c@Ac@?OAk@Aa@AIAK?M?E?e@AK?SCWAYASA_@CKASCs@Gi@Gi@E_@I[Ee@Gi@Gc@EOCUCICOCi@IIASEe@IYGm@Me@I_@IKCg@MYGUGOEYISEUI_@KYIc@M{@WUIu@Wo@Us@W_@O]MIEaAa@]OkAi@UM_@QOIsAs@OGQK}@g@MIe@YUMOK{@i@WO_@UQM{@g@gAs@[QKIc@WGEc@Wy@i@k@[e@[UOc@Wc@YOIcAo@a@W}@k@[QKGw@g@c@YgAs@c@WkBkAcAm@i@[e@[c@WQKUO_@UoAu@[S_Ak@c@WSMQIe@YWQq@a@QMSMUMSM_@UWOs@c@KIa@Ue@Y_@Us@c@a@WSOSK{@i@a@WKGWQEC{@g@[SWQaAo@SOYQm@c@ECaAq@WScBqAQMQOQMcAy@c@_@OMq@o@QMQOOOOOQOq@m@OOsBoBc@c@]]KICCQQ[[k@i@USOQQO_@]QQMMUUSSGGUS[Y_@a@q@o@oBkBOMa@_@OOCCKKq@o@o@o@a@_@IIIIo@m@KKCCCAACyBsBCCo@o@EEKKKImCkCIKa@_@a@_@a@a@MMq@m@a@a@_@_@q@o@QOOOUUKKKIUWECIIOOWUII_@_@uAoAe@e@y@w@cAaA_@]SSKKQOOOOOOOa@_@k@k@US_@_@sAoAOOOOQQ_@]OOQOSSKKOOQOOOOOa@_@OOOOQOOOOOOOQOOOOQa@]_@_@q@q@QMGGWWaAaAOOa@_@a@_@o@o@OOWW{@w@YWYYo@o@q@o@OOQOQOq@o@y@w@i@c@USeBuAcAw@UOc@[c@[c@[[Um@_@UOUMkAs@m@_@c@USKSKw@c@OGi@YUKSKUKOG}@a@u@[k@WUICAMGUIWKc@OQISGCAQGg@QUIYKMCSIUGSGOECASGSGUGUG}@WSGYGc@KUGQEUEUGSESEKCICo@MQCSESEUEQCWEUCAAOCIAMCk@ISCWESCUCWCQCUCQCYC[E]CKAe@EUAUCSCYAUCe@Ce@CK?k@CSCU?UASAWAUAU?SAU?WAQ?WAm@AuACWAa@?IAU?UAS?U?aACU?SA]AQ?U?UAS?WAU?SAU?QAY?eEImBCi@AUAk@AeEGUAU?k@Ao@Ac@AW?UAaACS?m@AE?O?e@AWAY?A?UAS?SAW?UAS?UAS?Y?g@Ai@AK?_@AEA]?K?i@AWAq@AM?A?UAk@AU?UAi@Ai@?YAU?UA_AA_BCOAcAA_ACk@AS?k@Ak@Ak@AwACmBEk@AW?g@AaAAwAEw@AkAAk@AUAk@Ai@AU?UAU?UAU?k@Aa@AI?k@Ak@Aa@AM?]AM?U?GAM?U?UAk@AI?a@AQAC?O?y@AK?UAU?UAe@AE?k@AU?k@AaACU?UA{@Ak@AK?uEIS?}@Co@AU?mBEk@AS?WAuACE?e@?k@Aw@AIAU?UAk@AI?KAS?WAs@AO?}@AUAU?UAU?WAC?e@AQ?]AQ?UAUAU?UAaAAY?QAaAA{@CY?wACaACU?UAo@AW?k@A]Ak@A_@A_BCwCEg@AMA{ACS?UA[?A?UASAwACk@AqAE{CIUAUAU?UAUAWAUAU?UAUAUAUAk@AUAc@A]Am@CUAcCGUAG?IAU?QASASAQ?SAQAS?u@CEAcBEeBGqBGS?gBGI?wDMeAC]AqCIqHUeBG]AO?o@C[Ak@Aq@C{@EaAC_ACgBG_ACE?i@COA{CI]AOAS?{@EuDKmBGaBEsDM_DImBGo@CeDKoACo@Cm@Ao@CUAUAUAUAk@A}AE{@EcCGUAUAUAUAU?UAk@CU?UAi@CUAa@AWAQ?w@Ck@CU?UASAUAU?UAUAU?UAWAS?WAU?UAU?UAU?k@CU?m@Ak@AU?UAU?UAU?U?UAW?UAS?A?UAU?UAU?U?UAU?UAU?UAU?M?G?UAU?W?UAU?UAU?UAU?k@AQ?YAU?UAU?UAW?U?UAU?k@AC?QAU?UAU?U?UAU?_AAKAY?]A_@?w@Cs@Aa@?s@AmBCUAI?I?W?UAI?e@AQ?E?e@AU?YAcAAS?c@AC?yAAWAeAC[?c@AgBC[?UAU?sACe@AC?_BCU?O?GAaAAUAU?qBCa@AA?uDESAS?U?uACm@Ak@AyACU?WAS?W?k@ASAU?QAE?i@?k@AUA_@AS?Y?WAc@AiAAoAAcACSA[?a@?IAeFGsEGQAiBCaAAm@Ao@Ai@AqBCM?U?UAU?UAU?k@AUAg@?k@Am@AaACS?k@Ag@AU?S?E?OAS?G?S?g@Ae@AC?A?O?E?sACmBCQAk@?UAU?SAU?aAAUAU?UAk@?UAS?WAg@AyAAO?o@AUAU?WAo@Ac@?QAM?K?wACU?UAU?UAW?wACk@Ac@?E?QAU?k@AO?E?UAU?KAC?u@AC?E?O?UAcCCE?UAO?E?O?EAU?O?E?EAK?C?Q?OA_@?OAE?O?]AK?U?IAK?S?_@AM?U?OAY?SAE?O?g@A]?KA_@?UAS?U?GAM?O?E?A?UAI?I?G?OAI?O?QAE?U?K?I?IAA?M?I?S?QAK?I?YAU?E?e@AS?A?_@AA?G?SAI?Q?QAO?G?SAA?U?]AK?W?GAc@?UAM?G?U?SAU?K?IAU?M?I?QAm@AK?G?WAU?C?O?QAE?S?E?QAC?O?UAU?UAQ?G?K?YAW?SAU?U?EAM?W?IAE?[?SA]?MAU?S?UAK?W?_@AG?M?SAW?OAE?wAAKAI?U?G?MAS?E?OAO?E?o@AO?[AW?c@AU?EAU?]?GAe@?WAY?SAK?_@?A?UAS?WAS?UAY?Q?C?UAS?WAS?o@ASAU?]?C?QAU?k@AUA_AA[?WAW?UAE?Q?m@AU?UAW?QAC?U?UAA?U?E?YAG?S?K?KAK?K?M?IAK?M?Q?UAU?]AU?C?_ACm@?E?OAU?WAW?O?o@AYAU?S?MAU?UAS?U?EAO?U?G?MAU?S?UAU?C?SAU?G?KAU?Q?k@Ag@Ak@A_AAaAAcAAkBEwAAaAAwACkBC_ACiAAy@AaAA_ACU?m@A}@AWAaAAaAAk@A[?OA_AAaAAa@AkAAaAC_AAkBCcAA_ACwAAUAk@A_AAaAAm@Ak@Ai@AU?k@A_AAwACk@AU?k@AsACo@Ai@?SAW?i@Am@A_AAwACW?k@A_ACk@?UAk@?k@AUAi@?m@Ai@AUAk@AU?U?k@AUAU?i@Ak@AU?k@?Q?{A?i@?m@?_A@aA@aABaABuAFS@W@]@yAH_AFWBa@BC?_@BA?QB_AHaAH_AJk@F_AJw@JeANu@JUDkAP_ANg@Je@Ho@LUDSDi@LWDk@LGBMBQDg@Jm@Ne@LSF]H[HYHi@NkA\\}@XkBj@c@NA?g@PyBt@C@SFoAb@[JoBp@UF}CdAKDUF_@NE@eBl@[HMFSFy@X}@Xq@Ta@N{JdDgDhAMDaAZ}Bv@}Bt@OFwBr@mDjASHeA\\g@PWHSFMF_@JA@eBj@_@LQFKD[Ji@Pg@Pe@Pk@P_@LGBWHqAb@E@_A\\a@LA@SFQFOFE@SFIDKBSHQDC@QFSFCBQDSFGBIBSHKDIBQFUFg@PUHQFUHGBMBQHWHODUHMDGBQFIBKDSFE@KDOFE@SFUHQFKBGDG@KDSFA?SHSFMDEBUFQHUFQFGBKDWHg@PSFSFUHUHOFUHSFA?QFSHODE@SHSFSHi@PQFQFWHSFGBKDSFUHIBIDSFE@OFSFC@OFSFUHSF}@ZQFSFMDGBUHMDC@SFSHSFA?SHSFQFi@PQFWHSHSFA?SHQFUHUHODWHKDGBSFQFC@UHQFIB]LKDw@VG@WJg@NGBKDi@PSHODC@UFQFC@MFIBIBWHSFSHSFMDE@SHWHE@KDQFC@QFSFC@QFe@NA@UHSFSFC@MDSHODGBQFSFSHMDG@SHGBIBUFSHA?SHKD[JC@MDUFQHKBGBUFMFC@YHQFYJODQFMDq@TQFSHSFGBKDSFKDIBSFOFC@UFQFUHSFSHE@ODIDIBSFKDIBQFUHQFUHMDE@UHQFSFIDIBSFUHIBIBUHSFSHSFQFUHA@QFODE@SHG@KDQFUHQFE@SFQHSFSHA?QFSFKDIBSHSFSHQFA?UHSFUHQFWHQFMDGBUHMDSHSFo@Tg@NYJc@N{@Xk@Re@P}@X}@Xg@Pi@P_Bh@{@XWHg@P{@XmC|@{@Zi@PSFE@wAf@iA^]J_A\\c@Ne@Nm@Rg@N}Ah@C@SFMFgA\\c@NUHSFSHE@e@NoAb@g@P{Bt@}@Ze@Nk@Re@N{@XsC`Aa@N}@Xi@P[Ju@VaA\\c@N{@Xi@PSHqDlAuAb@]LSFWHe@PaBj@g@Ng@Pe@PSFk@PKDQHSFSFSHi@RWJe@PODEBQFIDIBSHKDIBQHSHg@RWLg@Ta@Pk@Va@RSHMFEBSJQHSJQJSJQHQHk@Zy@b@e@VOJg@Xc@Vc@VC@_@VC@a@VC@gAr@c@Zm@^[Pk@^oAz@]R]TMJQJ_J~FoAv@wA~@_Al@{@j@q@b@]R}E`DqAz@cDzBQJOJIDIHSJOJSLQLOJMHSLQJSNc@Xc@XgAr@SJs@d@mBnAyA~@SNMJIDuA|@oChBe@XgAr@gAr@mBnASNoBnAyA~@yAbA{A`AmBnA{AbAyA~@}BzA_C|AiEpCm@`@cBfA{E~CgInFiIlFkBnA{@j@_@Ve@Xc@Zs@d@]TUL]T{@h@]VgAr@w@f@cAp@oCfBeBhAWPa@V{@j@qA|@o@^q@d@k@\\s@f@k@\\{@l@u@d@g@\\]V[Rc@Xm@`@i@\\i@\\_@Vm@`@a@V_An@YPkAv@a@VYPk@^q@b@YPe@Zq@b@qAz@u@d@e@\\kAr@eAt@k@\\o@b@qAx@w@h@aHpEw@h@iBlAiAr@mAv@kAx@}B|AcBjAyAhA}BjBkA`AYXoAdAgAdAiAhA_A~@}@`Aw@z@c@d@cAjA{BlC{BjCoElFWXm@t@cDzDcCtCoCdDkAtAs@x@s@|@aAfAwAbBgEbF_BnBm@r@aCrCeAlA{@dAo@t@kAvAkBxB{BlCqCdDkAtAu@z@wAdBoAzAyAbBmB|BgEbFiBvBy@`AkC~CyCnDoAzAkBzB{BjC}BlCyBjCc@h@i@n@yAdB{AhBoB|BwAbBsGzH}AhBcGfHiGpHm@r@g@l@[^[^sEpFkAvAm@r@UToCbD{CrD_EzESTSRMNSRm@n@eB`BsApAa@^OLq@l@yBdBgAx@m@`@YR[Te@ZUPkAr@c@XMFyC`B}DnBoAj@u@Xg@RoAf@}@ZcBj@}@VuA`@iAZ[HiB`@uAZuAVuAT{@NE@uARmBTuALoBPyAJsAHyAFwADmBByA@mB?uA?yA?M?_@?{AAcA?aCAo@?yC?o@?s@?g@?M?u@?i@?k@Ag@?s@?Q@S?k@?c@?_@?W?g@?M?Y?W?W@U?W?Q?U@Q?K?W@Y@q@@U?U@U?W@Q@U?W@E?M@Q@Y@i@@UBO@[@k@DI?I@U@WBS@E@_@BYBWBU@i@Fi@Dk@Fk@Fe@DUDYBq@JuBXm@HcANm@Jq@JeARm@Jw@PSD[FKBMBy@Rm@Lk@NWFG@KBC@QDQDSFe@LWHg@Lg@Ni@Pe@NcBh@g@PWH]Li@POFsAd@}Br@]L]JGBUH_@L_@LOFeA\\y@XgA^yAf@_Bj@mA`@YJqBt@mBr@}@ZUHSHUFSHSHSFSHUHSF[LWHOFQFQFWJODSHSHSFg@PSHSHSFSHUHQFSHc@NWHA@g@PUHa@Lg@Pm@TE@[Ji@RIBe@Ne@PWHe@NE@WJwC`Am@To@R[JYJ]L]LUHq@TWHQFC@k@R_@Le@NUH]Lk@RSFOFc@Na@Lc@Ng@PWHMDm@Rk@Re@Pi@PSFUHa@NSFWJSFSFSHUHQFUFSHSHUHQDSHSHSFUHQFSHSFUHSFSHQFSHUHSFSHUHQFUFSHSFSHSHSFSHSFSHSFSHUHSFSHWHe@PGBSFa@Ne@Ng@PSHi@P{@Zg@PSFOFg@PC@SFSH}@Xc@Pk@Re@NWHSHg@P{@XiBp@w@VoAb@{@Xg@Pw@Xm@Re@PWH[Lq@Tc@Nc@NyAf@k@Rk@RGBi@Pa@NGBg@Pg@P}@Z{@Xe@PSHKB_@NODYJSHiAb@YJ_@NYLSHSHSHSHQHSJSHSHMFQJUHQHSJSHQJSHe@VSJQHSJSJSJc@TSJQJSLYN]RQJQJSJQLQJQJSLQJQJQLQJSLQJSNOJc@XQLQLQJQLQLc@ZOLc@\\QLQLOLQLu@j@OL_@ZUPMLc@\\OLa@\\QP_@\\QNOLONONQP_@^QNOLQPMLa@^_@^QNOLONONONQNONONQNONONOLONa@^OL_@`@QLONONMJc@b@ONONQL{@x@OPURQNONONMLA?QPOLONQN_@\\QNONOLOLQPOLQNQNm@f@WT_@XSPMJGFKHMJQNMJSNEDKFONQLQLQLOLQLQLQLQLQLOLQLQLQLQLQLQLQJQLQLQLQLQJQLQL_@T[R{BrAyBrAcFzCA?KFWNIF[PQJQLQJQJSJc@Xe@VWP{@f@_@Ti@\\KFIDULEBSLi@\\s@`@[RaAj@eBdAs@`@_@TGDKF}@f@e@Za@Tk@\\oAt@m@^g@XYPMHYP}BtA{A|@QJIDC@}@j@GBIF_@TWPQJOJQLQJQLQJSNOHSNQLOJQJOLC@OJQLOJSLSNQLSLOJQJQLMFCBSLQJOJSLQJSLgAn@A@QJQJiAp@EBKFiAr@QJe@Vu@d@e@Xw@d@QJQJe@XKFEBe@XQJQJMHC@QJGDIFKDGDC@MHaCxAKDEDQHA@c@VOJC@OJe@XQJw@b@kC~A_Aj@iAp@QJQJgAp@ULQJQJQJa@Vi@ZKFEBe@XMHC@MHC@QJOJw@d@SJmBjAkAp@QJQLSJQLQJSJQJQL{D|BIFYNQJg@XUNQJiF|Cw@f@aB`Ao@^QJQJu@d@QJQJOJSJQJQJQLc@ViAn@QLSJa@VSLQJQJQJQJQJQJQJSLOHy@f@g@XCBGDSLuBpAQHSLOHA@SLMFQJWNEBKHMFCBSJOHA@QJSLQJMHE@GDIDKHk@ZQLSJQJ]RGDQJSLMHWLQLQJy@d@]TC@]Ts@`@]Ry@d@e@XQJGDgAn@KHGBmAt@IDQJSLQJQL}A|@}BtAy@d@_B`AYPuAx@uCdBKFGBa@VULQJe@XMHC@OJQJC@QLQJSJQLQJOHSLC@MHSLQJw@d@OJyAz@c@Vm@^QJA@c@V]REBA@QJULGDWPi@XOJmAt@MFA@WPULwBpAe@XSLC@KFMHWNOJA@SJA@EBKFQJe@XC@OHc@VMHYPw@b@QJMHMHKFQJOHC@MJKD?@OHMFQLQJSJQJSLQJc@Ve@XQJ?@m@\\GDULSLe@VOJQJA@A@MFMHC@UNQJQJSLQJc@Ve@XQJSLc@VSLQHSLQLOHSLIDA@KFMFSLQJQJQLIDKFOHQLQJULg@ZKDABKDGDQJKFEBe@XA@MHSLQJSJID]TIDEBSLQJQJQLSJGDSLa@T{@f@YRQJKDYRQJSJQJ?@QJSLc@Ve@XSJw@d@QLQJQJQJSJSLQJQLQJSJQLSJA@OJQJSJQLc@VSJSLOJWNMH[Po@^WN}@h@GDc@VQJQLOHSJWPOHGDaAj@WNe@Xo@`@QJQJSLMHULEBMHQJm@\\cBdAQJOHULSLQJQLA?QJQLQJ_@RYPYP]Rc@V?@QJm@\\]RQJQLSJQJQLSJQJSLQJSJQLQJQJSLQJQJQJSLQJQLSJSJQLQJQJSLQJQJQJSLSJOJSLQJSLSJOJQJSLQJe@XA@QHOJg@XSNOHkAp@OJSLQJSJQLQJSJQJQLSJc@XMFEBQJQLSJQJQJSLQJQLSJQJe@XQJSLQJQJSLQJSJQLQJe@XQJQJSLQJQJeAp@_@VYNs@b@m@\\KFe@Xg@XMHSLSLQJSJQLSJMJSJQJk@\\u@b@WNIFe@XC@MFc@XiAp@SLQJOHQJULOHGDKFSJy@b@g@XGBOHc@TA?A@KFSJSHSJg@TSJQHSJSHSHSHSJSHSHQHSHSHQHSHSHSHSHMDEBUHSFSHSHSHSHSHSFSHUHSHUHw@ZUHQHSFSHc@PUHQHSHUFSHSHSHSHSFSHSHSHSFSHg@RUHUHSHSHSHg@RSFs@XGBUHcC~@i@RYJ{@ZSHSHIBIDSHSHSFSHSHSHSHUHSFSHSHSHSHg@Pg@R]L]Ng@Pi@RcBn@g@RSFKF[Jg@RUFSHSHg@R[LKBIDSHSHSHKD[JSHy@Z_A\\w@Xw@ZA?SHSHg@ReBn@SHg@Rg@Pg@ROFC@qAd@SHQF}@\\A@q@V]LuAh@MDSHi@R_Bj@UJUHUHSHWJUHYJo@Vi@RmCbASHSHiE~AeBp@SHg@PyBx@e@RUHSHUHKDGBSHSHSFSHQFC@SHSHSHSFSHSHSHSHSHSHUFSHSHSHQFEBOFUHQFA@QFUHQHC@QFSHSHKBIDSHSFQHUHSHSFSHSHSHUHQHUHSHSFUJQFSHUHSHSHSFSHSHSHSHUHSHSFEBKDUHSHSHSFSHUHQHUHSHSHQFUHSHSFUHSHMDEBUFSHSFUHSFSFSFSHUFSFUFSFSFSFWHUFQDSFUFUFSDSFUFKBG@UFSDUFUDSFUDSDUFUDSDUDUDSDUDUDUDSDUDUDUDSDUBSDA?UDSDSBQDC?SDWDG@MBSDUBSDUDSDWDSBWDSDSDUDUBSDUDUDUDSBUDUDSDUDSDUBG@MBUDMBG@SDWDSBUDUDSDUDUBIBI@UDUDUBUDKBG@UDUDSDE?ODUBQDC?UDSDSBSDA?WFSBeAPYDmATsB\\oBZ}B`@m@HsEv@aANm@Jk@JqDl@w@Li@Ji@Hc@Hk@Jm@JOD_ANs@LMB{@Ns@LA?k@JsAT]F{@NE?KBa@Hk@Jm@Jm@Jk@Hi@Ji@JA?WDs@Li@H_@HmBZgARm@Jk@Jk@JI@K@_BXYDuAT{B`@[DWD_@F_@Hc@HSBg@H]FIBI@_ANuCf@aC`@mARYFu@LK@_@HYDOBSDmARG@_@HMB]FMBSDUDq@Li@Lc@H[HWFQD_@JUFQD]HaATKBo@Pi@P_@J{@Vg@Nc@Ni@Ne@Pi@PSHi@P}@Zg@RSHg@Rm@VKD_@NYLg@RUJc@REBOF]Ni@VWLUHQJUJOFQHgBx@YLQHQHSJUJUJQHSHm@X}@`@{@`@a@RYLmAj@YL_@P_@POFoAl@yAp@{BbAsDdBe@Tk@Vg@Tg@Tg@TSJSJSHg@Vy@^i@Te@Tg@TSJe@R{@`@g@Tg@TQJ[L{Ar@w@^g@Te@Ti@V{Ar@g@Ty@`@KD]Ne@Ti@Vg@TSHSJUJe@TUJSHe@TULg@Tg@Tg@TQHULSHSJSJYJMHg@Tg@TSJSHe@Te@Rg@TMFCBUJg@TUJg@TUJWL_@P[La@Rg@VMF_A`@k@XSHqAl@SJQHWLUJOFk@Xg@Tg@TUJg@Tg@Vi@Te@Ti@TSJg@V]NKDe@TUJSJSHSJg@Tg@Tg@Te@TULi@Te@Tg@Ti@Vi@VQHUJg@TSJa@PQHA@y@^UJQJQHUJQHSJSHSJSHSJEBMFSHQHSJSHSJOHUJC@QHQHSJSHQHSJSJSHQHSJSHQJUJQHQHUJQHSJSHSJUJQHC@QHQHUJSJSHSJSHUJQHIBKDSJSHSHMDGBSHSFSHSHC@QFSFUHUHSFUHSFUFSFUHWFUFUFUFUFSFUDUFUFSDSDUFSDWDSDA@c@Hm@JG@MBUDOBYDUDC@E@K@WDMBE@WDWDSDSBUDIBK@UDSDUB?@UBUDSDUDUDSBIBK@G@MBUDSDA?UDUDWDSBWFSBE@KBSBWDSDSDSBE@g@HWDQDUDWDUDUDM@E@YFQB[FUDG@OBQDYDUDUDUDUDSBSDC?UDUDSDWDSBSDC@UBUDSDC?QDWDUDUDUDWDQBUDUDC@QBUDSDG@C?MBUDSDUBUDUDWDSDWDG@OBUDUDUDUDUDOBC?SDUDOBE@SBODE?WDC@OBUDA?QDUDMBG@UDUBUDA@SBSDUDSDWDaANSDUBWDO@G@SBUDUBUBI@K@WBQBA?UBS@YBWBSBC?i@DWBU@U@WBU@W@W@O@U@Y@Q?K@M?Y@U?S@W?W@U?W?W@W?U?SAI?M?U?S?W?S?W?U?U?U?U?U?U?U?Y?U?U?W?U?A?S?U?U?U?S?A?U?W?m@?U?Y?}@AY?k@?q@?c@?u@?k@?o@?U?A?Q?W?U?U?W?Q?W?W?S?S?W?A?k@?U?U?UAW@IAM?U?W?U?Q?C?U?S?U?U?W?S?U?W?U?U?i@?W?G?M?U?S?a@?M?i@?U?A?U?U?WAW?I?K?U?W?S?Y?U?W?W?W?S?W?U?O?Y?K?I?U?U?[?O?I?M?G?M?W?Q?W?Q?U?U?S?S?W?SAW?S?W@OAC?S?aA?oB?W?C?Q?{@?o@?W?o@?uA?U?e@?q@Ak@?U?W?O?C?uB?cC?]?g@?u@?S?e@?g@?e@?i@@}@?Q?aA?U?Y?{@?k@?k@?W?S?U?k@AM?]?k@?U?k@?U?S?A?W?S?k@?U?W?U?U?S?k@?aA?i@?W?S?W?U?U?M?G?U?SAo@?U?k@?k@?i@?W?k@?I?a@?U?i@?k@?S?k@?i@?S?a@?G?SAk@?U?U?S?U?S?U?U?U?O?E?i@?S?S?W?S?U?Q?C?U?I?c@?i@?yA?sA?Y?o@?}@AU?i@?E?O?k@?S?k@?S?S?A?W?i@?i@?S?S?m@?U?g@?W?S?W?U?C?Q?W?U?U?U@m@?W@S@U?S@A?U@U@M?G@W@S@A?U@U@U@U@UBU@WBUBU@SBWBUBUBUBUBUBUBUBUDUBWDSBk@HSDUDUDUDUDUBGBKBUDUDUDSFUDSD[HQDSDIBKBUFSFSDSFWHSFUFUHSFWHQFUFSHSHA?SFUHIDIBSHUHQHUHSHSHk@REBKDUHQHUHSHMFG@SHSHSHSHSHSHUHSHSHSHSHUHSHSHQHSHQFC?SJYJSHUHUJSHUHWJUJA?QFUJWJSHUHUHUJSHOFE@SHi@RUJSHUHSHUJSFUJOFC@a@Nu@Zg@P_@NWJ]NUHUJUHSFSJUHUHSHUJQFYLUHUHUJSHUHSHUHSJWHUJSHUHUHSJSHUHSHUHSHSHKDE@k@TUJUHUHUJYJWJYL[JUJ[Lq@V[LWJWJYJWJ[LGBQFqAf@WJWJYLYJ[LSHSHUHSHQFWLe@PUHA@QHSHSHSFA@QHg@Pi@TSHUHg@RYJOFSFSHIDIBSHQFSHGDKBSHSHSHSHe@ROFk@Rg@Ra@NEBg@Pe@Ri@Rg@Rg@R[LMFi@Ri@Rg@RWJQFEBw@XSHUJSHSFg@Ti@Rm@To@VWJWJUHk@Tk@Tw@ZoDtA{@\\WJUHYLUHUJWHSHCBUHWHUJUJSFeAb@SHWHo@Vk@TWJSHWJg@RG@SHYLUHUJA?UHSHWJUJSHWHWJIDMDUJWJWJYJWJWJWJWJWJWHgAb@YLWJSHC@SHGBSFWJUJYJWJo@VYLUH[LWHo@XOD]No@VIBQFUJo@VWJE@QHWJUHA@WHGBMDUJQFOFQHSFgAb@QHQFQHSFSHOHUHg@RSF?@QFSHSFSHSHQHSFA@SHUHSHUJQFUHk@TYJUJUHYLKDIBWJWJo@VWJSHC@WJUHYLYJUJWHC@UJWJUHUJMDaFnBkAb@UJE@OFWJGBIBWJSHWJWJC@SHWJWJWJWJUHWJE@OHYJWJSHYJGBg@RC@MFg@PCBQFSHQFE@SJUHGBKDSHWJQFUHSHA@QFSHKDIBSFSHUHYJ"
                                    },
                                    "start_location": {
                                        "lat": 25.9348563,
                                        "lng": -80.2155609
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.5 mi",
                                        "value": 885
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 64
                                    },
                                    "end_location": {
                                        "lat": 27.4126653,
                                        "lng": -80.3986628
                                    },
                                    "html_instructions": "Take exit <b>152</b> toward <b>Ft Pierce</b><div style=\"font-size:0.9em\">Toll road</div>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "uogfDz{uiNQCc@HSDM@QDO@i@FiAHY@{@Au@CUA_@Eq@IaASk@MwAYu@Og@Iq@E[AE?Q?Y?Q?A?K@I@E@QJ{@J_BL}@JaBJWBi@B{@Fu@HICEAGAGCICGEIGECECGGGK"
                                    },
                                    "start_location": {
                                        "lat": 27.4049094,
                                        "lng": -80.3988579
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "367 ft",
                                        "value": 112
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 14
                                    },
                                    "end_location": {
                                        "lat": 27.4129125,
                                        "lng": -80.3975674
                                    },
                                    "html_instructions": "Merge onto <b>FL-70</b>",
                                    "maneuver": "merge",
                                    "polyline": {
                                        "points": "e`ifDrzuiNOsAE]YgB"
                                    },
                                    "start_location": {
                                        "lat": 27.4126653,
                                        "lng": -80.3986628
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.4 mi",
                                        "value": 572
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 57
                                    },
                                    "end_location": {
                                        "lat": 27.4146674,
                                        "lng": -80.3921191
                                    },
                                    "html_instructions": "Continue straight to stay on <b>FL-70</b><div style=\"font-size:0.9em\">Pass by Wendy's (on the right)</div>",
                                    "maneuver": "straight",
                                    "polyline": {
                                        "points": "uaifDxsuiNUkAY}Ag@yB]wAKe@S_AiA{EK_@SaA_BaH"
                                    },
                                    "start_location": {
                                        "lat": 27.4129125,
                                        "lng": -80.3975674
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "221 mi",
                                        "value": 355025
                                    },
                                    "duration": {
                                        "text": "3 hours 0 mins",
                                        "value": 10816
                                    },
                                    "end_location": {
                                        "lat": 30.3026826,
                                        "lng": -81.641262
                                    },
                                    "html_instructions": "Slight <b>right</b> to merge onto <b>I-95 N</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "ulifDvqtiNBQ@MAMG[WiAAIG[CIEQQy@EIOo@Ow@Ke@WeA_@aB_@cBs@_DAQCWAMAG?O@O@K@K@I@IDMDQHMFMFIFGHIJGJGJGBCFAFA@AHAFAHADAB?H?F@H?F@F@F?D@JDH@BBFBDB@?BBFDFDDFFHDJDHBF@FBF?B@D@F@L?J?@?H?J?HADCLCFCJEHCFEFCDEDCDEDEBEDC@C@EDGBGBCBC?CBYFOBE?]@U@[?[@U@A?]Pu@?SAoB?a@A}AAc@?c@?iA@_@@iABcCCwA?U?O?uA?eAAk@?{@?q@AK?Y?Q?}@?gB?_A?_@AI?m@?cA?yBBuB?U?aAAcA?m@?aA?i@?[?g@?{@?_D?k@?W?U?k@?M?I?Q?a@?kA?i@?i@?Y?a@?G?aD?S?Y@SAi@?i@@e@?g@@w@@gADY@i@Bi@Bi@DqALuALu@Ji@Hc@Fq@Lo@Lc@H{@PUFo@Nm@Na@LG@e@NSFUHUFc@NYJUHoA`@eA\\a@NgBj@SHi@Pi@Pg@PmA^uAd@k@Ri@PSFQFUHKBa@NKBC@i@Ps@Vq@R]Lc@NaF`BQFk@P}@Xk@R_@LA?YJi@PsAb@QFcBj@YJC@SFc@NUHQFw@VC@c@N{Ad@cBj@a@NE@i@Pg@PgA\\y@Xa@Ng@Ne@N]LA@_@LODo@Te@N_AZA?[LKDSHc@Rq@\\MFQJMFYPOJWPSJWRi@`@i@b@EBMLONOLEFON_@^KJMNKJCDQRIJi@r@QVKLADGFGJMTGJEFCFAD[j@Yj@A@Sd@Sd@O\\a@~@Uj@Sf@O\\i@nAc@fAg@fAGRa@~@Uh@Qb@OZ{@tBKVSf@mArCcB`E[r@Yt@KTm@xAyAjDUh@KTu@jBa@|@aA~Bi@rAWl@i@lAYn@Qb@?@O\\]x@KT_@|@c@dAGL]x@_@|@GPq@~A]v@uAdDm@xAYr@y@nBUj@Sb@Wn@KTa@~@KRc@bAYn@k@lAw@`Bk@lAc@|@Yl@S`@GLKP[n@g@`Ag@~@[l@m@jAq@nAEHc@t@Wd@Yf@a@r@q@lAqAvB?@OTi@|@qAtB{@tACFg@v@A@MR]f@s@`AEFe@n@GJWZGFe@l@e@j@Y^c@d@IHSVQR[^QPc@b@c@d@YVYXk@j@a@^_@\\]ZQNa@\\SPOJi@d@A?YTe@^_@Xe@\\QLi@^]Tq@d@w@f@UNq@`@g@Xo@^c@Tm@\\_Ad@gAh@]No@Z_@Pe@P_@PG@c@PgAb@{Ah@s@V[HC@m@RqA`@sAb@g@N}@X[JmCx@gA\\aAX{@XuBn@cAZa@LcBh@wAb@oA`@{Ad@qA`@qA^iCx@a@Lc@LgA\\eA\\u@TyBp@oA`@uA`@m@R_@LmA^c@Ni@NUHeAZeAZSHy@VsA`@}Ad@sAb@w@TWHiA^i@Nc@N_Cr@_AX_@LgA\\sA`@y@Vq@R?@iA\\q@RaBh@{Ad@wBp@mA^mA\\aA\\cBf@eBh@i@Pe@NeAZ_Bf@g@Nw@Vs@TMDSF_AX{@XuA`@SFmA`@kBj@YHsBn@]JgA\\{Br@qA`@k@PQFUFsAb@w@Xi@Ng@Pa@Ji@Pi@PODWHgBj@i@Pu@T[J{@VE@y@Vu@Vo@Pg@Pm@PG@]JSFSFi@Pg@NUFC@q@R]JE@a@Lk@PSF{@T]JUHIBoBl@[Jq@RMDQFgBj@WJa@Lm@TODaA\\e@R[Ju@XkAf@UHUJg@RYLMF_@No@Xa@RUJQHk@XC@kAj@SHIDsAr@]PaB|@y@d@WNSLs@`@]Rq@`@GDu@f@a@Vo@`@m@`@OJOLi@^c@XYRIFc@Zs@h@QL_Ar@c@\\qA~@c@Zg@`@UPy@p@ONMJC@a@\\IDGFQLQNSNIHEBQLOLQLQLOLQLA@OLQLQNQLA@MJQNQLQLA@a@ZOLSNOLQLA?OLQLOLSNCBKHgAz@OLQLOJABa@ZQLQLOLA@QLQLQNOLQLQLQLEDKHOLQLOJSNOLOLC@YTIFOLQLOJQNIFGFQLQLQLQNQLQNQLOLQLOLQNGDIFQLc@ZOLEDKHQLSNo@f@C@QNQLOLOLQNQLQLQLa@\\OJe@^QNOJQNQLQLQNOLQLQNOLGBIHQLQLu@j@a@Z?@QLQNQLQLOLC@MJQNQLQNGDIFQLQNOLQJQNQLQNQLQNUPIHSLOLQLQNQLQLONKHEBc@ZQNQLk@b@IFQNOLSLONQJOLA@QLQNOLQLOJOLQNSNQLQNOJQLQNQNQLOLu@j@SNOLQLQLOLQLOLQLA@a@Zc@\\QLOLQLA@OLu@j@s@h@QLONQLc@\\QLOLSNa@ZA@_@XQLQNQLQLOLQNQLQNQLQLOLQL?@QLQLQNQLOLSNOLQLQNMJC@QLQNOLQLQLQLONQLQLQLOLA@OLQLQLQLONSLONKFi@`@QNOLQLQLQNQLOLMJiAz@u@j@s@j@UP_@ZQLQLQLKHuAdAGF]X}@n@g@`@{AjAKJIFMHc@\\OLg@^c@\\a@Zc@\\WP[Vu@j@a@\\c@ZWRKHQLOLc@\\c@\\c@ZOLQNc@Zs@j@c@\\a@Zc@\\gAx@s@j@c@Za@\\c@Zc@\\OLc@\\QLQLa@\\c@Zc@\\c@\\a@Zc@\\WRm@d@c@\\c@Za@\\c@\\c@Zs@j@u@j@a@Zc@\\c@Za@\\c@ZQNc@\\c@Za@\\c@\\c@Za@\\c@Zc@\\a@ZWR]Va@\\c@\\c@ZOLc@\\c@\\a@Zc@\\c@Zc@\\c@\\a@Zc@\\c@\\c@\\a@Zc@Za@\\c@Zc@\\c@\\a@ZUPcAv@a@Zc@\\c@\\a@Zc@\\c@Zc@Zc@ZSLQJMHUNi@Z_@Te@VYNa@RIFQHYLWNSHe@Rk@Ve@RSHQHi@RA@{@^e@RMDWLg@Rg@Tg@R[LyCnAyD~AaIfDoCjAqDzAoDzAsGnCgBt@mBx@_Bp@gCfA_CbA{B~@oEjBkChAaGdC_DrA}D`BwB~@{CpA{IrDaBr@oAh@_Bp@{QzHiCdAUJy@^YN{@^iAd@w@\\oAh@[LSHSHoAh@oAh@g@Re@RYJa@LUJe@Rg@RUJ[LSJs@Z{@\\y@^UHSHqBz@y@^_A^SJUHc@Ri@TGB_Ab@YLSHy@^UJC@sB|@w@\\wB~@CBOFuB~@{@`@c@Pa@Pq@VSHSJSH]NSHu@\\]NOFu@Zu@Zc@POH]NmAf@[LUJKDs@XiAb@kAd@GBs@Xi@RSHQHA?i@RQFUHuAb@KBSHYFg@NIBc@JODi@LUFSDUFUD_@Hs@Lm@JUD[D]FYDg@FK@I@o@FQBE?}@Hg@DS@M@O@c@BC?U@[@{@BoA@E?q@@s@AQ?I?o@?wCAA?U?Q?o@?U?w@?[?U?WAS?m@?g@?m@?s@AqA?_A?k@?i@AcA?S?U?U?gCAS?S?k@?a@?[?sDAeAAuC?yAAaA@A?}@@G?a@@cABaAFU@_AFw@FI@SBa@BK@UBWD_@D_@Di@Ho@JUDc@H_@H_@Fa@J]HIBs@P}@TYHMBe@L_Cn@oA\\WF[H}@VQFSDUFcBd@mAZkBf@w@Tu@R{Bl@_@Jq@PWF{@TiBd@o@NyBj@A?qCr@UFODQDg@LsA\\i@N[FWH[Fe@LoA\\UHaAV{@TIBaAVm@NQDoA\\yFzAkI|BG@]JUFa@JYHe@Lq@RmAZWHw@RODi@NWHg@LG@{A`@eAXs@RC@{@Te@Ly@Tq@PYHa@J_Cn@]JsA\\KDKB}@T[HC@e@LWFMDsA^g@LKBIBoA\\UFSFWFQFc@JcAXqA\\A@}@T}@VWFk@NQFg@LUFKD]HSFi@No@Ri@NEBa@Jw@VUHg@Pq@Ts@V[LYJq@Vs@XUHQHk@Tc@RyAp@gAf@QHg@VWLKDQHWLUJmAl@{@`@QHcAb@MFw@ZCBc@Pq@Vg@Ry@Xe@P{@Z{@XGBWH}@Xm@RUFIB_AXa@J[H{@Tg@LaCj@oAXi@LUDg@JUFqAV_ARkB`@UDqAXcATg@J}Bf@cATyBd@C?ODWDSDSFUDSDWFYFe@JUDSDQDe@J}A\\kCj@sBb@mAVqAVkB`@}Cp@UDUDSFeB^G?KBKB[HG@QDiB^q@NsIhBu@NUFwDx@SDSDSDuCn@w@N}RfEmCj@{Bd@cB^cB^A?k@LqDv@mATi@Le@J]FaDp@wDx@mB`@}Bf@iDr@oBb@mFhA{@P_Dp@gDp@aBZs@L_@He@HaC`@cC^w@N{@Lk@Fy@LgANsOvBsAPe@F{@LgC\\_ALuARcALuAPUDi@H{ARe@FoAPw@Jc@H]D]DkFt@_@DaBTE?eANk@Jew@lKqc@bG_H~@}BZaBVaPvBmC\\c@DeALoFj@cBPgAJYBI?UBgAJM@_@Dg@FoBP[B_@DUBo@Fo@F[BQBq@Fo@Fi@DC@S@UDk@FWB}BTC?g@Dg@Fk@Fo@FM@[Dm@Dk@FE@o@Fo@Fm@FSBC?WBWBYBm@FM@I@YBWBaAJA@o@Fe@BI@iAJQBG@O@WBYBc@FO@YB]DaAHMBYB_@Bg@DWBUBWBWBUBU@I@M@S@UBm@DE@Q@UBW@k@BO@_@BW@W@U@c@@[@]@o@@o@@k@@Y@cA@o@@K?a@?k@?A?aA?cAAi@?m@Am@As@?_@AW?i@AiBEmGI_CC}CEaAAoBC}@Ce@?aACkBCE?I?]Ak@AS?UAQ?E?S?UAU?WAS?OAm@AW?SAU?WA[AKAeACk@AU?UA_ACWAi@Ac@Aa@CU?SA[AQAWAUAc@AQAK?YAWAUAUAUAU?WAUAUAg@Cs@AUA{@ES?GAO?WAwAE_BGoBGW?UAWAUAUAWAYA]AK?WAA?a@A_@AWAk@CUAUAW?m@CWAW?SAYASAWAi@AWASASAW?[AOASASAW?UAS?UAE?g@AcACo@C_ACU?WA}CIWAU?UAW?SAUAC?wAEaACq@AkBEo@C_DGaACWAqBEWAaACU?A?oDIa@AsAEg@Am@AUAk@AU?UAw@A}EMe@AgAC}AEeBG]AqACUAwEKI?o@CU?c@A}AEoAEuACeACs@C_BC_@AmDKY?G?eACgCG}AEC?[Ai@ASAm@Ao@AKAo@Au@Cq@AA?e@AsAEcDGg@AsAEuBEUAkACk@CY?uBKi@EUASASCWAGAOAg@EUCi@Ee@GUCKAy@KmDc@kAO_@Ek@Ig@G}@MqAOc@Gs@I]Ee@Gk@Ew@IM?WCa@A{@Ca@AYAK?[?I?a@?O@W@E?u@@e@Bi@B]BG?c@Dk@Fg@FWDi@Fg@JMBaAPaATg@LyBr@iAb@y@\\m@XwAt@c@Vc@Vq@d@{@p@i@`@a@\\e@b@iA`Aq@l@UPyBlBWXKJc@^cBxAeCzBsHxG}AtAcA|@{@t@mBdBqAhAy@r@ONwCjCu@n@u@p@CBYVmAfAyBlBe@`@IHGFURgDxCiA`Au@r@A?sAlAaCvBwBjByClCq@l@cA|@a@\\yDjDuBjBs@l@qDdDGFMLQLQNIFm@h@oAhAk@f@i@d@QNWTcA~@QLi@f@OLq@l@SPeCzBeB|AQNo@j@QPOLYVm@f@QPMJg@b@iAbAKJOLKJo@j@s@n@a@ZQP_@\\OLyBnByDhDyBpBSNs@n@g@b@a@^OL_@Zw@r@sAjAc@`@m@j@wBlBcA|@a@^[XmC~Ba@^aA|@GDu@n@{AtAwDfD_CrBaEpDg@d@KHyClCeDvCYVy@t@WTc@^kAdAsAjAa@^eFpEgPxN}BrBYVe@`@sAlAo@h@CBWROL]XSN[RYPSLe@XQJy@`@]PODOHq@Ve@PSFq@Ta@JA?aATw@Nc@HI@a@Di@HUBg@DY@i@DY@i@@U?C?Q@S?W?o@AU?uAAk@AS?wA?uJImCAaEEeDA_@?w@AuAAkEEU?oECmDCmECsDC}@A{LIm@?uAAm@@A?g@?]@gABs@DE?uBL_AFs@HqANm@HM@_@HWDuATaANsATiBZuCd@}@NwAT}@NyAVoARWDOBkARa@FQDE@kIrAmB\\gAPcAPa@F_ANsQvC{B^wAVwAT_C^s@LmBZaAP]DgBZiBXgCb@yAVsB\\s@JiOdCoATqARQBu@LsCd@aAN}@NYFOBuARuEv@iAP{@NaBV}@Nk@JsEv@{AVwATk@HyDn@kEt@{GfAuGfAYDkCb@a@HA?a@Fu@L_MrB{QzCQB}B^MBYDi@HcEr@yCf@{HpAiBXaC`@QBe@HiARaBVwAToShD_BVe@HUDqCd@qKdBYFcDh@]D}@PsItAgMtBsy@bNyATqDl@[DE@a@Hk@He@H_APiAPuB^mANi@JUBOD[D}@NUDsB\\k@Js@Jq@LeAPg@Hi@Hg@Hi@Jm@Ji@Hq@J_@HYDYDg@HUDSDo@JUDI@sATo@J}@P_ANm@Jy@LaAPu@Lg@Hu@LMBOBc@Fm@Ji@Jc@Fo@Lm@Jm@Hq@LI@u@LqAToARu@LUD[DUDm@Jy@NK@gBZq@Ju@LgARaAN_@F_@Fa@Hm@J{@LaAPaAPq@J_AN}@Ni@Ji@H_APWDSBo@Jk@JUDa@Hi@HOBE@WFmB^KBKBa@HC@kAZ_AX[JA?g@P}@ZaA\\]Ni@Tc@P[Nc@RULk@XWLe@Vs@`@SL_@Ti@\\YPq@b@i@Zw@f@g@Zu@f@q@`@YP_@Va@VUNQJA?[Ri@\\WPa@Ve@Zc@Vk@^k@^e@Xm@^_@TQLa@Va@Ve@ZYPe@XEBe@Zm@^[RWPw@f@wBrAi@\\oAx@o@`@QJWN_@Ve@Zy@f@a@VUNIFi@\\c@VCBm@^c@XQLSJIFSLKFQLQJKFq@d@MFWPUN]Rc@XOJo@`@[RoAv@]T]RWPoAv@m@`@_@TSLs@b@s@d@q@b@_@TC@_@Vs@b@a@Xc@Xk@\\aAn@QJe@Xu@f@gAp@WP_@Tk@\\s@b@SNSLYR{A~@a@VQJu@f@u@d@c@XYPUNi@\\_@Tw@f@[RQJOJcBfA{@h@YP_@Vi@\\QJy@h@MHq@b@QJ]RQNg@ZKHC@_@TEBIDo@b@k@\\[RIFgEjCy@h@{A`Ae@XgAr@aAl@u@f@]R]Ts@b@KFwBtAmKxGuD`CmAt@aAn@y@f@iAr@qBpAe@X?@QJqAx@wAz@s@d@iAt@_@TKFKFSL[R_@VaAl@cAn@_Al@]T]TA?oAx@g@ZIDOJiAr@mAv@KF{@j@]RGDKFaBdAa@VKFaBdAyBvAOHi@\\_BbAWP[Rw@f@KFE@c@Xa@V_@VQJwDbC}DdCCB}@j@cAn@[Re@Z}@j@cAn@m@^EBYRe@Vm@`@i@Zc@Xk@^uCfBs@d@iDvB_Al@gAt@k@\\yA|@{A`AULiFfDA@A?cF`DgAr@gAp@c@XGDa@V]T_@TA@o@`@yDbCIFq@b@qBnA}AbAGBg@ZYRKFSLULsA|@oAv@QJ]TsBpAYRk@^s@b@QJ[RGDk@^_An@]V]X[Vc@^QNk@j@c@b@i@l@EDGHQPCDQRKNa@h@KLU\\CDGHA@W`@SZGJS\\GJGJKRkBdDs@pAA@s@lAYj@ILKPe@v@[j@GL[h@wBxDc@v@KP}@~Ae@z@a@r@iBdDo@hAg@x@s@rAKP{@zACFm@bAWd@qFtJyBzDMT_AbBw@vAqA|BQZe@x@mAxBCDkAtBu@pA_@n@S`@k@bAgB|C?@MR[j@Yf@m@fAA@k@bAo@jAu@pAINYf@S\\S\\A@Ub@ABKPSZOXw@tAwCjF]j@e@|@Yd@gB`DS^KRmCxEc@x@a@r@GJKP]l@mAxBy@xAq@jAs@nA_@p@c@v@]l@k@`AMTa@t@MTGHMTMToBlDk@bAMTi@~@_BvC{D`HU^e@z@e@x@Wd@QZc@t@_EjHk@bAw@tAiApBk@dAGJU^MT_A~AMVYf@KNe@r@EHQXW^OP]`@a@f@KL]\\IHEFUTOL_@\\SPOJ]VWRYRc@Xo@`@k@XMFi@XEBMDQJYJYLUHe@PODC@o@PWFKD_@HMBKBMBe@Js@JUBa@FC?MBO@i@DK@M@Q@i@Bs@@I@U?y@@wEAE?u@?Q?[?mE?e@?Q?w@?cA?_B?A?cCAI?gA?wE?eA?iA?iA?iB?w@?eF?g@?G?w@?o@A{A@cB?wB?eAAk@?iD?qA?_@?sB?mC?aBAuB?}D?_B?[?A?kC?kB?qAAA?uF?kB?aA?q@?gA?}A?_A?c@?{B?I?gB?I?wB?sC?U?kA?{F?iFA}C?uF?e\\A{A?mF?iA?eA?eEAkE?wC?qC?aA?U?mA?W?I?K@K?]?eBAcC?Q?K?E?yA?S?_A?g@?E?aA?iC?iCA}A?uB?C?C?M?M?C?a@?oA?yA?_D?sC?eA?_A?e@?sA?gA?W?o@?c@?_B?mA?kAAmF?mC?c@?uB?{A?}B?oA?[?}@?a@?iA?I?Y?I?sDAkB?Q?Q?{@?wN?kK?_H?m@?g@?w@?o@?A?iE?c@?K?c@?oC?_AA_A?cB?o@?S?k@?cA?yA?q@?c@?c@?u@A[@Y?c@?iA?eB?mBAy@?k@?gA?gF?eC?_f@AmC?wA?sP?aFAwJ?iA?}A?aB?sB?sA?iB?u@?_A?K?c@?E?]?c@?aA?Q?Y?_A?i@?{A?C?iA?_@?U?]?IAg@?k@?S?a@?Q?i@?oA?Q?q@?I?_A?G?I?O?s@?s@?i@?u@?k@?q@?G?sA?c@?qA?gA?i@?sA?cA?M?gC?G?kA?C?y@?eBAS?W?}@?iC?a@@S?e@?O?o@@i@?oABiABQ@M@}@BS@aBH[@Q@i@D_@@YBs@Fy@FM@iAJC@a@DkAJWDUBkALG@wARI@e@HOBy@LcAPs@L_@FUFgBZMBm@LaARoATG@_AR[FWF]Fg@Hg@JaAPaB\\{Bb@uFdAUDuBb@a@Fs@NcLxBaF~@aARg@JiCf@kHtAoCh@_F`A{@NG@kI~AG@_BZc@H_AR_HpA_BZiDp@{Cj@aBZcEx@_Ev@qS|DUDe@Jc@HMBGB_@F]HmATy@N]HwAXe@HWF}@PiATqAVw@NqAVc@HyAXk@L{AX_@FeB\\mB^{Bb@eBZIBiB\\_@Hs@Nw@NsAVQBaDl@wAXeATo@LyAXg@JmATg@JqATqAV}AZi@Ji@Js@Nc@Hi@Ja@HMDeAPi@LM@_BZe@H}@P_BZcAR_Dl@QDwAVyAZ{@NiAR}@RC?aARUDw@NIB{@Pm@LmATmATo@Lo@Ly@N_APm@LqAVsE|@QBQDWDUFk@Jk@JUFUDUDUDWFUDi@JSDOB[FmATmATk@J}@RWDe@HUDi@J_ARUDSDk@LSDc@HoB^k@JwAXg@HODWDk@LSDi@JUDUDC@c@HUDUDsAVUDi@LUDSDUDSDUDUD_APSFUDSDUDSDUDSDUDUDSDUDUDSDUFSDUDUDSDUDSDUDi@JMBG@SDUFUDSDUDUDSDUDi@JUDi@JC@g@HSDSFSBWFSDUD_APSDMDG@UDiB\\UDSDSDk@JSDUFk@JSDSDUDUDSDUDSDUDUDSDUDUDSDk@LUD}@PSDWDSDm@Lg@JSDUDSDUDWD_F`A_BZk@JKBIBA?m@JsB`@qAVuAVk@LaDl@GB_APg@JqB^oATi@J]H[FMBI@KBQDgARq@Li@L}@PmB^e@Hq@NC?w@Na@Hu@N[FKBQBsB`@w@Nq@NaAP{AZg@HaAPk@Lu@Nu@NSDWD{@Pk@JUDi@L}@NWFSD{@PYDuAXgB\\KBs@LIBYFe@H_APUDUFUDYDYFSDWFu@NiB^cAT}@Py@P_@Hy@P]H_@HOFYHKBm@Pm@RWH[Ja@NODKFu@V_A`@YLULA?WLo@ZKDEBg@Vg@X}@f@q@b@_@Vi@\\WPu@h@k@b@_@X[XKFEFyApAIHo@n@k@j@u@x@{@`AIJy@dA_@f@c@l@QVc@n@INYb@W`@OTUb@a@r@KRMTgApBk@dAIPi@`AiBhDs@tAS^a@t@Yh@OXOXi@bAINi@`AKP]p@cCrEg@~@qChFk@fAi@bAw@xAGHaAjB]j@CFk@~@y@rA_AzACBU^A@U\\iA`Bm@z@y@fACBeC`D_@d@uA|Ay@~@g@h@u@x@k@l@o@n@sAnAe@d@i@d@KJ{BlBABmBzAgAz@m@d@GD_@Vq@f@w@h@e@ZIDkAv@_@TeCzAUNo@\\sDtB}@f@mAr@{@f@IDoAr@i@ZaB~@KHaCrAuAx@OH}DzB_DhBmDrBkBdAg@Xy@d@i@ZMF_@RaB~@_CvAo@^q@\\OJo@^wAx@oAr@y@d@u@b@{@d@w@d@iAp@iAn@y@d@{@f@w@b@qBjAy@d@iAn@YN]Tg@XiAn@y@f@}Az@MHMFaAj@y@f@kAp@sAt@MH]Ri@ZkAp@{@d@gAn@y@d@m@\\[Py@d@e@Xw@b@}@f@u@d@MF_@TMFc@V{@f@uAv@q@^_Aj@WNy@b@iAp@mAp@o@^EBWNaAj@oAr@cAl@sAv@kAn@y@f@{@d@{Az@w@d@cB`Ae@Xw@`@eAn@oAr@_B~@s@`@SLo@\\_CtA}Az@_B|@cCvAqBjA}A|@cCvAcCtAc@Tc@VmAr@mAr@uDvBuAv@iAn@_B~@kAp@kAp@a@TaB~@qBjA{Az@wAx@OHOHwAz@_Ah@qBhAk@\\o@\\]RUL_@RaE~B_@TsBjA]R_GfDoAr@e@XmAp@WNSLy@d@c@TgEbC_Aj@MFKFuAv@GD[R]R}@h@y@d@OJm@ZSJA@_CrAOHkBdA[Py@f@c@Va@V}@d@GD_@Ri@Za@TOJmC|AgAn@{@f@qC~Ai@XiAp@qAt@MHiAn@e@ViAn@g@Ze@V_B~@w@b@e@X{Az@QJ{@f@iAn@i@Zc@VgBbA]RMH{@f@s@`@}@f@}D|B[PyCdBkAp@YPoC|AMHC@i@ZoAr@qAt@qAt@QJiCxAMHw@b@a@Ti@Ze@XSJgAn@SJSLWNOHULu@b@_B|@mBhAcCtAe@Xc@V_@RgGnDQJk@Z}A|@yCdBmAr@QHKFyAz@oAt@aAh@kAp@KFyAz@gAn@c@V}@f@KF]RA?o@^k@\\a@TsBjAmBfAq@Zi@VoCjAC@gA`@eA\\sA`@u@RaG~AgD|@aCn@gW`HgJdCq@Pc@LaB`@wCv@w@RaDz@i@N_AViAZaHjBo@NQFUFUDc@HK@UDSDc@FK@k@FOBC?[DkAFm@BM@K?[?i@@i@?i@?aC@aA?a@?i@?O?mA?q@?kB?eB?_@?_A?[?A?_@@}@?o@AwA@aA?cA?[?iE?}D?c@?eE?wA?}B?uC@qB?kC?s@?y@@aG?qB?eB?Q?W?[?iC?S?mE?sD?m@?m@?U?S?S?S?G?e@@W?yA?U?m@?k@?k@?U?cA?U?m@?qB?qB?U?y@?a@?k@?aA?u@?c@@o@Aw@?qC@o@?qA?o@@i@?S?yA@eA@{A@u@@qDFs@@iLRm\\j@mJPsCDI?cDF]@_@@cEFU@sABE?{GLsCDcBBq@@]@}ABg@BmDD{ADeGFiCBU@Y?U?U?A?W@U?U?S?A?U?W?e@@q@?W?U?Y?W?U?e@AC?U?I?a@?A?UAU?U?U?Y?S?O?yEAe@?mBAw@?e@AcKCk@AeA?e@?eAAW?S?G?w@AW?S?W?U?a@?_@AS?W?S?U?U?UAW?U?U?U?U?UAS?W?k@?S?S?U?UAS?U?U?W?S?U?W?S?UAU?U?U?U?U?U?W?UAU?U?U?U?U?S?UAW?U?U?U?U?U?WAU?S?U?U?U?S?WAS?U?U?W?QAS?I?K?U?aA?_AAU?S?U?U?U?U?UAU?U?U?U?U?U?U?UAY?S?S?W?Y?Q?S?W?S?U?Y?S@U@U@W@C?O@Y@WBA?SBWBS@UDWBUBUDWBUDUDUBUDWFSDWDq@PIB[HGB[Ha@Js@V}@\\QHSHi@Te@VSHIDIFg@VQJSLg@ZA?OJQNQJYRKHSNOJu@j@gLrIqBzAaHfFsFbEe@^eChBkDhCsB|AuB|Ao@d@GFsHvFgAz@y@l@c@ZkAz@]VkEbDYTsBzAaE|CuAbAi@`@MJ{AfAiDfCe@^cAt@q@f@{C|B}AjAe@^k@`@_@VaCfBSNgDdCe@\\QLs@h@QNkBtAQLs@h@e@\\QLaBlAeBpAmBvA{AjAaCfBy@l@iAz@}AhAw@l@SNuEhDoEfDQLc@\\w@j@u@j@u@j@u@j@mBvAc@Z_CfBc@Zw@j@s@h@w@l@eAv@c@\\QLQLe@ZYRg@Za@TYLa@TUJe@RYJc@PMDKDUHOD[JUFA?MD[Fg@LYFUDQB[FQB[DSBQB[BUBY@UBQ@Y@S@[@S?S?Y@[?M?Y?SAQ?sA?k@?i@?Y?a@?W?aAAsA?Y?w@?mBA_A?o@?y@?q@?_A?o@AuA?k@?i@?aA?k@?_AAcB@ka@G_@?_A?aA?uCAU?Q?yA?iB?U?k@?aBAiD?mFAwXEmJAsEAiB?eF?i@A]?}A?o@?O?A?C?eIAS?k@?uAAc@?yB?oCAg@?sB?O?y@?sAAi@?{@?Q?q@?_EAk@?o@?gD?kFA}@?Y?q@?_B?W?cAAm@?uDA}@?c@?aC?k@AoD?yCAqA?c@?[?yA?oA?[?c@AyE?cEAu@?wGAyUEyIAyC?s@?_PCcA?q@?kGA_FA{F?aBAyB?{B?kBAyA?qA?Y?y@?aAAmA?g@?kCAY?a@?iB?uB?yBAmC?cJCiB?kE?iEAuC?k@?[?uAAcA?g@?uA?I?m@Ae@?U?Y?Q?}A?S?a@A[?w@?gA?uAAwD?[?e@?E?aA?aDAuDAI?mA?A?]?k@?_A?i@?cC?qCAA?cC?cAAO?mC?O?U?oA?qDAuA?Y?eBAaE?u@?y@AeA?g@?kE?]?U?gA?a@Ag@?{@?]?i@?k@?]?kAAcA?qB?qBAeA?u@?wA?m@@K?W@O?Q@sBLUBk@Fm@HgARm@Ls@Po@PcAZa@LSFi@PKDWHq@ReBf@eCv@_AXy@TYJwDjAq@RyAb@yAb@m@Rc@Lg@NuAb@y@VWHK@c@LG@kA^SH[Ho@RIBa@LiBj@w@TSH}Ad@k@PoA^q@Rm@Re@NeAZkBj@m@PuBp@q@Ro@RgBh@q@RsA`@IDuA`@wBp@k@PgAZg@P}Ad@}@X_AXyAb@wBp@k@Pi@PgAZs@TcDbAmF~Ac@N]Jy@VeBh@oA^_Cr@kA^]J]JwAd@qA^}Ad@_GhBsIjCyAb@WHy@Vc@LQD_Bh@[HiDdAiBj@}FfBwBn@mBl@mBl@sBp@mBl@sBn@iBj@cAZg@NMDSFC@aAZIBe@NmDfAMBu@TkBl@UHWFQHgAZgA\\a@LUFwExAa@La@LKDUFMDkBj@o@R]HQD]Jq@RIDSFg@NeCt@OHuC~@q@RoBl@}@Ti@P}@X}Af@w@Te@N}@Xs@Ty@ViBj@m@P}@VcA\\u@TuA`@WHWH_@LA?}C`AyAb@iCt@yAb@kCv@[JqA^_D`AsBn@a@No@Py@VUHcBf@cBh@kDdAg@NQD[JeCv@}DlAcBh@kA\\OF_@JwBp@aBf@mCx@KDs@R}Af@s@ReA\\gAZm@Rg@NmDfAaFzAy@X_FzAcAXyAd@oBl@wDjA}Br@qA`@gBh@}Ad@oA`@kA\\eA\\gBh@iCv@q@TqDfA{DlASFs@REBk@PgDbAi@PcAZwFdB}ExA{C~@{Af@]JYHy@Ve@NgA\\o@RiBj@YF?@}Ad@w@TUHkA\\ODSHMBsAb@wBn@WHg@NkBl@sBn@}Bp@}Br@aAZcAZwA`@o@TYHYHa@Jc@Jc@HE@o@JSBa@Fy@Hs@Fc@Be@BcA@w@@{@AQ?{@EyAIA?UCg@G]E}@Mi@KeCk@sAYc@Kg@KWG_@I_AS_AUqBc@oAYeAUWI}@QqBe@A?eCk@y@QkAYq@MyA]y@So@Oi@KUGSEa@KaB]mBc@qBc@gAUoAYm@MuA[s@QeAUu@Qm@M_AUmCk@g@Mw@QYG{@S}@SuBe@kAWu@Oa@Ic@Ig@GSCSCw@Im@E[A{@E_AAYAo@@O?U@]?c@Be@B]BUBG@e@Dk@Fg@HSBUDk@JaARQBg@JaAPk@JQDYDKBq@LuAVe@H}AZu@Lq@Lk@J}@PuAV_APuCj@QBy@Nc@HaBZaCd@{B`@eAPKBkB\\]Fg@JWFe@HWDuAVk@LA?SDuAVk@J{B`@wCj@SBoB^g@JUDc@H[FiB\\UDw@NyAVmB^]FMBi@JUDi@J_APaAP_APi@Ji@Ji@JOB]Hg@HUDUDi@J_APi@Jk@Ji@Jk@J}@Pk@JuAVg@J]HuEx@{@P{E|@cHpAi@Ja@Fs@NcHnAuDr@oB^A?o@LsAV_APUDE@yDr@_AP_APoDp@UD}@PuAVi@JUDMBG@UDSDUDSDWDgF`Ai@HwB`@{AXaDl@q@Lg@HC@g@JG@w@Ni@JwAVs@LgCd@gGjA[F_@FaAPwB`@gB\\kCd@QDe@HOBODSDo@JE@s@LSDSDi@Jk@Jc@HYFg@Hi@J{@PSBUDUDSDi@Jg@Jg@Jm@JOBQDiARwE|@kCf@aCb@{@NsAVy@NuHvAc@HiEv@}GnAiATu@LmCh@UB_Cb@wGnAa@HgB\\yB`@cF|@A@WDI@{AXwOvC_Cb@sB^[FG@w@N}@PqAVwBb@u@NSDSDUFSDSDa@HYFUD_@H]Fg@LUDQDa@HG@SDSD{@Rk@JSFSDSDWDUF}@P{A\\u@NyAZ_@HWDg@LUDSDUDg@Lk@JSDUFQBC@g@Jg@La@HYFa@Ha@HC@c@Ha@HIBSDa@J[FSDUDUFUDIB]Fi@Li@JSDUFa@Ha@Jc@HUFQDSDSDWDi@Lg@JUDSFUDUDSDSFUDUDWFo@LUDODa@Hg@JUFC?QDg@JWF[FKBw@Pq@LSDUFSDUDSDSFUDSDUDUFSDUDQDUFSDi@JUDi@LSDUDSFSDUDaARYFKBi@LSDi@Jg@JUFk@JSDSF{@PaARa@H]HC?c@Jk@LOBQDG@SDUFSDSDWFWD_@Hk@L_@Hi@JYF[HyAZa@HyAZk@LI@q@Na@Jm@JWFSDC@m@LC@WDi@LOBw@N_@He@Jk@Le@Je@Jg@JSD[FIB{@Pe@Ji@Jc@J{@PSDSDg@Je@JQDA@g@Jg@Jg@JQDUDi@Lg@Jg@JQDSDSDe@JOBUFSDQBSFi@Jy@Pg@Jg@Je@Ji@JQD{@Pe@Ji@LOBUFi@LiARI@UDg@Jk@HSDSBUDi@Hi@Hi@HUBi@Hi@HUBO@YDi@FS@WD}@H_AHWBS@i@Fi@DUBi@Dk@Fi@DUBU@i@FU@SBUBU@UBSBU@UBSBi@DUBi@DE@e@DUBS@i@FU@k@FUBS@k@FS@UBUBSBW@QBE@O@UBU@SBUBA?S@UBSBU@UBQBA?UBU@SBUBi@DUBUBU@SBA?SBU@SBUBU@SBUBUBi@DUBUBS@UBSBW@SBUBS@UBUBS@UBUBU@UBSBI@iAJg@DSBeBLoFf@qE^k@FyD\\}@HaAHA?k@FiAHkALk@DE?c@Dm@Fy@Hi@Do@DcAJuALaAHu@HM@m@DcBNgAJsALeBNw@F}@HeAJcAHM@UBoBPy@Hg@DcAJi@DK@w@HC?y@Li@HaAN{@Nm@JWF]HE@]Hu@Rc@Jy@TgAZaAXqA^}Ad@YH}@Ve@LWHe@Ng@Le@NYHODk@PWHw@TgAZo@P]J}@Vu@TQDQFm@PgAZYHSFUHOBe@Ni@NwBn@_AVaBd@aCr@mA\\iA\\mA\\mA\\w@V{Ab@kBf@q@Rg@NmCv@_AXuBl@kBh@cAZoA\\YJUF_Cp@oCv@u@T_AVeAZkA\\aAXaAXA?oA^_AXMDE?_AXyAb@{@V{@VsBj@iA\\eAZmA\\_AVQF_AXUFMDOD]JaAX_AVcBf@sA^s@TmA\\uA`@kBh@iA\\mA^mAZgCt@iAX}Bn@oBd@QDSDSFSDUFUDQDi@J}@RUDi@JSFUDSDSDUDSFUDSDSDUDUDSFi@Ji@Jg@Ji@LUDSFUDSDSDSDi@J}@Rk@Jg@Li@Ji@Ji@Jg@LUDi@JSDUFg@JUD}@Ri@JSDUFMBE@i@Ji@Ji@LSDUDSDSDUFUDQDUDUDi@LSDi@JSDUDg@Ji@Li@Ji@Ji@LSDUDSFUDSDi@Ji@Lg@Jk@Jg@JUFg@Ji@JUDSFSDUDUDSFUDSDSDSDUDSDUFg@JWDQDUDUFSDi@Jg@Ji@Li@Ji@Ji@Jg@Li@JSDk@Lg@J_ARi@Ji@LSDSDUDSDSDUDUFSDSDOB[FSFSDUDSDSDSDUFSDWDQDUDQDWFSDSDUDSFSDUDSDUFSDSDUDSFi@LUFQDUFSFSFUFSFSFg@NUFOFE@UHC@ODSFOFa@NqAb@eBn@i@PoIzCqUnIuHhCg@RSF_@N_@L_@Na@Na@NWHc@Nc@P_@L]Lg@PMDQH{@ZC@YJWH]Li@Ro@Tk@Rs@VWJ[J_@LEBYJ_@LC@YJa@Nk@Rg@Pg@Ro@TSH_@Lg@Pi@Rc@Nw@Xi@Rq@Ta@Nq@VSFMDSHQFa@N_@Le@P_@Ng@Rg@Pk@R]Lc@Na@Ng@RWHi@PqAd@QH_A\\MDwAf@e@P[Lm@RsCdAID_@LOFSFm@TIB_@Na@NWH[Lg@P_@LWJKDG@WJ_@Na@NMDu@XUHk@Re@POFWHYJGBOF]LUHODMFa@L?@e@Ne@PSF]LYJg@PUHSHWHA@MDQFWHKDWJQFUHqAb@k@RQHUHQFSFQFKDq@VYHMFg@Pa@Na@NQFMDUHUJMDSH[JIBUJIBOF_@L]LKDm@Rg@Rg@Pk@Rc@Ng@PQHSFGBEBWHYJUJMDQFMD]LQFOFa@Ng@PQHMD[Jg@RKBMFWHSHSFSHSHOFWHQFIDYJUHSFIDODEBMDUHKDWJ_@Lg@Pa@Ng@P]LYLa@LWJSHWHQFWJYJODUJMDi@P]NSFQFa@Ni@R_@N_@LGB]LODi@RWJIB[Le@PSHG@GBSHUHSHSJWJe@P]NWLUJSJKD[NOFWNUJIFIBWN[NMFYPe@VGDSJg@X_@Te@VGBEB_@Rg@ZIDSLg@X_@Rw@b@_@T]Pa@TQJUNUJWPa@ROJULiAn@QJGBA@SLWLMHEBQJSJULCBQJa@T[Nc@Vq@^a@Vu@`@YP_@R[PQHEDmAr@]Rc@Ve@Ze@Xg@XeAn@ULu@b@QJSLUJ[PQJ]Rc@Ts@^YNSLm@\\y@d@WLw@d@_Ah@_Ah@_Af@o@^SLULa@Ty@d@iAn@CB_B|@y@d@w@b@EBw@d@q@^oAr@EB{@f@oAr@ULQJu@b@y@b@]RsAt@ULKFWN_B~@[Pc@To@^EBWNWNSLWLGBUNa@Tg@X_Ah@kBdA]Re@VYPm@\\y@d@mAp@q@`@q@^iBdAi@Zc@T]ReCvAEBa@T]Po@^]R]Ra@Te@X_@RQJA?c@VmAp@c@VQJ{@f@eB`Ag@Xk@\\WNm@\\_@R_B|@q@`@ULIDWNYPC@GBkEdCA?eH~DmC|Ai@ZYNo@^{EnCw@b@gAn@e@Vw@b@w@b@e@X}A|@s@`@_B|@mBfAOHCBu@`@qAt@q@^i@ZULOJGB[PGDa@TKFo@^_@RQJe@VYPMH]R]PeAl@g@XoC|Ac@VeAl@WNe@Xc@TKHgBbAOHA@OHUL?@IDYNwAx@uAv@]PA@}@h@}@f@{CdB]RGDk@Z_B|@_Aj@OHSJq@^q@`@ULy@d@k@Zm@\\qAv@]PWNWNEBi@XQJgAn@[NQJgBbAw@d@}@f@u@`@s@b@w@b@y@b@EDeAj@gAn@_Ah@{BnAwC`BUNgAl@uAv@WNs@`@IF_@Ri@ZWNYPYNc@VUNqAr@{BpAA@QJWN}@f@q@`@YN_Aj@yA|@OFuAz@OH}@h@GDu@d@MHuAx@E@kAp@u@`@s@^aAh@}BnA_Af@IDq@^MH]RULuAv@wAz@QJ}@f@}D~Bo@\\c@TKFQJg@Vc@VC@k@Zy@b@KDaAd@eAf@m@Tg@TcA`@IBs@ViA`@k@PEBe@Lu@T_@JcAVw@RYF]Hu@P}@PA@e@HOBMBYFYDSBgBVYDk@F]DK@UBK@_@DaAJ[Bi@Bk@DS@g@Bi@Bg@B_ADY@m@Ba@@I?k@BU@Q@e@@]Ba@@mADU@}@DaADg@BM?O@M?W@k@Bc@BI?g@Bg@Bq@Bi@Bk@@k@Ba@Bq@Bc@@aDLk@Bo@B{AFK@Q@S?e@Bs@B[BcADcADG?K@g@@[Bk@BaADi@@c@BkADmBHU@i@BS@Q@cBHA?a@@i@Bi@BE?oAFm@BiADW@C?u@Di@BQ@e@@_@BQ@i@@a@BW@k@BK@sAFi@Ba@@m@DK@]@O@o@FWBYBq@HG@g@Fg@Fm@J}@N_@Fc@J[F[FGBg@JQFa@HIBYHg@Lk@Pe@Nm@RQHc@NaA^eA`@gAb@gA`@s@XiBr@A@A?_@NA?aA^a@PWJy@Zo@VaA^YJs@X{Aj@gAd@s@Xk@RUJmAd@i@ROHUHaA^A@oBt@gAb@]Nk@RiAd@i@TE@KD[LOFi@TwBx@g@RcA`@}@\\sAh@cA`@c@PC@c@Pk@Tg@Pi@TuChA{@\\q@XYJeAb@g@Ri@Ro@VUH{@\\C@w@XkAd@[LA@yAj@e@Pq@VWLC@q@VMDOFSHa@NOFk@Tc@PeA`@u@Ze@Pk@T_@No@VGB]LYLSHg@Pq@XYJu@Xu@XsAh@[J_A^a@NA?UJoBx@iAb@w@\\{Al@k@Tk@Te@PcA^MDsAf@UJm@T]LSHa@P_@NSHmAd@o@TA@k@TcA^u@ZeA`@g@R_@N_@N}B|@s@XgAb@[Lo@Vm@TYLwAj@yAl@aAb@IBgAd@YNu@Xe@Tm@Vm@XC@eDvAa@PIDa@NIDy@Zi@TaA^SHQFe@RsAh@C@kBt@}@\\KDe@Pa@NuAh@MDIDIBWJ_@Ni@RsAf@k@VQFA@g@Pu@Xm@VYJKDq@VSH_@Nq@Vs@XUHGD]JUJwBz@}@\\g@Rg@R_@RYNo@\\[P_@V_@TWPSL{@n@MLGDUR_@ZWVMLC@OPML]\\c@f@QTaAlAm@|@?@i@x@MTKPOVEHYj@g@|@o@pA{AtCcApB}@bBk@hAy@~AqAdCS`@cCzE_@r@KRYh@KRq@pAKTaAjBaDjG]r@yArCYj@_BzCm@lAe@|@k@hAq@pAcBbDKTKR[j@a@z@MRc@z@KTYh@oBvDKTILGNS\\Wh@Yh@Wf@]p@GJKRKTKRKRWd@S`@yBhEw@zAoBxDGNqBzDoAdCQ\\EHa@t@MXU`@c@x@a@r@Yd@[h@i@z@QVU^KN]d@{@lAe@l@e@n@MN_@b@]`@]`@MLST_@`@c@f@KJa@^QPUTIJy@v@URGFEDWRa@\\i@d@KHa@Za@\\u@j@UPOJMJo@`@m@^SLQJe@Xe@XSLQJQJSJQJQJSJw@`@[PMFUJiAh@eBx@kAj@ULQHg@TQHSJg@TSJg@TIDkB|@qAl@A@qB~@_Bv@}FpCy@^c@R_@P?@_@PID_Ab@]NC@q@\\QHiAj@SHSJe@TSJe@Tw@^y@^s@\\eAf@c@R[Nw@^qB`AeBx@oAl@IDSJ{Ar@w@^aDzA_ChA]PSHQHe@Tg@VSHmAl@kHjDgBx@cBx@wBbA_@R_F|Bc@TSJy@^g@Te@VQHSJg@TSJe@TSJSHSJEB_@PSHYN_@Pe@TSJQHi@VOFULKDYLSLSHe@TQHUJKFsAn@SJe@Tg@Te@TGB_@P_Ad@}@`@[P{@^q@\\o@Z_Bt@c@Tu@\\m@Xe@TSJMFaDzAmAj@g@Vg@Te@TQHUJ]PYNy@^g@Tm@VUJ]N{@Zg@Rg@Pi@R{@Vi@PSFUFy@Tk@Ps@PGBsA^k@Pe@Lw@VYJSHUHSFk@TUHSHg@RYNYLa@PuAp@_Af@QJ_@RMH]R]VQJYPCBQLSLa@XQLu@h@QN{@n@C@YRA@MHSNg@^}@n@SNSNi@\\YPg@XSLULULWLUJULUJSJWJUJWJUHWJSHo@To@RC@i@NWFUHWF_AT_@JUDm@Nu@Rs@Pm@L_@Ja@JYFUF_ATgBb@UFo@Nq@PeAVsCr@s@PSDA@g@Le@JWHsA\\SDgAXu@PqBf@WFo@NUFeBb@QDo@N{@TcB`@eBb@u@PiHdBQDg@LiBd@UD}A`@kCn@WHYFgAXk@LGBuA\\QDqAZe@L{@ReAVg@Lq@PiAX]HcBb@o@Ng@LyA^gAVu@R_AT{Bh@mBd@oAZ_B^}Bj@[HiBb@}@TqAZaDx@uA\\iBb@}A^ODODkCn@GB}D`A{[~HoEfA}@TaAT]Ha@Jm@N}Bl@sA\\}A\\g@LcAVcBb@sCr@UFUDi@NkBb@WHKB}A^]J]Hc@JE@G@ODSDYD[HYHE@mAZYFQDWFg@LUFSDoBf@g@Li@NODMDmAXe@LoBf@gAVmBd@]J}Ct@kAXsA\\a@JoAZsAZ{@Pu@PiAXUFUDUFgDz@_@Hs@PeAVo@P[H{A\\oBf@cBb@oCn@cAXq@NoHhB{Bj@wBh@eB`@uA\\cEbA{@R_B`@aAVoBd@}A^{@TuA\\wD~@sAZ_ATsBh@u@PUFiDx@aEbAaFnAaAT_Cj@MBMDYHMBa@J_ATk@NkAXcB`@a@JkBd@SDqAZmBd@kAXE@[HmAXmA^QDk@NUFSDQD[JWFIBe@LUDuA\\}A^A?oBf@kBb@c@LQDODu@RE@kAVgBb@iAXQDy@R{@TyBh@OD{@TA?A?E@aAVA?cAV_ATMDcATODk@NeAVkAXgDv@cCl@}Bj@A@qAZaATcB`@A@qAZeBb@e@Li@LoAZeAVkAXYHoBd@w@RcEbAo@Nc@L}@Ri@NUFUD{@Tk@LaAV{@RMBEBgDx@aATKBi@NcAVuAZm@Ny@Ru@PEBk@LkAXq@Pk@L[HQDcAVG@a@JcB\\iAVYFgATYFmATeAR_BZgB^g@JwAZ]Hs@NeB`@q@P}A^c@LiAX}A`@[Jm@P]HUHQDaAXWHuBn@[HQF]JiCr@a@JA@eAZcHjB}q@vPiP~D{DbAyD|@mCf@q@L}ARcBP}AL{AJyBF_@@qB@uRMgBAwAAk@?aAAk@Ai@?k@?k@A_AAcA?aAA_AAi@?aAAaAAaA?wAAuAAaAA_AAk@A_A?cAA_AAaA?_AAaAAaAAaA?k@AaA?_AA_AAaAAm@?}@AcAA_AAk@?i@Ak@?aAAm@?aAAg@?c@AI?Y?Q?aAAk@?i@AW?}@AcA?_AAaAAuAAaA?uAAaAA_AAo@?[?a@AA?}@?o@Aa@?G?k@Ak@?_AA_AAk@?aAAaAA_@?a@AA?c@?Y?m@AS?O?[Ak@?i@AaA?c@AK@C?G?W?aAAw@AU?M?sBAU?SAcA?KA_@?[?E?{@AA?u@AK?_A?A?A?MCS?YAO?a@?OAwBAS?aAA]BS?k@Aw@?S?I?YAg@?C?O?_AAE?eAA{AAoBA_AAY?y@Au@CoBA}@A]?k@A_AAcA?m@Ag@?O@O?Q?k@?SAm@?o@AA?i@?[?O?_@AU?S?QAW?i@?YAW?S?m@?_@?I?W@U?U@U?O@G?U@U@SB[@UBQ@UBWBUBSDQ@QBMBQBOBQBIB[F]FWFUDWFUFUFSFUFUHSFk@PSHSFUHE@OFk@Pk@Rm@Ru@Vi@Pi@Pg@Pg@Nk@Ri@Pi@PuAd@sAb@uAd@uAb@u@VKBGBo@Rg@Pi@Pg@P{@X}@X}@Z{@Xi@P{@X}@ZA?_@Lq@T}@XoA`@qAb@g@PWHYH_@Li@Pg@P{@X}@ZoAb@i@Pi@P}@X{@X}@Z{@Xi@PSFg@Pi@P}@Z{@X}@Z{@X_AXIB]L}@X{@ZeBh@sAb@oAb@qAb@k@Re@N{@X{@X_AZ{@XqAb@]Ls@T}@X{@X}@Zg@N}@Z}@Xy@XUHi@Pi@Pg@PSFcM`EsL|DmExAoA`@kA`@}@XuAd@uAd@mA`@uAb@kA`@iA^oA`@aAZ}@Z}@Z}@X_AZsAb@sAb@qAb@sAb@uAd@mBn@{Bt@}Af@{Af@y@XuAd@uAb@sC~@e@Pu@Ta@NIB]La@LQFKBo@TE@]LqAb@UFg@PUHUFi@Ri@Pi@PUHg@PUFGBa@Le@PC?u@VEBg@PE?C@OBk@PsAd@sAb@}@Zi@PSFKFEB[Je@Ni@PSHYJMBQHA?WHUHi@Pi@P[Jg@PUHc@L}@Z_AX}@Z_AZaAZ{@X}@Zi@Pi@Pk@Rg@NMDWHSF}Ab@IBSFODUHaBh@{@Z_@J_@LyBt@SFG@cBj@}@Z{@X]La@Lo@T{@Z_@Le@No@To@Tg@Ng@Pi@Ps@T]Ly@XsAb@m@RKBEBC?C@K@o@Tc@NC?e@PE@QFg@Pi@P]NG@iA^}@ZmAb@g@Ni@Ri@PMDMHIBi@Pw@XUHSFi@P}@ZcBj@}@Z_AZ{@XmA`@sAb@y@XUHyBt@eBj@qA`@y@X}@Z}@Xs@TqAb@oAb@sAb@cBj@eBj@oA`@}@Z_AZ{@X}@XcAZC?EB]JoBl@gBf@{C|@k@Po@P]JC?_Bb@c@LOD[J{@TcAXy@Tm@PGBu@Ra@LgAZkAZC?SFMDSFsCv@oA\\kAZiAZA@eD|@G@cD|@o@PuA`@_EfAyBn@iAZiAZ}@VeD|@_AVwLfDcD|@qCv@uA`@kOdEcBd@e@LqDbAeCp@WHcAXgL`DiBf@UHa@JwEpAuCx@_FrAkLbDeCp@cD~@_FrAyQbFgL`DaEhA{ErAyA`@k@PaAT{DhAyQbFm@Pe@L[JoCt@a@LIBoElAy@TqBj@gAZk@Nu@Rq@RqCt@YHwBl@IB_@JqEnAUFIBaHlBaFtAMDYHgBd@MFC?SFq@RwA^_AXeAXmD`AmA\\aBd@_@J_@Ja@J_@Lk@Ni@NUFa@LaBd@aBb@{Cz@}Cz@IBc@LuBj@]HMDa@LMBuDdAe@Lm@PuA^QDgD~@KBoCv@mA\\o@PIBcAXe@L]Ju@Ru@TcBd@wA`@KBa@LA@ODo@Ng@N]Jc@Ja@JaAXcAXWHiBf@_AVKBwA`@{Bl@sA^qA^gBf@WFOF_Bb@o@PUHi@NeD|@iAZs@RQDUHWF}@Vy@Ta@LKBa@LiBf@_Dz@eD~@gAZe@L]JgBf@eBd@wA`@}Bn@sBj@IBWFSFOD_Cp@i@N[H}HxB{@V}@TUHMB]JODSFsCv@eAZ[Hk@NE@_@Lg@LUFODs@Rw@TKBc@L[JE@_AVYHQFgBd@w@TqBj@qA^uA^]JIBQDEBKBIBODkAZsA^{@VWHUFSDUHYHKBUFWHSDSFSFSFSF_AVSFSFUFi@NSDSFWHe@LSFg@LA@qA\\UFSFSFIBG@WHQDUFSFODYHIBa@LSDUHSDSFYHa@J_@LMBa@LE@SFKBKBQFQDk@NSHUDQFUFWHg@LMD[HSFUFSFUFUHQDSFSFYFOFSDUFSFUFe@N[HG@YHUHUFSDWHSFSFgBf@QDk@NSFUFSFA@IBm@NUHg@LWHQFm@RGBKBGBKDSFSHQFUJg@RUHe@RSJe@Ra@RSJ[NQJa@R[Na@TOJOHk@Ze@VQLc@Tg@X?@_@RWLSLc@Ve@Xg@Xe@VSLw@b@e@VQLc@Tg@Xy@f@s@^QJGDULWNgBbAeBbAcAj@_Ah@{@f@}@f@cB`AgBbA]Ri@ZaFpCsAv@s@`@EBoDrBIDSJQLSJUN{@f@KDQL]NgBdASLg@VSNOFUNULYNm@\\SLe@XiAn@g@XOHe@VULMHKFm@Z}@h@a@Ta@TYPe@VKHeFtCQJYN_Ah@oBfAQJi@Zc@VsAt@g@Z{GxDMHKF]Pe@XYNo@^iDnBiBdAYNKFg@X]PQLEB_@Ri@ZUL}BrAaCrAu@b@y@d@]RMHMHULQJULSJ_@Te@Xq@^gCvAo@^WNw@b@kDpBoAr@u@b@ULQJk@\\eB`AwCbBSJYPQHMJOFKFQJSLKFIDA@SJMHg@ZQHwBlAQLWLIFSJOHQJQJw@b@c@XGDKDGBq@`@QJIFg@XULo@^GBIDEBSLSJc@VSLQJSJy@f@SJ[PWN_@TUL_@ROJUL_@Rg@XQLg@VSLa@Tc@Vq@^_@RSLYPm@ZiAp@YPe@VQJQJQJQJQHCBOHQJQJQJA?u@b@c@Vw@b@QJOJe@Vc@VQJSJQJQJQJQJw@b@QJQJOJA?OHe@XQJMFEBQJQJQJQJIFGBQJQJQHSLQJQJQJSJQJQJQJQJw@b@QJQJQJiAn@QJQJiBdAC@QLw@b@QJc@TQLQH?@SJOHSLc@Va@TQJkAp@e@VQJQJSLSJ_@Ta@Ty@d@SJQJQJc@VSLa@TQH_@Re@Xc@VSJUNKFQJSJQJQJSLQJOHOHCBQHSJQJu@b@u@b@SJQLULMFIDqC~A]ROHOH?@SJc@VGBKFSL]RMFeAn@u@`@u@`@_B|@qAn@A@{BhAiAh@MHg@TYLUJu@\\eBv@g@Tk@TQHWLs@ZmBz@GBsJhESHq@ZSHoD~AcBt@oAj@g@TuCnAOHQHc@RiAf@o@XwIzDu@\\oAj@UJSHsB|@A@_@Nw@^IBC@KFi@TWJq@ZUJYLMFUJSHQJSHSHwB`AIDWJIDID[Lm@XMD_Ab@QHSHSHu@\\WLKDGBUJUJ{@^OFQHi@VUJ[N[LmAh@UJUJe@TOFaAb@IDIBSJQFSJUJQHUJSHSHULe@RUJ_@PWJSJWJOFSJYL]NWLIDgAd@s@ZkAh@A?_@PIB]PSHSJSHg@Tg@TSHWLOFQHSHc@RaAb@y@^e@RUJYLQHOH_DtAiAf@aAb@SHg@TWLa@PQHSJSHSHUJSHSJQHWJQHg@TaBt@YLOFSJQHIB]Pi@R{@`@QH{@^wB`AKDGBiCjAUHSJSHSJSHSJ}@`@q@XE@ULSHSJSHg@TSHg@TSJq@ZG@QJk@TSJg@TOFWJkCjACBw@\\y@^UHe@RQJSHUJQHi@TcAd@A?IDIBIDSJGBIBSJUJg@TMDEBSJOFWJSJSHSJSHSJSHyB`AWLKDSJYLMDWLOFIDIDUJSH[NuAl@YL[NSHc@RA?c@RSHUJQHQH]Nu@\\SHSJUHCBMDOHMDIDYN]Lm@XOFQHIDa@PQHWLQFy@^SJQHi@Ty@^MF[LSHSJSHQH_@PGBID]NYLa@Ro@V_@RWJQHQHA?c@RUJSHUJy@^i@TIDWLqAj@i@Tq@Z[LC@iAh@C@_@N[NE@s@\\SHUJi@Vc@PkAh@c@RmD|AuB~@{@`@g@T{@^i@TmAj@qAj@{@^uB~@}@`@o@XIDuCpAq@XUJQHUJe@T[LQHa@PSJGBIDULUJWLC@YNMFSJWLGDs@`@QJIFIDMHc@Xe@XQLCB[RWRYR[TCBKHQLMJUPa@^MJSPYVKHWVSRMJCD]\\[\\WX]\\WZONORQRUZ]b@ORk@t@W`@GJSZi@x@KNKPe@v@CFS^QZKRa@x@c@x@CFqAlCe@bAoAlCSd@OXWj@O\\gAzBABQ\\mAhCq@xACFSb@c@|@m@rA]r@[r@Ud@Wj@CBSb@?@S^ABKVQ\\IPMVCDO^QZGNIPYl@yA|CKRKT[p@GNQ\\EJOZYl@MVSb@MVEJO\\]t@_@t@[p@y@dBIPKTSb@Ud@GLMXUd@Wh@KVABOXS`@MX]v@Sb@OZOZKTQ^S`@Q^Q\\?@KROZIRMVQ\\Qb@c@z@Q`@OZ[n@MXSd@CBS`@MZSb@]p@Sb@[p@Wh@Ud@m@tAQ\\o@pA]v@GLINKTWh@MV]v@Yj@Uf@IRMVMTKTKTUf@Wf@?BKRUd@Wj@Wh@KTWh@Q^CFWh@MVWh@IRMVIPKR[p@[r@a@x@O\\Wh@Wh@]v@QZSd@m@nAABIPMVWj@Q\\Q`@Ub@GN]p@o@tA_@x@e@~@Yh@KRe@z@ABWb@MTKPMRWd@MROR_@n@KN[d@Yb@IJCDMPMP[`@MROPOROPY\\_@d@QRY\\GFk@n@MNUTi@l@_@^MLw@t@SR]ZMJ]Zc@^]ZWREDUP[Ta@ZKHIH_@VSNSNUNSLYRQLUNMHSLULOJ_@TWNQJSJQHWNOH[PMFSJa@RULQHC@UJSJi@TKD[N]NSHe@PC@OFWJi@Py@X[L_@LQD]L_@JUHUFSFSFe@NODMBOFSF}@VeBh@UFQD]Je@NUFe@NWHg@LUHe@LUHOD_AXgKzCeAZoA^kA^g@Ne@Lk@Py@VwA`@qA`@UF}@Xi@N}@XQDQF{@Vo@R{@Vi@NiBh@{EvAiBh@{@Xg@NaAXy@VqA^g@N{@Vk@Nc@Nm@Pi@Ng@N}@XQDOD_@Lw@T_@J_@Ls@Rm@Re@Lk@PSFe@LwAb@aAXUHy@Tg@NgBh@cD`AMD{Ad@cElAc@L_@Lg@Nc@Lk@P{Ab@[H[JgBh@iBh@u@TcAXA@}Ad@_OlEG@gEpAc@JuGnBYHSFkA\\}@X_AVi@P}@VYJMDa@LyAb@[HOF{Ab@}DjAg@NsK`D]Lc@LODoErAsF`B}Ab@oJtCeD`AmBj@}M~DcCr@_@Ls@Rq@R[H]Jg@NKDMBw@Ve@LIBcLhDqCx@o@Ra@LG@sBl@eDbAkA\\eI`Cw@Tg@NSFWFa@NWH{@ViA\\SFm@P}@VgCv@aCr@YHMD}@V_AVe@NGBMBa@LmA^k@No@Rc@LaAZgCt@gA\\g@NqIfCa@LoA^g@NQDa@Ly@VmA\\{Ad@eFzAUHqErAaFxAQF}Bp@gGhBQFcFzAuBl@{H~BsCz@oZ~I}@XeD`A_ZxI]JqErA{DjAaAXMDkA\\qOrEaD`A}@VMDuP`FoErAaElA_GdB{FdBSFMDSDe@NeBh@a@J]La@LqA\\mA^gDdAaWrHeAZ_D~@iAZsTvGWH{@Tm[jJmErAQDeBh@yBp@[JQFKBQDWHIBGBUHSDSHWHe@LUHWHOFi@Pg@Pg@PSHUHaA\\MFc@NA@YJk@Ra@NEB]LaA^UJsDvAq@X_@NQFUHe@Ri@RmAf@qAf@i@R{@\\UHw@\\YJOFSH[LiAb@GB[LsAh@m@Tc@P{B|@ODYLoBt@m@Vk@TcBp@QFa@Na@NgAb@q@XuAh@WJy@Ze@PMDUJOFkCdAC@c@Ng@TuAd@}EnBeE`Bq@XkAd@IBw@ZaBp@A?_@NcC~@cC`AsBx@a@NgFpBeAb@KBC@EBUHKD]NC@[LODg@To@Va@N_@Nk@RoAf@i@RQHq@Vc@PaC~@_A^y@ZyBz@s@XoHvC_C~@QFaBp@e@RuAf@c@Rk@RoAf@MFs@VkCdAgBp@QHSHe@PYJiAd@o@Vy@ZqHvCc@P]LSHQFUJA?SHcBp@A?SHSHUJSFSJQFWJu@XiBr@cA`@MFQFKDC@OFMFOFUH{@\\g@Ri@Te@PWJ[LQFMF_@NWJMDOFGBi@RQFk@RQHi@P[JKD_@Le@NKDc@Lq@RUFUHSFcAXa@JYHSDSFg@LWFq@Nk@LSFe@HWFc@JgARKBaB\\ODm@LUDi@JC@QDUDUDSFK@IBUDi@Jk@LSDWDWFg@Ji@Lk@Jk@Lg@Jm@LSDi@JUFi@Jk@Li@Jk@Li@JYFm@Lw@NaARsAXi@LUDE@e@J}@PaARiB^k@Ji@LUDi@JYFg@J_ARWDk@Lg@Jk@L}@Pa@H]HiDr@aARi@JuCl@y@P[FUDk@L}@R_APk@Li@JWFQDk@JwAZo@LMBuAXSDk@LiATs@LaARk@Li@Ji@Lm@Li@JUDi@LsAXkATuBb@k@L_AP_ARUDw@P]F_ARwAZQDk@Ji@LkAT}A\\uAXUDuAX}@PuAXWFMB]Hi@JSDMBcATkATa@Ji@Jm@L}Bd@g@J_AR_BZc@Jk@J}@Pk@JC@iB\\g@Jk@Lk@JSDQDeATe@HYFSDWFSDSDi@LUDk@LQBSFQBq@Na@HOBe@JqAXkB`@G@mAVi@JA?i@LgB\\ODI@sBb@QBa@JmFfASDUD[FMBUF[Fc@JUD}@PG@k@LeB\\g@Lg@JE@i@JSDk@L]F]HQDOBMBa@HE@A@[FE@G@i@J{AZsDv@gFdAmHxAsDt@_ARk@Lm@LiB^_Cd@YFa@Hg@J]HsAV_ARa@HKBgB^e@JKBaB\\A?_ARKBmATqAXMBwAXwCn@aAPE@mCj@QDUDoB`@}Bd@QDgATUDQDWDg@JoB`@wBb@A@]Hm@L_@FE@oDt@KBs@NMB}@PWFy@P}@P}@Ro@Jk@L]HuAXKBA?a@Hu@Nq@NGBeATKBMBIBQD_@Ji@N]JWHa@LA?KBq@VWHOF{@Za@PKFUJi@TYLKFWJGDKFULk@XKF]RYN]TIDe@XYRo@b@EB[TGDWRKFMJQLA@IFWTMJMJSPi@d@e@b@KHo@j@IFGFOLiAdAQLa@`@GDUTWR_@\\[ZA?w@r@a@^WR[ZIFq@l@a@^KHED[XOLu@p@OLc@`@ONKHA@URo@j@GFi@d@QNIHMJQPIFYVm@h@k@h@i@d@a@^c@^QNs@n@ONURo@j@cA|@c@`@_@\\ED[VIHGDONEBUTEBw@r@y@t@_@ZIHQPm@h@a@\\i@f@QNe@`@]Z[Xi@d@A@QPMJm@h@]ZaAz@{@t@}AvAMLi@d@]ZURYVc@`@a@\\yApAe@b@YVIFq@l@k@h@gA`AUTo@h@CBcA|@ONA?o@l@wAnAe@b@KHs@n@k@f@k@f@eA`AaAz@CBsAlAc@^a@^IH[XqAjAOLA@q@l@OLs@n@C@q@n@a@\\QPSPKJ[XIFa@^KHm@h@MLkB`Bm@h@ONcBzAA@mBbBMLOLABoAfAURKHSR_@\\SPQNQPk@f@YVKH_Ax@_@\\IJy@r@g@d@i@b@a@^IFGHa@\\]XQPEDSPSNQNIFSPQLOLOLUP_@XKHgAx@YRe@\\c@XABm@`@YR]T[PSLQLa@VWPu@b@YPGBy@f@MFk@\\_@Pk@Zk@ZUJSJkAl@y@b@A?a@R{BjASJkAl@u@^sAp@SJiAl@gB|@gCpAQH}@d@oAn@sBdAqBdAWLgB|@wAt@CBeCnA_@RGBmAn@e@Tk@XqBdAmAl@sAr@OHmAl@w@`@CBe@Tg@VkAl@g@VoAn@uBfASJQHOHe@VE@u@^ULg@VEB_@ROF_Ad@iAl@C@{@b@g@Xe@Te@VcAf@]PMFsAp@e@VUJQJUJmAp@cAf@q@\\QHq@\\q@\\yDnBs@^mB`AkAl@kAl@iB~@g@VOHSL}@b@e@VSJm@ZiB~@qAn@oAp@{At@YPi@V_Bx@kAl@mCtAaHlDiAl@mAn@w@^i@ZYLCBC@]Pu@`@mCtAwAr@UJsBdAcCnAgCpAUJmGbDiB|@EBm@ZmE|BiB`AwCxAKF_JrE{BhAu@`@k@XUL[NOHo@Zo@\\C@s@^KDA@QHQHa@TA@{@b@MFIDQJ{@b@m@XOHa@TOH[NSJIDg@VMFk@XULKFSHQJo@\\_@PQJy@`@mAn@sAp@MFkAl@qAp@w@`@m@Zu@^g@V[PsAp@WLOHs@^i@Xw@^CBcBz@OHuAr@eAh@QHWLyAv@_@PMHIDqAn@GDwAr@ULwAt@MFeAh@q@\\s@^_@RiAj@{@b@OHEBqBbAOFoAp@o@ZeB|@sAr@]PQHiAj@EDc@R{Av@}Av@y@`@OHkAn@u@\\a@TYLu@`@uAt@yAt@}@b@y@b@A?c@Tc@T}@d@UJi@Xo@\\}Av@oAn@KF_ClAKFqAn@GDgAh@SJ?@c@TSJQHGBGDUJ]Ru@^QHKFg@Vi@XID_Af@UJe@V]NMFeAj@c@RaAf@OH}Av@{@b@QJKDIDu@`@mAl@y@b@g@VA@iDdBoAn@o@Zm@ZULa@RoAp@SHmAn@c@TeB|@IFqAn@c@TSJoAn@QHQJMFeAj@MFw@`@{@b@w@`@SJy@`@IFm@ZMFk@XSJOH[Ps@\\C@gB~@eAh@OH[NMFUL_@ROHWLSJm@ZOHWLk@Zu@^m@ZeAh@[PYL]Ro@Z{@b@o@ZE@YNE@k@Xc@P[N[L_@NWHk@Rg@Py@Vs@TuA\\_ATwAX_@H]FeANUDa@DSB[DWBK@k@Fi@DO@m@DI@a@B[@I@s@B[@i@@E?[@c@@M@K?O@[@a@@U?m@Bq@@w@BU@aABq@BM?Y@e@@M@[@Q?K@c@@W@m@@I@_@@_AB{@BG?uADG?c@@I@_@@W?m@BK?aCFeBFQ?mAD]@W?Y@O@{AD{@Bi@@U@_ABG?y@Bk@BU?]@a@B_ABS?Y@Q@m@@m@BS?k@BU@W@gBDeADU?s@BI@a@@i@@qADC?cBFaADM?]@a@@]@M@qADI?{@BK@k@@uBFu@Bu@BiABm@B}@BO?q@BaABO?q@Bw@BU@s@B{@BS?A?g@@_@Bk@@S@k@@y@Bm@B_ABe@@M@s@@W@gABG@c@@aELs@@e@@u@@w@@}@@o@?uA?UA_A?s@A_@A[?s@C_@Am@A_@Ag@Cc@Ak@C_BEc@CgAEe@AuAEsAEk@CqBGoEOcAEo@CkDKkFQgL_@oFQeAEmACe@CiCImAEK?eACUAKAaAA}@AcAAU?k@?i@@g@@g@?W@O@[@_@@S@U@U@U@U@Y@K@Y@Q@WBS@YBUBS@SBWBUBUBQ@WDSBWBUBSDUBUBUDMBK@c@HSBWDUDODUDWDSDUDQDWFQDWFUDKBIBSFQDUFSDQFq@Pi@Pk@Pu@VKBeA^OFm@TSHa@N_A`@OFUJSHSJQHIDKDQHULSHSJSLYN]Pe@XQHSLSJQJQLSLOHSNQJQLQJA@OJQJIFEBQNSLOJSNc@\\a@ZSNOLQNQNCBUPA@UPSR_@ZQPOLg@f@EBSRSROLQPOLONGFg@d@QPCBMLQNUT{@x@QPc@`@MLQNOPONC@qCnCqApAYXKHOP_@^}BzBQNq@p@]^_@^aA~@a@`@a@^a@`@YXOL_@`@YVKLSPONiChCi@f@QRc@`@sApAaA`A_@^a@`@OLOP]\\[Z]Z[Zq@n@a@`@]^SPON_@^a@^ONONONSTkBfBOPSRsEnEONwCtCqInIoBlBYXqApAoAlAq@p@k@h@}@|@KJe@b@MNON{@x@e@d@eAdA}AzAKJa@`@oAlAm@l@gAdAkAjAYVg@f@w@v@gAfAcAbAu@t@a@b@uAvAA@cBdBaB`BcAbAaI~Hy@v@ONwCrCwAvAi@h@OP]Zq@n@c@d@IHQP[ZiAfAc@d@a@^WVa@`@]Z_@^_@`@e@`@c@f@qAnAu@t@eBbBsBpBUTgAdA{@z@{@x@g@f@YXEDgDbDq@r@YVCBq@p@wAvAg@f@IFYXwAvAe@d@}@x@YX{@z@yAnAy@r@MJ{@r@s@j@w@l@y@n@SL[VMHC@q@d@a@XYPcAp@}@j@KFk@^y@d@CBu@`@e@Vg@Xu@`@c@Tg@V]Pg@T_@Ru@\\]N_@PYLqCjAkAf@SHC@WJGDa@N[Lq@XOFC@cAb@_Bn@}CpAm@VkEfBmBx@_@Nq@XeEdBo@VYLoAh@i@RoAh@qDzAUHg@R{@^A?_A`@o@Xk@TGBi@R}Ap@y@\\gBr@gAb@]PoBx@A?w@\\e@P{@^cA`@A@yAl@g@Re@R{@\\eBt@IBkCfAu@Zq@XMFeBr@]NeAb@i@Tq@XaA`@y@ZaAb@_A^_Bp@aBp@WJ}An@{B~@_C`AaBp@oAh@u@ZMDw@\\q@V_@LoAb@}@VoA\\m@Nw@P[FYF_BXOBSDw@JkANUBe@DaBLw@FeBFS@o@@Q?s@@q@?_A?u@Ao@AA?UAi@CYAOAA?I?WCI?y@GC?_@E_@CWC]EiAK_CWC?c@EeAKs@I_AK_AI?AA?C?GAa@EWC}@KI?A?AAE?a@ESCOCq@Ge@Gq@G]EUCw@GSCeAM_AI_@EKAOCo@Ii@EWCUCm@G_@EcBQ{AOgCW[Cu@Iy@Iy@IkAMUCUCWCUCUCUCUCWCUCUCUCUCSAUC[ESC]Ca@E[EQASCWCUCSCWCUCUCWCSCWCWCUCUCSCWC]CQAQCUAUAUAEAM?UAW?UAU?O?E?U@M?m@DQ?W@SB[BQ@MBG?G@Q@UDa@FYD[DUDSDQDQDSFUFSDQFQFQFSFUHMDKDSJOFQH_@PWLULUJQLWLMHQJOHCBOH[POHMH_@RMFSLQJQJQJg@XQJQJSLSJSJQJWNQJMH[NKHSJSJSLQJQJSJSLQJOHGDs@^w@b@YPMHkBdAIDc@Vo@^gGjDyAz@q@^e@V[PSLWLYPw@b@k@Z}@h@wDvBqBfAkLtGeBbAcAj@gGlDOHs@`@aAj@aAh@m@\\s@`@q@`@cDjBo@\\iAn@a@Tw@d@sAt@_@Rc@VwAv@g@XeAl@c@VKF_@RIF_Ah@QH?@A?ULKFC@WNKFA@_@R_@TmBdAa@TMHA@SJmCzAcAl@C@WNGDy@b@KH}@d@}BrAoC|AoC`BMFSLyCbBmC|AqAt@uAv@}EnCkBdA_DhB_Ah@{Az@c@VIDc@VQJ_@RgCxAk@ZoAr@m@\\SLe@Ve@Ve@Xg@XQJe@VSLQJSJQJSLQJSJQJSJQLQJSLSLQJQJUPKBC@QJQLQLSLQLQLQLOLQLSNQLCDMHQLQNOLQNQNQNOLQNQNQNONQPONQNQPMLQNOPONOPONONUTKLQPa@b@ONOPON[\\SRQPONOPONOPONONOPMNa@b@ONQP]^OPQNOPONOPONKLWV_@`@_AbAq@p@ONa@b@k@n@WV}@~@[\\KLaAbAONOPONONSROPONOPONOPMJQROPONKLA@OLQROPKHABSRONONOPONMNQPKJSTOPONONQRMJQTSRiAlAu@t@m@n@m@p@IHONIJONKLURMPONQN?@ONKLUR_@b@QPQPIJQPOPONQPSTKJc@d@KL_B`BSVWVQROLOPONQRA@KH_@b@k@l@QP_@`@OPONQPONOPONOPONCB]^ONONOPON_@`@IHWVOP_@`@SROPONOPONOPQNOPON_@`@OPiAjAGFOPOPa@`@ONOP_@`@ONOPONONOPONOPMLSRKJOPONONOPONOPONOPONSRGFGHONOPEDWXIHYZUV_@\\OPWTONKJQNs@p@}@x@YRe@`@a@Za@ZYV}@t@MHg@^[ToA~@KFMHsA~@UNq@d@QJy@f@C@{A`Ak@^]TA?OJOJ_B`A[TGD{@h@eBdAMHEBIFeBfAq@b@ULoAx@KFGDUNq@`@SLUNGDWNWPA@eC|AA@s@d@q@`@MHEBe@Xg@ZoAv@s@d@IDYRgAp@kAv@kAr@aAn@OHOJc@VKH]TGBQLSJSLq@b@i@\\aAl@_Al@{@j@_BbAqAx@e@Zo@^aJzFqAx@o@^y@h@gHpEe@ZWNg@Zo@`@a@VYPmAv@y@h@SLA@mAx@iAx@YRIF{@n@oA`AGDGFq@j@aAv@SPQNA@}@x@ON[XA@YVcA`A[XCDu@v@A@s@r@_@`@IJeAhACD_@`@MNYZuAzAkApAeAjAq@t@yA`BQRIHkApA{@|@MNqAxAq@r@uAzAMNOPSRGFOPc@f@uB|BiBpBgAlAe@h@IHu@v@Y\\e@f@qAvAu@x@i@l@oAtAOPONOP_@`@WVMNIH[\\k@n@{@z@KLEBOPMNKLUTKJu@z@[\\OPqCzCa@b@e@h@m@n@WZcAfAy@|@{@~@g@f@IHKHSP[VQLQNo@b@_@TYPULWLQJy@b@[N}@f@]POHiAj@yAv@"
                                    },
                                    "start_location": {
                                        "lat": 27.4146674,
                                        "lng": -80.3921191
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.1 mi",
                                        "value": 235
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 9
                                    },
                                    "end_location": {
                                        "lat": 30.3045678,
                                        "lng": -81.64229069999999
                                    },
                                    "html_instructions": "Take exit <b>348</b> toward <b>Interstate 95 service Rd</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "wn}wDzphqNUEUHUJE@UJ_@NIDOFMFIDSJSJSJUJKFSLULOJq@b@"
                                    },
                                    "start_location": {
                                        "lat": 30.3026826,
                                        "lng": -81.641262
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.5 mi",
                                        "value": 816
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 31
                                    },
                                    "end_location": {
                                        "lat": 30.3103446,
                                        "lng": -81.64747589999999
                                    },
                                    "html_instructions": "Take the ramp to <b>Downtown</b>/<wbr/><b>Main St Bridge</b>/<wbr/><b>Acosta Brg</b>",
                                    "polyline": {
                                        "points": "qz}wDhwhqNMHIFUPED]Va@\\QP[XCBMLQNONMNmBtBIHGFOPu@x@k@l@GH]\\WXEJ[ZOL[\\OLe@`@EDEDSNOLURQLQL_@VOH}A`Ay@b@c@TUNSLOLIHGDGF]XONEDEBEF"
                                    },
                                    "start_location": {
                                        "lat": 30.3045678,
                                        "lng": -81.64229069999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.7 mi",
                                        "value": 1144
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 45
                                    },
                                    "end_location": {
                                        "lat": 30.31433729999999,
                                        "lng": -81.6576734
                                    },
                                    "html_instructions": "Continue onto <b>Interstate 95 service Rd</b>",
                                    "polyline": {
                                        "points": "s~~wDvwiqNOLOPOPQPMNIJCFOPMRKRMP[j@[f@KRYd@MTMRGLEDMTGHCFORKNOTQTKLGHILOPOPONOPMNMNONQRQPOPGFUVOROPKNORKPMRS^KTITKTADABEJADGPIXGRGVEVGXEVCVADCXARCX?X?@AV?V@V?J?f@?L?d@@Z@~B?Z@P?Z?V?Z@n@@X?Z?B?R@V?X?F@fA@T?V"
                                    },
                                    "start_location": {
                                        "lat": 30.3103446,
                                        "lng": -81.64747589999999
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "299 ft",
                                        "value": 91
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 5
                                    },
                                    "end_location": {
                                        "lat": 30.3146852,
                                        "lng": -81.6585151
                                    },
                                    "html_instructions": "Take the <b>FL-10</b>/<wbr/><b>US-1</b>/<wbr/><b>Prudential Dr</b> exit toward <b>Main St Bridge</b>/<wbr/><b>Ocean St</b>",
                                    "maneuver": "ramp-right",
                                    "polyline": {
                                        "points": "sw_xDlwkqNGPCHAJALAHAJA@CLGPADIPCDKRGH"
                                    },
                                    "start_location": {
                                        "lat": 30.31433729999999,
                                        "lng": -81.6576734
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "1.2 mi",
                                        "value": 1938
                                    },
                                    "duration": {
                                        "text": "3 mins",
                                        "value": 176
                                    },
                                    "end_location": {
                                        "lat": 30.3312381,
                                        "lng": -81.6552402
                                    },
                                    "html_instructions": "Continue onto <b>FL-10 W</b>",
                                    "polyline": {
                                        "points": "yy_xDv|kqN]\\QLWNA?UHMBQDKBM@WBMBKBK?]@k@?g@?}@CeAC}@Co@C_@CE?G?A?A?[A]Ac@A_@AC?I?K?A?C?GAE?u@AkBEiAEyBIy@CQAA?OAq@EmBIiCMgAGeAEgAGsBKG?Q?YAEAC?GAEACAICCACAACCACACCCCECCECCCEEGEKYe@Wg@We@MYMSMQIKIGUOIECAaAWMGg@MeAS[GyCm@y@QwAWeASSEy@O]Gc@KYGYEa@IqCg@}@Q[GMCq@M"
                                    },
                                    "start_location": {
                                        "lat": 30.3146852,
                                        "lng": -81.6585151
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "0.1 mi",
                                        "value": 171
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 27
                                    },
                                    "end_location": {
                                        "lat": 30.33273359999999,
                                        "lng": -81.654819
                                    },
                                    "html_instructions": "Continue onto <b>N Ocean St</b>",
                                    "polyline": {
                                        "points": "gacxDfhkqNi@KmAU]GkB]g@K"
                                    },
                                    "start_location": {
                                        "lat": 30.3312381,
                                        "lng": -81.6552402
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "384 ft",
                                        "value": 117
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 16
                                    },
                                    "end_location": {
                                        "lat": 30.3330064,
                                        "lng": -81.6559944
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>E State St</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "qjcxDrekqNUzAIh@Kx@Kh@"
                                    },
                                    "start_location": {
                                        "lat": 30.33273359999999,
                                        "lng": -81.654819
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "285 ft",
                                        "value": 87
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 21
                                    },
                                    "end_location": {
                                        "lat": 30.332246,
                                        "lng": -81.656216
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>N Main St</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "ilcxD|lkqNf@LB?TDtAX"
                                    },
                                    "start_location": {
                                        "lat": 30.3330064,
                                        "lng": -81.6559944
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance": {
                                        "text": "190 ft",
                                        "value": 58
                                    },
                                    "duration": {
                                        "text": "1 min",
                                        "value": 16
                                    },
                                    "end_location": {
                                        "lat": 30.332119,
                                        "lng": -81.65562849999999
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>E Union St</b>",
                                    "maneuver": "turn-left",
                                    "polyline": {
                                        "points": "qgcxDjnkqNVgB@M"
                                    },
                                    "start_location": {
                                        "lat": 30.332246,
                                        "lng": -81.656216
                                    },
                                    "travel_mode": "DRIVING"
                                }
                            ],
                            "traffic_speed_entry": [],
                            "via_waypoint": []
                        }
                    ],
                    "overview_polyline": {
                        "points": "uqf|CzmmhNcGkAhGhB|PbLNd@jHzKxMpTfMrSeBnF_IsKu@aAqDaFaLoEe]U}v@uDor@lEumAz`@swD`FslAkAcxAdJigEjGulCdEiqBvDsy@dH}l@vi@mgAnu@ozExH{~@_b@_cAsz@geAoIi}ClHs_HvKgjBlJcyASokD`GilDxAyl@aMiq@of@ar@ui@ytCy}B}~AapA{j@iW_jAaBo}@hKouCfA{eF~E}gL|DsjEtEiyCbMenHiKooGr@siP~Ee_Cr@cw@Mo`Ao\\ieCglBis@qq@s}@}i@ioB_JwrCqE{_IgQmeEwFicByBk~AuBwvArRk|B~u@acAx\\mfBll@kiAxa@iiBpkAekC~dBszAftAqaBfoByxAhbBifAx]aqAhA_nCtv@svBhu@kpAnbAqrBzoAsvE`qCuhD`rBeqEvgB{wFtkA}nCpoAcpA|d@shAfRixArAqvBGw|AxHk~D`}Aw|Abm@kw@pBqQc{@bAqOyBjIgeBNgxAb_@yr@x^ky@znBuy@~nAsqBpu@cxBfq@_iAvb@kn@|d@_dAxw@yxA~hAadA~w@qoBbbAazCjpAu|@~VsxAbBenBpg@mcDj`AowD~v@csFzr@onChDgsDgJstAwGy|@`i@mhAdbAofBx}A_hAr_A{o@dDu|AnAccBvXyeI`sAi_BvWsrAf_@cgCt_BggFzcD}bAb}AgmA`xBec@pt@gX|LknCXilKQeaCEqsBnWm~GfrAa{B~b@uyAhYcd@xOg`@~e@wi@t`A_y@~p@_}B~qAy{FjeDwwBpnAymBlj@qm@n@qsCZqhDbDo|Ab@atFtyDk}JPimDa@}gAMwu@zOioCbz@}`Cpt@clD|eAogAx\\{u@tMytBka@ahBb[sxGfnAatCrk@q}Brd@srCpVq`F`rA{rBfb@odGfuBkmHh`Ey`B|~@eyArr@krCxPeqDlvAywApk@q^`Xgn@|lAq}@|{AwlAfo@ctDtbBabAr`@ogCln@kfHveBgyHpiB}oE}BgbAGoiAr]ojFjeBc|QnnFccEziAolBfv@yxGzwDi|Gh~Co`CleAel@`r@ci@viAmpAt_C__DhgAkcLtgDqlIhoCynD|pAo~Dzx@{jEz|@sp@f^cq@dm@}_CnrBkqFtqCgwDfnB{oAzo@aeAz[ggDjIsrBwCen@tRcpCfkCanBtlBeeB`z@avBbt@{|@sGux@sGmf@pRwsEfjC{mA`nAmyAdvAsaBxdAcmAxiA_pBvcBkXfc@?`ZoKdHst@mFyg@qOwH`DpDgA"
                    },
                    "summary": "Florida's Tpke and I-95 N",
                    "warnings": [],
                    "waypoint_order": []
                }
            ],
            "status": "OK"
        }, "places": [
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7665181,
                    "lng": -80.2019991
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Calle Ocho Plaza",
                "place_id": "ChIJw3-9-Y622YgRYWXCmMaNMek",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7789389,
                    "lng": -80.1878931
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Themidnightclubrentals",
                "place_id": "ChIJ30KwmJq32YgRoLPKAjeAzgk",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7896077,
                    "lng": -80.2172372
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Whateverforever09",
                "place_id": "ChIJW3Dmjri32YgRmXArI-EokJE",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.92864149999999,
                    "lng": -80.1955076
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "name": "Claroma Shops",
                "place_id": "ChIJAfgMFWmv2YgR4C3_ELSt4j8",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Shopping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.740819,
                    "lng": -80.278453
                },
                "icon": None,
                "name": "the-biltmore-hotel-miami---coral-gables",
                "place_id": None,
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Camping"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7623624,
                    "lng": -80.19407199999999
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Hampton Inn & Suites by Hilton Miami Brickell Downtown",
                "place_id": "ChIJn-2Oo4a22YgR-fOW2Yuryjo",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7588046,
                    "lng": -80.1922639
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Four Seasons Hotel Miami",
                "place_id": "ChIJB4u6yIC22YgRSudXSqzWT0k",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.77052149999999,
                    "lng": -80.18933919999999
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Kimpton EPIC Hotel",
                "place_id": "ChIJlWF1Gp222YgRkg_v_MAt_Sc",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7709263,
                    "lng": -80.1910809
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Hyatt Regency Miami",
                "place_id": "ChIJlZUqA5222YgRzjtasuQFBNg",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            },
            {
                "business_status": "OPERATIONAL",
                "location": {
                    "lat": 25.7754416,
                    "lng": -80.18836689999999
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "name": "Dump Hotel",
                "place_id": "ChIJEZE3EZ622YgRsVmaEQPx0Pk",
                "in_route": True,
                "origin": False,
                "destination": False,
                "category_name": "Hotel & Lodging"
            }]
        }
    }}
)
