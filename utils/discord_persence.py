from pypresence import Presence
from pypresence.exceptions import InvalidPipe
import time

def run_persence(current_version: str):
    try:
        RPC = Presence("EDIT-HERE")  # add your RPC ID
        RPC.connect()
        RPC.update(
            state=f"Version {current_version}", 
            details="python-bot-hyper-boilerplate", 
            start=time.time(), 
            large_image="EDIT-HERE",  # add your RPC image name
            large_text="EDIT-HERE", 
            small_image="EDIT-HERE", 
            small_text="EDIT-HERE"
        )
    except InvalidPipe:
        pass