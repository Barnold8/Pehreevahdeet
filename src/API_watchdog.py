import settings
import time

from enum import Enum

class Eye(Enum): # Use of enum means I could seperate sleep timers for each API without them needing to share a timer

    OCR         = 1
    TRANSLATION = 2

class Watchdog:

    ocr         = False
    translation = False

    def closeEye(eye_id: Eye):
        if settings.Dev.DEBUG_WATCHDOG:
            print("closeEye | Debug: Closing eye")
        match eye_id:
            case Eye.OCR:
                Watchdog.ocr = True
            case Eye.TRANSLATION:
                Watchdog.translation = True
            case _:
                print(f"Watchdog.closeEye | Error: an invalid ID ({eye_id}) was entered")
    
    def attemptSleep(eye_id : Eye):
        if settings.Dev.DEBUG_WATCHDOG:
            print("closeEye | Debug: Sleeping") 
        match eye_id:
            case Eye.OCR:
                if Watchdog.ocr:
                    time.sleep(settings.System.API_COOLDOWN)
                    Watchdog.ocr = False
            case Eye.TRANSLATION:
                if Watchdog.translation:
                    time.sleep(settings.System.API_COOLDOWN)
                    Watchdog.translation = False
            case _:
                print(f"attemptSleep | Error: an invalid ID ({eye_id}) was entered")
