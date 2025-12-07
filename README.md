# PyPass
This is a Python module I made for generating passwords! It's my first ever python module.

TestPyPi page: [link](https://test.pypi.org/project/PyKeyGen/)

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
then, use:
   ```python
   from PyKeyGen_Xorg import PyKeyGen as PyPass # "as PyPass" is optional, but if you decide not to do it, throught the tutorial when I use PyPass, use PyGenKey (eg, PyPass.__version__() -> PyGenKey.__version__())
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
    ```python
    1.0.1
    ```
#### Generating a password
##### Character Sets & Arrays
To generate a password you first need to make an array of characters. Here is a list of available character sets:
* ``` PyPass.lowercase: a, b, c, d, ..., z ```
* ``` PyPass.uppercase: A, B, C, D, ..., Z ```
* ``` PyPass.digits: 0, 1, 2, 3, ..., 9```
* ``` PyPass.punctuation: . , ; : [ @ #, etc...```
  
To make an array use:
   ```python
   arr = PyPass.lowercase
   ```
To use multiple character sets in an array, add a + in between each one:
   ```python
   arr = PyPass.lowercase + PyPass.uppercase + PyPass.digits
   ```
##### ```genNew()``` function
To generate a password, use the ```genNew()``` function. To use the ```genNew()``` function, call it and put the array you made into the argument parentesis.
   ```python
   PyPass.genNew(arr)
   ```
The ```genNew()``` function already prints out the password for you, so you dont have to worry about using ```print()```. Here is the ouput of the code:
   ```python
   JuqqtXxi
   ```
To put it in a loop use the ```for``` loop.
   ```python
   for i in range(12):
       PyPass.genNew(arr)
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
     from PyKeyGen_Xorg import PyGenKey

     inp = int(input("Enter how many passwords you would like to generate: ")) # Make sure its is an integer
     arr = PyGenKey.lowercase + PyGenKey.uppercase + PyGenKey.digits

     if inp <= 100: # Sets a limit of 100
         for i in range(inp):
             PyGenKey.genNew(arr)
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
