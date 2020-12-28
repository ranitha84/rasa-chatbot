# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


from utilities import zomatopy
from utilities.location_check import  LocationCheck

from utilities.email_utility import  send_email
import settings
global restaurants

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        zomato = zomatopy.initialize_app(settings.ZOMATO_CONFIG)
        try:
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            price = tracker.get_slot('price')
            restaurant_found = 'notfound'
            global restaurants
            restaurants, response = zomato.get_loc_cus_price_results(loc, price, cuisine)
            if response == 'no results':
                response = "No results found for your search criteria!!!"
            else:
                top5_restaurants = restaurants.head(5)
                print(restaurants.head())
                # top 5 results to display
                if len(top5_restaurants)>0:
                    restaurant_found = 'found'

                    response = "We found the following restaurants for you!!!\n"
                    for index, row in top5_restaurants.iterrows():
                        response = response + str(row["restaurant_name"]) + ' (rated ' + row[
                            'restaurant_rating'] + ') in ' + row[
                                       'restaurant_address'] + ' and the average budget for two people ' + str(
                            row['budget_for2people']) + "\n"
                else:
                    response = "No results found for your search criteria!!!"
            dispatcher.utter_message("-----\n" + response)
            return [SlotSet('location', loc), SlotSet('cuisine', cuisine), SlotSet('price', price), SlotSet('restaurant_found', restaurant_found)]
        except Exception as e:
            dispatcher.utter_message("-----\n Sorry we don't serve the specified location. Please specify a different location")
            return [SlotSet('location', None), SlotSet('cuisine', None), SlotSet('price', None),
                    SlotSet('restaurant_found', 'notfound')]


class EmailService(Action):
    def name(self):
        return 'action_email_details'

    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')
        print('recipient is {}'.format(recipient))
        try:
            global restaurants
            res = restaurants
            if len(res) > 0:
                top10 = res.head(10)
                print("got this correct email is {}".format(recipient))
                send_email(recipient, top10)
        except Exception as e:
            dispatcher.utter_message("We are facing an issue while sending email :(")


class CheckLocation(Action):
    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        print('checking location')
        try:
            loc = tracker.get_slot('location')
            location_check = LocationCheck()
            check = location_check.check_location(loc)
            print(check)
            return [SlotSet('location', check['location']), SlotSet('location_found', check['location_found'])]
        except:
            dispatcher.utter_message(
                "-----\n Sorry we don't serve the specified location. Please specify a different location")
            return [SlotSet('location', None), SlotSet('location_found', 'notfound')]

class ResetSlots(Action):
    def name(self):
        return 'action_reset_slots'

    def run(self, dispatcher, tracker, domain):
        print('reset slots')

        return [SlotSet('location', None),
                SlotSet('location_found', None),
                SlotSet('price', None),
                SlotSet('email', None),
                SlotSet('cuisine', None)]