import socket
import json
from utils.config import config

class youki:
    def __init__(self,path):
        self.config=config(path)
        self.talker={
            "talker_list":[],
            "nickname":"id"
        }
        self.HOST = 'localhost'
        self.PORT = 8080

    def get_request(self,username,identity,msg):
        request_data=self.create_request(username,identity,msg)
        response=self.send_request(request_data)
        return response


    def create_request(self,username,identity,msg):
        # Create a JSON request for a 'chat' event with 'chisadou' identity
        request = {
            "event_type": "chat_qq_bot",
            "chat_qq_bot": {
                "identity": identity,
                "message": {
                    "chat_name": username,
                    "content": msg
                }
            }
        }
        return json.dumps(request)

    def send_request(self,request_data):
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                # Connect to the server
                client_socket.connect((self.HOST, self.PORT))
            
                # Send the request data
                client_socket.sendall(request_data.encode('utf-8'))

            
                # Receive the response from the server
                response = client_socket.recv(4096).decode('utf-8')


                return response
        
            except Exception as e:
                print(f"Error: {e}")
