import requests, json, argparse
from json2html import *

def mosyle_handler(body_json):
    url = 'https://businessapi.mosyle.com/v1/devices'
    headers = { 
        'Content-type': 'application/json', 
        'accesstoken': ''
    }
    json_in = body_json
    response = requests.post(url, json=json_in, headers=headers)
    response_json = response.json()
    dumped_response = json.dumps(response_json, indent=1)
    return dumped_response

def shutdownDevice(device):
    body = {
        "operation": 'shutdown_devices',
        "devices": device
        }
    return body
    
def restartDevice(device):
    body = {
        "operation": 'restart_devices',
        "devices": device
        }
    return body

def infoDevice(device):
    body = { 
        "operation": "list", 
        "options":
        {
            "os": "ios",
            'deviceudids': device 
        }
    }
    return body

def main():
    # Argument definition
    parser = argparse.ArgumentParser(
        description='## Mosyle API wrapper',
        prog='mosyle', 
        usage='%(prog)s [options] device')
    # Restart argument
    parser.add_argument(
        '--restart', 
        help='restart device', 
        action='store_true')
    # Shutdown argument
    parser.add_argument(
        '--shutdown', 
        help='shutdown device', 
        action='store_true')
    # Info argument
    parser.add_argument(
        '--info', 
        help='get device info', 
        action='store_true')
    # Device argument
    parser.add_argument(
        'device', 
        metavar='device')
    
    args = vars(parser.parse_args())
    
    handler = {
        'shutdown': shutdownDevice, 
        'restart': restartDevice,
        'info': infoDevice
    }
    
    for key,value in args.items():
        if value == True:
          command = key
          device = args['device']
    command_data = handler[command](device)
    command_results = mosyle_handler(command_data)
    print(command_results)
main()
