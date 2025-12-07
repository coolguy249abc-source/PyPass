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
    ```
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
    print(f"Character size: {length_char}")
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
               PyGenKey.genNew(arr)
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
