# Classes here to provide default values and be edited when config is read. If config fails to read, the defaults here work in the program's favour

class Screen:
    MONITOR_INDEX        = 0
    PREFER_FIRST_MONITOR = False

class Image:
    SCREENSHOT_AREA      = [1920,1080]

class Language:
    TARGET_LANGUAGE      = 'en'

class Dev:
    SHOW_WARNINGS        = False
    SHOW_SCREENGRABS     = False
    SHOW_SETTINGS        = False
    RUN_COUNT            = 2


def loadConfig(path:str) -> None:

    try:

        with open("path","r") as file:
            content = json.load()
    
            # Screen

            Screen.MONITOR_INDEX        = content["screen"]["monitor_index"]
            Screen.PREFER_FIRST_MONITOR = content["screen"]["prefer_first_monitor"]
            
            # Image

            area = content["image"]["screenshot_area"]
            area = area.split("x")

            Image.SCREENSHOT_AREA = area 

            # Settings

            Language.TARGET_LANGUAGE = content["language"]["target_language"]

            # Dev

            Dev.SHOW_WARNINGS    = content["dev"]["show_warnings"]
            Dev.SHOW_SCREENGRABS = content["dev"]["show_screengrabs"]
            Dev.SHOW_SETTINGS    = content["dev"]["show_settings"]
            Dev.RUN_COUNTS       = contents["dev"]["run_counts"]
        


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

Language
{line}   

    Target Language:        {Language.TARGET_LANGUAGE}

Dev
{line}

    SHOW_WARNINGS:          {Dev.SHOW_WARNINGS}
    SHOW_SCREENGRABS:       {Dev.SHOW_SCREENGRABS} 
    SHOW_SETTINGS:          {Dev.SHOW_SETTINGS}
    RUN_COUNT:              {Dev.RUN_COUNT}
""")


