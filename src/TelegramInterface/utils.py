#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import time
import os
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import uuid


def parse_yaml(yaml_file):
    """
        Parse yaml file to object and return it
        :param: yaml_file: path to yaml file
        :return: yaml_object
    """
    with open(yaml_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return False


def connect_to_database():
    con = sqlite3.connect('login_data.db')
    return con


def close_connection_to_database(connection):
    connection.commit()
    connection.close()


def create_user_in_database(chat_id):
    # Create connection
    connection = connect_to_database()
    cursor = connection.cursor()
    # Delete entry if existing and create new one
    cursor.execute('REPLACE INTO user VALUES (?,?,?,?)', (chat_id, '', '', 'enter_username'))
    # Close connection
    close_connection_to_database(connection)


def get_user_state_from_database(chat_id):
    # Create connection
    connection = connect_to_database()
    cursor = connection.cursor()
    # Execute SQL query
    cursor.execute('SELECT state FROM user WHERE chat_id=?', (str(chat_id),))
    state = cursor.fetchone()
    if state:
        state = state[0]
    # Close connection
    close_connection_to_database(connection)
    return state


def get_all_registered_users():
    """
    Get all chat_ids from users that are registered
    :return: List of chat_ids
    """
    new_user_list = []
    # Create connection
    connection = connect_to_database()
    cursor = connection.cursor()
    # Execute SQL query
    cursor.execute('SELECT chat_id FROM user WHERE state=?', ('registered',))
    user_list = cursor.fetchall()
    for registered_user in user_list:
        new_user_list.append(registered_user[0])
    # Close connection
    close_connection_to_database(connection)
    return new_user_list


def init_sqlite_table(database_name):
    # Create connection
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    # Execute SQL query
    sql = "CREATE TABLE user(" \
          "chat_id INTEGER PRIMARY KEY)"
    cursor.execute(sql)
    connection.commit()
    # Close connection
    connection.close()
