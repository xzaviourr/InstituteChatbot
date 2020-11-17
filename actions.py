from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.database.queries import recommend_person


class ActionSendMessage(Action):

    def name(self) -> Text:
        return "action_send_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("person")
        msg = tracker.get_slot("message")
        dispatcher.utter_message(text="name: " + str(name) + " msg: " + str(msg))
        return []


class ActionRecommendPerson(Action):
    def name(self) -> Text:
        return "action_recommend_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        skill = tracker.get_slot("topic")
        dispatcher.utter_message(recommend_person(skill))
        return []