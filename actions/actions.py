from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from actions.database.queries import *


class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionSendMessage(Action):

    def name(self) -> Text:
        return "action_send_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("person")
        msg = tracker.get_slot("message")
        sender_id = tracker.get_slot("user_id")
        if sender_id is None:
            dispatcher.utter_message(text="You need to sign in first")
        else:
            dispatcher.utter_message(text=send_message(sender_id, name, msg))
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


class ActionAddSkill(Action):
    def name(self) -> Text:
        return "action_add_skill"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        skill = tracker.get_slot("topic")
        user_id = tracker.get_slot("user_id")
        if user_id is None:
            dispatcher.utter_message(text="You need to sign in first")
        else:
            dispatcher.utter_message(add_skill(user_id, skill))
        return []


class SignupForm(FormAction):
    def name(self):
        return "signup_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["first_name", "last_name", "email", "password"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "first_name": self.from_text(),
            "last_name": self.from_text(),
            "email": self.from_text(),
            "password": self.from_text(),
        }

    def validate_email(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        if value.endswith("@iiitm.ac.in"):
            return {"email": value}
        else:
            dispatcher.utter_message("Please use G-Suite email")
            return {"email": None}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        flag, msg = register(tracker.get_slot("first_name"), tracker.get_slot("last_name"), tracker.get_slot("email"),
                             tracker.get_slot("password"))
        if flag == 0:
            dispatcher.utter_message(msg)
            return []
        else:
            dispatcher.utter_message(msg)
            return [SlotSet("user_id", flag)]


class SigninForm(FormAction):
    def name(self):
        return "signin_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["email", "password"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "email": self.from_text(),
            "password": self.from_text(),
        }

    def validate_email(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
        if value.endswith("@iiitm.ac.in"):
            return {"email": value}
        else:
            dispatcher.utter_message("Please use G-Suite email")
            return {"email": None}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        flag, msg = login(tracker.get_slot("email"), tracker.get_slot("password"))
        if flag == 0:
            dispatcher.utter_message(str(msg))
            return []
        else:
            dispatcher.utter_message(str(msg))
            dispatcher.utter_message(show_pending_messages(flag))
            return [SlotSet("user_id", flag)]


class ShowPendingMessages(Action):
    def name(self) -> Text:
        return "action_show_messages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = 2
        if user_id is None:
            dispatcher.utter_message(text="You need to sign in first")
        else:
            dispatcher.utter_message(show_pending_messages(user_id))
        return []
