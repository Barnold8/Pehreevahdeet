import sys
def errPrint(*args:str, **kwargs:str)->None:
    print(*args, file=sys.stderr, **kwargs)


def getAPIKey(path:str)->str:

    try:
        with open(path,'r') as file:
            try:
                key =  file.readlines()[0]
                return  ''.join(key.split())
            except IndexError:
                errPrint(f"Error: {path} is either empty or corrupt")
    except FileNotFoundError as FNFE:
        errPrint(f"Error: {path} does not exist")


