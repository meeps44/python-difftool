import urllib.request, json, os, logging, difflib, sys
from pathlib import Path
from datetime import date

def listToString(input_list:list) -> str:
    # initialize an empty string
    str1 = " "

    str1 = str1.join(input_list)
    str1 = str1.replace(" ", "\n")
    return str1

# Azure Norway IP-ranges
ip_ranges = ["AzureContainerRegistry.NorwayEast",
"AzureContainerRegistry.NorwayWest",
"AzureContainerRegistry.NorthEurope",
"Storage.NorwayEast",
"Storage.NorwayWest",
"ServiceBus.NorwayEast",
"ServiceBus.NorwayWest"]

#TODO: Get URL to update dynamically
ms_url = https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20220110.json
# filename = ms_url.rsplit('/', 1)[-1]
today = date.today().strftime("%b-%d-%Y")
filepath = "/var/www/html/"
filename = f"ServiceTags_Public_{today}.json"
# filename = filepath + filename

# Download json-file from Microsoft
try:
    with urllib.request.urlopen(ms_url) as url:
        data = json.loads(url.read().decode())
except urllib.error.HTTPError:
    logging.warning(f"\tHTTP Error 404: Site {ms_url} Not Found")
    exit(1)
except urllib.error.URLError:
    logging.warning(f"\tURLError: Malformed URL {ms_url}")
    exit(1)

json_object = json.dumps(data, indent = 4)

# Write to file on disk
with open(filename, "w") as file:
    for x in data['values']:
        if (x['name'].__eq__(ip_ranges[0])):
            file.write(listToString(x['properties']['addressPrefixes']))
        elif (x['name'].__eq__(ip_ranges[1])):
            file.write(listToString(x['properties']['addressPrefixes']))
        elif (x['name'].__eq__(ip_ranges[2])):
            file.write(listToString(x['properties']['addressPrefixes']))
        elif (x['name'].__eq__(ip_ranges[3])):
            file.write(listToString(x['properties']['addressPrefixes']))
        elif (x['name'].__eq__(ip_ranges[4])):
            file.write(listToString(x['properties']['addressPrefixes']))
        elif (x['name'].__eq__(ip_ranges[5])):
            file.write(listToString(x['properties']['addressPrefixes']))
        elif (x['name'].__eq__(ip_ranges[6])):
            file.write(listToString(x['properties']['addressPrefixes']))


# TODO: Check if old file exists at {filepath}
oldfile = True

# If oldfile exists: 
# Check file differences and write Slack-message if state changed

#file1 = open('ServiceTags_Public_20220110.json', 'r').readlines()
#file2 = open('ServiceTags_Public.json', 'r').readlines()
if oldfile:
	old_file = filename
	new_file = filename
	with open(new_file, "r").readlines() as f1, open(old_file, "r").readlines() as f2:
		delta = difflib.unified_diff(f1, f2, old_file.name, new_file.name)
		sys.stdout.writelines(delta)

#eksisterende = ["192.168.0.0","192.168.1.0"]
#ny_nedlastet = ["192.168.0.0","192.168.2.0"]
#print("Disse er fjernet: " + str(set (file1) - set(file2)))
#print("Disse er lagt til: " + str(set (file2) - set(file1)))

# Check file size (experimental)
try:
    filesize = os.path.getsize(filename)
    if (filesize < 1000):
        logging.warning(f"\tFile size less than 1000! File size should be at least 1000")
    print(f"File size {filename} (bytes):\n{filesize}")
except FileNotFoundError:
    print(f"FileNotFoundError: {filename} not found")