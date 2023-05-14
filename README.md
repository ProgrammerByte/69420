# Welcome to the world of 69420
An esolang with mutable numbers. To use this transpiler run the following command in an adequate command prompt:
```
py 69420.py name_of_file.69420
```
The file extension doesn't necessarily need to be .69420, for example you could use .txt or .py.

The code formatting rules are similar to those of Python (as you will see later on in the README), so a python code editor may be useful for finding indentation issues.

> **_NOTE:_** There are many times throughout this guide where I use a number e.g. `3` and refer to it as if it's value has not been changed prior. Keep this in mind when debugging.
<br>

## Table of Contents
  - [Section 1: Creating a program with input and output](#section-1-creating-a-program-with-input-and-output)
    - [1.1 - The standard library](#11---the-standard-library)
    - [1.2 - Printing to the console](#12---printing-to-the-console)
    - [1.3 - Numbers as other numbers](#13---numbers-as-other-numbers)
    - [1.4 - Strings](#14---strings)
    - [1.5 - Comments](#15---comments)
    - [1.6 - Outputting characters](#16---outputting-characters)
    - [1.7 - The "Hello World!" program](#17---the-hello-world-program)
    - [1.8 - The "cat" program](#18---the-cat-program)
  - [Section 2: Mathematical operations](#section-2-mathematical-operations)
    - [2.1 - The absolute function](#21---the-absolute-function)
    - [2.2 - The factorial function](#22---the-factorial-function)
    - [2.3 - The derrangements function](#23---the-derrangements-function)
  - [Section 3: Runtime bindings](#section-3-runtime-bindings)
    - [3.1 - Runtime bindings with return type](#31---runtime-bindings-with-return-type)
    - [3.2 - Using runtime bindings to construct keywords](#32---using-runtime-bindings-to-construct-keywords)
    - [3.3 - Immediate bindings](#33---immediate-bindings)
  - [Section 4: Conditional code blocks](#section-4-conditional-code-blocks)
    - [4.1 - Boolean operations](#41---boolean-operations)
    - [4.2 - If, else if, and else](#42---if-else-if-and-else)
    - [4.3 - While loops](#43---while-loops)
  - [Section 5: List and set operations](#section-5-list-and-set-operations)
    - [5.1 - Adding an item to a list or a set](#51---adding-an-item-to-a-list-or-a-set)
    - [5.2 - Subtracting one set from another](#52---subtracting-one-set-from-another)
    - [5.3 - Sorting a list](#53---sorting-a-list)
    - [5.4 Sum of elements in list or set](#54-sum-of-elements-in-list-or-set)
    - [5.5 - Converting a list to a set](#55---converting-a-list-to-a-set)
    - [5.6 - Converting a set to a list](#56---converting-a-set-to-a-list)
    - [5.7 - Getting the maximum element from a list or set](#57---getting-the-maximum-element-from-a-list-or-set)
    - [5.8 - Getting the minimum element from a list or set](#58---getting-the-minimum-element-from-a-list-or-set)
    - [5.9 - Creating lists or sets in shorthand form with ellipsis](#59---creating-lists-or-sets-in-shorthand-form-with-ellipsis)
  - [Section 6: For loops and advanced set/list building](#section-6-for-loops-and-advanced-setlist-building)
    - [6.1 - For loops](#61---for-loops)
    - [6.2 - The membership operator and for loops](#62---the-membership-operator-and-for-loops)
    - [6.3 - The membership operator in boolean logic](#63---the-membership-operator-in-boolean-logic)
    - [6.4 - The membership operator in set/list builder notation](#64---the-membership-operator-in-setlist-builder-notation)
    - [6.5 - The subsets operator in set/list builder notation](#65---the-subsets-operator-in-setlist-builder-notation)
    - [6.6 - The sublists operator in list builder notation](#66---the-sublists-operator-in-list-builder-notation)
  - [Section 7: Methods, classes, and exception handling](#section-7-methods-classes-and-exception-handling)
    - [7.1 - Defining methods](#71---defining-methods)
    - [7.2 - Exception handling](#72---exception-handling)
    - [7.3 - Defining classes and instantiating objects](#73---defining-classes-and-instantiating-objects)
    - [7.4 - Class constructor](#74---class-constructor)
    - [7.5 - Class methods](#75---class-methods)
  - [Section 8 - Further functionality](#section-8---further-functionality)
    - [8.1 - Dictionaries](#81---dictionaries)
    - [8.2 - Exiting a program](#82---exiting-a-program)
    - [8.3 - Compatibility with Python packages](#83---compatibility-with-python-packages)
  - [Section 9: Examples](#section-9-examples)
    - [9.1 - Calculating the area of a circle](#91---calculating-the-area-of-a-circle)
    - [9.2 - FizzBuzz](#92---fizzbuzz)

## Section 1: Creating a program with input and output
In this section we will cover some of the basics of 69420 to cover what you need to create a simple hello world program.

### 1.1 - The standard library
The standard library contains many useful functions when programming with 69420. As the standard library is written in (almost) pure 69420 the usage of it is unnecessary, however heavily reduces the amount of boilerplate in your programs.

If you want to import it then the first line of your file must be as follows:
```
69420
```
Now let's write a basic program.
<br>
<br>
<br>

### 1.2 - Printing to the console
If you have imported the standard library then you can output the value of a number with the `1337` function for example:
```
69420
1337(1)
```
Has the following output:
```
1
```
<br>

### 1.3 - Numbers as other numbers
But what if 1 should be 2? We can do the following instead:
```
69420
1 = 2
1337(1)
```
The above program outputs the number 2 as we are assigning the value of 2 to 1 before printing the value of 1 to the console.

This can get quite complicated quite quickly:
```
69420
1 = 2
2 = 1 + 3
3 = 1 + 2
1337(3)
```
The above program outputs 7 as we are doing the following:
<ol>
  <li>Assigning the value 2 to 1</li>
  <li>Assigning the value 1 (now 2) + 3 to 2 which is 5</li>
  <li>Assigning the value 1 (now 2) + 2 (now 5) to 3 which is 7</li>
  <li>Printing the value of 3 which is 7</li>
</ol>
<br>

### 1.4 - Strings
We can output strings in 69420 similarly to how we usually would with either double quotes (`"`) or single quotes (`'`) for example the line:
```
1337("!?~^&{}][></\£")
```
Has the output:
```
!?~^&{}][></\£
```
<br>

However the line:
```
1337("Hello, World!")
```
Has the output:
```
, !
```
The reason why is because...
<br>
<br>
<br>

### 1.5 - Comments
All upper and lowercase letters are ignored by the 69420 transpiler for example the following program has perfectly valid syntax:
```
69420 imports standard library
1 trivially = 2 by inspection
hello1world3fizz3buzz3foo(bar1zip)zap Outputs one
```
<br>

### 1.6 - Outputting characters
Numbers can be converted to letters (by ASCII code) in 69420 by using the `~` operator for example:
```
1337(~72)
```
Outputs
```
H
```
<br>
However don't forget that these values can still change for example:

```
72 = 73
1337(~72)
```

Outputs

```
I
```

<br>

### 1.7 - The "Hello World!" program
We can use string concatentation to create a "Hello World!" program as follows:
```
69420
1337(~72 + ~101 + ~108 + ~108 + ~111 + ~32 + ~87 + ~111 + ~114 + ~108 + ~100 + ~33)
```
<br>

### 1.8 - The "cat" program
The cat program is one which feeds its input into it's output.

We can take input from the console with the `6969` function from the standard library as follows:
```
69420
4 = 6969("? ") asks for input and outputs a question mark
1337(4)
```

> **_NOTE:_** You can cast this input to an integer with `1000(6969("? "))` or to a float with `1357(6969("? "))`

<br>
<br>

## Section 2: Mathematical operations
69420 supports many mathethematical operations including the following:  <br>
Addition (`+`) e.g. `3 + 2` gives `5`  <br>
Subtraction (`-`) e.g. `3 - 2` gives `1`  <br>
Division (`/`) e.g. `3 / 2` gives `1.5`  <br>
Integer divison (`//`) e.g. `3 // 2` gives `1` <br>
Moduli (`%`) e.g. `5 % 2` gives `1` <br>
Exponent (`**`) e.g. `2 ** 3` gives `8` <br>
Bitwise AND (`&`) e.g. `8 * 9` gives `8` <br>
Bitwise OR (`|`) e.g. `8 | 9` gives `9` <br>
Bitwise XOR (`^`) e.g. `8 ^ 9` gives `1` <br>
Logical shift right (`>>`) e.g. `8 >> 2` gives `2` <br>
Logical shift left (`<<`) e.g. `8 << 2` gives `32` <br>
<br>
<br>

### 2.1 - The absolute function
The absolute function (`~|some_number|~`) is defined for numbers such that the magnitude of that number is returned i.e.

```
~|-12|~
```

Returns 

```
12
```

<br>

The absolute function is also defined for getting the size of a list or a set for example

```
~|[1,2,3]|~
```

and

```
~|{1,2,3}|~
```

both return

```
3
```

<br>

The standard library also allows for the following alternative syntax for getting the size of a list or a set:

```
13674([1,2,3])
```

<br>

### 2.2 - The factorial function
The factorial function (`~!!`) is defined for positive numbers for example
```
~!!3~.
```

returns

```
6
```

<br>
In-fact the following are equivalent forms of this same expression:

```
~!!3)
```

and

```
~!!3|~
```

<br>
The factorial function is also defined over a set or a list as the product of all items in that set or list for example

```
~!![8, 2, 3]~.
```

returns
```
48
```
<br>

### 2.3 - The derrangements function
The derrangements function (`~!`) for a positive integer n returns the number of ways in which those n items can be rearranged such that no one item is in the position in which it started in. More formally this can be computed as: <br>

$round(\frac{n!}{e})$

<br>

This can be used in 69420 for example
```
~!3~.
```
returns

```
2
```

<br>
Likewise this method is also defined for lists and sets (although it doesn't have a well defined meaning other than the product of the items divided by Euler's constant) for example

```
~![2,3]~.
```

returns

```
2
```

<br>

## Section 3: Runtime bindings
Runtime bindings (denoted by the opening tag `[<` and closing tag `>]`) are useful for arbitrarily defining numbers before the contents of the rest of the program executes. <br><br>
For example

```
1337(2)
[<2 = 4>]
```

outputs 

```
4
```

This is because the value of `2` is set in the runtime binding before the value is printed to the console. <br>
<br>
<br>
### 3.1 - Runtime bindings with return type
if a runtime binding has an evaluatable value then it will be replaced with that value at runtime. For example

```
2 = 4
1337([<2 + 1>])
```

outputs 

```
3 
```

This is because `[<2 + 1>]` is replaced with `3` once executed. <br>
<br>
This also means that the following has an output of `21`:

```
[<9 + 10>] = 21
1337(11 + 8)
```

<br>

### 3.2 - Using runtime bindings to construct keywords
The main use of runtime bindings is to create keywords.

```
[<13 = ~105 + ~102>]
13 = 12

[<13>] 13 == 12:
    1337("?")
```

In the above code we set the value of `13` to be the keyword `if`, then we use it in place of the `if` keyword. In fact this is what the standard library does. <br>
<br>
<br>

### 3.3 - Immediate bindings
We can use the `!` operator to have values bound to it immediately after first set in a runtime binding. For example we could rewrite the previous example as

```
[<13 = ~105 + ~102>]
[<13 = 14>]
13 = 12

13! 13 == 12:
    1337("?")
```

where `13!` is set to the first evaluated value of `13` in the runtime bindings (`if`). <br>
<br>
In fact we can rewrite the above as follows:

```
[<61 = 59+2>]
[<1067 = ~40>]
[<1068 = ~41>]
[<1069 = ~61>]
[<1070 = ~34>]
[<1071 = ~33>]
[<13 = ~105 + ~102>]
[<13 = 11>]
13 = 12

13! 13 1069!1069! 12:
    1337!1067!1070!1071!1070!1068!
```

<br>
To further demonstrate the order of runtime and immediate bindings, the program

```
69420
[<7 = 3>]
7 = 5
[<7 = 4>]

1337(7!)
1337([<7>])
1337(7)
```

outputs

```
3
4
5
```

<br>

## Section 4: Conditional code blocks
There are many bindings from the standard library which allows us to write conditional code blocks as you will observe throughout this section.

### 4.1 - Boolean operations
69420 uses `61!` to represent `True`, `60!` to represent `False`, and `404` to represent `None`<br>
<br>
69420 also supports the following boolean operations:  <br>
And (`&&` or `11!`) e.g. `61! 11! 60!` and `60! && 60!` is `False`  <br>
Or (`||` or `10!`) e.g. `61! 10! 60!` and `61! || 61!` is `True` <br>
Not (`¬` or `0!`) e.g. `¬60!` and `0! 60!` is `True` <br>
<br>
<br>

### 4.2 - If, else if, and else
If statements are represented by `1!`, else if is represented by `2!`, and else is represented by 3!. <br>
<br>
Here's an example which outputs `?`, `!`, `*` if the value of `16` is `0`, `1`, or `2` respectively, or outputs `@` otherwise:

```
1! 16 == 0:
    1337("?")
2! 16 == 1:
    1337("!")
2! 16 == 2:
    1337("*")
3!:
    1337("@")
```

<br>
The if statement can also be represented by `=>` therefore we can also write an if statement as follows:

```
=> 16 == 0:
    1337("?")
```

<br>

### 4.3 - While loops
While loops are represented by `42!` for example

```
42! 0 < 3:
    0 += 1
    1337(0)
```

outputs

```
1
2
3
```

<br>
Continue statements are represented by `555!` for example

```
42! 0 < 3:
    0 += 1
    1! 0 == 2:
        555!
    1337(0)
```

outputs

```
1
3
```

<br>
Break statements are represented by `556!` for example

```
42! 0 < 3:
    0 += 1
    1! 0 == 2:
        556!
    1337(0)
```

outputs

```
1
```

<br>

## Section 5: List and set operations
There are many list and set operations in 69420 as this section will cover.

### 5.1 - Adding an item to a list or a set
We can add an item to a list or a set by using the `+` operator for example

```
4 = [1, 2]
4 += [3]
1337(4)
```

outputs

```
[1, 2, 3]
```

<br>

### 5.2 - Subtracting one set from another
We can subtract one set from another by using the `-` operator for example

```
4 = {1, 2, 3}
4 -= {1, 3}
1337(4)
```

outputs

```
{2}
```

<br>

### 5.3 - Sorting a list
We can sort a list with the `1234` function from the standard library for example

```
1337(1234([3,1,2]))
```

outputs

```
[1, 2, 3]
```

<br>

### 5.4 Sum of elements in list or set
We can get the sum of elements in a list or set with the `13610` function from the standard library for example

```
1337(13610([3,1,2]))
```

outputs

```
6
```

<br>

### 5.5 - Converting a list to a set
We can convert a list to a set with the `537` function from the standard library for example

```
1337(537([1,1,2]))
```

outputs

```
{1, 2}
```

<br>

### 5.6 - Converting a set to a list
We can convert a set to a list with the `1157` function from the standard library for example

```
1337(1157({1, 2, 3}))
```

outputs

```
[1, 2, 3]
```

<br>

### 5.7 - Getting the maximum element from a list or set
We can get the maximum element from a list or set with the `1999` function from the standard library for example

```
1337(1999([1,3,2]))
```

outputs

```
3
```

<br>

### 5.8 - Getting the minimum element from a list or set
We can get the minimum element from a list or set with the `1001` function from the standard library for example

```
1337(1001([1,3,2]))
```

outputs

```
1
```

<br>

### 5.9 - Creating lists or sets in shorthand form with ellipsis
We can create a list or a set in shorthand form by specifying the first, second, and last elements of the list or set. For example

```
{0, 2, ... 8}
```

creates the set

```
{0, 2, 4, 6, 8}
```

Of course assuming that 0, 2, and 8 have not been altered earlier on in the program. <br>

Alternatively we can specify only the first and last element and the difference between elements will be kept at 1 for example

```
[3...6]
```

creates the list

```
[3, 4, 5, 6]
```

<br>
Additionally we can combine this with other operations for example

```
{1...10} - {2, 4...10}
```

creates the set

```
{1, 3, 5, 7, 9}
```

<br>
This also works for a descending range so long as you specify the second element for example

```
{3, 2...-1}
```

creates the set

```
{3, 2, 1, 0, -1}
```

<br>

## Section 6: For loops and advanced set/list building
Similar to standard Python, 69420 supports set, list, and dictionary comprehension. This section will explore how this can be used in a 69420 program.

### 6.1 - For loops
In 69420, for loops are declared with the `4!` keyword from the standard library (or alternatively `:|:` as we will observe later on), and range can be specified by the `412100!` keyword (for one to one-hundred get it?). <br>

If `41200!` is given one parameter then this is how many values to count for (starting from 0) for example

```
4! 3 412100!(3):
    1337(3)
```

outputs

```
0
1
2
```

<br>

If `41200!` is given two parameters then this is the start and end values to count between for example

```
4! 3 412100!(3, 5):
    1337(3)
```

outputs

```
3
4
```

<br>

If `412100!` is given three parameters then the third value represents the step for example

```
4! 3 412100!(3, 9, 2):
    1337(3)
```

outputs

```
3
5
7
```

<br>

### 6.2 - The membership operator and for loops
We can use the `£` operator to specify membership, for example the following code iterates over every element of the set `{1, 2, 3}`:

```
4! 4 £ {1, 2, 3}:
    1337(4)
```

<br>

Alternatively we could use `12!` instead of `£`. <br>

This effectively means that if we want to iterate over a range without using `412100!` then we can do it as follows:

```
4! 4 £ {1, 3...99}:
    1337(4)
```

or with alternative syntax

```
:|: 4 12! [1, 3...99]:
    1337(4)
```

<br>

### 6.3 - The membership operator in boolean logic
We can use the membership operator(s) in boolean logic for example

```
1! 3 £ [1, 2, 3]:
    1337("!")
```

will output `!` if `3` is in the list `[1, 2, 3]`
<br>
<br>
<br>

### 6.4 - The membership operator in set/list builder notation
In 69420, builder notation with the membership operator is of the form `{f(x) :|: x £ set => p(x)}` which basically means: <br>

For every element in the set (or list), check it against some predicate (boolean expression), and if it holds then x (or some mapping of x) will appear in the new set or list. <br>

Here's an example of a set being constructed from the set `{1...19}` where every element is even:

```
{4 :|: 4 £  {1...19} => 4 % 2 == 0}
```

Or using alternative syntax:

```
{4 4! 4 12! { 1 ... 19 } 1! 4 % 2 == 0}
```

<br>

Here's an example of a list being constructed from the set `{1, 3...19}` where the square of the element is greater than 25:

```
[4 :|: 4 12! {1,3...19} => 4 ** 2 >= 25]
```

And now let's suppose that we want to add 1 to every resulting element:

```
[4 + 1 :|: 4 12! {1,3...19} => 4 ** 2 >= 25]
```

<br>

Let's now consider three ways in which we can get the previous result (without +1 to every element) whilst excluding numbers from the set `{10...15}`:

```
[4 :|: 4 12! {1,3...19} => 4 ¬12! {10...15} && 4 * 4 >= 25]
[4 :|: 4 12! {1,3...19} - {10...15} => 4 * 4 >= 25]
[4 4! 4 12! { 1 , 3 ...   19 } => 4 0! 12! {10...15} 11! 4 * 4 >= 25]
```

> **_NOTE:_** For testing if a number is not in a set we can use either `¬12!`, `0! 12!`, `0! £`, or `¬ £`
<br>
<br>

### 6.5 - The subsets operator in set/list builder notation
In 69420, it's also possible to consider all subsets of a given set (or subsequences of a given list) with the `~£` operator for example

```
1337([4 :|: 4 ~£ {1, 5, 3} ~.])
```

outputs

```
[[1, 3, 5], [1, 3], [1, 5], [1], [3, 5], [3], [5], []]
```

<br>

We can combine this with predicate logic to only consider subsets that have a product that is at least five for example

```
1337([4 :|: 4 ~£ {1, 5, 3} ~. => ~!!4~. >= 5])
```

outputs

```
[[1, 3, 5], [1, 5], [3, 5], [5]]
```

<br>

The maximum size of the subsets/subsequences can be given by adding a `, size` after the set for example

```
1337([4 :|: 4 ~£ {1, 5, 3}, 1 ~.])
```

outputs

```
[[1], [3], [5], []]
```

<br>

Likewise the minimum size of the subsets/subsequences can be given by adding a `, size` after the previous `, size` for example

```
1337([4 :|: 4 ~£ {1, 5, 3}, 2, 1 ~.])
```

outputs

```
[[1, 3], [1, 5], [1], [3, 5], [3], [5]]
```

This is especially useful for efficiency as this has exponential time complexity.
<br>
<br>
<br>

### 6.6 - The sublists operator in list builder notation
There is also an operator for considering all of the sublists of a list (`~$`) for example

```
[4 :|: 4 ~$ [1, 5, 3] ~.]
```

creates the list

```
[[], [1], [1, 5], [5], [1, 5, 3], [5, 3], [3]]
```

<br>

Likewise, we can use predicate logic, max, and min lengths of sublists to alter the list constructed (see section 6.5). The main difference is that this is relatively ill defined for sets as sets don't have much in the way of natural ordering.
<br>
<br>
<br>

## Section 7: Methods, classes, and exception handling

### 7.1 - Defining methods
In 69420 methods can be defined with `420!`, with `200!` being used for return values and `400!` being used for exceptions. The following code block defines a method titled `141` which divides one number by another number, however if the divisor is `0` then an exception is raised:

```
420! 141(55, 56):
    1! 56 == 0:
        400!
    200! 55 / 56
```

<br>

### 7.2 - Exception handling
Suppose that our `141` method from section 7.1 raised an error then how could we handle this? Well we can use `9000!` to define a try block, `9001!` to define a catch block, and `8999!` to define a finally block:

```
9000!:
    141(12, 0)
    1337(~70)
9001!:
    1337(~69)
8999!:
    1337("!")
```

This outputs the following:

```
E
!
```

where the `E` is from the catch block and the `!` is from the finally block.
<br>
<br>
<br>

### 7.3 - Defining classes and instantiating objects
We can declare a class called `29` with `256!` and we can also use `.` to return a method attribute. For example the code

```
256! 29:
    14159 = "!?"

3 = 29
1337(3.14159)
```

outputs

```
!?
```

<br>

### 7.4 - Class constructor
We can declare a constructor for a class `256` with `255!` and with the object self being passed as the first parameter. For example the code

```
256! 256:
    255!(254, 255="!"):
        254.255 = 255

3 = 256("?")
1337(3.255)
```

outputs

```
?
```

<br>

### 7.5 - Class methods
We can declare a method for a class in the same way in which we declare a standard method, however the object's self needs to be passed as the first parameter. For example the code

```
256! 256:
    256 = "?"
    255!(254, 255="!"):
        254.255 = 255

    420! 254(254, 257=""):
        200! 254.255 + 254.256 + 257

3 = 256(",")
1337(3.254("."))
```

outputs

```
,?.
```

<br>

## Section 8 - Further functionality

### 8.1 - Dictionaries
Dictionaries can be used in the same way in which they are usually used in python. For example the code

```
1423 = {
    69: 70,
    70: 71,
    71: 69
}
1337(1423[69])
```

outputs

```
70
```

<br>

### 8.2 - Exiting a program
The function `9876543210()` can be used to exit a program
<br>
<br>
<br>

### 8.3 - Compatibility with Python packages
Using bindings it's possible to use functionality from any Python package. We can use `69420!` to import any package we like however we need to spell out the name of the package and the functions from the package with runtime bindings. <br>

In the following program we import the `math` package and call `math.sin(1)`:

```
69420
[<474 = ~109 + ~97 + ~116 + ~104>]
[<475 = ~115 + ~105 + ~110>]

69420! 474!
1337(474!.475!(1))
```

<br>

## Section 9: Examples
Here are some example programs written in 69420.

### 9.1 - Calculating the area of a circle

```
69420                 imports standard library

3 = 22 / 7            value of PI
420! 314(90):
    200! 3 * 90 * 90  computes pi r squared

1337(314(4))          computes the area of a circle with radius four
```

<br>

### 9.2 - FizzBuzz

```
69420
30 = ~70 + ~105 + ~122 * 2              Fizz
50 = ~66 + ~117 + ~122 * 2              Buzz
150 = 30 + 50                           FizzBuzz
7 = ~72 + ~111 + ~119                   How
8 = ~102 + ~97 + ~114                   far
9 = ~116 + ~111                         to
10 = ~99 + ~111 + ~117 + ~110 + ~116    count
12 =  7 + ~32 + 8 + ~32 + 9 + ~32 + 10 + ~63 + ~32

16 = 1000(6969(12)) asks how far to count and takes number

4! 4 412100!(1, 16+1):
    1! 4 % 5 == 0 && 4 % 3 == 0:
        1337(150)
    2! 4 % 5 == 0:
        1337(50)
    2! 4 % 3 == 0:
        1337(30)
    3!:
        1337(4)
```
