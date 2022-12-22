import json
import os
from webbrowser import open as webopen

import httpx

current_version = "v0.1.2" 

print("\nPIPUpdater | v0.1.2 | Made by AsuxAX")

# Update checking
print("\n[*] Checking for updates...")
try:
    latest_version = httpx.get("https://api.github.com/repos/AsuxAX/PIPUpdater/releases/latest").json()["tag_name"]
except Exception as err:
    print(f"[!] An error occurred while checking for the latest version. Skipping update checking...\n[?] Error: {err.__class__.__name__}: {err}")
    latest_version = None
if latest_version:
    if current_version != latest_version:
        print(f"[!] Update found! {current_version} --> {latest_version}")
        while True:
            choice = input("[?] Do you want to be redirected to the GitHub page to download the latest version? (y/n) ").lower()
            if choice == "y":
                webopen("https://github.com/AsuxAX/PIPUpdater/releases/latest")
                break
            elif choice == "n":
                break
            else:
                print("Invalid option.")
    else:
        print("[!] No update found!")

# PIP package update checking
print("\n[*] Checking for outdated packages...")
outdated_packages = json.loads(os.popen("python -m pip list --outdated --format json").read())
if len(outdated_packages) != 0:
    while True:
        choice = input(f"[!] Found {len(outdated_packages)} outdated package(s).\n[?] Do you want to continue? (y/n) ").lower()
        if choice == "y":
            # PIP package updating
            for package_dict in outdated_packages:
                print("\n[*] Updating", package_dict["name"], "to version", package_dict["latest_version"], "from version", package_dict["version"], "\b...")
                package_update_output = os.popen("python -m pip install -U " + package_dict["name"]).read()
                if "ERROR" in package_update_output:
                    print("[!] An error occurred while trying to update the package.\n[?] Check if the package is installed despite an error by pip using: python -m pip list")
                else:
                    print("[!] Successfully updated", package_dict["name"], "to version", package_dict["latest_version"], "from version", package_dict["version"], "\b!")
            print("\n[!] Updated all packages!")
            input("\nPress any key to exit the program.")
            break
        elif choice == "n":
            input("\nPress any key to exit the program.")
            break
        else:
            print("Invalid option.")
else:
    print("[!] Found no outdated packages.")
    input("\nPress any key to exit the program.")
