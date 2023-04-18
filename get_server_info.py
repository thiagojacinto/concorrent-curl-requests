import subprocess
import json

list = [
    "Akita",
    "Borzoi",
    "Chow",
    "otterhound",
    "ovcharka", 
    "papillon",
    "pekinese",
    "pembroke"
]

BASE_URL="https://dog.ceo/api/breed/"
BASE_RESOURCE="/images/random"
CURL="/usr/bin/curl"
CURL_SILENT_OPTION="-s"

def execute_requests():
    """
    Execute CURL process within a simple Python script. 
    
    Handle HTTP requests and responses using curl inside of a Python script.
    """

    api_output = {}
    for item in list:
        
        api_output[item] = subprocess.run(
            [CURL, CURL_SILENT_OPTION, f"{BASE_URL}{item.lower()}{BASE_RESOURCE}"],
            text=True,
            stdout=subprocess.PIPE
            )

    for item, response in api_output.items():    
        output = json.loads(response.stdout)
        print("- {}:  {}".format(item, output["message"]))
    
if __name__ == "__main__":
    execute_requests()
    