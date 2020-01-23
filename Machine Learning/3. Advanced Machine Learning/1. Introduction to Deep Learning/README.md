<h1>Week 1: Introduction to optimization</h1>



<h2>Linear model as the simplest neural network</h2>


<h3>Linear regression</h3>

Linear models are building blocks for deep neural networks.

For prediction purposes linear models can sometimes outperform fancier nonlinear models, especially in situations
- with small numbers of training cases,
- low signal-to-noise ratio or sparse data.

For an input vector $X^{\top} = (X_1, X_2, \cdots, X_p)$, and a real valued output $Y$ to predict, the linear regression model has the form

$$f(X) = \beta_0 + \sum_{j=1}^p X_j \beta_j$$

where $\beta_j$'s are unknown parameters or coefficients and the variables $X_j$ can come from different sources:
- quantitative inputs;
- transformations of quantitative inputs, such as log, square-root or square;
- basis expansions, such as $X_2 = X_1^2, X_3 = X_1^3$, leading to a polynomial representation;
- numeric or “dummy” coding of the levels of qualitative inputs.
- interactions between variables, for example, $X_3 = X_1 \cdot X_2$

No matter the source of the Xj, the model is _linear in the parameters_.

<img src="../1. Introduction to Deep Learning/images/least_squares.jpg">

From a statistical point of view, this criterion is reasonable if the training observations $(x_i,y_i)$ represent independent random draws from their population. Even if the $x_i$’s were not drawn randomly, the criterion is still valid if the $y_i$’s are conditionally independent given the inputs $x_i$.

<img src="../1. Introduction to Deep Learning/images/least_squares_plot.jpg">

How do we minimize (3.2)? Denote by $X$ the matrix with each row an input vector, and let $y$ be the vector of outputs in the training set. Then we can write the residual sum-of-squares as

$$RSS(\beta) = (y - X \beta)^{\top} (y - X \beta)$$

By differentiating the above equation w.r.t $\beta$ we obtain the unique solution

$$\hat \beta = (X^{\top}X)^{-1} X^{\top} y$$

Therefore the fitted values at the training inputs are

$$\hat{y} = X \hat{\beta} = X (X^{\top}X)^{-1} X^{\top} y$$

The matrix $H = X (X^{\top}X)^{-1} X^{\top}$ is sometimes called the "hat" matrix.

<img src="../1. Introduction to Deep Learning/images/least_squares_prediction.jpg">

We minimize $RSS(\beta) = \|y − X \beta \|^2$ by choosing $\hat{\beta}$ so that the residual vector $y − \hat{y}$ is orthogonal to this subspace. This orthogonality is the result of assuming that $X$ has full column rank, meaning the columns of the matrix are linearly independent and hence $X^{\top}X$ is positive definite meaning it is a symmetric matrix with all positive eigenvalues. The resulting estimate $\hat{y}$ is hence the _orthogonal projection_ of y onto this subspace. The hat matrix $H$ computes the orthogonal projection, and hence it is also known as a projection matrix.

It might happen that the columns of $X$ are not linearly independent, so that $X$ is not of full rank. This would occur, for example, if two of the inputs were perfectly correlated, (e.g., $x_2 = 3x_1)$. Then $X^{\top}X$ is singular and the least squares coefficients $\hat{\beta}$ are not uniquely defined. However, the fitted values $\hat{y} = X \hat{\beta}$ are still the projection of $y$ onto the column space of $X$; there is just more than one way to express that projection in terms of the column vectors of $X$. The non-full-rank case occurs most often when one or more qualitative inputs are coded in a redundant fashion. There is usually a natural way to resolve the non-unique representation, by recoding and/or dropping redundant columns in $X$.

Rank deficiencies can also occur in signal and image analysis, where the number of inputs p can exceed the number of training cases N. In this case, the features are typically reduced by filtering or else the fitting is controlled by regularization.

Up to now we have made minimal assumptions about the true distribution of the data. In order to pin down the sampling properties of $\hat{\beta}$, we now assume that the observations $y_i$ are uncorrelated and have constant variance $\sigma^2$, and that the $x_i$ are fixed (non random). The variance–covariance matrix of the least squares parameter estimates is then given by

$$Var(\hat{\beta}) = (X^{\top} X)^{-1} \sigma^2$$

To draw inferences about the parameters and the model, additional assumptions are needed. We now assume that the linear regression model is the correct model for the mean; that is, the conditional expectation of Y is linear in $X_1, \cdots ,X_p$. We also assume that the deviations of Y around its expectation are additive and Gaussian. Hence

$$Y = E(Y | X_1, \cdots, X_p) + \epsilon \\
= \beta_0 + \sum_{j=1}^p X_j \beta_j + \epsilon
$$

where the error $\epsilon$ is a Gaussian random variable with expectation zero and variance $\sigma^2$. This is a multivariate normal distribution with mean vector and variance–covariance matrix as shown.

In addition $\hat{\beta}$ and $\hat{\sigma}^2$ are statistically independent. We use these distributional properties to form tests of hypothesis and confidence intervals for the parameters $\beta_j$.

<h3>Linear classification</h3>

Since our predictor G(x) takes values in a discrete set $\mathcal{G}$, we can always divide the input space into a collection of regions labeled according to the classification. The boundaries of these regions can be rough or smooth, depending on the prediction function. For an important class of procedures, these decision boundaries are linear; this is what we mean by linear methods for classification.

<img src="../1. Introduction to Deep Learning/images/binary_classification.jpg">

When your labels are either 1 or -1, you essentially have a linear model which needs to be transformed in someway to get -1 or 1, this can be easily done using sine.

For a multi-class classification problem with K classes:

<img src="../1. Introduction to Deep Learning/images/multi_class_classification.png">

Here we build a separate classifier for each class and assign the sample the class which gives the largest score among all the classifiers.

Now, that we have a model, we need a loss function so the model can learn, let's take the simplest one, accuracy loss:

$$\frac{1}{l} \sum_{i=1}^l [a(x_i) = y_i]$$

Accuracy is just a ratio of correctly classifying points in our training set. This metric is good and could be easily interpreted, but it has two disadvantages:

- It is not differentiable
- Doesn't assess model confidence

Accuracy doesn't work so what about mean squared error:

<img src="../1. Introduction to Deep Learning/images/mse_classification.png">

Here if our model predicts one, then the guess is correct and the loss is zero. If our model gives a prediction between zero and one, then it's unconfident in its decision and we penalize it for low confidence. If the model gives the value lower than zero, then it misclassifies this point. So we give it an even larger penalty. That's okay, but if the model predicts a value larger than one, then we penalize it. We penalize it for high confidence, and that's not very good. So what if we just take one branch of it:

<img src="../1. Introduction to Deep Learning/images/classification_branch_loss.png">

There are many loss functions that look like this one, and all of them lead to their own classification methods. We will look into logistic regression, but first we need to convert our scores from linear classifiers to probability distribution:

<img src="../1. Introduction to Deep Learning/images/logits.png">

We have some vector of scores z, which has components w transposed by x, though these are scores for each of our classes. Dot products can have any sign and have any magnitude. So we cannot interpret them as probability distributions, and we should somehow change it. We'll do it in two steps. At first step, we take first component of our vector and take e to the degree of this component and we do the same for all the components. So, after this step, we have a vector e to the degree of z that has only positive coordinates. So now we need only to normalize these components to get a distribution. We can interpret it as a probability distribution. This transform is called a _softmax function_.

Now that we have a probability distribution of scores, we need to measure the distance between the predicted distribution and the target distribution. To do it, we use _cross entropy_:

<img src="../1. Introduction to Deep Learning/images/entropy.png">

Cross entropy is just a minus log of the predicted class probability for the true class.

<img src="../1. Introduction to Deep Learning/images/cross_entropy_loss.png">

<h3>Gradient descent</h3>

Gradient descent is a generic method that can optimize any differentiable loss function.

<img src="../1. Introduction to Deep Learning/images/gradient_descent.png">

<img src="../1. Introduction to Deep Learning/images/gradient_descent_pseudo_code.png">

<img src="../1. Introduction to Deep Learning/images/gradient_descent_plot.jpg">

<img src="../1. Introduction to Deep Learning/images/mse_derivative.png">

There is an analytical solution to mean squared error but gradient descent has a lot of advantages over the analytical solution:
- Easy to implement
- Very general, can be applied to any differentiable loss function
- Requires less memory and computations (for stochastic methods)

But there is a situation when analytical solution for linear model and MSE loss can be effective, for example when you have a small number of features (about 100 or less). In such cases matrix $X^{\top} X$ is not very large and can be easily inverted.


<h2>Regularization in machine learning</h2>


<h3>Overfitting problem and model validation</h3>

Overfitting is when the data memorizes the training set and performs well on the training set and fails to perform on a test set.

<img src="../1. Introduction to Deep Learning/images/overfitting_example.jpg">

<h3>Model regularization</h3>

Usually overfitted models have large weights and good models tend to not have very large weights and we can look into solving overfitting in terms of the size of the weights. To reduce the size of the weight, we modify our loss function to include a regularizing term $\lambda R (w)$:

<img src="../1. Introduction to Deep Learning/images/regularization.jpg">

Lambda, the regularization strength controls the tradeoff between model quality on a training set and model complexity.

__Ridge Regression__

For example, we can use _L2 penalty_ as a regularizer where $\|w\| = \sum_{j=1}^d w_j^2$. This regularizer drives all the coefficient closer to zero. So it penalizes our model for very large weights.

It can be shown this unconstrained optimization problem is equivalent to constraint optimization problem:

<img src="../1. Introduction to Deep Learning/images/l2_penalty.jpg">

where there is a one to one correspondence between C and lambda regularization strength.

The ridge solutions are not equivariant under scaling of the inputs, and so one normally standardizes the inputs before solving.

__Lasso Regression__

There is another penalty called _L1 penalty_ where $\|w\|_1 = \sum_{j=1}^d |w_j|$. This drives some weights exactly to zero and is able to learn sparse models but L1 penalty can't be optimized with simple gradient methods because the derivative of an absolute value is zero so we need other optimization techniques. We can also show that this unconstrained optimization problem is equivalent to constraint optimization problem.

There are other regularization techniques:
- Dimensionality reduction
- Data Augmentation
- Dropout
- Early Stopping
- Collect more data


<h2>Stochastic methods for optimization</h2>


<h3>Stochastic gradient descent</h3>

In gradient descent, if we take our loss function as mean squared error, to make one update, we have to sum all the squared errors and this grows huge with increasing number of examples. To overcome this problem we use _stochastic gradient descent_.

<img src="../1. Introduction to Deep Learning/images/stochastic_gradient_descent.jpg">

Stochastic gradient descent is very similar to gradient descent with only one difference. We start with some initialization $w^0$, and then on every step at a time t, we select some random example from our training set and calculate the gradient only on this example and then we take a step in the direction of this gradient. So in stochastic gradient descent we approximate the gradient of all the loss function by the gradient of loss function on only one example.

This can lead to noisy updates due to using one example at a time but on the other hand, it only needs one example on each step and can be used in online settings. One thing we should be careful about is choosing the learning rate. Since the updates are made per example, having too large of a learning rate or too small can lead to overshooting from global minima or getting stuck on local minima. To overcome some of the problems, we can use _mini-batch gradient descent_.

<img src="../1. Introduction to Deep Learning/images/mini_batch_gradient_descent.jpg">

In mini-batch gradient descent, on every iteration we choose m random examples from our training sample. The updates of mini-batch gradient descent have much less noise than stochastic gradient descent and this might still can be used in online learning setting. But the learning rate still should be chosen carefully.

<h3>Gradient descent extensions</h3>

If our function is difficult, for example, it has elliptic level lines then gradient descent will oscillate, and it will take many iterations for it to converge to the minimum. To improve this, we can somehow change our gradient descent methods.

__Momentum__

In this method, we maintain additional vector h at every iteration.

<img src="../1. Introduction to Deep Learning/images/momentum_gradient_descent.jpg">

$h_t$ is just a weighted sum of gradients from all iterations. Suppose that we have some function and for some coordinates of our parameter vector the gradients always have the same sign, so they lead us to the minimum. And for some coordinates, the sign of the gradient changes from iteration to iteration. So, vector $h_t$ would be large for component where gradients have the same sign on every iteration, and will make large steps by this coordinates. And for coordinates that change sign, they will just cancel each other and ht will be close to zero. So, $h_t$ cancels some coordinates that lead to oscillation of gradients, and help us to achieve better convergence.

__Nesterov Momentum__

Nesterov momentum is an extension of the momentum method. In simple momentum method, on every iteration, we calculate the gradient at current point $w^{t-1}$. We take a gradient step from it by $g_t$, and we then get our momentum, $h_t$. But since it's certain that we'll move in the direction of the momentum, it will be more clever to, first, step in the direction of $h_t$ to get some new approximation of parameter vector. And then to calculate gradient at the new point, $w^{t-1} + (-h_t)$.

<img src="../1. Introduction to Deep Learning/images/nesterov_momentum.jpg">

In practice, this method indeed leads to better convergence than momentum method.

Momentum method and Nesterov momentum method work better with difficult functions with complex level sets. But they still require to choose learning rate, and they're very sensitive to it. So now we'll discuss some other optimization methods that try to choose learning rate adaptively, so we don't have to choose it ourselves.

__AdaGrad__

AdaGrad method chooses learning rate adaptively.

<img src="../1. Introduction to Deep Learning/images/AdaGrad.jpg">

But since the auxiliary parameter, G accumulates squares of gradient, and at some step it can become too large. So to somehow overcome this, we need some other methods like AdaGrad. Another advantage of AdaGrad is that it chooses its own learning rate for each example.

__RMSprop__

RMSprop is very similar to AdaGrad, but here we take an exponentially weighted average of squares of gradients on every step.

<img src="../1. Introduction to Deep Learning/images/RMSprop.jpg">

This method overcomes the problem of large sums of square gradients. And here, our learning rate depends only on last examples from our gradient descent method.

__Adam__

In RMSprop, we maintained an additional variable, and it will be augmented by $v^t_j$. And is just an exponentially weighted sum of gradients from all iterations. As we go from momentum method, an approximation of gradient from one step can be noisy and lead to oscillations. So to smooth our gradients we maintain another auxiliary variable, $m^t_j$, that is essentially a sum of gradients.

<img src="../1. Introduction to Deep Learning/images/Adam.jpg">



<h1>Week 2: Introduction to neural networks</h1>



<h3>Perceptrons</h3>

A perceptron takes several binary inputs, $x_1, x_2, \cdots,$ and produces a single binary output. Weights, $w_1, w_2, \cdots,$ real numbers express the importance of the respective inputs to the output. The neuron's output, 0 or 1, is determined by whether the weighted sum $\sum_j w_j x_j$ is less than or greater than some threshold value, (-bias). Just like the weights, the threshold is a real number which is a parameter of the neuron.

A network of perceptrons can be used to simulate a circuit containing many NAND gates. And because NAND gates are universal for computation, it follows that perceptrons are also universal for computation. The computational universality of perceptrons is simultaneously reassuring and disappointing. It's reassuring because it tells us that networks of perceptrons can be as powerful as any other computing device. But it's also disappointing, because it makes it seem as though perceptrons are merely a new type of NAND gate. That's hardly big news!

<h3>Sigmoid neurons</h3>

Let's say we want to devise a learning algorithm that can automatically tune the weights and biases of a network of artificial neurons. We can define learning as when we make a small change in some weight (or bias) in the network, this small change in weight causes a small corresponding change in the output of the network.

Now, if our network contains perceptrons, a small change in the weights or bias of any single perceptron in the network can sometimes cause the output of that perceptron to completely flip, say from 0 to 1. That flip may then cause the behaviour of the rest of the network to completely change in some very complicated way. We can overcome this problem by introducing a new type of artificial neuron called a _sigmoid neuron_.

Sigmoid neurons are similar to perceptrons, but modified so that small changes in their weights and bias cause only a small change in their output. Just like a perceptron, the sigmoid neuron has inputs, but instead of being just 0 or 1, these inputs can also take on any values between 0 and 1. Also just like a perceptron, the sigmoid neuron has weights for each input and an overall bias b, but the output is not 0 or 1. Instead it's $σ (w \cdot x + b)$ where σ is called the _sigmoid function_ (a.k.a _logistic function_) and is defined by:

$$σ(z) = \frac{1}{1 + e^{-z}}$$

<img src="../1. Introduction to Deep Learning/images/activation_functions.jpg">

The purpose of activation functions is to introduce non-linearities into the network.


<h2>The simplest neural network: MLP</h2>


<h3>Multilayer perceptron (MLP)</h3>

<img src="../1. Introduction to Deep Learning/images/neuron.jpg">

MLP Notation:

<img src="../1. Introduction to Deep Learning/images/mlp_notation.jpg">

With these notations, the activation $a^l_j$ of the jth neuron in the lth layer is related to the activations in the (l−1)th layer by the equation

<img src="../1. Introduction to Deep Learning/images/activation.jpg">

To rewrite the above expression in a matrix form, we define a weight matrix $w^l$ for each layer, $l$. The entries of the weight matrix $w^l$ are just the weights connecting to that layer l. Similarly, for each layer l we define a bias vector, $b^l$. The last ingredient is the vectorizing function $\sigma$. With these notations, we can write the vectorized form of activation as:

<img src="../1. Introduction to Deep Learning/images/vectorized_activation.jpg">

<img src="../1. Introduction to Deep Learning/images/w_and_b.jpg">

<img src="../1. Introduction to Deep Learning/images/activation_to_matrix.jpg">

<h3>Chain rule</h3>

<img src="../1. Introduction to Deep Learning/images/chain_rule.jpg">

<img src="../1. Introduction to Deep Learning/images/computation_graph_derivative.jpg">

<h3>Backpropagation</h3>

__Backpropagation vs SGD__

Backpropagation is an efficient method of computing gradients in directed graphs of computations, such as neural networks. This is not a learning method, but rather a nice computational trick which is often used in learning methods. This is actually a simple implementation of chain rule of derivatives, which simply gives you the ability to compute all required partial derivatives in linear time in terms of the graph size (while naive gradient computations would scale exponentially with depth).

SGD is one of many optimization methods, namely first order optimizer, meaning, that it is based on analysis of the gradient of the objective. Consequently, in terms of neural networks it is often applied together with backpropagation to make efficient updates. You could also apply SGD to gradients obtained in a different way (from sampling, numerical approximations etc.). Symmetrically you can use other optimization techniques with backpropagation as well, everything that can use gradient/jacobian.

__Backpropagation__

The goal of backpropagation is to compute the partial derivatives ∂C/∂w and ∂C/∂b of the cost function C with respect to any weight w or bias b in the network.

<img src="../1. Introduction to Deep Learning/images/backpropagation_chain.jpg">

For backpropagation to work we need to make two main assumptions about the form of the cost function.

1. The cost function can be written as an average $C = \frac{1}{n} \sum_x C_x$ over cost functions $C_x$ for individual training examples, $x$. The reason we need this assumption is because what backpropagation actually lets us do is compute the partial derivatives $\partial C_x / \partial w$ and $\partial C_x / ∂b$ for a single training example. We then recover ∂C/∂w and ∂C/∂b by averaging over training examples.

2. The cost can be written as a function of the outputs from the neural network, cost C = $C(a^L)$. For example, the quadratic cost function satisfies this requirement, since the quadratic cost for a single training example x may be written as:

<img src="../1. Introduction to Deep Learning/images/quadratic_cost.jpg">

__The four fundamental equations behind backpropagation__

Backpropagation is about understanding how changing the weights and biases in a network changes the cost function. Ultimately, this means computing the partial derivatives $\partial C / \partial w_{jk}^l$ and $\partial C / \partial b_j^l$. But to compute those, we first introduce an intermediate quantity, $\delta_j^l$, which we call the error in the jth neuron in the lth layer. Backpropagation will give us a procedure to compute the error $\delta_j^l$, and then will relate $\delta_j^l$ to $\partial C / \partial w_{jk}^l$ and $\partial C / \partial b_j^l$.

We define the error $\delta_j^l$ as:

$$\delta_j^l \equiv \frac{∂C}{∂z^l_j}$$

Backpropagation is based around four fundamental equations. Together, those equations give us a way of computing both the error $\delta_j^l$ and the gradient of the cost function.

1. An equation for the error in the output layer:

$$δ^L_j = \frac{∂C}{∂a^L_j} σ′(z^L_j)$$

The first term on the right measures how fast the cost is changing as a function of the jth output activation. The second term on the right measures how fast the activation function σ is changing at $z^L_j$.

We can rewrite the above equation in a matrix-based form, as

$$δ^L = ∇_aC ⊙ σ′(z^L)$$

2. An equation for the error in terms of the error in the next layer:

$$δ^l = ((w^{l+1})^{\top} δ^{l+1}) ⊙ σ′(z^l)$$

Suppose we know the error $δ^{l+1}$ at the (l+1)th layer. When we apply the transpose weight matrix, $w^{l+1})^{\top}$, we can think intuitively of this as moving the error backward through the network, giving us some sort of measure of the error at the output of the lth layer.

By combining equation  1 and 2, we can compute the error for any layer in the network.

3. An equation for the rate of change of the cost with respect to any bias in the network:

$$\frac{∂C}{∂b^l_j} = δ_j^l$$

4. An equation for the rate of change of the cost with respect to any weight in the network:

$$\frac{∂C}{∂w^l_{jk}} = a_k^{l-1} δ_j^l$$

A weight will learn slowly if either the input neuron is low-activation (the σ function becomes very flat when $σ(z^L_j)$ is approximately 0 or 1. When this occurs we will have $σ′(z^L_j) \approx 0)$, or if the output neuron has saturated, i.e., is either high- or low-activation.

__The backpropagation algorithm__

<img src="../1. Introduction to Deep Learning/images/backpropagation_equations.jpg">

<img src="../1. Introduction to Deep Learning/images/backpropagation_algorithm.jpg">

In practice, it's common to combine backpropagation with a learning algorithm such as stochastic gradient descent, in which we compute the gradient for many training examples.

<img src="../1. Introduction to Deep Learning/images/gradient_descent_with_backprop.jpg">

The backpropagation algorithm is a clever way of keeping track of small perturbations to the weights (and biases) as they propagate through the network, reach the output, and then affect the cost.

Review these videos from 3Blue1Brown:
- [But what is a Neural Network? | Deep learning, chapter 1](https://www.youtube.com/watch?v=aircAruvnKk&t=922s)
- [Gradient descent, how neural networks learn | Deep learning, chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w&t=8s)
- [What is backpropagation really doing? | Deep learning, chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U&t=579s)
- [Backpropagation calculus | Deep learning, chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8)



<h2>Matrix derivatives</h2>


<h3>Efficient MLP implementation</h3>

<img src="../1. Introduction to Deep Learning/images/matrix_multiplication.jpg">

<img src="../1. Introduction to Deep Learning/images/backward_pass_dense.jpg">

<img src="../1. Introduction to Deep Learning/images/gradient_vector.jpg">

<img src="../1. Introduction to Deep Learning/images/python_passes.jpg">

<h3>Other matrix derivatives</h3>

<img src="../1. Introduction to Deep Learning/images/jacobian.jpg">


<h2>Philosophy of deep learning</h2>


<h3>What Deep Learning is and is not</h3>

__Downsides__

- No Core theory
    - Relies on intuitive reasoning
- Needs tons of data
    - You need either large dataset or heavy wizardy
- Computationally heavy
    - Running on mobiles/embedded is a challenge
- Pathologically overhyped
    - People expect of it to make wonders

Deep learning is a language in which you can hint your model on what you want it to learn.

<h3>Deep learning as a language</h3>

A way of producing hints is by the way you train the model.



<h1>Week 3: Deep Learning for Images</h1>



<h2>Introduction to CNN</h2>


<h3>Motivation for convolutional layers</h3>

<img src="../1. Introduction to Deep Learning/images/image_representation.jpg">

A MLP can't be used for image related tasks because:
1. If an object is in different position than where it was in during training in an image, the network won't be able to identify it because it optimized the neurons in specific locations using backpropagation to learn the object as it was on the training image.

<img src="../1. Introduction to Deep Learning/images/cat_mlp.jpg">

Convolution is a dot product of a kernel, or a filter, and a patch of an image (local receptive field) of the same size:

<img src="../1. Introduction to Deep Learning/images/convolution.jpg">

<img src="../1. Introduction to Deep Learning/images/convolution_example.jpg">

<img src="../1. Introduction to Deep Learning/images/convolution_correlation.jpg">

Convolution is the same as cross-correlation with a flipped kernel, but here we are performing the convolution operation without flipping the filter. This is referred to as the cross-correlation operation in literature. Computationally this difference does not affect the performance of the algorithm because the kernel is being trained such that its weights are best suited for the operation, thus adding the flip operation would simply make the algorithm learn the weights in different cells of the kernel to accommodate the flip. So we can omit the flip.

Another interesting property of convolution is translation equivariance. It means that if we move the input (translate) and imply convolution, it will actually act the same as if we first applied convolution, and then translated an image.

<img src="../1. Introduction to Deep Learning/images/convolution_translation.jpg">

<h3>Understanding Convolutions</h3>

The standard definition of convolution:

<img src="../1. Introduction to Deep Learning/images/convolution_definition.jpg">

Convolutions are an extremely general idea. We can also use them in a higher number of dimensions. For example in a 2D case, a, b and c becomes vectors.

__Convolution: The Operation__

The 2D convolution is a fairly simple operation at heart: you start with a kernel, which is simply a small matrix of weights. This kernel “slides” over the 2D input data, performing an element-wise multiplication with the part of the input it is currently on, and then summing up the results into a single output pixel.

<img src="../1. Introduction to Deep Learning/images/2d_convolution.gif">

The size of the kernel directly determines how many (or few) input features get combined in the production of a new output feature. Therefore it has a direct impact on whether or not an input feature falls within roughly the same location of the input pixel on the output layer.

__Convolutional vs fully connected layer__

In convolutional layer, the same kernel is used for every output neuron, and that way, we share parameters of the network and train a better model, this introduces sparsity, here parameters are the weights of the network. Saying that the weights are the same is the same thing as saying that multiple neurons are identical.

The difference between fully connected layer and a convolutional layer is, in a fully connected layer each output feature will be weighted by every single input feature, whereas in a convolutional layer, the output feature looks at input features coming from roughly the same location.

__The Multi-Channel Version__

In the 1 channel case, where the term filter and kernel are interchangeable, in the general case, they’re actually pretty different. Each filter actually happens to be a collection of kernels, with there being one kernel for every single input channel to the layer, and each kernel being unique.

Each filter in a convolution layer produces one and only one output channel, and they do it like so:

- Each of the kernels of the filter “slides” over their respective input channels, producing a processed version of each. Some kernels may have stronger weights than others, to give more emphasis to certain input channels than others (eg. a filter may have a red kernel channel with stronger weights than others, and hence, respond more to differences in the red channel features than the others).

    <img src="../1. Introduction to Deep Learning/images/filters_a.gif">

- Each of the per-channel processed versions are then summed together to form one channel. The kernels of a filter each produce one version of each channel, and the filter as a whole produces one overall output channel.

    <img src="../1. Introduction to Deep Learning/images/filters_b.gif">

- Finally, then there’s the bias term. The way the bias term works here is that each output filter has one bias term. The bias gets added to the output channel so far to produce the final output channel.

    <img src="../1. Introduction to Deep Learning/images/filters_c.gif">

Each filter processes the input with its own, different set of kernels and a scalar bias with the process described above, producing a single output channel. They are then concatenated together to produce the overall output, with the number of output channels being the number of filters. A nonlinearity is then usually applied before passing this as input to another convolution layer, which then repeats this process.

__Convolution: The Intuition__

The convolution, as a whole, is still a linear transformation, but at the same time it’s also a dramatically different kind of transformation. For a matrix with 64 elements, there’s just 9 parameters which themselves are reused several times. Each output node only gets to see a select number of inputs (the ones inside the kernel). There is no interaction with any of the other inputs, as the weights to them are set to 0.

So with backpropagation coming in all the way from the classification nodes of the network, the kernels have the interesting task of learning weights to produce features only from a set of local inputs. Additionally, because the kernel itself is applied across the entire image, the features the kernel learns must be general enough to come from any part of the image.

Each kernel in a filter is randomly initialized to some distribution (Normal, Gaussian, etc.). By having different initialization criteria, each kernel gets trained slightly differently. They eventually learn to detect different features in the image.

CNNS understand two things: first, they understand a decomposition of their visual input space as a hierarchical-modular network of convolution filters, and second, they understand a probabilistic mapping between certain combinations of these filters and a set of arbitrary labels.

__Spatial arrangement__

Three hyperparameters control the size of the output volume: the depth, stride and zero-padding.

1. First, the _depth_ of the output volume is a hyperparameter: it corresponds to the number of filters we would like to use, each learning to look for something different in the input. For example, if the first Convolutional Layer takes as input the raw image, then different neurons along the depth dimension may activate in presence of various oriented edges, or blobs of color. We will refer to a set of neurons that are all looking at the same region of the input as a depth column (some people also prefer the term fibre).

2. Second, we must specify the _stride_ with which we slide the filter. When the stride is 1 then we move the filters one pixel at a time. When the stride is 2 (or uncommonly 3 or more, though this is rare in practice) then the filters jump 2 pixels at a time as we slide them around. This will produce smaller output volumes spatially.

3. As we will soon see, sometimes it will be convenient to pad the input volume with zeros around the border. The size of this _zero-padding_ is a hyperparameter. The nice feature of zero padding is that it will allow us to control the spatial size of the output volumes (most commonly as we’ll see soon we will use it to exactly preserve the spatial size of the input volume so the input and output width and height are the same).

__Receptive Field__

A essential design choice of any CNN architecture is that the input sizes grow smaller and smaller from the start to the end of the network, while the number of channels grow deeper. This, as mentioned earlier, is often done through strides or pooling layers. Locality determines what inputs from the previous layer the outputs get to see. The receptive field determines what area of the original input to the entire network the output gets to see.

<img src="../1. Introduction to Deep Learning/images/color_image.jpg">

<img src="../1. Introduction to Deep Learning/images/kernel_not_enough.jpg">

<img src="../1. Introduction to Deep Learning/images/receptive_field.jpg">

So to grow the receptive field faster, we can increase the _stride_ in our convolutional layer to reduce the output dimensions.

__Strides__

<img src="../1. Introduction to Deep Learning/images/stride.jpg">

But how do we maintain translational invariance with the stride? We use pooling layers.

__The Pooling Layer__

The pooling kernel does not have any weights associated with it; it simply applies an aggregation function (e.g. mean, max) to all of the pixel values contained within its receptive field and sends that value to the output array.

The function of the pooling layer is to progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network, and hence to also control overfitting.

<img src="../1. Introduction to Deep Learning/images/pooling.jpg">

A major benefit of pooling is also a major disadvantage of CNNs. Pooling encourages location invariance by helping the network be more tolerant of small shifts in images. But this looses relational information on objects.

__Computing Spatial Size of Output volume__

We can compute the spatial size of the output volume as a function of the input volume size (W), the receptive field size of the Conv Layer neurons (F), the stride with which they are applied (S), and the amount of zero padding used (P) on the border. You can convince yourself that the correct formula for calculating how many neurons “fit” is given by (W − F + 2P) / S + 1.

For example for a 7x7 input and a 3x3 filter with stride 1 and pad 0 we would get a 5x5 output. With stride 2 we would get a 3x3 output.

__Calculating the number of Parameters__

- Convolutional layers: (n * m * l) * k + k = ((n * m * k) + 1) * k, where
n,m=filter size,
l=number of feature maps as inputs (For inputs it will be the number of channels),
k=number of filters.

- Fully Connected Layer: (n + 1) * m, where n=inputs, m=outputs.

__Backpropagation for CNN__

Gradients are first calculated as if the kernel weights were not shared. Then the gradients of the same shared weights are summed up.

<img src="../1. Introduction to Deep Learning/images/convolution_backprop.jpg">

- Forward Pass:

<img src="../1. Introduction to Deep Learning/images/backprop_forward.jpg">

- Backward Pass

We can assume that we get 𝜕h as input (from the backward pass of the next layer) and our aim is to calculate 𝜕w and 𝜕x. It is important to understand that 𝜕x (or 𝜕h for previous layer) would be the input for the backward pass of the previous layer. We are basically obtaining the gradients w.r.t feature maps and use that to calculate the weights for the filter maps.

<img src="../1. Introduction to Deep Learning/images/backprop_backward.gif">

<img src="../1. Introduction to Deep Learning/images/backprop_backward.jpg">

- _Pooling layer_: Backpropagation of the pooling layer computes the error which is acquired by the single value “winning unit” since at the pooling layer, forward propagation results in an NxN block being reduced to a single value.

    To keep track of the “winning unit” its index noted during the forward pass and used for gradient routing during backpropagation. Gradient routing is done in the following ways:

    - Max-pooling - the error is just assigned to where it comes from - the “winning unit” because other units in the previous layer’s pooling blocks did not contribute to it hence all the other assigned values of zero.

    - Average pooling - the error is multiplied by 1/N×N and assigned to the whole pooling block (all units get this same value).


<h2>Modern CNNs</h2>


<h3>Training tips and tricks for deep CNNs</h3>

__Activation Functions__

- Sigmoid Activation

<img src="../1. Introduction to Deep Learning/images/sigmoid_activation.jpg">

For huge positive or huge negative argument (like 10 or -10) the sigmoid function derivative becomes close to 0. Using the chain rule when we will multiply further gradients by this small number it will lead to slow convergence. This is called the problem of vanishing gradients.

The plot below shows the sigmoid activation function and its first derivative:

<img src="../1. Introduction to Deep Learning/images/sigmoid_activation_derivative.jpg">

Two other problems are, one the output of the sigmoid is not zero centered, remember  that neural networks like when the inputs have zero mean and standard variance (normalized). Two, the exponent of x is computationally expensive.

- Tanh Activation

<img src="../1. Introduction to Deep Learning/images/tanh_activation.jpg">

Is zero centered but pretty much like sigmoid

- ReLu Activation

<img src="../1. Introduction to Deep Learning/images/relu_activation.jpg">

Is fast to compute, its gradients do not vanish for positive x's, and in practice it provides faster convergence. But it has problems too, one it is not zero centered, and two, it can die because this activation function is zero for a negative axis. Which means that if you're unlucky during initialization of your neuron, you can have weights that will give you zero activation and this neuron will never update because for that part where x is less than zero, you have zero gradient.

- Leaky ReLu Activation

<img src="../1. Introduction to Deep Learning/images/leaky_relu_activation.jpg">

__Weights Initialization__

- Zero initialization: Fails to break symmetry because neurons in the same layer will learn the same thing (because of backpropagation they will always get the same updates).

-  Linear models work best when inputs are normalized. Neuron is a linear combination of inputs plus activation. Neuron output will be used by consecutive layers. That means that it would be great if we can normalize the outputs of the neuron.

- It's important to constrain the variance of hidden outputs in our network. Because that leads to constrained gradients and that leads to better convergence. When gradients of different outputs become of different scale (like 1 to 100) gradient descent methods slow down drastically, this is called ill-conditioning.

__Batch Normalization__

Batch normalization that controls mean and variance of outputs before activations.

<img src="../1. Introduction to Deep Learning/images/batch_normalization.jpg">

- Why normalize images by subtracting datasets' image mean?

Subtracting the dataset mean serves to "center" the data. Additionally, you ideally would like to divide by the sttdev of that feature or pixel as well if you want to normalize each feature value to a z-score.

The reason we do both of those things is because in the process of training our network, we're going to be multiplying (weights) and adding to (biases) these initial inputs in order to cause activations that we then backpropagate with the gradients to train the model. We'd like in this process for each feature to have a similar range so that our gradients don't go out of control (and that we only need one global learning rate multiplier).

Another way you can think about it is deep learning networks traditionally share many parameters - if you didn't scale your inputs in a way that resulted in similarly-ranged feature values (ie: over the whole dataset by subtracting mean) sharing wouldn't happen very easily because to one part of the image weight w is a lot and to another it's too small.

- Covariate Shift

Covariate shift refers to the change in the distribution of the input values to a learning algorithm. For instance, if the train and test sets come from entirely different sources (e.g. training images come from the web while test images are pictures taken on the iPhone), the distributions would differ.

In the context of deep learning, we are particularly concerned with the change in the distribution of the inputs to the inner nodes within a network. A neural network changes the weights of each layer over the course of training. This means that the activations of each layer change as well. Since the activations of a previous layer are the inputs of the next layer, each layer in the neural network is faced with a situation where the input distribution changes with each step. This is problematic because it forces each intermediate layer to continuously adapt to its changing inputs.

The basic idea behind batch normalization is to limit covariate shift by normalizing the activations of each layer (transforming the inputs to be mean 0 and unit variance). This, supposedly, allows each layer to learn on a more stable distribution of inputs, and would thus accelerate the training of the network.

In practice, restricting the activations of each layer to be strictly 0 mean and unit variance can limit the expressive power of the network. Therefore, in practice, batch normalization allows the network to learn parameters $\gamma$  and $\beta$  that can convert the mean and variance to any value that the network desires.

<img src="../1. Introduction to Deep Learning/images/batch_normalization_2.jpg">

__Dropout__

<img src="../1. Introduction to Deep Learning/images/dropout.jpg">

<h3>Overview of modern CNN architectures</h3>

__AlexNet__

<img src="../1. Introduction to Deep Learning/images/alexnet.jpg">

__VGG (2015)__

<img src="../1. Introduction to Deep Learning/images/vgg.jpg">

__Inception V3 (2015)__

<img src="../1. Introduction to Deep Learning/images/inception.jpg">

- 1x1 Convolutions

<img src="../1. Introduction to Deep Learning/images/1_1_convolutions.jpg">

- Basic Inception Block

<img src="../1. Introduction to Deep Learning/images/inception_block.jpg">

__ResNet (2015)__

<img src="../1. Introduction to Deep Learning/images/resnet.jpg">

- Residual Connections

<img src="../1. Introduction to Deep Learning/images/residual_connections.jpg">


<h2>Applications of CNNs</h2>


<h3>Learning new tasks with pre-trained CNNs</h3>

__Transfer Learning__


<h3>A glimpse of other Computer Vision tasks</h3>

<img src="../1. Introduction to Deep Learning/images/other_cv_tasks.jpg">

__Semantic Segmentation__

- Max unpooling

- Learnable unpooling


__Object Detection + localization__



<h1>Week 4: Unsupervised representation learning</h1>



<h2>Intro to Unsupervised Learning</h2>


<h3>Unsupervised learning: what it is and why bother</h3>



<h2>Autoencoders</h2>


<h3>Autoencoders 101</h3>

Autoencoders are an unsupervised learning technique in which we leverage neural networks for the task of representation learning. Specifically, we'll design a neural network architecture such that we impose a bottleneck in the network which forces a compressed knowledge representation of the original input. If the input features were independent of one another, this compression and subsequent reconstruction would be a very difficult task. However, if some sort of structure exists in the data (ie. correlations between input features), this structure can be learned and consequently leveraged when forcing the input through the network's bottleneck.

<img src="../1. Introduction to Deep Learning/images/autoencoder.jpg">

This network can be trained by minimizing the reconstruction error which measures the differences between our original input and the consequent reconstruction.

The ideal autoencoder model balances the following:
- Sensitive to the inputs enough to accurately build a reconstruction.
- Insensitive enough to the inputs that the model doesn't simply memorize or overfit the training data.

This trade-off forces the model to maintain only the variations in the data required to reconstruct the input without holding on to redundancies within the input. For most cases, this involves constructing a loss function where one term encourages our model to be sensitive to the inputs (ie. reconstruction loss) and a second term discourages memorization/overfitting (ie. an added regularizer).

Autoencoders may be thought of as being a special case of feed forward networks and may be trained with all the same techniques, typically mini-batch gradient descent following gradients computed by back-propagation.

<h3>Autoencoder architecture</h3>

__Undercomplete autoencoder__

The simplest architecture for constructing an autoencoder is to constrain the number of nodes present in the hidden layer(s) of the network, limiting the amount of information that can flow through the network. An autoencoder whose code dimension is less than the input dimension is called undercomplete.

<img src="../1. Introduction to Deep Learning/images/undercomplete_autoencoder.jpg">

An undercomplete autoencoder has no explicit regularization term - we simply train our model according to the reconstruction loss. Thus, our only way to ensure that the model isn't memorizing the input data is to ensure that we've sufficiently restricted the number of nodes in the hidden layers.

__PCA vs Autoencoders__

An undercomplete autoencoder learns to span the same subspace as PCA and can be thought of as a more powerful (nonlinear) generalization of PCA since they are built from neural networks which are capable of learning nonlinear relationships. PCA attempts to discover a lower dimensional hyperplane which describes the original data, whereas autoencoders are capable of learning nonlinear manifolds (a manifold is defined in simple terms as a continuous, non-intersecting surface).

<img src="../1. Introduction to Deep Learning/images/pca_vs_autoencoder.jpg">

__Regularized Autoencoders__

Undercomplete autoencoders, with code dimension less than the input dimension,can learn the most salient features of the data distribution. We have seen that these autoencoders fail to learn anything useful if the encoder and decoder are given too much capacity.

A similar problem occurs if the hidden code is allowed to have dimension equal to the input, and in the overcomplete case in which the hidden code has dimension greater than the input. In these cases, even a linear encoder and a linear decoder can learn to copy the input to the output without learning anything useful about the data distribution.

Regularized autoencoders use a loss function that encourages the model to have other properties besides the ability to copy its input to its output. These other properties include sparsity of the representation, smallness of the derivative of the representation, and robustness to noise or to missing inputs. A regularized autoencoder can be nonlinear and overcomplete but still learn something useful about the data distribution, even if the model capacity is great enough to learn a trivial identity function.

__Sparse autoencoders__

Sparse autoencoders offer us an alternative method for introducing an information bottleneck without requiring a reduction in the number of nodes at our hidden layers. Rather, we'll construct our loss function such that we penalize activations within a layer. For any given observation, we'll encourage our network to learn an encoding and decoding which only relies on activating a small number of neurons. It's worth noting that this is a different approach towards regularization, as we normally regularize the weights of a network, not the activations.

<img src="../1. Introduction to Deep Learning/images/sparse_autoencoder.jpg">

We allow our network to sensitize individual hidden layer nodes toward specific attributes of the input data. Whereas an undercomplete autoencoder will use the entire network for every observation, a sparse autoencoder will be forced to selectively activate regions of the network depending on the input data. As a result, we've limited the network's capacity to memorize the input data without limiting the networks capability to extract features from the data. This allows us to consider the latent state representation and regularization of the network separately, such that we can choose a latent state representation (ie. encoding dimensionality) in accordance with what makes sense given the context of the data while imposing regularization by the sparsity constraint.

There are two main ways by which we can impose this sparsity constraint; both involve measuring the hidden layer activations for each training batch and adding some term to the loss function in order to penalize excessive activations. These terms are:

- _L1 Regularization_: We can add a term to our loss function that penalizes the absolute value of the vector of activations a in layer h for observation i, scaled by a tuning parameter λ.

    <img src="../1. Introduction to Deep Learning/images/sparse_autoencoder_l1.jpg">

- _KL-Divergence_: In essence, KL-divergence is a measure of the difference between two probability distributions. We can define a sparsity parameter ρ which denotes the average activation of a neuron over a collection of samples. This expectation can be calculated as $\hat{p}_j = \frac{1}{m} \sum_i [a^{(h)}_i (x) ]$ where the subscript j denotes the specific neuron in layer h, summing the activations for m training observations denoted individually as x. In essence, by constraining the average activation of a neuron over a collection of samples we're encouraging neurons to only fire for a subset of the observations. We can describe ρ as a Bernoulli random variable distribution such that we can leverage the KL divergence (expanded below) to compare the ideal distribution ρ to the observed distributions over all hidden layer nodes $\hat{p}$.

    <img src="../1. Introduction to Deep Learning/images/sparse_autoencoder_kl.jpg">

__Denoising autoencoders__

Rather than adding a penalty to the cost function, we can obtain an autoencoder that learns something useful by changing the reconstruction error term of the cost function. Traditionally, autoencoders minimize some function such that it encourages to learn to be merely an identity function if they have the capacity to do so. A denoising autoencoder instead minimizes the distance between a original copy and a corrupted version of it by some form of noise. Denoising autoencoders must therefore undo this corruption rather than simply copying their input.

__Stochastic Encoders and Decoders__

A general strategy for designing the output units and the loss function of a feed forward network is to deﬁne an output distribution p(y | x) and minimize the negative log-likelihood −log p(y | x). In that setting, yis a vector of targets, such as class labels.

In an autoencoder, x is now the target as well as the input. Yet we can still apply the same machinery as before. Given a hidden code h, we may think of the decoder as providing a conditional distribution p_decoder(x | h). We may then train the autoencoder by minimizing −log p_decoder(x | h). The exact form of this loss function will change depending on the form of p_decoder. As with traditional feed forward networks, we usually use linear output units to parametrize the mean of a Gaussian distribution if x is real valued. In that case, the negative log-likelihood yields a mean squared error criterion. Similarly, binary x values correspond to a Bernoulli distribution whose parameters are given by a sigmoid output unit, discrete x values correspond to a softmax distribution, and so on. Typically, the output variables are treated as being conditionally independent given h so that this probability distribution is inexpensive to evaluate, but some techniques, such as mixture density outputs, allow tractable modeling of outputs with correlations.

To make a more radical departure from the feed forward networks we have seen previously, we can also generalize the notion of an encoding function f(x) to an encoding distribution p_encoder(h | x).

Any latent variable model p_model(h, x) deﬁnes a stochastic encoder p_encoder(h | x) = p_model(h | x) and a stochastic decoder p_decoder(x | h) = p_model(x | h).

In general, the encoder and decoder distributions are not necessarily conditional distributions compatible with a unique joint distribution p_model(x, h)



<h3>Autoencoder applications</h3>

__Convolutional autoencoder__


__Image retrieval with autoencoder__


__Cheap image morphing__



<h2>Word Embeddings</h2>


<h3>Natural language processing primer</h3>



<h3>Word embeddings</h3>




<h2>Generative Adversarial Networks</h2>


<h3>Generative models 101</h3>



<h3>Generative Adversarial Networks</h3>



<h3>Applications of adversarial approach</h3>

__Style Transfer__




<h1>Week 5: Deep learning for sequences</h1>



<h2>Introduction to RNN</h2>


<h3>Motivation for recurrent layers</h3>

__Language Modeling__

<img src="../1. Introduction to Deep Learning/images/language_modeling.jpg">

__n-gram Language Models__

To compute the probabilities mentioned above, the count of each n-gram could be compared against the frequency of each word. This is called an n-gram Language Model. Before deep learning, the way to learn a language model was using n-gram language model. A n-gram is a chunk of n consecutive words. They can be uni-grams, bi-grams, tri-grams or 4-grams. The main idea is to collect statistics about how frequent different n-grams are and use these to predict next word.

<img src="../1. Introduction to Deep Learning/images/n_gram.jpg">

But how long should the context be? In some cases, the window of past consecutive n words may not be sufficient to capture the context. For instance, consider the sentence "As the proctor started the clock, the students opened their ______". If the window only conditions on the previous three words "the students opened their", the probabilities calculated based on the corpus may suggest that the next word be "books" - however, if n had been large enough to include the "proctor" context, the probability might have suggested "exam". This leads us to two main issues with n-gram Language Models: Sparsity and Storage.

_Sparsity Problems with n-gram Language Models_

<img src="../1. Introduction to Deep Learning/images/n_gram_sparsity.jpg">

In practice you don't usually have n bigger than 5 because it makes the sparsity problem worse.

_Storage problems with n-gram Language models_

We know that we need to store the count for all n-grams we saw in the corpus. As n increases (or the corpus size increases), the model size increases as well.

_Window-based Neural Language Model_

The "curse of dimensionality" above was first tackled by Bengio et al in A Neural Probabilistic Language Model, which introduced the first large-scale deep learning for natural language processing model. This model learns a distributed representation of words, along with the probability function for word sequences expressed in terms of these representations.

<img src="../1. Introduction to Deep Learning/images/window_based_lm_a.jpg">

<img src="../1. Introduction to Deep Learning/images/window_based_lm_b.jpg">

<h3>Simple RNN</h3>

Unlike the conventional translation models, where only a finite window of previous words would be considered for conditioning the language model, Recurrent Neural Networks (RNN) are capable of conditioning the model on all previous words in the corpus.

<img src="../1. Introduction to Deep Learning/images/rnn_a.jpg">

<img src="../1. Introduction to Deep Learning/images/rnn_b.jpg">


<h2>Modern RNNs</h2>


<h3>The training of RNNs is not that easy</h3>

<img src="../1. Introduction to Deep Learning/images/rnn_loss.jpg">

<img src="../1. Introduction to Deep Learning/images/rnn_training.jpg">

The amount of memory required to run a layer of RNN is proportional to the number of words in the corpus. We can consider a sentence as a minibatch, and a sentence with k words would have k word vectors to be stored in memory. Also, the RNN must maintain two pairs of W, b matrices. As aforementioned, while the size of W could be very large, it does not scale with the size of the corpus (unlike the traditional language models). For a RNN with 1000 recurrent layers, the matrix would be 1000 × 1000 regardless of the corpus size.

<img src="../1. Introduction to Deep Learning/images/rnn_training_a.jpg">

__Evaluating Language Models__

The standard evaluation metric for Language Models is perplexity. Perplexity is a measure of confusion where lower values imply more confidence in predicting the next word in the sequence (compared to the ground truth outcome). It is basically 2 to the power of the negative log probability of the cross entropy error function.

<h3>Backpropagation for RNNs</h3>

<img src="../1. Introduction to Deep Learning/images/rnn_backpropagation_a.jpg">

<h3>Dealing with vanishing and exploding gradients</h3>

Recurrent neural networks propagate weight matrices from one time step to the next. Recall the goal of a RNN implementation is to enable propagating context information through faraway time-steps.

<img src="../1. Introduction to Deep Learning/images/vanishing_gradients_a.jpg">

<img src="../1. Introduction to Deep Learning/images/vanishing_gradients_b.jpg">

_Vanishing gradient_ is a problem because gradient signal from faraway is lost because it’s much
smaller than gradient signal from close-by. When the gradient value goes to zero, it can go undetected while drastically reducing the learning quality of the model for far-away words in the corpus. So model weights are only updated only with respect to near effects, not long-term effects. Another way to look at this is as gradients measure the effect of the past on the future.

_Exploding gradient_

<img src="../1. Introduction to Deep Learning/images/exploding_gradients.jpg">

_Solution to the Exploding & Vanishing Gradients_

<img src="../1. Introduction to Deep Learning/images/gradient_clipping.jpg">

To solve the problem of vanishing gradients, we introduce two techniques. The first technique is that instead of initializing W(hh) randomly, start off from an identity matrix initialization.

The second technique is to use the Rectified Linear Units (ReLU) instead of the sigmoid function. The derivative for the ReLU is either 0 or 1. This way, gradients would flow through the neurons whose derivative is 1 without getting attenuated while propagating back through time steps.

_Is vanishing/exploding gradient just a RNN problem?_

<img src="../1. Introduction to Deep Learning/images/vanishing_exploding_gradient.jpg">

<h3>Long Short-Term Memory (LSTM)</h3>

<img src="../1. Introduction to Deep Learning/images/lstm_a.jpg">

<img src="../1. Introduction to Deep Learning/images/lstm_b.jpg">

<img src="../1. Introduction to Deep Learning/images/lstm_c.jpg">

The LSTM architecture makes it easier for the RNN to preserve information over many time steps.

- e.g. if the forget gate is set to remember everything on every time step, then the info in the cell is preserved indefinitely
- By contrast, it’s harder for vanilla RNN to learn a recurrent weight matrix Wh that preserves info in hidden state

LSTM doesn’t guarantee that there is no vanishing/exploding gradient, but it does provide an easier way for the model to learn long-distance dependencies.

<h3>Gated Recurrent Units (GRU)</h3>

<img src="../1. Introduction to Deep Learning/images/gru.jpg">

<img src="../1. Introduction to Deep Learning/images/gru_a.jpg">

- Researchers have proposed many gated RNN variants, but LSTM and GRU are the most widely-used.
- The biggest difference is that GRU is quicker to compute and has fewer parameters.
- There is no conclusive evidence that one consistently performs better than the other.
- LSTM is a good default choice (especially if your data has particularly long dependencies, or you have lots of training data).
- Rule of thumb: start with LSTM, but switch to GRU if you want something more efficient.

<h3>Bidirectional RNN</h3>

So far, we have focused on RNNs that condition on past words to predict the next word in the sequence. It is possible to make predictions based on future words by having the RNN model read through the corpus backwards.

<img src="../1. Introduction to Deep Learning/images/bidirectional_rnn_a.jpg">

<img src="../1. Introduction to Deep Learning/images/bidirectional_rnn_b.jpg">

Note: bidirectional RNNs are only applicable if you have access to the entire input sequence.

- They are not applicable to Language Modeling, because in LM you only have left context available.

If you do have entire input sequence (e.g. any kind of encoding), bi-directionality is powerful (you should use it by default).

For example, BERT (Bidirectional Encoder Representations from Transformers) is a powerful pre-trained contextual representation system built on bi-directionality.

<h3>Multi-layer RNN</h3>

- RNNs are already “deep” on one dimension (they unroll over many time steps)
- We can also make them “deep” in another dimension by applying multiple RNNs – this is a multi-layer RNN.
- This allows the network to compute more complex representations
- The lower RNNs should compute lower-level features and the higher RNNs should compute higher-level features.
- Multi-layer RNNs are also called stacked RNNs.

<img src="../1. Introduction to Deep Learning/images/multi_layer_rnn.jpg">

High-performing RNNs are often multi-layer (but aren’t as deep as convolutional or feed-forward networks).

For example: In a 2017 paper, Britz et al find that for Neural Machine Translation, 2 to 4 layers is best for the encoder RNN, and 4 layers is best for the decoder RNN.

- However, skip-connections/dense-connections are needed to train deeper RNNs (e.g. 8 layers)


<h2>Applications of RNNs</h2>


<h3>Practical use cases for RNNs</h3>

__Part of Speech Tagging__

<img src="../1. Introduction to Deep Learning/images/pos.jpg">

__Sentence Classification__

<img src="../1. Introduction to Deep Learning/images/sentence_classification.jpg">

__Encoder Module__

<img src="../1. Introduction to Deep Learning/images/encoder_module.jpg">

__Generate Text__

<img src="../1. Introduction to Deep Learning/images/generate_text.jpg">



<h1>Week 6: Final Project</h1>
