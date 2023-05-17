import asyncio
import json

DOGS_LIST = [
    "Akita",
    "Borzoi",
    "Chow",
    "otterhound",
    "ovcharka", 
    "papillon",
    "pekinese",
    "pembroke",
    "rottweiler",
    "saluki",
    "samoyed",
    "schipperke",
    "schnauzer",
    "basenji",
    "beagle",
    "bluetick",
    "borzoi",
    "bouvier",
    "boxer",
    "brabancon",
    "briard",
    "buhund",
]

BASE_URL="https://dog.ceo/api/breed/"
BASE_RESOURCE="/images/random"

CURL="/usr/bin/curl"
CURL_SILENT_OPTION="-s"

InfoResponse = dict[str, str]

async def get_info(url: str) -> InfoResponse:
    """Send HTTP requests"""
    print("[DEBUG] Fetching {}".format(url))
    response = {}

    process = await asyncio.create_subprocess_shell(
        " ".join([CURL, CURL_SILENT_OPTION, url]),
        stdout=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    response["stdin"] = url
    response["stdout"] = json.loads(stdout)
    response["stderr"] = stderr
    return response

def report(output_list: list):
    """"Report output presentation"""

    for item in output_list:
        item_name :str = item["stdin"].split("/")[5]
        print(item_name)

        if item["stderr"] is not None:
            print("\t [ERROR]", item["stderr"])
            next
        
        print("\t", item["stdout"]["message"])


async def execute_requests(options_list):
    """Async function to final format the HTTP request and send it"""

    endpoints = ["{}{}{}".format(BASE_URL, item.lower(), BASE_RESOURCE) for item in options_list]

    response_list = await asyncio.gather(
        *[get_info(endpoint) for endpoint in endpoints]
    )

    report(response_list)

def run(program):
    """Use asyncio's power to run parallel requests"""
    
    return asyncio.run(program)

if __name__ == "__main__":
    run(execute_requests(DOGS_LIST))