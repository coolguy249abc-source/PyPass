import random
import string

length = 8
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
punctuation = list(string.punctuation)
space = " "
emojis = list("🔥💀✨🥶🧠🎉🔑🧩")
digits = list(string.digits)
current_version = 1.1

wordslist = ["banana", "horse", "cat", "dog", "Matt", "singer", "choir", "footsteps",
         "apple", "market", "mango", "fries", "burger", "waterpark", "toy", "pillow",
         "calm", "door", "tie", "computer", "python", "ever", "forever", "snake", "feisty",
         "yorkie", "sap", "lol", "memz", "epik", "dawg", "pet", "lmao", "chicken", "sushi",
         "Texas", "fish", "Luke", "Matt"]

PRESETS = {
    "simple": lowercase + digits,
    "strong": lowercase + uppercase + digits,
    "mega": lowercase + uppercase + digits + punctuation,
    "memz": emojis
}

def genPassphrase(words=4, seperator="-"):
    chosen_words = [random.choice(wordslist) for _ in range(words)]
    passphrase = seperator.join(chosen_words)
    return passphrase

def pickEmoji():
    return random.choice(emojis)

#def getStrength(password):
   # if len(password) <= 4:
       # print("Weak")
   # elif len(password) >= 8:
    #    print("Decent")
   # elif len(password) >= 12:
   #     print("Strength: 12")
   # elif len(password) >= 16:
   #     print("Medium")
   # elif len(password) >= 20:
   #     print("Strong")
   # elif len(password) >= 50:
   #     print("Mega")
   
def getStrength(password):
    length = len(password)
    score = 0

    if length >= 8: score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    if any(c in uppercase for c in password): score += 1
    if any(c in digits for c in password): score += 1
    if any(c in punctuation for c in password): score += 1

    levels = {
        0: "Weak",
        1: "Weak-ish",
        2: "Medium",
        3: "Decent",
        4: "Strong",
        5: "Very Strong",
        6: "Uncrackable",
        7: "CRAZY"
    }

    return levels.get(score, "Unknown")


def setLength(Thelength):
    if not isinstance(Thelength, int):
        raise TypeError("Length must be an integer.")
    if Thelength <= 0:
        raise ValueError("Length must be a positive integer.")
    else:
        global length
        length = Thelength
        return  length

def genNewPrint(array):
    if not array:
        raise IndexError("IndexError: genNewPrint() index empty.")
    else:
        password_list = random.choices(array, k=length)
        password = "".join(password_list)
        print(password)

def genNew(array):
            if not array:
                raise IndexError("IndexError: genNewPrint() index empty.")
            else:
                password_list = random.choices(array, k=length)
                password = "".join(password_list)
                return password

#def combine(combined, combiner):
    #return combined + combiner
    
def combine(*items):
    return "".join(str(i) for i in items)


def presetGen(name):
    if name not in PRESETS:
        raise ValueError("Unknown preset name.")
    return genNew(PRESETS[name])


def getLength():
    return length

def __version__():
    print_version = str(current_version)
    return print_version
