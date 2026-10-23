
try:
    from PIL import ImageGrab
    import screeninfo
    import pytesseract

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")

def test_main():

