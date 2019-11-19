<h1>Object Oriented Programming</h1>



<h2>Goals, Principles, and Patterns</h2>


In object-oriented paradigm each __object__ is an _instance_ of a _class_. Each class presents to the outside world a concise and consistent view of the objects that are instances of this class, without going into too much unnecessary detail or giving others access to the inner workings of the objects. The class definition typically specifies _instance variables_ also known as _data members_ that the object contains, as well as the _methods_ also known as _member functions_ that the object can execute. This view of computing is intended to fulfill several goals and incorporate several design principles.


<h3>Object-Oriented Design Goals</h3>

Software implementations should achieve _robustness_, _adaptability_, and _reusability_.

<h3>Object-Oriented Design Principles</h3>

Chief among the principles of the object-oriented approach, which are intended to facilitate the goals outlined above, are the following:

- __Modularity__: refers to an organizing principle in which different components of a software system are divided into separate functional units.

- __Abstraction__: is to distill a complicated system down to its most fundamental parts. Applying the abstraction paradigm to the design of data structures gives rise to _abstract data types_ (ADTs). An ADT is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the types of parameters of the operations. An ADT specifies what each operation does, but not how it does it. We will typically refer to the collective set of behaviors supported by an ADT as its public interface.

    Python supports abstract data types using a mechanism known as an _abstract base class_ (ABC). An abstract base class cannot be instantiated (i.e., you cannot directly create an instance of that class), but it defines one or more common methods that all implementations of the abstraction must have. An ABC is realized by one or more concrete classes that inherit from the abstract base class while providing implementations for those method declared by the ABC.

- __Encapsulation__: yields robustness and adaptability, for it allows the implementation details of parts of a program to change without adversely affecting other parts, thereby making it easier to fix bugs or add new functionality with relatively local changes to a component.

<h3>Design Patterns</h3>

_Design pattern_ describes a solution to a “typical” software design problem. A pattern provides a general template for a solution that can be applied in many different situations. It describes the main elements of a solution in an abstract way that can be specialized for a specific problem at hand. It consists of a name, which identifies the pattern; a context, which describes the scenarios for which this pattern can be applied; a template, which describes how the pattern is applied; and a result, which describes and analyzes what the pattern produces.

<h2>Software Development</h2>


Traditional software development involves several phases. Three major steps are:
1. Design
2. Implementation
3. Testing and Debugging


<h3>Design</h3>

While general prescriptions are hard to come by, there are some rules of thumb that we can apply when determining how to design our classes:

- __Responsibilities__: Divide the work into different actors, each with a different responsibility. Try to describe responsibilities using action verbs. These actors will form the classes for the program.

- __Independence__: Define the work for each class to be as independent from other classes as possible. Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program. Give data (as instance variables) to the class that has jurisdiction over the actions that require access to this data.

- __Behaviors__: Define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be well understood by other classes that interact with it. These behaviors will define the methods that this class performs, and the set of behaviors for a class are the interface to the class, as these form the means for other pieces of code to interact with objects from the class.

Defining the classes, together with their instance variables and methods, are key to the design of an object-oriented program. A common tool for developing an initial high-level design for a project is the use of _CRC_ (Class-Responsibility-Collaborator) cards. The main idea behind this tool is to have each card represent a component, which will ultimately become a class in the program, write the responsibilities of the class and list the collaborators for this component.

The design process iterates through an action/actor cycle, where we first identify an action (that is, a responsibility), and we then determine an actor (that is, a component) that is best suited to perform that action.

As the design takes form, a standard approach to explain and document the design is the use of _UML_ (Unified Modeling Language) diagrams to express the organization of a program. One type of UML figure is known as a class diagram. An example of such a diagram is shown below:

<img src="../images/class_diagram.png">

<h3>Pseudo-Code</h3>

As an intermediate step before the implementation of a design, programmers are often asked to describe algorithms in a way that is intended for human eyes only. Such descriptions are called _pseudo-code_.

<h3>Coding Style and Documentation</h3>

[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

Python provides integrated support for embedding formal documentation directly in source code using a mechanism known as a _docstring_. Formally, any string literal that appears as the first statement within the body of a module, class, or function (including a member function of a class) will be considered to be a docstring.

A docstring is stored as a field of the module, function, or class in which it is declared. It serves as documentation and can be retrieved in a variety of ways. An external tool named pydoc is distributed with Python and can be used to generate formal documentation as text or as a Web page. Guidelines for authoring useful docstrings are available at [PEP 257](https://www.python.org/dev/peps/pep-0257/)

<h3>Testing and Debugging</h3>

Testing is the process of experimentally checking the correctness of a program, while debugging is the process of tracking the execution of a program and discovering the errors in it.

__Testing:__

Testing every method of a class atleast once - method coverage.
Testing each code statement in the program atleast once - statement coverage.

There are two main testing strategies, _top-down_ and _bottom-up_, which differ in the order in which components are tested. Top-down testing proceeds from the top to the bottom of the program hierarchy. It is typically used in conjunction with _stubbing_, a boot-strapping technique that replaces a lower-level component with a stub, a replacement for the component that simulates the functionality of the original. For example, if function A calls function B to get the first line of a file, when testing A we can replace B with a stub that returns a fixed string. Bottom-up testing proceeds from lower-level components to higher-level components.

As software is maintained, the act of _regression testing_ is used, whereby all previous tests are re-executed to ensure that changes to the software do not introduce new bugs in previously tested components.

__Debugging:__

The simplest debugging technique consists of using print statements to track the values of variables during the execution of the program. A better approach is to run the program within a _debugger_, which is a specialized environment for controlling and monitoring the execution of a program. The standard Python distribution includes a module named pdb, which provides debugging support directly within the interpreter.


<h2>Class Definitions</h2>


<h3>Example: CreditCard Class</h3>



<h3>Operator Overloading and Python’s Special Methods</h3>



<h3>Example: Multidimensional Vector Class</h3>



<h3>Iterators</h3>


<h3>Example: Range Class</h3>


<h2>Inheritance</h2>


<h3>Extending the CreditCard Class</h3>



<h3>Hierarchy of Numeric Progressions</h3>



<h3>Abstract Base Classes</h3>



<h2>Namespaces and Object-Orientation</h2>


<h3>Instance and Class Namespaces</h3>



<h3>Name Resolution and Dynamic Dispatch</h3>






<h2>Shallow and Deep Copying</h2>






<h2>Exercises</h2>


<h3>Reinforcement</h3>



<h3>Creativity</h3>



<h3>Projects</h3>
