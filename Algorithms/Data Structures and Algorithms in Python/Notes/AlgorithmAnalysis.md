<h1>Algorithm Analysis</h1>



A _data structure_ is a systematic way of organizing and accessing data, and an _algorithm_ is a step-by-step procedure for performing some task in a finite amount of time.

To be able to classify some data structures and algorithms as “good,” we must have precise ways of analyzing them. The primary analysis tool used in this book involves characterizing the running times of algorithms and data structure operations, with space usage also being of interest.

The run time:
- increases with the input size.
- may also vary for different inputs of the same size.
- is affected by the hardware environment (eg: the processor, clock rate, memory, disk).
- is affected by the software environment (eg: the operating system, programming language) in which the algorithm is implemented and executed.
- will be smaller if the computer has a much faster processor
- will be small if the implementation is done in a program compiled into native machine code instead of an interpreted implementation.

In spite of the possible variations that come from different environmental factors, we would like to focus on the relationship between the running time of an algorithm and the size of its input. We are interested in characterizing an algorithm’s running time as a function of the input size.



<h2>Experimental Studies</h2>


We can study the run time of algorithms by executing it on various inputs and recording the time spent during each execution. This can be done in python as below:

```python
from time import time
start time = time( ) # record the starting time
# run algorithm
end time = time( ) # record the ending time
elapsed = end time − start time # compute the elapsed time
```

An elapsed time measured in this fashion is a decent reflection of the algorithm efficiency, but it is by no means perfect. The time function measures relative to what is known as the “wall clock.” Because many processes share use of a computer’s _central processing unit_ (or CPU), the elapsed time will depend on what other processes are running on the computer when the test is performed. A fairer metric is the number of CPU cycles that are used by the algorithm. This can be determined using the clock function of the time module, but even this measure might not be consistent if repeating the identical algorithm on the identical input, and its granularity will depend upon the computer system. Python includes a more advanced module, named timeit, to help automate such evaluations with repetition to account for such variance among trials.

We can also perform independent experiments on many different test inputs of various sizes and visualize the results by plotting the performance of each run of the algorithm:

<img src="../images/fig31.png">

To be meaningful, this analysis requires that we choose good sample inputs and test enough of them to be able to make sound statistical claims about the algorithm’s running time.

__Challenges of Experimental Analysis__

While experimental studies of running times are valuable, especially when fine-tuning production quality code, there are three major limitations to their use for algorithm analysis:

- Experimental running times of two algorithms are difficult to directly compare unless the experiments are performed in the same hardware and software environments.

- Experiments can be done only on a limited set of test inputs; hence, they leave out the running times of inputs not included in the experiment (and these inputs may be important).

- An algorithm must be fully implemented in order to execute it to study its running time experimentally.


<h3>Moving Beyond Experimental Analysis</h3>

__Counting Primitive Operations:__

To analyze the running time of an algorithm without performing experiments, we perform an analysis directly on a high-level description of the algorithm (either in the form of an actual code fragment, or language-independent pseudo-code). We define a set of _primitive operations_ such as the following:

- Assigning an identifier to an object
- Determining the object associated with an identifier
- Performing an arithmetic operation (for example, adding two numbers)
- Comparing two numbers
- Accessing a single element of a Python list by index
- Calling a function (excluding operations executed within the function)
- Returning from a function.

Instead of trying to determine the specific execution time of each primitive operation, we will simply count how many primitive operations are executed, and use this number _t_ as a measure of the running time of the algorithm. The implicit assumption in this approach is that the running times of different primitive operations will be fairly similar. Thus, the number, t, of primitive operations an algorithm performs will be proportional to the actual running time of that algorithm.

__Measuring Operations as a Function of Input Size:__

To capture the order of growth of an algorithm’s running time, we will associate, with each algorithm, a function $f(n)$ that characterizes the number of primitive operations that are performed as a function of the input size $n$.

__Focusing on the Worst-Case Input:__

<img src="../images/fig32.png">

An _average case_ analysis usually requires that we calculate expected running times based on a given input distribution, which usually involves sophisticated probability theory. Therefore, we will characterize running times in terms of the _worst case_. Worst case analysis is much easier than average-case analysis, as it requires only the ability to identify the worst-case input, which is often simple.


<h2>The Seven Functions Used in This Book</h2>


<h3>The Constant Function</h3>

The simplest function is the _constant function_,

$$f(n) = c$$

for some fixed constant c, such as c = 5, c = 27, or $c = 2^{10}$. That is, for any argument n, the constant function $f(n)$ assigns the value c. In other words, it does not matter what the value of n is; $f(n)$ will always be equal to the constant value c.

Because we are most interested in integer functions, the most fundamental constant function is $g(n) = 1$ and any other function $f(n) = c$ can be written as $f(n) = cg(n)$.

The constant function characterizes the number of steps needed to do a basic operation on a computer, like adding two numbers, assigning a value to some variable, or comparing two numbers.

<h3>The Logarithm Function</h3>

$f(n) = log_b n$ for some constant _b > 1_. This function is defined as:

$$x = log_bn \ \text{iff} \  b^x = n$$

By definition, $log_b 1 = 0$. The value b is known as the _base_ of the logarithm.

<img src="../images/log_rules.png">

<h3>The Linear Function</h3>

$$f(n) = n$$

This function arises in algorithm analysis any time we have to do a single basic operation for each of n elements. For example, comparing a number x to each element of a sequence of size n will require n comparisons. The linear function also represents the best running time we can hope to achieve for any algorithm that processes each of n objects that are not already in the computer’s memory, because reading in the n objects already requires n operations.

<h3>The N-Log-N Function</h3>

$$f(n) = n log \ n$$

This function grows a little more rapidly than the linear function and a lot less rapidly than the quadratic function; therefore, we would greatly prefer an algorithm with a running time that is proportional to $nlog \ n$, than one with quadratic running time. We will see several important algorithms that exhibit a running time proportional to the n-log-n function. For example, the fastest possible algorithms for sorting n arbitrary values require time proportional to $nlog \ n$.

<h3>The Quadratic Function</h3>

$$f(n) = n^2$$

The main reason why the quadratic function appears in the analysis of algorithms is that there are many algorithms that have nested loops, where the inner loop performs a linear number of operations and the outer loop is performed a linear number of times. Thus, in such cases, the algorithm performs $n \times n = n^2$ operations.

<h3>The Cubic Function and Other Polynomials</h3>

$$f(n) = n^3$$

__Polynomials:__

Most of the functions we have listed so far can each be viewed as being part of a larger class of functions, the _polynomials_. A polynomial function has the form,

$$f(n) = a_0 + a_1n+ a_2n^2 + a_3n^3 + \cdots + a_dn^d$$

where the a's are the constants and _d_ is the _degree_ of the polynomial.

__Summations:__

The above polynomial f(n) can be written as a summation notation:

$$f(n) = \sum_{i=0}^d a_i n^i$$

<h3>The Exponential Function</h3>

$$f(n) = b^n$$

<img src="../images/exponent_rules.png">

__Geometric Sums:__

<img src="../images/geometric_sum.png">

Summations as shown in Proposition 3.5 are called _geometric_ summations.

<h3>Comparing Growth Rates</h3>

<img src="../images/function_growth_rates.png">

When discussing logarithms, we noted that the value is generally not an integer, yet the running time of an algorithm is usually expressed by means of an integer quantity, such as the number of operations performed. Thus, the analysis of an algorithm may sometimes involve the use of the _floor function_ and _ceiling function_, which are defined respectively as follows:

- $\lfloor x \rfloor$ = the largest integer less than or equal to x.
- $\lceil x \rceil$ = the smallest integer greater than or equal to x.


<h2>Asymptotic Analysis</h2>


We analyze algorithms using a mathematical notation for functions that disregards constant factors. Namely, we characterize the running times of algorithms by using functions that map the size of the input, n, to values that correspond to the main factor that determines the growth rate in terms of n.


<h3>The “Big-Oh” Notation</h3>

Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numbers. We say that $f(n)$ is $O(g(n))$ if there is a real constant $c > 0$ and an integer constant $n_0 \geq 1$ such that

$$f(n) \leq cg(n), \qquad \text{for} \ n \geq n_0$$

This definition is often referred to as the “big-Oh” notation, for it is sometimes pronounced as “ $f(n)$ is big-Oh of $g(n)$.”

<img src="../images/big_oh.jpg">

The big-Oh notation allows us to say that a function $f(n)$ is “less than or equal to” another function $g(n)$ up to a constant factor and in the asymptotic sense as n grows toward infinity. This ability comes from the fact that the definition uses “$\leq$” to compare $f(n)$ to a $g(n)$ times a constant, c, for the asymptotic cases when $n \geq n_0$. So, it is best to say

"$f(n)$ __is__ $O(g(n))$."

Alternatively, we can say “$f(n)$ is __order of__ $g(n)$.” For the more mathematically inclined, it is also correct to say, “$f(n) \in O(g(n))$,” for the big-Oh notation, technically speaking, denotes a whole collection of functions.

__Characterizing Running Times Using the Big-Oh Notation__

The big-Oh notation is used widely to characterize running times and space bounds in terms of some parameter n, which varies from problem to problem, but is always defined as a chosen measure of the “size” of the problem.

__Some Properties of the Big-Oh Notation__

The big-Oh notation allows us to ignore constant factors and lower-order terms and focus on the main components of a function that affect its growth.

<img src="../images/big_oh_prop_1.jpg">

Thus, the highest-degree term in a polynomial is the term that determines the asymptotic growth rate of that polynomial.

We rely on the mathematical fact that $log \ n \leq n \ \text{for} \ n \geq 1$.

<img src="../images/big_oh_example_1.jpg">

__Characterizing Functions in Simplest Terms__

In general, we should use the big-Oh notation to characterize a function as closely as possible. While it is true that the function $f(n) = 4n^3 + 3n^2$ is $O(n^5)$ or even $O(n^4)$, it is more accurate to say that $f(n)$ is $O(n^3)$.

__Big-Omega__

Just as the big-Oh notation provides an asymptotic way of saying that a function is “less than or equal to” another function, the following notations provide an asymptotic way of saying that a function grows at a rate that is “greater than or equal to” that of another.

Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numbers. We say that $f(n)$ is $\Omega(g(n))$, pronounced “ $f(n)$ is big-Omega of $g(n)$,” if $g(n)$ is $O(f(n))$, that is, there is a real constant $c > 0$ and an integer constant $n_0 \geq 1$ such that

$$f(n) \geq cg(n), \qquad \text{for} \ n \geq n_0$$

This definition allows us to say asymptotically that one function is greater than or equal to another, up to a constant factor.

<img src="../images/big_omega_example_1.jpg">

__Big-Theta__

<img src="../images/big_theta.jpg">

<img src="../images/asymptotic_bounding.jpg">

For further reference, watch [Asymptotic Bounding 101: Big O, Big Omega, & Theta](https://www.youtube.com/watch?v=0oDAlMwTrLo)

<h3>Comparative Analysis</h3>



<img src="../images/big_O_complexity.jpg">

<h3>Examples of Algorithm Analysis</h3>




<h2>Simple Justification Techniques</h2>


<h3>By Example</h3>



<h3>The “Contra” Attack</h3>



<h3>Induction and Loop Invariants</h3>



<h2>Exercises</h2>
