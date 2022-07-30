import os
import sys
import requests
import json
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent
print(f"POSITION : {BASE_DIR}")
print(sys.argv)
# try:
#     command = [
#         f"curl -s --location --request GET 'https://{sys.argv[1]}/ticker-config-api/' --header 'Authorization: Basic {sys.argv[2]}' --form 'ticker_id={sys.argv[3]}' | jq '.' > {BASE_DIR}/config.json"]
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output = process.stderr.read()
#     exitstatus = process.wait()
#     if exitstatus == 0:
#         pass
#     else:
#         print(output.decode('utf-8'))
# except Exception as e:
#     print(e)
#     exit()


try:
    headers = {
        'Authorization': f'Basic {sys.argv[2]}',
    }

    files = {
        'ticker_id': (None, sys.argv[3]),
    }

    response = requests.get(f'http://{sys.argv[1]}/ticker-config-api/', headers=headers, files=files)



    print(type(response.json()))
    print(json.dumps(response.json(),indent=3))

    with open(f"{BASE_DIR}/config.json", "w") as outfile:
        outfile.write(json.dumps(response.json(), indent=3))
    print("Done")
except Exception as e:
    print(e)
    exit()




with open(f"{BASE_DIR}/config.json", "r") as f:
    conf = json.load(f)

CONFIG = conf

try:
    if bool(CONFIG['static_ticker_logo_name']):
        command = [f"wget -O {BASE_DIR}/media/logo_gtk.png {CONFIG['static_ticker_logo_name']}"]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stderr.read()
        exitstatus = process.wait()
        if exitstatus == 0:
            pass
        else:
            print(output.decode('utf-8'))
except:
    print("Static Logo Not Found")
    pass

try:
    if bool(CONFIG['main_ticker_logo_name']):
        command = [f"wget -O {BASE_DIR}/media/logo.png {CONFIG['main_ticker_logo_name']}"]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stderr.read()
        exitstatus = process.wait()
        if exitstatus == 0:
            pass
        else:
            print(output.decode('utf-8'))
except:
    print("Main Logo Not Found")
    pass


try:
    if bool(CONFIG['moving_ticker_logo_name']):
        command = [f"wget -O {BASE_DIR}/media/myvideo.mp4 {CONFIG['moving_ticker_logo_name']}"]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stderr.read()
        exitstatus = process.wait()
        if exitstatus == 0:
            pass
        else:
            print(output.decode('utf-8'))
except:
    print("Animated Logo Not Found")
    pass

try:
    if bool(CONFIG['emergency_ticker_condition']):
        if CONFIG['emergency_ticker_style'] == "static":
            command = [f"wget -O {BASE_DIR}/media/logo_gtk.png {CONFIG['emergency_ticker_logo_name']}"]
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = process.stderr.read()
            exitstatus = process.wait()
            if exitstatus == 0:
                pass
            else:
                print(output.decode('utf-8'))
        elif CONFIG['emergency_ticker_style'] == "dynamic":
            command = [f"wget -O {BASE_DIR}/media/myvideo.mp4 {CONFIG['emergency_ticker_logo_name']}"]
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = process.stderr.read()
            exitstatus = process.wait()
            if exitstatus == 0:
                pass
            else:
                print(output.decode('utf-8'))
except:
    print("Emergency Logo Not Found")
    pass