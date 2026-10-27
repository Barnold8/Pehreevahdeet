# Pehreevahdeet

Pehreevadheet, based on the russian word for "translate" (переводить), is an autonomous translation tool. Pehreevadheet takes a screenshot of a screen, or a sub-section of a screen and translates that autonomously into your language of choice.

This tool came about to solve the problem of communications in video games. When playing competitive games, communications are important. So how do you read what people say if you don't speak the language? Pehreevahdeet has you covered. 


# Requirements

[Python](https://www.python.org/) 3.16 or newer

# How to install

**If you arent using [Git](https://git-scm.com/), please download this repo, unzip it and follow from step 2** 

1. Clone this repo
    * ``git clone https://github.com/Barnold8/Pehreevahdeet``
2. CD into the repo
    * ``cd Pehreevahdeet``
3. Initiate the venv
    * ``python -m venv venv``
4. Run the venv  
    * How to activate venv on Linux: 
        * ``source venv/bin/activate``
          * Note: This may be different for differing distros. But using ``source venv/bin/<one of the files>.<extension>`` will work for whatever flavour of Linux you're using.
    * How to activate venv on Windows
        * ``C:\Users\Your Name> venv\Scripts\activate ``
5. Install the modules needed
    * ``pip install -r .config/requirements.txt``
6. Get the OCR API key
    1. Get your OCR api key [>>here<<](https://ocr.space/ocrapi/freekey)
    2. Create a file in the .config directory named **"API_KEY_OCR"** (make sure this has no file extension)
    3. Enter the contents of your API key in **"API_KEY_OCR"**
7. Get the Translation API key
    1. Go to [**this website**](https://rapidapi.com/flybyapi1/api/multi-format-ai-translator-the-most-complete/playground/translate)
    2. At the top click **Run**
    3. This will take you to a **sign up/sign in page**. Either make a new account or sign in
    4. When you are logged in, you will be returned to that same page. Look for a tab named **Authorization**. Click it.
    5. You will see some field with the name **X-RapidAPI-Key**, copy that value
    6. Create a file in the .config directory named **"API_KEY_TRANSLATE"** (make sure this has no file extension)
    6. Enter the contents of your API key in **"API_KEY_TRANSLATE"**
8. Run the program
    * ``python src/main.py``

For more ways to run the program, look at the "**Usage**" section

# Usage

To start the program in the most default mode, simply run

``python src/main.py``

This will not enable any warnings to be logged (when i make that feature) or any other features

# Config

# TO BE CONSTRUCTED

![image](https://d1csarkz8obe9u.cloudfront.net/posterpreviews/notice-under-construction-design-template-16aab28647cdc546dbe5d975d2eb6146_screen.jpg?ts=1737375136)
