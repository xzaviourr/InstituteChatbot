import sqlite3
from datetime import datetime


def recommend_person(skill):
    """
    Recommends person with the appropriate skill
    :param skill: name of the skill
    :return: reply
    """
    conn = sqlite3.connect("actions/database/donna.db")
    cursor = conn.cursor()

    skill_copy = skill
    skill = skill.upper()
    query = "SELECT skill_id FROM Skills WHERE skill_name = '{}';".format(skill)
    cursor.execute(query)
    skill_id = cursor.fetchone()

    if skill_id is None:
        conn.close()
        return "Looks like no one I know, has ever explored this before"
    else:
        query = """SELECT first_name, last_name, batch, year FROM Users, UserSkills WHERE UserSkills.skill_id = '{}'
                AND Users.user_id = UserSkills.user_id ORDER BY UserSkills.timestamp;""".format(skill_id[0])
        cursor.execute(query)
        users = cursor.fetchall()
        conn.close()
        if users is None:
            return "Looks like no one I know, has ever explored this before"
        else:
            reply = """Few people you may get in touch for {} are\n""".format(skill_copy)
            for user in users:
                reply += "{} {}\t-\t{} {} batch \n".format(user[0], user[1], user[2], user[3])
            return reply


def send_message(sender_id, receiver_name, msg):
    """
    Takes the incoming message and adds it to the pending messages table
    :param sender_id: Integer value of sender_id
    :param receiver_name: String type name of the recepient
    :param msg: Message that needs to be sent
    :return: reply
    """
    conn = sqlite3.connect("actions/database/donna.db")
    cursor = conn.cursor()
    first_name, last_name = receiver_name.upper().split(' ')
    query = "SELECT user_id FROM Users WHERE first_name = '{}' AND last_name = '{}';".format(first_name, last_name)
    print(query)
    cursor.execute(query)
    receiver_id = cursor.fetchone()
    if receiver_id is None:
        conn.close()
        return "Looks like the user you are looking for is not connected with us though me, Message transfer failed :("
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO PendingMessages(sender_id, receiver_id, timestamp, message) VALUES({}, {}, '{}', '{}');".format(sender_id, receiver_id[0], timestamp, msg)
        cursor.execute(query)
        conn.commit()
        conn.close()
        return "Message sent :)"


def add_skill():
    pass


def register(first_name, last_name, email, password):
    """
    Registers a new user if not exists, otherwise returns an error
    :param first_name: first name of the user
    :param last_name: last name of the user
    :param email: email id of the user
    :param password: password that he wants to set
    :return: Reply
    """
    conn = sqlite3.connect("actions/database/donna.db")
    cursor = conn.cursor()
    email = email.upper()
    query = "SELCT email FROM Users WHERE email = '{}'".format(email)
    if query is not None:
        return [0, "User already exists"]
    else:
        batch, num = email.split('_')
        batch = batch.upper()
        year = num[0:4]
        query = "INSERT INTO Users(first_name, last_name, password, email, batch, year) VALUES('{}', '{}', '{}', {}, {});".format(
            first_name.upper(), last_name.upper(), password, email, batch, year)
        cursor.execute(query)
        query = "SELECT user_id FROM Users WHERE email = '{}'".format(email)
        cursor.execute(query)
        uid = cursor.fetchone()
        conn.commit()
        conn.close()
        return [uid, "User successfully registered"]


def login(email, password):
    """
    Initiates the login process. Returns successful or unsuccessful
    :param email: email of the user
    :param password: password entered by the user
    :return: reply
    """
    conn = sqlite3.connect("actions/database/donna.db")
    cursor = conn.cursor()
    query = "SELECT user_id, email, password FROM Users WHERE email = '{}'".format(email.upper())
    cursor.execute(query)
    data = cursor.fetchone()
    conn.close()

    if data is None:
        return [0, 'User not registered, please register first']
    else:
        if password == data[2]:
            return [int(data[0]), "Sign in successful"]
        else:
            return [0, 'password incorrect']


def show_pending_messages(user_id):
    """
    Function to show pending messages
    :param user_id: user id of the user
    :return: messages
    """
    conn = sqlite3.connect("actions/database/donna.db")
    cursor = conn.cursor()
    query = """SELECT Users.first_name, Users.last_name, PendingMessages.message FROM Users, PendingMessages WHERE 
                Users.user_id = PendingMessages.sender_id AND receiver_id = {};""".format(int(user_id))
    cursor.execute(query)
    messages = cursor.fetchall()
    if messages is None:
        return "No pending messages for you"
    else:
        reply = "Pending Messages\n"
        for msg in messages:
            reply += "From: " + str(msg[0]) + " " + str(msg[1]) + "\nMessage: " + str(msg[2]) + "\n\n"
        return reply

# print(recommend_person("python"))
# print(send_message(1, 'anuraag tiwari', 'call me back'))
print(show_pending_messages(2))