<h1>Week 1: Statistics of Datasets</h1>



<h2>Mean values</h2>


<h3>Mean of a dataset</h3>

<img src="../3. Principal Component Analysis/images/mean.png">


<h2>Variances and covariances</h2>


<h3>Variance of one-dimensional datasets</h3>

<img src="../3. Principal Component Analysis/images/variance_1d.png">

<h3>Symmetric, positive definite matrices</h3>

A $n \times n$ symmetric real matrix $M$ is said to be __positive definite__ if $x^{\top} Mx > 0$ for all non-zero $x$ in $\mathbb{R}^{n}$

<img src="../3. Principal Component Analysis/images/positive_definite.png">

A $n \times n$ symmetric real matrix $M$ is said to be __positive semi-definite__ or __non-negative definite__ if $x^{\top} Mx > 0$ for all $x$ in $\mathbb{R}^{n}$

<img src="../3. Principal Component Analysis/images/positive_semi_definite.png">

<h3>Variance of higher-dimensional datasets</h3>

Covariance of a 3x3 matrix is given below:

<img src="../3. Principal Component Analysis/images/covariance.png">

Covariance of X and Y is defined below:

<img src="../3. Principal Component Analysis/images/covariance_xy.png">

Variances of higher-dimensional data sets is defined below:

<img src="../3. Principal Component Analysis/images/variance_multi_d.png">


<h2>Linear transformation of datasets</h2>


<h3>Effect on the mean and (co)variance</h3>

<img src="../3. Principal Component Analysis/images/linear_transformation.png">

<img src="../3. Principal Component Analysis/images/translations.png">



<h1>Week 2: Inner Products</h1>



<h2>Dot product</h2>


The dot product is one specific example of an inner product. Not all inner products are the dot product, however.

<img src="../3. Principal Component Analysis/images/dot_product.png">

<img src="../3. Principal Component Analysis/images/dot_product_angle.png">


<h2>Inner products</h2>


<h3>Inner product: definition</h3>

<img src="../3. Principal Component Analysis/images/inner_product.png">

<img src="../3. Principal Component Analysis/images/inner_product_example.png">

<h3>Inner product: length and distances of vectors</h3>

<img src="../3. Principal Component Analysis/images/inner_product_lengths.png">

I watched [Example of a Matrix of an Inner Product](https://www.youtube.com/watch?v=Om3BEqhOK88) to understand how to calculate the lengths and to calculate the distance:

$$d(X,Y)^2 = \langle X - Y, X - Y \rangle = \langle X, X \rangle + \langle Y, Y \rangle - 2 \langle X, Y \rangle$$

<h3>Basis vectors</h3>

<img src="../3. Principal Component Analysis/images/basis.png">

This sounded awfully like a eigenvector, and for the question, "what is the relationship between eigenvector and basis vector?" in Quora, the following answer provided the best explanation:

"_Think of a vector space with some number of dimensions. You can choose any set that may be linearly independent vectors as your basis. The basis is arbitrary, as long as you have enough vectors in it and they’re linearly independent._

_Eigenvectors, on the other hand, are properties of a linear transformation on that vector space. If a linear transformation affects some non-zero vector only by scalar multiplication, that vector is an eigenvector of that transformation. Different linear transformations can have different eigenvectors._

_Since you can choose any arbitrary basis for a space, but the eigenvectors are properties of a linear transformation, it follows that the eigenvectors are independent of the basis, and the basis is independent of the eigenvectors of any transformation._

_Do eigenvectors always form a basis? asks a related but more specific question. The answer is, no, the linearly independent eigenvectors of a linear transformation on a vector space may be, but are not necessarily, a basis for the space._"

<h3>Inner product: angles and orthogonality</h3>

<img src="../3. Principal Component Analysis/images/inner_product_angles.png">

<h3>Inner products of functions and random variables</h3>

Inner products and norms on function spaces play an absolutely essential role in modern analysis and its applications, particularly Fourier analysis, boundary value problems,
ordinary and partial differential equations, and numerical analysis.

Let $[a, b] ⊂ \mathbb{R}$ be a bounded closed interval. Consider the vector space $C^0 [a, b]$ consisting of all continuous scalar functions $f(x)$ defined for $a ≤ x ≤ b$. The integral of the product of two continuous functions:

<img src="../3. Principal Component Analysis/images/inner_product_function.png">

defines an inner product on the vector space $C^0 [a, b]$.  The associated norm is:

<img src="../3. Principal Component Analysis/images/function_norm.png">

and is known as the $L^2$ _norm_ of the function $f$ over the interval $[a, b]$. The $L^2$ inner product and norm of functions can be viewed as the infinite-dimensional function space versions of the dot product and Euclidean norm of vectors in $\mathbb{R^n}$.



<h1>Week 3: Orthogonal Projections</h1>



<h2>Projections</h2>


<h3>Projection onto 1D subspaces</h3>

<img src="../3. Principal Component Analysis/images/projection_1d.png">

<h3>Projections onto higher-dimensional subspaces</h3>

<img src="../3. Principal Component Analysis/images/projection_k_d.png">

<h3>Orthogonal Projections onto Higher-Dimensional Subspaces</h3>

<img src="../3. Principal Component Analysis/images/projection_notes_fig.png">

<img src="../3. Principal Component Analysis/images/projection_notes_a.png">

<img src="../3. Principal Component Analysis/images/projection_notes_b.png">

<img src="../3. Principal Component Analysis/images/projection_notes_c.png">



<h1>Week 4: Principal Component Analysis</h1>



<h2>PCA derivation</h2>


<h3>Vector spaces</h3>

<img src="../3. Principal Component Analysis/images/vector_space.png">

_Remark_. A “vector multiplication” $ab, a, b \in \mathbb{R^n}$, is not defined. Theoretically, we could define an element-wise multiplication, such that $c = ab$ with $c_j = a_j b_j$. This “array multiplication” is common to many programming languages but makes mathematically limited sense using the standard rules for matrix multiplication. By treating vectors as n × 1 matrices (which we usually do), we can use the matrix multiplication. However, then the dimensions of the vectors do not match. Only the following multiplications for vectors are defined: $ab^{\top} \in \mathbb{R^{n×n}}$ (outer product), $a^{\top}b \in \mathbb{R}$ (inner/scalar/dot product).

__Vector Subspaces:__

Intuitively, Vector subspaces are sets contained in the original vector space with the property that when we perform vector space operations on elements within this subspace, we will never leave it. In this sense, they are “closed”.

<img src="../3. Principal Component Analysis/images/vector_subspace.png">

- For every vector space $V$ the trivial subspaces are $V$ itself and {0}.

- The solution set of a homogeneous linear equation system $Ax = 0$ with $n$ unknowns $x = [x1, \cdots , x_n]^{\top}$ is a subspace of $\mathbb{R^n}$.

- The solution of an inhomogeneous equation system $Ax = b, \ b \neq 0$ is not a subspace of $\mathbb{R^n}$.

<h3>Orthogonal complements</h3>

[Orthogonal complement](https://www.khanacademy.org/math/linear-algebra/alternate-bases/othogonal-complements/v/linear-algebra-orthogonal-complements)


[Orthogonal Decomposition](https://www.youtube.com/watch?v=43b1ltFAwuc)

<img src="../3. Principal Component Analysis/images/orthogonal_complements.png">

<h3>Problem setting and PCA objective</h3>

The key idea in PCA is to find a lower dimensional representation of vectors that can be expressed using fewer basis vectors.

<h3>Multivariate chain rule</h3>

In the multivariate case, where $x \in \mathbb{R^n}$, the basic differentiation rules that we know from school (e.g., sum rule, product rule, chain rule) still apply. However we need to pay attention because now we have to deal with matrices where multiplication is no longer commutative, i.e., the order matters.

<img src="../3. Principal Component Analysis/images/multivariate_chain_rule.png">

<img src="../3. Principal Component Analysis/images/multivariate_chain_rule_matrices.png">

<h3>Finding the coordinates of the projected data</h3>



<h3>Reformulation of the objective</h3>

We can reformulate the loss function as the variance of the data projected onto the subspace that we ignore. Therefore, minimizing this loss is equivalent to minimizing the variance of the data that lies in the subspace that is a orthogonal to the principal subspace. In other words, we are interested in retaining as much variance after projection as possible.


<h3>Lagrange multipliers</h3>

Lagrange multipliers is a strategy for finding the local maxima and minima of a function subject to equality constraints (i.e., subject to the condition that one or more equations have to be satisfied exactly by the chosen values of the variables).

<img src="../3. Principal Component Analysis/images/lagrange_multipliers.png">

<h3>Finding the basis vectors that span the principal subspace</h3>




<h2>PCA algorithm</h2>


<h3>Steps of PCA</h3>

<img src="../3. Principal Component Analysis/images/pca_steps.png">

<h3>PCA in high dimensions</h3>

<img src="../3. Principal Component Analysis/images/pca_high_dim.png">

<h3>Other interpretations of PCA</h3>

Five different perspectives of PCA that lead to different objectives:

- Minimizing the squared reconstruction error,
- Minimizing the autoencoder loss, maximizing the mutual information,
- Maximizing the variance of the projected data,
- Maximizing the likelihood in a latent variable model.

All these different perspectives give us the same solution to the PCA problem. The strengths and weaknesses of individual perspectives become more clear and important when we consider properties of real data.
