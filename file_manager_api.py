import requests
import json

class Client:

    def __init__(self, server_url, username, password):
        self.url = server_url

        self.username = username

        self.password = password

        search = json.loads(requests.post(url=server_url + "/search",
                                          data=json.dumps({"cred": "username", "con": username})).text)

        # dionysus: Did you know that id is what makes session database and users database related?
        # athena: Even I did not know that!

        if len(search["result"]) != 1:
            raise Exception("user not found")

        try:
            cre = json.loads(requests.post(url=server_url + "/authenticate",
                                           data=json.dumps({"username": username, "passwd": password})).text)

            self.id, self.session_id = cre["id"], cre["session_id"]

            self.cookies = {"id":self.id, "session_id":self.session_id}

        except:

            raise Exception("something went wrong")



    def read_file(self, file):

        return requests.post(url=self.url + "/file_manager",
                             data=json.dumps({"mode":"read_file","dir":self.id, "file":file}),
                             cookies=self.cookies).text

    def list_files(self):

        return json.loads(requests.post(url=self.url + "/file_manager",
                                        data=json.dumps({"mode":"list_files","dir":self.id}),
                                        cookies=self.cookies).text)["files"]


    def write_file(self, file, content = ""):

        requests.post(url=self.url + "/file_manager",
                             data=json.dumps({"mode": "write_file", "dir": self.id, "file": file, "content":content}),
                             cookies=self.cookies)

