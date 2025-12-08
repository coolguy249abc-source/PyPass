import random
import string

length = 8
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
punctuation = list(string.punctuation)
digits = list(string.digits)
current_version = "1.0.001"

def setLength(Thelength):
    global length
    length = Thelength
    return length

def genNewPrint(array):
            password_list = random.choices(array, k=length)
            password = "".join(password_list)
            print(password)

def genNew(array):
            password_list = random.choices(array, k=length)
            password = "".join(password_list)
            return password
            
def getLength():
    return length

def __version__():
    print_version = str(current_version)
    return print_version
