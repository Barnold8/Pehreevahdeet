# Classes here to provide default values and be edited when config is read. If config fails to read, the defaults here work in the program's favour
import json
import jsonschema
from jsonschema import validate

class Screen:
    MONITOR_INDEX        = 0
    PREFER_FIRST_MONITOR = False

    def load(content:dict):
        Screen.MONITOR_INDEX        = content["monitor_index"] if content["monitor_index"] > 0 else 0
        Screen.PREFER_FIRST_MONITOR = content["prefer_first_monitor"]
            
class Image:
    SCREENSHOT_AREA      = [1920,1080]
    X_OFFSET             = 0
    Y_OFFSET             = 0
    THRESHOLD            = 50.0

    def load(content:dict):
        area = content["screenshot_area"]
        for coord in area:
            if coord < 0:
                area = [1920,1080]
                break

        Image.SCREENSHOT_AREA = area
        
        Image.X_OFFSET        = content["x_offset"] if content["x_offset"] > 0 else 0
        Image.Y_OFFSET        = content["y_offset"] if content["y_offset"] > 0 else 0
        Image.THRESHOLD       = content["image_difference_threshold"] if content["image_difference_threshold"] > 0 else 50.0

class Language:

    TARGET_LANGUAGE = 'en'

    def load(content:dict):

        try:
            with open(".config/locales","r") as file:
                accepted_languages = file.readlines()
        except FileNotFoundError as FNFE:
            print("Error: Could not load locales file. Defaulting to 'en'")
            accepted_languages = ['en']

        Language.TARGET_LANGUAGE = content["target_language"] if content["target_language"] in accepted_languages else 'en' # default to english


class System:
    POLL_RATE            = 50 
    API_COOLDOWN         = True
    CLEAR_TERMINAL       = True

    def load(content:dict):
        System.POLL_RATE      = content["poll_rate"] if content["poll_rate"] > 0 else 50
        System.API_COOLDOWN   = content["api_cooldown"]
        System.CLEAR_TERMINAL = content["clear_terminal"]

class Dev:
    SHOW_WARNINGS        = True
    SHOW_SCREENGRABS     = False
    SHOW_SETTINGS        = False
    LIMITED_RUN          = False
    DEBUG_LANGUAGE       = False
    DEBUG_WATCHDOG       = False
    DEBUG_IMAGE          = False
    RUN_COUNT            = 2

    def load(content:dict):
        Dev.SHOW_WARNINGS    = content["show_warnings"]
        Dev.SHOW_SCREENGRABS = content["show_screengrabs"]
        Dev.SHOW_SETTINGS    = content["show_settings"]
        Dev.DEBUG_LANGUAGE   = content["debug_language"]
        Dev.DEBUG_WATCHDOG   = content["debug_watchdog"]
        Dev.DEBUG_IMAGE      = content["debug_image"]
        Dev.LIMITED_RUN      = content["limited_run"]
        Dev.RUN_COUNT        = content["run_count"] if content["run_count"] > 0 else 1

def validateConfig(content: dict)->bool:
    
    try:
        with open(".config/config.json") as file:
            schema = json.load(file)
    except FileNotFoundError as FNFE:
        print(f"Could not find config file. Reverting to default settings")
        return False
       
    try:
        validate(instance=content,schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Config file is invalid\nError:{"="*46}\n\n{e}\n\nSkipping config load...")
        return False

def loadConfig(path:str) -> None:

    try:

        with open(path,"r") as file:
            content = json.load(file)

            validateConfig(content)
             
            # Screen

            Screen.load(content["screen"])

            # Image

            Image.load(content["image"])

            # Language

            Language.load(content["language"])

            # System

            System.load(content["system"])

            # Dev

            Dev.load(content["dev"])

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
    Prefer  First Monitor:  {Screen.PREFER_FIRST_MONITOR}

Image
{line}

    Screenshot area:        {Image.SCREENSHOT_AREA[0]}x{Image.SCREENSHOT_AREA[1]}
    X offset                {Image.X_OFFSET}
    Y offset                {Image.Y_OFFSET}
    Threshold               {Image.THRESHOLD}

Language
{line}   

    Target Language:        {Language.TARGET_LANGUAGE}

System

    Poll  Rate:             {System.POLL_RATE}
    API   Cooldown          {System.API_COOLDOWN}
    Clear Terminal          {System.CLEAR_TERMINAL}
Dev
{line}

    SHOW_WARNINGS:          {Dev.SHOW_WARNINGS}
    SHOW_SCREENGRABS:       {Dev.SHOW_SCREENGRABS}
    SHOW_SETTINGS:          {Dev.SHOW_SETTINGS}
    LIMITED_RUN:            {Dev.LIMITED_RUN}
    DEBUG_LANGUAGE          {Dev.DEBUG_LANGUAGE}
    DEBUG_WATCHDOG          {Dev.DEBUG_WATCHDOG}
    DEBUG_IMAGE             {Dev.DEBUG_IMAGE}
    RUN_COUNT:              {Dev.RUN_COUNT}
""")


