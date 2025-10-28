# This is an example code for testing ha backup upload endpoint. 
import hashlib
import requests
import os 
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trigger a backup via fleet assistant API"
    )
    parser.add_argument("--FleetAssistantServerIP", required=True, type=str)
    args = parser.parse_args()

    FleetAssistantServerIP = args.FleetAssistantServerIP

    BackupPATH = ""
    FleetAssistantServerIP = "" 

    file_path = "/data/fleet-assistant-connector-dev/changeme.tar"
    url = "http://localhost:8000/ha_upload_backup"

    # Calculate hash before sending
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    expected_hash = sha256.hexdigest()

    headers = {
        "X-Filename": os.path.basename(file_path),
        "X-Checksum-Sha256": expected_hash,
    }

    with open(file_path, "rb") as f:
        r = requests.post(url, data=f, headers=headers)
 
    print(r.json())
