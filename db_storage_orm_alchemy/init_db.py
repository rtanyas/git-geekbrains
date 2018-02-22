import sqlite3
import os

import constants


def init_database(database):
    artifact_folder = constants.ARTIFACTS_FOLDER_NAME
    if not os.path.exists(artifact_folder): os.makedirs(artifact_folder)
    conn = sqlite3.connect(os.path.join(artifact_folder, database))
    conn.isolation_level = None
    cursor = conn.cursor()
    if database == constants.DB_SERVER:
        cursor.executescript("""
            drop table if exists client;
            drop table if exists client_details;
            drop table if exists contact_list;
            create table client (gid integer primary key autoincrement, login text unique, birthday date); 
            create table client_details (gid integer primary key autoincrement, login_time datetime, address text, client_id integer references client (gid));  
            create table contact_list (gid integer primary key autoincrement, client_id text unique);       
        """)
    elif database == constants.DB_CLIENT:
        cursor.executescript("""
        drop table if exists messages;
        create table messages (gid integer primary key autoincrement, from_client integer, to_client integer, message text); 
        """)
    conn.commit()