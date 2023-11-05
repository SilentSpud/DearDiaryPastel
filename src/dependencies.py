import os
from urllib.request import urlopen
from zipfile import ZipFile
import json

def setup_jpexs():
    # if jpexs is already installed, don't do anything
    if os.path.exists("ffdecpy/ffdec/"):
        return

    # Check the GitHub API for the latest release
    response = urlopen("https://api.github.com/repos/jindrapetrik/jpexs-decompiler/releases/latest")

    if response.status != 200:
        raise Exception(f"Error Checking GitHub API for JPEXS: {response.status}, {response.reason}")

    latest = json.loads(response.read().decode('utf-8'))
    version = latest['tag_name'].replace("version", "")
    url = None
    for asset in latest['assets']:
        if f"ffdec_lib_{version}.zip" in asset['name']:
            url = asset['browser_download_url']
            break
    if not url:
        raise Exception("No JPEXS zip was found in the latest release from the GitHub API")

    # Fetch the zip file, and extract it
    response = urlopen(url)
    with open("ffdec.zip", "wb") as f:
        f.write(response.read())
    with ZipFile("ffdec.zip", "r") as zip:
        zip.extractall("ffdecpy/ffdec/")
    os.remove("ffdec.zip")