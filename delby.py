"""
===== Intro =====
# Here at Delby, we admire NASA’s engineering mission. But beyond that, we can use data from NASA to learn about how space interacts
# with Earth. Solving global warming is unfortunately outside the scope of an interview question, so your goal is somewhat simpler: use
# NASA’s public HTTP APIs to create a function which determines which of four locations has seen the brightest shooting stars since 2017.
# This can be handy if you're trying to find a good spot to do some night sky watching. :-) 
# 
# ===== Steps =====
# 
# 2.  Pull up the documentation for the API you'll be using:
#       https://ssd-api.jpl.nasa.gov/doc/fireball.html
# 
# 3.  Implement a function fireball() whose function signature looks like this
#       Object fireball(double latitude, double longitude)
# 
# When there is enough data to do, it should return the brightness & location for the brightest shooting star seen since 2017 at location.
# 
#     The human eye can see a lot of the night sky, so give your latitude and longitude a buffer of +/- 15. For example, if you are looking
#     for shooting stars at the Delby SF Office 
#          37.7937007,  -122.4039064
#     You would look for shooting stars within these coordinates: 
#          (22.7937007   <--> 52.7937007,
#          -107.4039064 <--> -137.4039064)
# 
#     The brightness should be determined using the energy from each shooting star (a higher ‘energy’ meaning a brighter star).     
#     You can use the https://ssd-api.jpl.nasa.gov/doc/fireball.html API to get the information you will need to compute this.
#  
#     *Note* that Latitude and Longitude can be written in a few different formats. We suggest converting the returned data to Signed
# Degrees from the given Degrees plus Compass Direction.
#     
#     To convert, take any Southern Latitude and make it negative, take any Western Longitude and make it negative.
#     
#     For example:
#     San Francisco - latitude: 37.79N, longitude: 122.40W
#     This can be converted to (37.39, -122.40)
#     
#     Signed Degrees:
#      - Latitudes range from -90 to 90.
#      - Longitudes range from -180 to 180.
#      
#     Degrees plus Compass Direction:
#     Latitudes range from 0 to 90.
#     Longitudes range from 0 to 180.
#     Use N, S, E or W as either the first or last character, which represents a compass direction North, South, East or West.

# 4.  With your function, determine which of four locations had the brightest shooting star(2017). Print location & brightness for star.
#     Use these Delby Office Locations to figure out which Office saw the brightest star since 2017 (2017-01-01 -> 2021-01-01)
#     Boston -        latitude: 42.36, longitude: -71.05
#     London -        latitude: 51.51, longitude: -0.12
#     NCR -           latitude: 28.58, longitude: 77.31
#     San Francisco - latitude: 37.79, longitude: -122.40

# 5.  Add any tests for your code to the main() method of your program so that we can easily run them.
# 
# 6.  Implement error handling. On basis of language you're using, Adjust the function signature to do in an idiomatic way

# ====== FAQs =====
# Q:  Won't we be able to see a wider longitude range the higher our latitude (with an extreme of either the North or South Pole)?
# A:  That is correct. But to help simplify this problem you can just assume that we can only see the +/- 15 degrees regardless of your 
# location.
#     
# Q:  What if the +/- 15 degrees creates a location that is beyond the typical boundary conditions for Latitude and/or Longitude?
# A:  If a location is near a maximum boundary (-90, 90) or (-180, 180) it is fine to limit the visible box to that boundary. eg, a location
#     at (-80, 175) can have a visibility box of:
#          (-90 <--> -65,
#          160  <--> 180)
# 
# Q:  How do I know if my solution is correct?
# A:  Make sure you've read the prompt carefully and you're convinced your program does what you think it should in the common case. If 
# your program does what the prompt  dictates, you will get full credit. We do not use an auto-grader, so we do not have any values for you
#     check correctness against.
"""


# importing supporting modules
import sys
import requests

LAT_LONG_RANGE = 15


class HitShootingStarAPI(object):
    """
    class to hit the NASE api and get response
    Handles the exception if any exception is raised
    Maps data received from API with respective keys
    """
    def __init__(self, *args, **kwargs):
        self.API_URL = "https://ssd-api.jpl.nasa.gov/fireball.api"
        self.params = {"date-min": "2017-01-01", "req-loc": "true"}
        self.fields = list()
        self.all_location_points = list()

    def get_mapped_data(self, data):
        self.all_location_points.append(dict(zip(self.fields, data)))

    def hit_api(self):
        try:
            r = requests.get(url=self.API_URL, params=self.params)
            response_content = r.json()
        except Exception as ex:
            print("Exception occured while  fetching data is: {0}".format(str(ex)))
            return False, str(ex)
        import pdb;pdb.set_trace()

        data_values = response_content.get('data')
        self.fields = response_content.get('fields')
        
        # map the latitude/longitude data with their respective feilds/keys        
        for item in data_values:
            self.get_mapped_data(item)
        return True, self.all_location_points

class DelbyLoction(object):
    def  __init__(self, location_name, ltd, lgt, ltd_dir, lgt_dir):
        """
        initialising Delby office locations
        params:
            location_name: Office location's name
            ltd: latitude for office location
            lgt: longitude for office location
            ltd_dir = latitude direction (N, S)
            lgt_dir = longitude direction (E, W)
        returns:
            Initialise DelpbyLocation Object with received params.
        """
        self.location_name = location_name
        self.latitude = ltd
        self.longitude = lgt
        self.latitude_dir = ltd_dir
        self.longitude_dir = lgt_dir


def get_brightest_star(max_brightness, del_location, all_location_points):
    # get brightest star for Delby-office-locations out of all given locations points
    # considering the case where 
    # * location is near boundary, we can adjust the same with +/-15 degrees regardless of your location
    latMin = del_location.latitude - LAT_LONG_RANGE;
    latMax = del_location.latitude + LAT_LONG_RANGE;
    longMin = del_location.longitude - LAT_LONG_RANGE;
    longMax = del_location.longitude + LAT_LONG_RANGE;


    for data_point in all_location_points:
        # making a check if directions are same for Delby location points and 
        # all location points
        if del_location.latitude_dir == data_point.get('lat-dir') and \
            del_location.longitude_dir == data_point.get('lon-dir'):
            # making a check if latitude & longitude of location points lies in a boundary (adjusted)
            if latMin <= float(data_point.get('lat')) <= latMax and \
                longMin <= float(data_point.get('lon')) <= longMax:

                # making a check if approximate total impact energy is greater than max-brightness observed till now
                total_impact_energy = float(data_point.get('impact-e'))
                if max_brightness < total_impact_energy:
                    max_brightness = total_impact_energy

    return max_brightness


def fireball(mapped_data):
    # function to identify the location which encountered the brigtest shooting star from given date.

    # assuming we've 0 brightness as maximum at first and their is no office that has seen 
    # brightest shooting star since given date to start the process.
    maximum_brightness = 0
    office_with_max_brightness = None

    # iterating through delby offices
    for office in delby_locations:
        brightness = get_brightest_star(maximum_brightness, office, mapped_data)
        if brightness > maximum_brightness:
            maximum_brightness = brightness
            office_with_max_brightness = office

    if not office_with_max_brightness:
        print("With all the location points/data received from API, there was not a great match for the location with "
            "given latitude/latitude-dir & longitude/longitude-dir. So encoutering issue while calculating location that "
            "has seen brightest shooting star within given span of time")
        sys.exit()
    print("{0} has seen the brightest shooting stars since given time with energy of {1} Joules.".format(
        office_with_max_brightness.location_name, maximum_brightness))

# Creating an array-kind holding Delby office locations with their:
# 1. Location Name
# 2. Latitude
# 3. Longitude
# 4. Latitude Direction
# 5. Longitude Direction
delby_locations = list()        
delby_locations.append(DelbyLoction("Boston", 42.36, -71.05, "N", "W"))
delby_locations.append(DelbyLoction("London", 51.51, -0.12, "N", "W"))
delby_locations.append(DelbyLoction("NCR", 28.58, 77.31, "N", "E"))
delby_locations.append(DelbyLoction("San Francisco", 37.79, -122.40, "N", "W"))

hit_api_obj = HitShootingStarAPI()
is_success, mapped_data = hit_api_obj.hit_api()

# when we are able to fetch data from NASAs API, 
# then we can calculate for the office which saw brightest shooting star
if is_success:
    fireball(mapped_data)
