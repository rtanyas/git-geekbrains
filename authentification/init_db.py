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
            create table if not exists auth (uid integer primary key autoincrement, user_login text not null, user_level integer not null, pass_hash char(64) not null);
           
            create table if not exists client (gid integer primary key autoincrement, login text unique, birthday date); 
            create table if not exists client_details (gid integer primary key autoincrement, login_time datetime, address text, client_id integer references client (gid));  
            create table if not exists contact_list (gid integer primary key autoincrement, client_id text unique);       
        """)
    elif database == constants.DB_CLIENT:
        cursor.executescript("""
        drop table if exists messages;
        drop table if exists client_contact_list;
        create table if not exists messages (gid integer primary key autoincrement, from_client integer, to_client integer, message text); 
        create table if not exists client_contact_list (gid integer primary key autoincrement, contact text unique);
        """)
    conn.commit()

