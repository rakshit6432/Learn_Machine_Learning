<h1>Week 1: Introduction to optimization</h1>



<h2>Linear model as the simplest neural network</h2>


<h3>Linear regression</h3>

Linear models are building blocks for deep neural networks.

<img src="../1. Introduction to Deep Learning/images/supervised_learning.png">

The goal of machine learning is to find a modal that fits the training set x by the best way.

<img src="../1. Introduction to Deep Learning/images/linear_model.png">

The above equation can be described in vector notation for a matrix of sample $X$ as:

$$a(X) = Xw$$

To measure a quality or measure an error of a model on some set we use the mean squared error for regression:

<img src="../1. Introduction to Deep Learning/images/mse.png">

In the above formula, by subtracting the target value from prediction, we calculate the deviation of target value from a predicted value, then we take a square of it and take the average of these squares of deviations over all the training samples. The next line gives the mean squared error in vector form.

Now that we have a loss function, that measures how well our model fits the data, we have to minimize it w.r.t $w$ to our parameter set. This is the essence of machine learning. We optimize loss to find the best model.

If you try to solve this using analytical methods, then you have to invert the matrices:

$$w = (X^{\top} X)^{-1} X^{\top} y$$

This becomes very difficult when you have more than 100 or 1000 features. Even reducing this to solve a system of linear equations is still quire hard and requires a lots of computational resources.

<h3>Linear classification</h3>

<img src="../1. Introduction to Deep Learning/images/binary_classification.png">

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

For example, we can use _L2 penalty_ as a regularizer where $\|w\| = \sum_{j=1}^d w_j^2$. This regularizer drives all the coefficient closer to zero. So it penalizes our model for very large weights.

It can be shown this unconstrained optimization problem is equivalent to constraint optimization problem:

<img src="../1. Introduction to Deep Learning/images/l2_penalty.jpg">

where there is a one to one correspondence between C and lambda regularization strength.

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











<h1>Week 3: Deep Learning for images</h1>











<h1>Week 4: Unsupervised representation learning</h1>









<h1>Week 5: Deep learning for sequences</h1>










<h1>Week 6: Final Project</h1>
