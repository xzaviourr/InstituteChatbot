import sqlite3


def create_users_table():
    """
    Users - Data of all the users are stored in the
    :return: None
    """
    conn = sqlite3.connect("donna.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Users;")
    cursor.execute("""CREATE TABLE Users(
                    user_id integer Primary key,
                    first_name text,
                    last_name text,
                    password text,
                    email text,
                    batch text,
                    year integer);""")
    conn.commit()
    conn.close()


def create_skills_table():
    """
    Skills - Mapping of skill name with skill id
    :return: None
    """
    conn = sqlite3.connect("donna.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Skills;")
    cursor.execute("""CREATE TABLE Skills(
                    skill_id integer Primary key,
                    skill_name text);""")
    conn.commit()
    conn.close()


def create_userskills_table():
    """
    UserSkills - Mapping of users with their skills
    :return: None
    """
    conn = sqlite3.connect("donna.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS UserSkills;")
    cursor.execute("""CREATE TABLE UserSkills(
                    user_id integer,
                    skill_id integer,
                    timestamp datetime);""")

    conn.commit()
    conn.close()


def create_pendingmessages_table():
    """
    PendingMessages - Messages that are still pending to be deliverd to the correct user
    :return: None
    """
    conn = sqlite3.connect("donna.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS PendingMessages;")
    cursor.execute("""CREATE TABLE PendingMessages(
                    message_id integer Primary key,
                    sender_id integer,
                    receiver_id integer,
                    timestamp datetime,
                    message text);""")
    conn.commit()
    conn.close()


# create_users_table()
# create_skills_table()
# create_userskills_table()
# create_pendingmessages_table()