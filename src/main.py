try:
    # Needed lib code

    # My own code

    import utils
    import image

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")


#TODO: find some easy way of setting up OCR on a system that isnt a headache

def main():
    
    if __name__ == "__main__":

        #monitors = screeninfo.get_monitors()
        #img = getScreen()
        #x.show()
        #print("Grabbing images")
        
        images = image.loadImages("samples")
        KEY = utils.getAPIKey('API_KEY')
        for img in images:
            print(image.OCR(img,KEY))

main()
