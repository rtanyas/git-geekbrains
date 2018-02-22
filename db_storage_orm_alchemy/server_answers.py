import json
import logging

GOOD_RESPONSE = {"response": 202}

class JIMAnswer(object):

    def server_response(self, sock, storage, data):
        if data["action"] == "add_contact":
            logger.debug("'{}'-request is received to add client '{}'.".format(data["action"], data["user_id"]))
            storage.add_contact(data["user_id"])
#            if storage.get_contact(data["user_id"]):
#                sock.send(json.dumps(GOOD_RESPONSE).encode())
        elif data["action"] == "del_contact":
            sock.send(json.dumps(GOOD_RESPONSE).encode())
        elif data["action"] == "get_contacts":
            pass

    @staticmethod
    def good_response_on_user_contact_request(user_quantity):
        return {
            "response": 202,
            "quantity": user_quantity}

    @staticmethod
    def user_contact(user_id, contact_list):
        return {
            "action": contact_list,
            "user_id": user_id}


logger = logging.getLogger('root')