import os
import sys
import requests
import json
from pathlib import Path
import subprocess

BASE_DIR = "/home/guest/.tickerv2"
print(f"POSITION : {BASE_DIR}")
print(sys.argv)


try:
    headers = {
        'tickerToken': sys.argv[2],
    }

    files = {
        'ticker_id': (None, sys.argv[3]),
    }

    response = requests.get(f'https://{sys.argv[1]}/ticker-config-api', headers=headers, files=files)
    print(type(response.status_code))
    print(response.status_code)

    if response.status_code != 200:
        print(response.text)
        exit(1)

    print(type(response.json()))
    print(json.dumps(response.json(),indent=3))

    with open(f"{BASE_DIR}/config.json", "w") as outfile:
        outfile.write(json.dumps(response.json(), indent=3))
    print("Done")
except Exception as e:
    print(e)
    exit(1)




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
    if CONFIG['emergency_ticker_condition']:
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
