
<h1>Linear Algebra</h1>



<h3>Matrices and Vectors</h3>


<h3>Addition and Scalar Multiplication</h3>


<h3>Matrix Vector Multiplication</h3>


<h3>Matrix Matrix Multiplication</h3>


<h3>Matrix Multiplication Properties</h3>


<h3>Inverse and Transpose</h3>



<h1>Probability</h1>






<h1>Supervised Learning</h1>



<img src="../2. Machine Learning/images/supervised_learning.jpg">

When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a __regression__ problem. When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a __classification__ problem.


<h2>Linear regression</h2>


To perform supervised learning, we must decide how we’re going to represent functions/hypotheses h in a computer. As an initial choice, let’s say we decide to approximate y as a linear function of x:

<img src="../2. Machine Learning/images/linear_regression_1.jpg">

<img src="../2. Machine Learning/images/linear_regression_2.jpg">

If you’ve seen linear regression before, you may recognize this as the familiar least-squares cost function that gives rise to the _ordinary least squares_ regression model.

<h3>LMS algorithm</h3>

We want to choose θ so as to minimize J(θ). To do so, let’s use a search algorithm that starts with some “initial guess” for θ, and that repeatedly changes θ to make J(θ) smaller, until hopefully we converge to a value of θ that minimizes J(θ). Specifically, let’s consider the _gradient descent_ algorithm, which starts with some initial θ, and repeatedly performs the update:

<img src="../2. Machine Learning/images/gradient_descent.jpg">

This is why we need good examples, having shitty features and shitty data affects the whole model because from the data side, if you have shitty data and you make a prediction and its way off, you end up having an unnecessarily large weight update. Similarly, if you are using bad features, when you make an update, you use all the feature values to update the parameters (note $x_j^{(i)}$ is a vector).

Note that, while gradient descent can be susceptible to local minima in general, the optimization problem we have posed here for linear regression has only one global, and no other local, optima; thus gradient descent always converges (assuming the learning rate α is not too large) to the global minimum. Indeed, J is a convex quadratic function.

_Stochastic gradient descent_ (also incremental gradient descent) is an algorithm where, we repeatedly run through the training set, and each time we encounter a training example, we update the parameters according to the gradient of the error with respect to that single training example only. Whereas _batch gradient descent_ has to scan through the entire training set before taking a single step—a costly operation if n is large—stochastic gradient descent can start making progress right away, and continues to make progress with each example it looks at. Often, stochastic gradient descent gets θ “close” to the minimum much faster than batch gradient descent. (Note however that it may never “converge” to the minimum, and the parameters θ will keep oscillating around the minimum of J(θ); but in practice most of the values near the minimum will be reasonably good approximations to the true minimum. For example, by slowly letting the learning rate α decrease to zero as the algorithm runs, it is also possible to ensure that the parameters will converge to the global minimum rather than merely oscillate around the minimum). For these reasons, particularly when the training set is large, stochastic gradient descent is often preferred over batch gradient descent.

<h3>The normal equations</h3>

Gradient descent gives one way of minimizing J. Let’s discuss a second way of doing so, this time performing the minimization explicitly and without resorting to an iterative algorithm. In this method, we will minimize J by explicitly taking its derivatives with respect to the $θ_j$’s, and setting them to zero.

__Least squares revisited__

Given a training set, define the _design matrix_ X to be the n-by-d matrix that contains the training examples’ input values in its rows:

<img src="../2. Machine Learning/images/least_squares.jpg">

Note that in the above step, we are implicitly assuming that $X^T X$ is an invertible matrix. This can be checked before calculating the inverse. If either the number of linearly independent examples is fewer than the number of features, or if the features are not linearly independent, then $X^T X$ will not be invertible. Even in such cases, it is possible to “fix” the situation with additional techniques, which we skip here for the sake of simplicity.

<h3>Probabilistic interpretation</h3>

<img src="../2. Machine Learning/images/probabilistic_interpretation_1.jpg">

<img src="../2. Machine Learning/images/probabilistic_interpretation_2.jpg">

which we recognize to be J(θ), our original least-squares cost function.

<h3>Locally weighted linear regression</h3>

<img src="../2. Machine Learning/images/locally_weighted_lr.jpg">


<h2>Classification and logistic regression</h2>


<h3>Logistic Regression</h3>

We could approach the classification problem ignoring the fact that y is discrete-valued, and use our old linear regression algorithm to try to predict y given x.

<img src="../2. Machine Learning/images/logistic_regression_1.jpg">

Similar to how we used some probabilistic assumptions to derive least squares regression using the maximum likelihood estimator, let's make some assumptions to our classification model and then fit the parameters via maximum likelihood.

<img src="../2. Machine Learning/images/logistic_regression_2.jpg">

If we compare this to the LMS update rule, we see that it looks identical; but this is not the same algorithm, because hypothesis function is now defined as a non-linear function.

<h3>Digression: The perceptron learning algorithm</h3>

Consider modifying the logistic regression method to “force” it to output values that are either 0 or 1 or exactly. To do so, it seems natural to change the definition of g to be the threshold function.

<img src="../2. Machine Learning/images/perceptron.jpg">

Even though the perceptron may be cosmetically similar to logistic regression and least squares linear regression, it is actually a very different type of algorithm; in particular, it is difficult to endow the perceptrons' predictions with meaningful probabilistic interpretations, or derive the perceptron as a maximum likelihood estimation algorithm.

<h3>Another algorithm for maximizing ℓ(θ)</h3>

Newton’s method performs the following update:

<img src="../2. Machine Learning/images/newtons_method.jpg">

In logistic regression setting, θ is vector-valued, so we need to generalize Newton’s method to this setting. The generalization of Newton’s method to this multidimensional setting (also called the _Newton-Raphson method_) is given by

<img src="../2. Machine Learning/images/newtons_raphson_method.jpg">

Newton’s method typically enjoys faster convergence than (batch) gradient descent, and requires many fewer iterations to get very close to the minimum. One iteration of Newton’s can, however, be more expensive than one iteration of gradient descent, since it requires finding and inverting an d-by-d Hessian; but so long as d is not too large, it is usually much faster overall. When Newton’s method is applied to maximize the logistic regression log likelihood function ℓ(θ), the resulting method is also called _Fisher scoring_.


<h2>Generalized Linear Models</h2>


<img src="../2. Machine Learning/images/glm.jpg">

<h3>The exponential family</h3>

To work our way up to GLMs, we will begin by defining exponential family distributions. We say that a class of distributions is in the exponential family if it can be written in the form

<img src="../2. Machine Learning/images/exponential_family.jpg">

<h3>Constructing GLMs</h3>

Consider a classification or regression problem where we would like to predict the value of some random variable y as a function of x. To derive a GLM for this problem, we will make the following three assumptions about the conditional distribution of y given x and about our model:

<img src="../2. Machine Learning/images/constructing_glm.jpg">

The third of these assumptions might seem the least well justified of the above, and it might be better thought of as a “design choice” in our recipe for designing GLMs, rather than as an assumption per se. These three assumptions/design choices will allow us to derive a very elegant class of learning algorithms, namely GLMs, that have many desirable properties such as ease of learning.


<h2>Generative Learning algorithms</h2>


Consider a classification problem in which we want to learn to distinguish between elephants (y = 1) and dogs (y = 0), based on some features of an animal. Given a training set, an algorithm like logistic regression or the perceptron algorithm (basically) tries to find a straight line—that is, a decision boundary—that separates the elephants and dogs. Then, to classify a new animal as either an elephant or a dog, it checks on which side of the decision boundary it falls, and makes its prediction accordingly.

Here’s a different approach. First, looking at elephants, we can build a model of what elephants look like. Then, looking at dogs, we can build a separate model of what dogs look like. Finally, to classify a new animal, we can match the new animal against the elephant model, and match it against the dog model, to see whether the new animal looks more like the elephants or more like the dogs we had seen in the training set.

Algorithms that try to learn p(y|x) directly (such as logistic regression), or algorithms that try to learn mappings directly from the space of inputs X to the labels {0, 1}, (such as the perceptron algorithm) are called __discriminative learning__ algorithms. Here, we’ll talk about algorithms that instead try to model p(x|y) (and p(y)). These algorithms are called __generative learning__ algorithms. For instance, if y indicates whether an example is a dog (0) or an elephant (1), then p(x|y = 0) models the distribution of dogs’ features, and p(x|y = 1) models the distribution of elephants’ features.

After modeling p(y) (called the _class priors_) and p(x|y), our algorithm can then use Bayes rule to derive the posterior distribution on y given x:

<img src="../2. Machine Learning/images/bayes_rule.jpg">

Here, the denominator is given by p(x) = p(x|y = 1)p(y = 1) + p(x|y = 0)p(y = 0), and thus can also be expressed in terms of the quantities p(x|y) and p(y) that we’ve learned. Actually, if were calculating p(y|x) in order to make a prediction, then we don’t actually need to calculate the denominator, since

<img src="../2. Machine Learning/images/bayes_rule_simplified.jpg">

<h3>Gaussian discriminant analysis</h3>

The first generative learning algorithm that we’ll look at is Gaussian discriminant analysis (GDA). In this model, we’ll assume that p(x|y) is distributed according to a multivariate normal distribution. Let’s talk briefly about the properties of multivariate normal distributions before moving on to the GDA model itself.

__The multivariate normal distribution__

<img src="../2. Machine Learning/images/multivariate_normal_distribution.jpg">

<img src="../2. Machine Learning/images/normal_distribution_plot_1.jpg">

<img src="../2. Machine Learning/images/normal_distribution_plot_2.jpg">

<img src="../2. Machine Learning/images/normal_distribution_plot_3.jpg">

<img src="../2. Machine Learning/images/normal_distribution_plot_4.jpg">

__The Gaussian Discriminant Analysis model__

<img src="../2. Machine Learning/images/gda_model.jpg">

__Discussion: GDA and logistic regression__

<img src="../2. Machine Learning/images/gda_model_logistic.jpg">

When would we prefer one model over another? GDA and logistic regression will, in general, give different decision boundaries when trained on the same dataset. Which is better?

We just argued that if p(x|y) is multivariate gaussian (with shared Σ), then p(y|x) necessarily follows a logistic function. The converse, however, is not true; i.e., p(y|x) being a logistic function does not imply p(x|y) is multivariate gaussian. This shows that GDA makes stronger modeling assumptions about the data than does logistic regression. It turns out that when these modeling assumptions are correct, then GDA will find better fits to the data, and is a better model. Specifically, when p(x|y) is indeed gaussian (with shared Σ), then GDA is _asymptotically efficient_. Informally, this means that in the limit of very large training sets (large n), there is no algorithm that is strictly better than GDA (in terms of, say, how accurately they estimate p(y|x)). In particular, it can be shown that in this setting, GDA will be a better algorithm than logistic regression; and more generally, even for small training set sizes, we would generally expect GDA to be better.

In contrast, by making significantly weaker assumptions, logistic regression is also more robust and less sensitive to incorrect modeling assumptions. There are many different sets of assumptions that would lead to p(y|x) taking the form of a logistic function. For example, if x|y = 0 ∼ Poisson(λ_0), and x|y = 1 ∼ Poisson(λ_1), then p(y|x) will be logistic. Logistic regression will also work well on Poisson data like this. But if we were to use GDA on such data—and fit Gaussian distributions to such non-Gaussian data—then the results will be less predictable, and GDA may (or may not) do well.

To summarize: GDA makes stronger modeling assumptions, and is more data efficient (i.e., requires less training data to learn “well”) when the modeling assumptions are correct or at least approximately correct. Logistic regression makes weaker assumptions, and is significantly more robust to deviations from modeling assumptions. Specifically, when the data is indeed non-Gaussian, then in the limit of large datasets, logistic regression will almost always do better than GDA. For this reason, in practice logistic regression is used more often than GDA.

<h3>Naive Bayes</h3>

In GDA, the feature vectors x were continuous, real-valued vectors. Let’s now talk about a different learning algorithm in which the x_j’s are discrete valued.

For our motivating example, consider building an email spam filter. We will represent an email via a feature vector whose length is equal to the number of words in the dictionary. The set of words encoded into the feature vector is called the vocabulary.

<img src="../2. Machine Learning/images/naive_bayes_1.jpg">

Even though the Naive Bayes assumption is an extremely strong assumptions, the resulting
algorithm works well on many problems.

<img src="../2. Machine Learning/images/naive_bayes_2.jpg">

When the original, continuous-valued attributes are not well modeled by a multivariate normal distribution, discretizing the features and using Naive Bayes (instead of GDA) will often result in a better classifier.

__Laplace smoothing__

If during inference your model comes across a word that it didn't see during training, it assigns a posterior probability of zero. To avoid this, we can use _Laplace smoothing_, which replaces the maximum likelihood estimate with

<img src="../2. Machine Learning/images/laplace_smoothing.jpg">

The two differences between the regular maximum likelihood estimate and the laplace smoothed one is that we have added a 1 to the numerator, and k to the denominator. This prevents the posterior probability from returning a zero when it encounters unseen words.


<h2>Kernel Methods</h2>


<h3>Feature maps</h3>


<h3>LMS (least mean squares) with features</h3>


<h3>LMS with the kernel trick</h3>


<h3>Properties of kernels</h3>






<h2>Support Vector Machines</h2>


<h3>Margins: Intuition</h3>



<h3>Notation</h3>



<h3>Functional and geometric margins</h3>



<h3>The optimal margin classifier</h3>



<h3>Lagrange duality</h3>



<h3>Optimal margin classifiers</h3>



<h3>Regularization and the non-separable case</h3>



<h3>The SMO algorithm</h3>


__Coordinate ascent__


__SMO__








<h2>Decision trees</h2>


<h2>Boosting algorithms and weak learning</h2>








<h1>Neural Networks</h1>


<h2>Deep Learning</h2>



<h2>Backpropagation</h2>



<h2>Evaluation Metrics</h2>



<h2>Regularization and model selection</h2>



<h2>Advice for Applying Machine Learning</h2>







<h1>Unsupervised Learning</h1>



<h2>k-means clustering</h2>



<h2>Mixture of Gaussians</h2>



<h2>The EM Algorithm</h2>



<h2>Factor analysis</h2>



<h2>Principal components analysis</h2>



<h2>Independent Components Analysis</h2>


<h2>Weak Supervision</h2>


<h2>On critiques of ML</h2>


<h2>Anomaly Detection</h2>


<h2>Recommender Systems</h2>






<h1>Reinforcement Learning and Control</h1>







<h1>Learning Theory</h1>
