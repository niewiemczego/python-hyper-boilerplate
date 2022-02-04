import os
import ctypes
from typing import Dict
from utils.log import color

def set_title(text: str, current_version: str):
    ctypes.windll.kernel32.SetConsoleTitleW(f"python-bot-hyper-boilerplate [{current_version}] | {text}")

def bot_info(current_version: str, license_data: Dict, license_key: str):
    print(f"Version:    {color(current_version)}".center(os.get_terminal_size().columns), flush=True)
    print(f"Welcome back       {color(license_data['user']['discord']['username'])}{color('#')}{color(license_data['user']['discord']['discriminator'])}!\n")
    print(f"Discord:	   {color(license_data['user']['discord']['username'])}{color('#')}{color(license_data['user']['discord']['discriminator'])}")
    print(f"License: 	   {color(license_key)}")
    print(f"License Type:	   {color(license_data['plan']['name'])}")