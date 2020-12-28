from utilities import zomatopy
import json
global city_dict
import settings

class LocationCheck:

    def __init__(self):
        global city_dict
        city_dict = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra',
                     'Ajmer',
                     'Aligarh', 'Allahabad', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum',
                     'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City', 'Chandigarh',
                     'Coimbatore', 'Cuttack', 'Dehradun',
                     'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad',
                     'Gorakhpur', 'Gulbarga',
                     'Guntur', 'Gurgaon', 'Guwahati‚ Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur',
                     'Jalandhar', 'Jammu',
                     'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam',
                     'Kolhapur', 'Kollam', 'Kota',
                     'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa',
                     'Mangalore', 'Meerut', 'Moradabad',
                     'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry',
                     'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi',
                     'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat',
                     'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli',
                     'Tirunelveli', 'Tiruppur', 'Ujjain', 'Vijayapura', 'Vadodara', 'Varanasi', 'Vasai-Virar City',
                     'Vijayawada', 'Visakhapatnam', 'Warangal']
        city_dict = [x.lower() for x in city_dict]

        self.zomato = zomatopy.initialize_app(settings.ZOMATO_CONFIG)

    def check_location(self, loc):
        print("going to check location")
        location_detail = self.zomato.get_location(loc, 1)
        location_json = json.loads(location_detail)
        location_results = len(location_json['location_suggestions'])

        if location_results == 0:
            return {'location_found': 'notfound', 'location': None}
        elif loc.lower() not in city_dict:
            return {'location_found': 'tier3', 'location': None}
        else:
            return {'location_found': 'found', 'location': loc}




