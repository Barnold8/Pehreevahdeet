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
    RUN_COUNT            = 2


def loadConfig(path:str) -> None:

    try:

        with open(path,"r") as file:
            content = json.load(file)   
            # Screen

            Screen.MONITOR_INDEX        = content["screen"]["monitor_index"]
            Screen.PREFER_FIRST_MONITOR = content["screen"]["prefer_first_monitor"]
            
            # Image

            area = content["image"]["screenshot_area"]
            area = area.split("x")
            area = [int(x) for x in area]

            Image.SCREENSHOT_AREA = area
            Image.X_OFFSET        = content["image"]["x_offset"]
            Image.Y_OFFSET        = content["image"]["y_offset"] 

            # Settings

            Language.TARGET_LANGUAGE = content["language"]["target_language"]

            # System

            System.POLL_RATE     = content["system"]["poll_rate"]

            # DeImage.THRESHOLDv

            Dev.SHOW_WARNINGS    = content["dev"]["show_warnings"]
            Dev.SHOW_SCREENGRABS = content["dev"]["show_screengrabs"]
            Dev.SHOW_SETTINGS    = content["dev"]["show_settings"]
            Dev.DEBUG_LANGUAGE   = content["dev"]["debug_language"]
            Dev.LIMITED_RUN      = content["dev"]["limited_run"]
            Dev.RUN_COUNT        = content["dev"]["run_count"]
        
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


