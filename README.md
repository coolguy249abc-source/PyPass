# PyPass
This is a Python module I made for generating passwords! It's my first ever python module.

TestPyPi page: [link](https://test.pypi.org/project/PyKeyGen/)
Github page: [link](https://github.com/coolguy249abc-source/PyPass/)

** POST NOTE: SOME DUDE ALREADY HAS THE NAME "PYPASS" SO IM RENAMING THE PYPI PAGE TO "PYKEYGEN" **

## Dependencies
Here are all the dependencies (dependency) you need to install:
   random
To install the dependencies run:
   ```bash
   pip install random
   ```
## Tutorial
### Installing
#### Using Python file
To use PyPass with PyPass.py, you need to place the PyPass.py file in the same directory as your project Python file (eg, main.py).
To include PyPass add:
  ```python
  import PyPass
   ```
at the top of your file.
#### Using pip
run this command in the terminal:
   ```bash
   pip install -i https://test.pypi.org/simple/ PyKeyGen
   ```
Run this to update:
  ```bash
  pip install -i https://test.pypi.org/simple/ PyKeyGen --upgrade
  ```
then, use:
   ```python
   from PyKeyGen_Xorg import PyGenKey as PyPass # "as PyPass" is optional, but if you decide not to do it, throught the tutorial when I use PyPass, use PyGenKey (eg, PyPass.__version__() -> PyGenKey.__version__())
   ```
### Using
#### Get version
to get the current version of PyPass (now PyKeyGen) use:

   ```python
   PyPass.__version__()
   ```
You might notice the code does not output anything because it isnt outputing the text. To make it output text use:

   ```python
   print(PyPass.__version__())
   ```
Then, the input should be similar to:
    ```
    1.0.1
    ```
#### Generating a password
##### Character Sets & Arrays
To generate a password you first need to make an array of characters. Here is a list of available character sets:
* ```PyPass.lowercase: a, b, c, d, ..., z ```
* ```PyPass.uppercase: A, B, C, D, ..., Z ```
* ```PyPass.digits: 0, 1, 2, 3, ..., 9```
* ```PyPass.punctuation: . , ; : [ @ #, etc...```
* ```PyPass.emojis: 🔥💀✨🥶🧠🎉🔑🧩```
* ```PyPass.space: " "```
  
To make an array use:
   ```python
   arr = PyPass.lowercase
   ```
To use multiple character sets in an array, add a + in between each one:
   ```python
   arr = PyPass.lowercase + PyPass.uppercase + PyPass.digits
   ```
##### ```genNewPrint()``` function
To generate a password, use the ```genNewPrint()``` function. To use the ```genNewPrint()``` function, call it and put the array you made into the argument parentesis.
   ```python
   PyPass.genNewPrint(arr)
   ```
The ```genNewPrint()``` function already prints out the password for you, so you dont have to worry about using ```print()```. Here is the ouput of the code:
   ```python
   JuqqtXxi
   ```
To put it in a loop use the ```for``` loop.
   ```python
   for i in range(12):
       PyPass.genNewPrint(arr)
   ```
output:
   ```python
     MxxrfJVe
     PbJCwgVI
     CvpOncKS
     NcTTMKWi
     cIRLWTjF
     RAGkjMWb
     nHJWofzF
     eZcJXJPP
     fEJdHNlF
     RDsKGgjj
     PuWAlTzw
     LjzBHloi
   ```
You can also use input to generate passwords. For example, the user might want to generate 10 passwords. to do that add an input variable:
  ```python
     # Tutorial file - tutorial.py
     from PyKeyGen_Xorg import PyGenKey

     inp = int(input("Enter how many passwords you would like to generate: ")) # Make sure its is an integer
     arr = PyGenKey.lowercase + PyGenKey.uppercase + PyGenKey.digits

     if inp <= 100: # Sets a limit of 100
         for i in range(inp):
             PyGenKey.genNewPrint(arr)
     else:
         print("Too much passwords.")
  ```
output:
  ```bash
  Enter how many passwords you would like to generate: 4
  tJE9nfs0
  nHNCJseP
  gqJItmZk
  EJmZnUX0
  ```
error:
  ```bash
  Enter how many passwords you would like to generate: 101
  Too much passwords.
  ```
##### ```genNew()``` function
The ```genNew()``` is the same as ```genNewPrint()```, but it doesnt print the password, it returns it. 

```python
print(genNew(arr))
```

##### Presets
You can use presets to generate passwords. Here are the current presets:
* ```"simple": lowercase + digits```
* ```"strong": lowercase + uppercase + digits```
* ```"mega": lowercase + uppercase + digits + punctuation```
* ```"memz": emojis```

To use presets, you can do 2 things.

###### Calling straight for PRESETS
You can use presets by calling them from the PRESETS dictionary.

```python
PyPass.genNewPrint(PyPass.PRESETS["strong"]) # You can replace strong with your desired preset
```

The output should be something like: ```zz1zgxb4```

###### Using the presetGen() function
The ```presetGen()``` function just calls the PRESET inside of the function. It is shorter and easier to understand compared to the previous method. To use it, call the function and place you desired preset inside of the argument perentesis.

> [!NOTE]
The ```presetGen()``` function already generates the password inside of it.

```python
PyPass.presetGen("memz") # lol
```
output: ```🧩✨🥶🥶🔑✨🧠💀```

##### Passphrase
A passphrase is a password with dictionary words in it. (like ```MattLuke123``` or ```TexasCity009```). You can use the ```genPassphrase()``` function to generate one. You can select how much words you want in your password, and what the seperator is. The default settings are: words=4, seperator="-". Here is how to use it:

```python
print(PyPass.genPassphrase(words=2, seperator="_"))
```

output: ```yorkie_lol```

Here is a list of all the words available:

"banana", "horse", "cat", "dog", "Matt", "singer", "choir", "footsteps",
"apple", "market", "mango", "fries", "burger", "waterpark", "toy", "pillow",
"calm", "door", "tie", "computer", "python", "ever", "forever", "snake", "feisty",
"yorkie", "sap", "lol", "memz", "epik", "dawg", "pet", "lmao", "chicken", "sushi",
"Texas", "fish", "Luke", "Matt"

> [!NOTE]
> Guess what? This function also returns! Make sure to put it in ```print()```!

#### Length
What I mean by "Length" is the password length. The default password length is set to 8 characters. Today, I am going to show you to use length.

##### View current length
To view the current length of passwords use the ```getLength()``` function.

```python
PyPass.getLength()
```
You might notice that like the ```__version__``` function, the ```getLength()``` function is also invisible; it's for the same reason too! To fix it, place the code in a ```print()``` function.

```python
print(PyPass.getLength())
```
The output should be something like:

```python
8
```
You can add this in your tutorial code (after the for loop):

```python
length_char = PyPass.getLength() # For this script, it is PyGenKey.getLength()
prit(f"Character size: {length_char}")
```

output:

```bash
Enter how many passwords you would like to generate: 2
SqJohY0i
MQJwmLs4
Character size: 8
```
##### setLength() function
The ```setLength()``` function sets the length (in characters) of your password(s). To use it call it, and place an integer (representing characters) inside of the argument perentasis.

```python
PyPass.setLength(16) # Add this somewhere in the tutorial code before the if and for statements
```

Updated ```tutorial.py``` code:

```python
from PyKeyGen_Xorg import PyGenKey

inp = int(input("Enter how many passwords you would like to generate: ")) # Make sure its is an integer
arr = PyGenKey.lowercase + PyGenKey.uppercase + PyGenKey.digits

PyGenKey.setLength(16)

if inp <= 100: # Sets a limit of 100
    for i in range(inp):
        PyGenKey.genNewPrint(arr)
        length_char = PyGenKey.getLength()
    print(f"Character size: {length_char}")
else:
    print("To much passwords.")
```

output:

```bash
Enter how many passwords you would like to generate: 2
SqJohY0i73DPL8eU
MQJwmLs4OUsxBEsg
Character size: 16
```

#### Combine
##### Using combine() function
The combine function combines multiple strings to use it, enter 2 or more strings in the argument perentesis:

```python
print(PyPass.combine("qwerty", "abc", "123"))
```

output: ```qwertyabc123```

Here is an example of the ```tutorial.py``` file using the ```combine()``` function to generate one big password.

```python
from PyGenKey_Xorg import PyGenKey

inp = int(input("Enter how many passwords you would like to generate: "))

arr = PyGenKey.PRESETS["mega"]
PyGenKey.setLength(4)

if inp <= 100:
    all_passes = [] # Stores passwords
    for i in range(inp):
        pw = PyGenKey.genNew(arr)
        all_passes.append(pw)
        print(pw)

    print("\nCombined:")
    print("".join(all_passes))

    print(f"\nCharacter size (per pass): {PyGenKey.getLength()}")
else:
    print("Too much passwords.")
```

output:
```bash
Enter how many passwords you would like to generate: 2
e)Cl
u&HU

Combined:
e)Clu&HU

Character size (per pass): 4
```


You might of noticed that I placed it inside of the ```print()``` function. The ```combine()``` function only returns the output, not prints.
##### Manualy
to do it manualy, just print out your 2 or more strings and add them.

```python
a = "qwerty"
b = "abc"
c = "123"
print(a + b + c)
```
#### Check strength
To check password strength use the ```getStrength()``` function. To use it, just call it and place yout password inside of the perentesis:
```python
print(PyPass.getStrength("qwerty12")) # Make sure it's in quotes
```
output: ```Medium```

> [!NOTE]
> The ```getStrength``` function does not print, it returns

The function checks how big your password is.

* 0: Weak
* 1: Weak-ish
* 2: Medium
* 3: Decent
* 4: Strong
* 5: Very Strong
* 6: Uncrackable
* 7: CRAZY

#### Emojis
##### Picking random emoji
To pick a random emoji use the ```pickEmoji()``` function. Note, the function return not prints.
```python
print(PyPass.pickEmoji())
```
output: ```🧩```
#### Bonus
##### GUI app using tkinter
```python
from PyKeyGen_Xorg import PyGenKey as PyPass
import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.geometry("700x600")
root.title("PyPass")

arr = PyPass.PRESETS["mega"]

def copy_text():
    text = passText.cget("text")  # get label text
    root.clipboard_clear()
    root.clipboard_append(text)

def submit():
    entry1_text = entry1.get()
    entry2_text = entry2.get()
    
    if int(entry1_text) >= 4:
        if int(entry2_text) <= 25:
            all_passes = []
            PyPass.setLength(int(entry1_text))
            
            for i in range(int(entry2_text)):
                pw = PyPass.genNew(arr)
                all_passes.append(pw)
                print(pw) # Debugging; you can remove if you want
            passText.config(text="\n".join(all_passes)) # "'\n'.join(all_passes)" makes each password start on a new line

def clear():
    passText.config(text=" ")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

titleLabel = tk.Label(root, text="Welcome to PyPass!", font=("Helvetica", 34))
titleLabel.pack(pady=20)

# Frame 1 - Length
frame1 = tk.Frame(root)
frame1.pack()
text1 = tk.Label(frame1, text="Length")
text1.pack(side="left")
entry1 = tk.Entry(frame1)
entry1.pack(side="right")

# Frame 2 - Amount
frame2 = tk.Frame(root)
frame2.pack()
text2 = tk.Label(frame2, text="Amount")
text2.pack(side="left")
entry2 = tk.Entry(frame2)
entry2.pack(side="right")

buttonSubmit = tk.Button(root, text="Submit!", command=lambda:submit())
buttonSubmit.pack(pady=5)

passText = tk.Label(root)
passText.pack()

buttonClear = tk.Button(root, text="Clear All", command=lambda:clear())
buttonClear.pack()

buttonClear = tk.Button(root, text="Copy to clipboard", command=lambda:copy_text())
buttonClear.pack(side="bottom", pady=25)

buttonQuit = tk.Button(root, text="Quit", command=root.destroy)
buttonQuit.pack(side="bottom", pady=15)

root.mainloop()
```

##### Simple Matrix
Just generate a bunch of big passwords infinitly, and make them green. As simple as that.
```python
# matrix.py
from PyKeyGen_Xorg import PyGenKey as PyPass
from colorama import *

print(Fore.GREEN)

while True:
    PyPass.setLength(75)
    PyPass.genNewPrint(PyPass.PRESETS["strong"])
```
