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

    accepted_languages = [ # todo load this from a file
        "aa",
        "ab",
        "ae",
        "af",
        "ak",
        "am",
        "an",
        "ar",
        "as",
        "av",
        "ay",
        "az",
        "ba",
        "be",
        "bg",
        "bi",
        "bm",
        "bn",
        "bo",
        "br",
        "bs",
        "ca",
        "ce",
        "ch",
        "co",
        "cr",
        "cs",
        "cu",
        "cv",
        "cy",
        "da",
        "de",
        "dv",
        "dz",
        "ee",
        "el",
        "en",
        "eo",
        "es",
        "et",
        "eu",
        "fa",
        "ff",
        "fi",
        "fj",
        "fo",
        "fr",
        "fy",
        "ga",
        "gd",
        "gl",
        "gn",
        "gu",
        "gv",
        "ha",
        "he",
        "hi",
        "ho",
        "hr",
        "ht",
        "hu",
        "hy",
        "hz",
        "ia",
        "id",
        "ie",
        "ig",
        "ii",
        "ik",
        "io",
        "is",
        "it",
        "iu",
        "ja",
        "jv",
        "ka",
        "kg",
        "ki",
        "kj",
        "kk",
        "kl",
        "km",
        "kn",
        "ko",
        "kr",
        "ks",
        "ku",
        "kv",
        "kw",
        "ky",
        "la",
        "lb",
        "lg",
        "li",
        "ln",
        "lo",
        "lt",
        "lu",
        "lv",
        "mg",
        "mh",
        "mi",
        "mk",
        "ml",
        "mn",
        "mr",
        "ms",
        "mt",
        "my",
        "na",
        "nb",
        "nd",
        "ne",
        "ng",
        "nl",
        "nn",
        "no",
        "nr",
        "nv",
        "ny",
        "oc",
        "oj",
        "om",
        "or",
        "os",
        "pa",
        "pi",
        "pl",
        "ps",
        "pt",
        "qu",
        "rm",
        "rn",
        "ro",
        "ru",
        "rw",
        "sa",
        "sc",
        "sd",
        "se",
        "sg",
        "si",
        "sk",
        "sl",
        "sm",
        "sn",
        "so",
        "sq",
        "sr",
        "ss",
        "st",
        "su",
        "sv",
        "sw",
        "ta",
        "te",
        "tg",
        "th",
        "ti",
        "tk",
        "tl",
        "tn",
        "to",
        "tr",
        "ts",
        "tt",
        "tw",
        "ty",
        "ug",
        "uk",
        "ur",
        "uz",
        "ve",
        "vi",
        "vo",
        "wa",
        "wo",
        "xh",
        "yi",
        "yo",
        "za",
        "zh",
        "zu",
    ]

    TARGET_LANGUAGE = accepted_languages[0]

    def load(content:dict):
        Language.TARGET_LANGUAGE = content["target_language"] if content["target_language"] in Language.accepted_languages else 'en' # default to english


class System:
    POLL_RATE            = 50 

    def load(content:dict):
        System.POLL_RATE     = content["poll_raterue"] if content["poll_rate"] > 0 else 50
        System.API_COOLDOWN  = content["api_cooldown"]


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
        Dev.DEBUG_IMAGE      = True
        Dev.LIMITED_RUN      = content["limited_run"]
        Dev.RUN_COUNT        = content["run_count"] if content["run_count"] > 0 else 1

def validateConfig(content: dict)->bool:
    # TODO: load schema from disk
    schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "title": "Generated schema for Root",
      "type": "object",
      "properties": {
        "screen": {
          "type": "object",
          "properties": {
            "monitor_index": {
              "type": "number"
            },
            "prefer_first_monitor": {
              "type": "boolean"
            }
          },
          "required": [
            "monitor_index",
            "prefer_first_monitor"
          ]
        },
        "image": {
          "type": "object",
          "properties": {
            "screenshot_area": {
              "type": "array",
              "items": {
                "type": "number"
              }
            },
            "x_offset": {
              "type": "number"
            },
            "y_offset": {
              "type": "number"
            },
            "image_difference_threshold": {
              "type": "number"
            }
          },
          "required": [
            "screenshot_area",
            "x_offset",
            "y_offset",
            "image_difference_threshold"
          ]
        },
        "language": {
          "type": "object",
          "properties": {
            "target_language": {
              "type": "string"
            }
          },
          "required": [
            "target_language"
          ]
        },
        "system": {
          "type": "object",
          "properties": {
            "poll_rate": {
              "type": "number"
            },
            "api_cooldown": {
              "type": "boolean"
            }
          },
          "required": [
            "poll_rate",
            "api_cooldown"
          ]
        },
        "dev": {
          "type": "object",
          "properties": {
            "show_warnings": {
              "type": "boolean"
            },
            "show_screengrabs": {
              "type": "boolean"
            },
            "show_settings": {
              "type": "boolean"
            },
            "limited_run": {
              "type": "boolean"
            },
            "run_count": {
              "type": "number"
            },
            "debug_language": {
              "type": "boolean"
            },
            "debug_watchdog": {
              "type": "boolean"
            }
          },
          "required": [
            "show_warnings",
            "show_screengrabs",
            "show_settings",
            "limited_run",
            "run_count",
            "debug_language",
            "debug_watchdog"
          ]
        }
      },
      "required": [
        "screen",
        "image",
        "language",
        "system",
        "dev"
      ]
    } 
        
    try:
        validate(instance=content,schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Config file is invalid\nError:{"="*46}\n\n{e}\n\nSkipping config load...")

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
    Debug  Language         {Dev.DEBUG_LANGUAGE}
    RUN_COUNT:              {Dev.RUN_COUNT}
""")


