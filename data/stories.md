## greetings
* greet
  - utter_greet
  
## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## thankyou
  - utter_welcome
  
## send user a message
* message_person
  - utter_what_message
* messages
  - action_send_message
  
## send message
* new_message
  - utter_whom_to_send
* persons
  - utter_what_message
* messages
  - action_send_message
  
## send given message to given person
* message_person_this_message
  - action_send_message

## recommending person
* recommend_person_with_given_info
  - action_recommend_person
 
## Adding new skill
* add_skill
  - utter_what_skill
* topics
  - action_add_skill
 
## Adding skill this skill
* add_skill_this_skill
  - action_add_skill
  
## signup
* signup
  - action_reset_all_slots
  - signup_form
  - form{"name": "signup_form"}
  - form{"name": "null"}
 
## signin
* login
  - action_reset_all_slots
  - signin_form
  - form{"name": "signin_form"}
  - form{"name": "null"}
  
## new messages
* new_messages
  - action_show_messages
  
## Show time
* time
  - utter_time