import requests, json
from json2html import *
import argparse

def mosyle_handler(mosyleList):
  mosyleCommand = str(mosyleList[0][0])
  phoneUUID = str(mosyleList[0][1])
  def restart_device(mosyleCommand, phoneUUID):
    url = 'https://businessapi.mosyle.com/v1/devices'
    headers = { 
    'Content-type': 'application/json', 
    'accesstoken': '' }
    body = { 
    "operation": mosyleCommand+'_devices', 
    "devices": phoneUUID 
    }
    response = requests.post(url, json=body, headers=headers)
    response_json = response.json()
    dumped_response = json.dumps(response_json, indent=1)
    return dumped_response
  response = restart_device(mosyleCommand, phoneUUID)
  return response

def main():
    # Argument definition
    parser = argparse.ArgumentParser(
        description='Mosyle API wrapper for actions on iOS devices',
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
    mosyleList = []
    for k,v in args.items():
        if v == True:
            params = [k, args['device']]
            mosyleList.append(params)
    out = mosyle_handler(mosyleList)
    print(out)
main()