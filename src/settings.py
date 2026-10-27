# Classes here to provide default values and be edited when config is read. If config fails to read, the defaults here work in the program's favour
import json

class Screen:
    MONITOR_INDEX        = 0
    PREFER_FIRST_MONITOR = False

class Image:
    SCREENSHOT_AREA      = [1920,1080]
    X_OFFSET             = 0
    Y_OFFSET             = 0
    THRESHOLD            = 50

class Language:
    TARGET_LANGUAGE      = 'en'

class System:
    POLL_RATE            = 50 

class Dev:
    SHOW_WARNINGS        = True
    SHOW_SCREENGRABS     = False
    SHOW_SETTINGS        = False
    LIMITED_RUN          = False
    DEBUG_LANGUAGE       = False
    DEBUD_WATCHDOG       = False
    RUN_COUNT            = 2


def loadConfig(path:str) -> None:

    try:

        with open(path,"r") as file:
            content = json.load(file)   
            
            
            # Screen

            screen = content["screen"]

            Screen.MONITOR_INDEX        = screen["monitor_index"]
            Screen.PREFER_FIRST_MONITOR = screen["prefer_first_monitor"]
            
            # Image

            image = content["image"]

            area = image["screenshot_area"]
            area = area.split("x")
            area = [int(x) for x in area]

            Image.SCREENSHOT_AREA = area
            Image.X_OFFSET        = image["x_offset"]
            Image.Y_OFFSET        = image["y_offset"] 

            # Language

            language = content["language"]

            Language.TARGET_LANGUAGE = language["target_language"]

            # System

            system = content["system"]

            System.POLL_RATE     = system["poll_rate"]
            System.API_COOLDOWN  = system["api_cooldown"]

            # Dev

            dev = content["dev"]

            Dev.SHOW_WARNINGS    = dev["show_warnings"]
            Dev.SHOW_SCREENGRABS = dev["show_screengrabs"]
            Dev.SHOW_SETTINGS    = dev["show_settings"]
            Dev.DEBUG_LANGUAGE   = dev["debug_language"]
            Dev.DEBUG_WATCHDOG   = dev["debug_watchdog"]
            Dev.LIMITED_RUN      = dev["limited_run"]
            Dev.RUN_COUNT        = dev["run_count"]
        
    except FileNotFoundError as FNFE:
        if Dev.SHOW_WARNINGS:
            print(f"loadConfig | Warning: {path} could not be found or the file could not be found. Program settings are staying as their default.")

def printSettings():

    line_amount = 42
    line = "="*line_amount  
    print(
    f"""
Screen
{line}

    Monitor Index:          {Screen.MONITOR_INDEX}
    Prefer First Monitor:   {Screen.PREFER_FIRST_MONITOR}

Image
{line}

    Screenshot area:        {Image.SCREENSHOT_AREA[0]}x{Image.SCREENSHOT_AREA[1]}
    X offset                {Image.X_OFFSET}
    Y offset                {Image.Y_OFFSET}
    Threshold               {Image.THRESHOLD}

Language
{line}   

    Target Language:        {Language.TARGET_LANGUAGE}

Dev
{line}

    SHOW_WARNINGS:          {Dev.SHOW_WARNINGS}
    SHOW_SCREENGRABS:       {Dev.SHOW_SCREENGRABS}
    SHOW_SETTINGS:          {Dev.SHOW_SETTINGS}
    LIMITED_RUN:            {Dev.LIMITED_RUN}
    Debug  Language         {Language.DEBUG_LANGUAGE}
    RUN_COUNT:              {Dev.RUN_COUNT}
""")


