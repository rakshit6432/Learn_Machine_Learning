<h1>Week 1: What is calculus?</h1>



In addition to the topics below, as a pre rec I also went through Khan Academies:
- [Finding Taylor polynomial approximations of functions](https://www.khanacademy.org/math/ap-calculus-bc/bc-series-new/bc-10-11/v/maclaurin-and-taylor-series-intuition)
- [Finding Taylor or Maclaurin series for a function](https://www.khanacademy.org/math/ap-calculus-bc/bc-series-new/bc-10-14/v/function-as-a-geometric-series)

topics to do some refreshing.


<h2>Functions</h2>

Essentially, a function is a relationship between some inputs and an output. So, for example, if I had a function for modeling the distribution of temperature in this room, I might input the x, y, and z coordinates of a specific location I'm interested in as well as the time, t. And then the function would return me the temperature at that specific point in space at that moment in time.


<h2>Gradients and derivatives</h2>


<h3>Rise Over Run</h3>

Calculus is just a set of tools for describing the relationship between a function and the change in its variables.

<img src="../2. Multivariate Calculus/images/rise_over_run.png">

<h3>Definition of a derivative</h3>

<img src="../2. Multivariate Calculus/images/derivative_def.png">

<img src="../2. Multivariate Calculus/images/derivative_equation.png">

<img src="../2. Multivariate Calculus/images/sum_rule.png">

<img src="../2. Multivariate Calculus/images/power_rule.png">

<h3>Differentiation examples & special cases</h3>




<h2>Time saving rules</h2>


<h3>Product rule</h3>

<img src="../2. Multivariate Calculus/images/product_rule.png">

<img src="../2. Multivariate Calculus/images/quotient_rule.jpg">

<h3>Chain rule</h3>

<img src="../2. Multivariate Calculus/images/chain_rule.png">



<h1>Week 2: Multivariate calculus</h1>



<h2>Moving to multivariate</h2>


<h3>Variables, constants & context</h3>



<h3>Differentiate with respect to anything</h3>

<img src="../2. Multivariate Calculus/images/multivariate_partial_derivative.png">


<h2>Jacobians - vectors of derivatives</h2>


<h3>The Jacobian</h3>

In vector calculus, the __Jacobian matrix__ of a vector-valued function in several variables is the matrix of all its first-order partial derivatives. When this matrix is square, that is, when the function takes the same number of variables as input as the number of vector components of its output, both the matrix and its determinant are referred to as the __Jacobian__.

<img src="../2. Multivariate Calculus/images/jacobian.png">

<h3>Jacobian applied</h3>

<img src="../2. Multivariate Calculus/images/jacobian_coordinates.png">


<h2>The Hessian</h2>

Before we get into Hessians, let's briefly look at gradients. The gradient is simply a collection of the derivative of the function for each direction. Each element of the gradient is simply the slope of the function in each direction. Next, the second derivative is simply the derivative of the derivative or the _rate of change of the slope_. The rate of change of the slope corresponds to how “curved” each loss function is. The sharper the curve, the more rapidly the slope changes.

In mathematics, the __Hessian matrix__ or __Hessian__ is a square matrix of second-order partial derivatives of a scalar-valued function, or scalar field. It describes the local curvature of a function of many variables.

<img src="../2. Multivariate Calculus/images/hessian.png">

Each row represents the change of the gradient in a certain direction. Alternatively, you could consider each column to be the gradient of one element of the gradient.



<h1>Week 3: Multivariate chain rule and its applications</h1>



<h2>Chain rule Introduction</h2>


<h3>Multivariate chain rule</h3>

<img src="../2. Multivariate Calculus/images/multi_variate_chain_rule.png">

<img src="../2. Multivariate Calculus/images/jacobian_chain_rule.png">


<h2>Neural Networks</h2>


<h3>Simple neural networks</h3>

<img src="../2. Multivariate Calculus/images/simple_nn.png">

<img src="../2. Multivariate Calculus/images/slp.png">

<img src="../2. Multivariate Calculus/images/slp_matrix.png">

<img src="../2. Multivariate Calculus/images/slp_complete.png">

<img src="../2. Multivariate Calculus/images/mlp.png">

<img src="../2. Multivariate Calculus/images/cost_function.png">

<img src="../2. Multivariate Calculus/images/slp_chain_rule.png">

<img src="../2. Multivariate Calculus/images/mlp_chain_rule.png">



<h1>Week 4: Taylor series and linearization</h1>



<h2>Taylor series for approximations</h2>


<h3>Power series</h3>

Taylor series are also referred to as power series. And this is because they are composed of coefficients in front of increasing powers of x.

<h3>Power series derivation</h3>

__Maclaurin series:__

<img src="../2. Multivariate Calculus/images/maclaurin_series_derived.png">

Although, what we've written here certainly does count as a tailless series because we're specifically looking at the point x equals 0, we often refer to this case as a Maclaurin series.

<img src="../2. Multivariate Calculus/images/maclaurin_series.png">

<h3>Power series details</h3>

_Maclaurin series_ says that if you know everything about a function at the point x equals zero, then you can reconstruct everything about it everywhere. The __Taylor series__ simply acknowledges that there is nothing special about the point x equals zero. And so says that if you know everything about the function at any point, then you can reconstruct the function anywhere.

<img src="../2. Multivariate Calculus/images/Taylor_series1D.png">


<h2>Multivariate Taylor Series</h2>


<h3>Linearization</h3>

<img src="../2. Multivariate Calculus/images/Taylor_series_error.png">

<h3>Multivariate Taylor</h3>




<h1>Week 5: Introduction to optimization</h1>



<h2>Fitting as minimization problem</h2>


<h3>Newton-Raphson in one dimension</h3>

The Newton-Raphson method is one of the most widely used methods for root finding. It can be easily generalized to the problem of finding solutions of a system of non-linear equations numerically, which is referred to as Newton's technique. Moreover, it can be shown that the technique is quadratically convergent as we approach the root, meaning that the square of the error at one iteration is proportional to the error at the next iteration ([Example](https://math.stackexchange.com/questions/1735193/in-practice-what-does-it-mean-for-the-newtons-method-to-converge-quadratically)).

Unlike the bisection and false position methods, the Newton-Raphson (N-R) technique requires only one initial value $x_0$, which we refer to as the initial guess for the root. Let $f(x)$ be a well-behaved function, and let $r$ be a root of the equation $f(x) = 0$. We start with the estimate $x_0$ of $r$. From $x_0$, we produce an improved—we hope—estimate $x_1$. From $x_1$, we produce a new estimate $x_2$. From $x_2$, we produce a new estimate $x_3$. We go on until we are ‘close enough’ to $r$ —or until it becomes clear that we are getting nowhere. The above general style of proceeding is called iterative. Of the many iterative root-finding procedures, the Newton-Raphson method, with its combination of simplicity and power, is the most widely used.

__The Newton-Raphson Iteration:__

<img src="../2. Multivariate Calculus/images/Newton_Raphson_Iteration.png">

Once the Newton Method catches scent of the root, it usually hunts it down with amazing speed. But since the method is based on local information, namely $f(x_n)$ and $f'(x_n)$, the Newton Method’s sense of smell is deficient.

If the initial estimate is not close enough to the root, the Newton Method may not converge, or may converge to the wrong root.

<h3>Gradient Descent</h3>

All algorithms for unconstrained gradient-based optimization can be described as follows. We
start with iteration number $k = 0$ and a starting point, $x_k$.

<img src="../2. Multivariate Calculus/images/gradient_general_algorithm.png">

There are two subproblems in this type of algorithm for each major iteration: computing the search direction $p_k$ and finding the step size (controlled by $\alpha_k$). The difference between the various types of gradient-based algorithms is the method that is used for computing the search direction.

The gradient descent method uses the gradient vector at each point as the search direction for
each iteration. The gradient vector is orthogonal to the plane tangent to the isosurfaces of the function. The gradient vector at a point, $g(x_k)$, is also the direction of maximum rate of change (maximum increase) of the function at that point. This rate of change is given by the norm, $\|g(x_k) \|$.

__Gradient Descent Algorithm:__

<img src="../2. Multivariate Calculus/images/gradient_descent_algorithm.png">


<h2>Lagrange multipliers</h2>

<img src="../2. Multivariate Calculus/images/Lagrange_multipliers.png">


<h3>Constrained optimization</h3>





<h1>Week 6: Regression</h1>



<h2>Introduction to linear regression</h2>


<img src="../2. Multivariate Calculus/images/least_squares.png">


<h3>Simple linear regression</h3>



<h2>Non-linear regression</h2>


<h3>General non linear least squares</h3>



<h3>Doing least squares regression analysis in practice</h3>
