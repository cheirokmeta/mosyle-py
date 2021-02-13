import requests, json, argparse

def mosyleRequest(body_json):
    # post request settings
    url = 'https://businessapi.mosyle.com/v1/devices'
    token = ''
    headers = { 
        'Content-type': 'application/json', 
        'accesstoken': token
    }
    # body_json is json data from argumentDefinitions
    json_in = body_json
    # send request to api and print results
    response = requests.post(url, json=json_in, headers=headers)
    response_json = response.json()
    dumped_response = json.dumps(response_json, indent=1)
    print(dumped_response)

def argumentDefinitions(command, device):
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
                "deviceudids": device 
            }
        }
        return body
    
    # argument -> function definition map
    handler = {
        'shutdown': shutdownDevice,
        'restart': restartDevice,
        'info': infoDevice,
        }
    
    return handler[command](device)

def main():
    # argparse definition
    parser = argparse.ArgumentParser(description='## Mosyle API wrapper', prog='mosyle', usage='%(prog)s [options] device')
    # command argument definition
    parser.add_argument('--command', help='command to send to target device', type=str, required=True)
    # device argument definition
    parser.add_argument('--device', help='target device', type=str, required=True)
    
    # store parser values in a dictionary
    args = vars(parser.parse_args())
    
    # gets json body for api request based on --command arg
    command_data = argumentDefinitions(args['command'], args['device'])
    
    # send json body to mosyle api request function
    mosyleRequest(command_data)
   
if __name__ == "__main__":
    main()

