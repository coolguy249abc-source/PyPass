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
