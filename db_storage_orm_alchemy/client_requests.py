import json
import time


def add_contact_request(sock, login):
    request = {
        "action": "add_contact",
        "user_id": login,
        "time": int(time.time())
    }
    sock.send(json.dumps(request).encode())

def del_contact_request(sock, login):
    request = {
        "action": "del_contact",
        "user_id": login,
        "time": int(time.time())
    }
    sock.send(json.dumps(request).encode())

def get_all_contacts(sock):
    request = {
        "action": "get_contacts",
        "time": int(time.time())
   }
    sock.send(json.dumps(request).encode())
