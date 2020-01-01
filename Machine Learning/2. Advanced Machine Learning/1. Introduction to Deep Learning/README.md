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



<h1>Week 3: Deep Learning for images</h1>



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

Another interesting property of convolution is translation equivariance. It means that if we move the input (translate) and imply convolution, it will actually act the same as if we first applied convolution, and then translated an image.

<img src="../1. Introduction to Deep Learning/images/convolution_translation.jpg">

__How does Convolutional Neural Networks Work__


__Backpropagation for CNN__

Gradients are first calculated as if the kernel weights were not shared. Then the gradients of the same shared weights are summed up.

<img src="../1. Introduction to Deep Learning/images/convolution_backprop.jpg">

__Convolutional vs fully connected layer__

- In convolutional layer, the same kernel is used for every output neuron, and that way, we share parameters of the network and train a better model.

- Convolutional layer can be viewed as a special case of a fully connected layer when all the weights outside the local receptive field of each neuron equals zero, and kernel parameter are shared between neurons.

<h3>Our first CNN architecture</h3>

__A Color Image Input__

<img src="../1. Introduction to Deep Learning/images/color_image.jpg">

<img src="../1. Introduction to Deep Learning/images/kernel_not_enough.jpg">

<img src="../1. Introduction to Deep Learning/images/receptive_field.jpg">

So to grow the receptive field faster, we can increase the _stride_ in our convolutional layer to reduce the output dimensions.

<img src="../1. Introduction to Deep Learning/images/stride.jpg">

But how do we maintain translational invariance with the stride? We use pooling layers.

<img src="../1. Introduction to Deep Learning/images/pooling.jpg">

But how does back propagation works for max pooling layer? Strictly speaking, maximum is not a differentiable function,but we will apply some heuristics here and make it work.


<h2>Modern CNNs</h2>


<h3>Training tips and tricks for deep CNNs</h3>

__Activation Functions__

- Sigmoid Activation

<img src="../1. Introduction to Deep Learning/images/sigmoid_activation.jpg">

For huge positive or huge negative argument (like 10 or -10) the sigmoid function derivative becomes close to 0. Using the chain rule when we will multiply further gradients by this small number it will lead to slow convergence. This is called the problem of vanishing gradients.

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

__Dropout__

<img src="../1. Introduction to Deep Learning/images/dropout.jpg">

__Data Augmentations__



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









<h1>Week 5: Deep learning for sequences</h1>










<h1>Week 6: Final Project</h1>
