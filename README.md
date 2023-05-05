# Flux
Flux is a templating language designed for the [kyozan](https://github.com/blaze0x0/kyozan) project. 
This project is in development and has few features.

### Syntax
example file:
```python
print("Hello world, This is an example")
print("My name is <<<<name>>>>")
```
Usage:
```python
# Make sure you are in the same directory as flux.py. Will release to pypi after completion.
import flux
modified = flux.parse_file("myfile.py", args={
    "name": "Joe Mama"
}
print(modified)
```
Output:
```
$ python3 example.py
print("Hello world, This is an example")
print("My name is Joe Mama")
```

### Mathematical Expression

Plain text example:
```
Hello, this is a plain text.
6 times 5 is <<<<6*5>>>>.
```
Output after flux:
```
Hello, this is a plain text.
6 times 5 is 30.
```

### Flux Functions
There are two functions in the flux module
- parse_text(text : str, args : dict)  --> string 
- parse_file(filename : str, args : dict) --> string

The parse_text function parses the given text
The parse_file function, well, parses the text in a file and returns the parsed text as a string

### Flux Class
For some reason,  you imported the Flux class from flux using
```python
from flux import Flux
```
What would you do? idc 😑
Anyways here's a quick overview.
```python
flux = Flux("hello <<<<name>>>>") # Initialisation
args = {
    "name": "Ben Dover"
}
parsed = flux.parse(args) # Parse the text
flux.reset("this is a new text for parsing! <<<<6*9>>>>") # Reset flux object with a new text
parsed2 = flux.parse({}) # Parse the new text

myresult = flux.evaluate("6*9") # A better way to evaluate mathematical expressions
```

### Interpreter
I have no idea if i should call it an interpreter but yeah, we have one:
![example.png](./example.mpeg)

### Todo
Note: The flux project is verryy incomplete and needs lot of upgrades.
- [ ] Add variable evaluation (i.e. myvar + 5)
- [ ] Allow multiple operator evaluation (i.e. 5+5+5)
- [ ] Add string addition (i.e. mystring + mystring)
- [x] Add better documentation
- [x] Allow square function (i.e. 5**5)


### Contribution
Contribution is very much appreciated ☺️👍
Here are our contributors:
 - [Blaze0x0](https://github.com/blaze0x0/) --> Founder
