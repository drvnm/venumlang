# VenumLang
this is a complete joke 


# EXAMPLE: fizzbuzz in venumlang
## stack operations
in venumlang you use the stack for everything you want to do.
To push something on the stack, simply type what you want

```
"someString" 5 // pushing "somestring" and 5 to the stack
print // will print 5 because 5 is on top of the stack
>> 5 
```
## Variables
you can assign numbers, strings, input and the top of the stack to variables
```cpp
x = 4 // x is now 4
y = "hello world" // y is now "hello world"
z = input // will ask the user for some input and assign it to z
i = pop // will assign the top of the stack to i.
```
you can now push these variables to the stack by simply referencing them
```cpp
x print
>> 4
y print
>> hello world
```
you can also increment variables like so:

```cpp
x = 0
x += 10
x print
>> 10

```

## comparisons
Comparison operators will compare the last 2 elements on the stack, and push the boolean value on top of the stack:
```
5 5 == print
>> True
```
You can use the following operators: ==, !=, >, >=, <, <=

## loops
VenumLang has something "similar" to while loops:
```cpp
x = 0 
100 x < do
    x += 1
    x println
endloop
```

## if statements
you can have if statements:
```cpp
x = 5

x 5 == if
    "They are equal!" println
end
```

## some other things
Include files: 
```cpp
include "someOtherFile.vlang"
```
this will replace these 2 tokens with the contents of that file.

### print vs println
this is obvious i assume

### operators
+ - * / % 

### halting
you can halt a program by using the halt keyword


uhhhhhhh thats it for now

