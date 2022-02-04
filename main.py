
from typing import List, Dict, Set
import os
import sys
import time
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import re
import uuid

from utils.authorization import get_license, update_license
from utils.log import color, info_log, error_log
from utils.discord_persence import run_persence
from utils.utils import set_title, bot_info

clear = lambda: os.system('cls')

__version__ = '0.0.0.1'

class PythonHyperBoilerplate:
    def __init__(self, settings_data: List):
        self.api_key = 'YOUR-HYPER-API-KEY'  # it's better to store it on server side
        self.license_key = settings_data['Settings'][0]['license_key']
        self.success_webhook = settings_data['Settings'][0]['success_webhook']
        self.license_data = get_license(self.api_key, self.license_key)
        self.discord_name = f"{self.license_data['user']['discord']['username']}#{self.license_data['user']['discord']['discriminator']}"
        run_persence(__version__)

    def main_menu(self):
        clear()
        set_title("Main Menu", __version__)
        bot_info(__version__, self.license_data, self.license_key)
        stores = ["Mode1", "Mode2", "Mode3"] 
        for i in range(len(stores)):
            print(f"[{color(i)}] {stores[i]}", end = "\n")
        user_decision = input(f"\n[{color('Bot')}] Choose Number(0-{len(stores)-1}) {color('>')} ")
        if user_decision == '0':
            pass
            # execute_mode1()
        elif user_decision == '1':
            pass
            # execute_mode2()
        elif user_decision == '2':
            pass
            # execute_mode3()
        else:
            self.main_menu()

    def check_license(self):
        set_title("Checking license", __version__)
        info_log("Checking license...")
        if self.license_data:
            hardware_id = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            if self.license_data.get('metadata', {}) == {}:
                updated = update_license(self.api_key, self.license_key, hardware_id)
                if updated:
                    self.main_menu()
                else:
                    os.system('pause >nul')
            else:
                current_hwid = self.license_data.get('metadata', {}).get('hwid', '')
                if current_hwid == hardware_id:
                    self.main_menu()
                else:
                    error_log("License is already in use on another machine. Please reset your key and try again")
                    os.system('pause >nul')
        else:
            error_log("License not found")
            os.system('pause >nul')


if __name__ == "__main__":
    try:
        os.system('mode con cols=150 lines=35')
        with open(f'{str(os.getcwd())}\\settings.json') as jsonFile:
            settings_data = json.load(jsonFile)
        PythonHyperBoilerplate(settings_data).check_license()
    except json.decoder.JSONDecodeError as err:
        error_log(f"\nFailed to launch bot due to misconfigured settings.json\n{err}")
        os.system('pause >nul')
    except KeyboardInterrupt as err:
        error_log("\nBot was closed manually")
        os.system('pause >nul')