<h1>Python Primer</h1>



<h2>Python Overview</h2>


<h3>The Python Interpreter</h3>

Python is formally an _interpreted_ language. Commands are executed through a piece of software known as the _Python interpreter_.


<h2>Objects in Python</h2>


Python is an object-oriented language and classes form the basis for all data types.


<h3>Identifiers, Objects, and the Assignment Statement</h3>

The most important of all Python commands is an _assignment statement_, such as `temperature = 98.6`. This command establishes temperature as an identifier (also known as a _name_), and then associates it with the _object_ expressed on the right-hand side of the equal sign, in this case a floating-point object with value 98.6. Identifiers in Python are case-sensitive.

<img src="../images/python_reserves.png">

Python identifier is most similar to a reference variable in Java or a pointer variable in C++. Each identifier is implicitly associated with the _memory address_ of the object to which it refers. A Python identifier may be assigned to a special object named None, serving a similar purpose to a null reference in Java or C++.

Unlike Java and C++, Python is a _dynamically typed_ language, as there is no advance declaration associating an identifier with a particular data type. An identifier can be associated with any type of object, and it can later be reassigned to another object of the same (or different) type.

A programmer can establish an _alias_ by assigning a second identifier to an existing object. For example, `original=temperature`. Once an alias has been established, either name can be used to access the underlying object. If that object supports behaviors that affect its state, changes enacted through one alias will be apparent when using the other alias (because they refer to the same object).

However, if one of the names is reassigned to a new value using a subsequent assignment statement, that does not affect the aliased object, rather it breaks the alias. For example: `temperature = temperature + 5.0` (temperature=103.6, original=98.6).

<h3>Creating and Using Objects</h3>

__Instantiation:__

The process of creating a new instance of a class is known as instantiation.  In general, the syntax for instantiating an object is to invoke the _constructor_ of a class. For example for a Widget class without parameters: `w = Widget()`.

Many of Python’s built-in classes support what is known as a _literal_ form for designating new instances. For example, the command temperature = 98.6 results in the creation of a new instance of the _float_ class; the term 98.6 in that expression is a literal form.

__Calling Methods:__

Python’s classes may also define one or more _methods_ (also known as _member functions_), which are invoked on a specific instance of a class using the dot (“.”) operator. When using a method of a class, it is important to understand its behavior. Some methods return information about the state of an object, but do not change that state. These are known as _accessors_. Other methods, such as the sort method of the list class, do change the state of an object. These methods are known as _mutators_ or _update methods_

<h3>Python’s Built-In Classes</h3>

A class is _immutable_ if each object of that class has a fixed value upon instantiation that cannot subsequently be changed.

<img src="../images/python_immutable.png">

The list, tuple, and str classes are sequence types in Python, representing a collection of values in which the order is significant.

A __list__ instance stores a sequence of objects. A list is a _referential_ structure, as it technically stores a sequence of _references_ to its elements.

Python’s __set__ class represents the mathematical notion of a set, namely a collection of elements, without duplicates, and without an inherent order to those elements. Only instances of immutable types can be added to a Python set. Therefore, objects such as integers, floating-point numbers,
and character strings are eligible to be elements of a set. It is possible to maintain a set of tuples, but not a set of lists or a set of sets, as lists and sets are mutable. The __frozenset__ class is an immutable form of the set type, so it is legal to have a set of frozensets.


<h2>Expressions, Operators, and Precedence</h2>


<h3>Compound Expressions and Operator Precedence</h3>


<h2>Control Flow</h2>


<h3>Conditionals</h3>


<h3>Loops</h3>



<h2>Functions</h2>


<h3>Information Passing</h3>


<h3>Python’s Built-In Functions</h3>



<h2>Simple Input and Output</h2>


<h3>Console Input and Output</h3>



<h3>Files</h3>



<h2>Exception Handling </h2>


<h3>Raising an Exception</h3>



<h3>Catching an Exception</h3>




<h2>Iterators and Generators</h2>





<h2>Additional Python Conveniences </h2>


<h3>Conditional Expressions</h3>




<h3>Comprehension Syntax</h3>




<h3>Packing and Unpacking of Sequences</h3>



<h2>Scopes and Namespaces</h2>





<h2>Modules and the Import Statement </h2>


<h3>Existing Modules</h3>
