#!/usr/bin/env python
# coding: utf-8

# # Lecture 5 -  Subrepresentations
# 
# ## Subrepresentations
# 
# A subrepresentation is a subvector space that is also a representation of $G$ under the same action.
# 
# ```{admonition} Definition (Subrepresentation)
# :class: definition
# 
# Let $V$ be a linear representation of a group $G$. A subspace $W$ of $V$ is a subrepresentation if $W$ is invariant under $G$ - that is, if $g.w\in W$ for all $g\in G$ and all $w\in W$.
# ```
# 
# ```{admonition} Examples (Subrepresentation)
# :class: example
# 
# - Every subspace is a subrepresentation of the trivial representation on any vector space since the trivial $G$ action takes every subspace back to itself
# 
# - The tautological representation of $D_4$ on $\mathbb{R}^2$ has no proper non-zero subrepresentations because there is no line taken back to itself under every symmetry of the square, that is, there is no line left invariant by $D_4$.
# - The vertex permutation representation of $D_4$ on $\mathbb{R}^4$, induced by the action of $D_4$ on a set of basis elements $\{e_1,e_2,e_3,e_4\}$ indexed by the vertices of a square does have a proper non-trivial subrepresentation. For example, the one dimensional subspace spanned by $e_1+e_2+e_3+e_4$ is fixed by $D_4$ -- when $D_4$ acts, it permutes $e_i$ so their sum remains unchanged. Therefore, for all $g\in D_4$, we have 
# 
# $$
# g.(\lambda,\lambda,\lambda,\lambda)=(\lambda,\lambda,\lambda,\lambda)
# $$
# 
# for all vectors in the one-dimensional subspace of $\mathbb{R}^4$. Then, $D_4$ acts trivially on this one-dimensional subrepresentation.
# 
# - Another representation of the vertex permutation representation of $D_4$ on $\mathbb{R}^4$ is the subspace $W\subset \mathbb{R}^4$ of vectors whose coordinates sum to 0. When $D_4$ acts by permutinf the coordinates, it leaves their sum unchanged, For example, $B$ sends $(1,2,3,-6)$ to $(-6,3,2,1)$ if vectors are labelled counterclockwise from the upper right. The space $W$ is a three-dimensional representation of $D_4$ on $\mathbb{R}^4$. Note that $W$ is a non-trivial subrepresentation since the elements of $G$ do move the vectors around in the space $W$.
# 
# - The standard representaion of $S_n$: Let $S_n$ acts on a vector space of dimension $n$, say $\mathbb{R}^n$, by permuting the $n$ vectors of a fixed basis. Note that the subspace spanned by the sum of the basis vectors is fixed by the action of $S_n$ -- it is a subrepresentation on which $S_n$ acts trivially. More interestingly, the $(n-1)$-dimensional subspace 
# 
# $$
# W=\left\{\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}:\sum_{i=1}^n x_i=0\right\} \subset\mathbb{R}^n
# $$
# 
# is also invariant under the permutation action. This is called the standard representation of $S_n$.
# 
# ```
# 
# ## Direct sum of representations
# 
# For representations that have non-zero subrepresentations, it is always possible to simplify the matrix representatives in such a way that all subrepresentations are clearly visible, as blocks in these matrices. Let us take the permutation representation of $S_4$, $\rho:S_3\to GL(\mathbb{R}^3)$:
# 
# $$
# \begin{align*}
# e\mapsto \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}, \qquad (12)\mapsto \begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}, \qquad (13)\mapsto \begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}\\
# (23)\mapsto \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}, \qquad (123)\mapsto \begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}, \qquad (132)\mapsto \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}
# \end{align*}
# $$
# 
# We know that it does have two subrepresentations:
# - a one-dimensional trivial representation 
# - a two-dimensional standard representation
# 
# Let us define
# 
# $$
# M=\begin{pmatrix}1&-\frac{1}{2}&-\frac{1}{2}\\0&\frac{\sqrt{3}}{2}&-\frac{\sqrt{3}}{2}\\1&1&1\end{pmatrix}
# $$
# 
# Then by direct calculation:
# 
# $$
# \begin{align*}
# M \rho(e) M^{-1} =\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\qquad M \rho((12)) M^{-1} =\begin{pmatrix}-\frac{1}{2}&\frac{\sqrt{3}}{2}&0\\\frac{\sqrt{3}}{2}&\frac{1}{2}&0\\0&0&1\end{pmatrix}\\
# M \rho((13)) M^{-1} =\begin{pmatrix}-\frac{1}{2}&-\frac{\sqrt{3}}{2}&0\\-\frac{\sqrt{3}}{2}&\frac{1}{2}&0\\0&0&1\end{pmatrix}\qquad M \rho((23)) M^{-1} =\begin{pmatrix}1&0&0\\0&-1&0\\0&0&1\end{pmatrix}\\
# M \rho((123)) M^{-1} =\begin{pmatrix}-\frac{1}{2}&-\frac{\sqrt{3}}{2}&0\\\frac{\sqrt{3}}{2}&-\frac{1}{2}&0\\0&0&1\end{pmatrix}\qquad M \rho((132)) M^{-1} =\begin{pmatrix}-\frac{1}{2}&\frac{\sqrt{3}}{2}&0\\-\frac{\sqrt{3}}{2}&-\frac{1}{2}&0\\0&0&1\end{pmatrix}\\
# \end{align*}
# $$
# 
# All these matrices are block-diagonal with a two-dimensional block and a one-dimensional block. By multiplying by $M$ from the left and $M^{-1}$ from the right we just changed the basis of the three-dimensional space. This change of basis exposed the seubrepresentations of the permutation representation of $S_3$.
# 
# ```{admonition} Definition (Direct sum of representations)
# :class: definition
# 
# Suppose that $G$ acts on vector spaces $V$ and $W$. We can define an action of $G$ coordinate-wise on their direct sum as:
# 
# $$
# g.(v,w)=(g.v,g.w)\in V\oplus W
# $$
# 
# The matrix associated to every $g$ acting on $V\oplus W$ will be a block diagonal matrix
# 
# $$
# \begin{pmatrix}
# \rho_1(g)&0\\0&\rho_2(g)
# \end{pmatrix}
# $$
# 
# obtained from the $n\times n$ matrix $\rho_1(g)$ describing the action of $g$ on $V$, and the $m\times m$ matrix $\rho_2(g)$ describing the action of $g$ on $W$. We call $V\oplus W$ the direct sum of representations of $G$.
# 
# ```
# 
# We are interested in decomposing representations in direct susm of their subrepresentations. To do it we need one more notion:
# 
# ```{admonition} Definition (Isomorphic representations)
# :class: definition
# 
# Two representations $V$ and $W$ of $G$ are isomorphic if there is a vector space isomorphism between them that preserves the action of $G$, that is, if there exists an isomorphism $\phi:V\to W$ such that 
# 
# $$
# R_V(g)=\phi^{-1}\circ R_W(g)\circ \phi
# $$
# 
# for all $g\in G$, where $R_V:G\to GL(V)$ and $R_W:G\to GL(W)$ are two representations.
# 
# ```
# 
# ```{admonition} Example (Isomorphic representations)
# :class: example
# 
# We have shown that there exists a matrix $M$ such that for all $g\in S_3$ we have
# 
# $$
# M R(g) M^{-1}=\begin{pmatrix}R_1(g)&0\\0&R_2(g)\end{pmatrix}
# $$
# 
# where $R$ is the permutation representation of $S_3$, $R_1$ is the standard representation of $S_3$, and $R_2$ is the trivial representation of $S_3$. This implies that 
# 
# $$
# R\cong R_1\oplus R_2
# $$
# 
# ```
# 
# ## Searching for subrepresentations
# 
# Let us consider the following four-dimensional representation $V$ of $D_4$ (called the vertex permutation representation):
# - for the rotation: $A \mapsto \begin{pmatrix}0&0&0&1\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix} 
# - for the horizontal reflection: $B \mapsto \begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix} 
# 
# The remaining matrices can be found using the fact that we have a group representation, i.e. it is a group homomorphism. For example
# 
# $$
# A^2=A\cdot A\mapsto \phi(A)\cdot \phi(A)=\begin{pmatrix}0&0&0&1\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix} ^2=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix} 
# $$
# 
# We want to find all subrepresentations of $V$. To find interesting subrepresentations of $V$, we can look for non-zero vectors in $\mathbb{R}^4$ whose orbits under the action of $D_4$ span proper subspaces of $V$. One way is to find vectors with small orbits. For example, the vector $(1,1,1,1)$ is fixed by $D_4$. It spans a one-dimensional subrepresentation of $V$ where $D_4$ acts trivially.
# 
# Another vector with a small orbit is $w=(-1,1,-1,1)$. Note that $A$ acts on $w$ to produce $(1,-1,1,-1)=-w$. Also the reflection $B$ acts the same way and produces $-w$. All other elements of $D_4$ act by superpositions of these two elements, and therefore the orbit of $w$ is just $\{w,-w\}$. Thus the one-dimensional subspace spanned by $w$ is a subrepresentation of $V$. This is not a trivial representation since some elements act by the multiplication by $-1$.
# 
# There is also a two-dimensional subrepresentation of $V$ that can be found by considering the orbit of $u=(1,1,-1,-1)$. Its orbit is:
# 
# $$
# \mathrm(Orb)(u)=\{(1,1,-1,-1),(-1,1,1,-1),(-1,-1,1,1),(1-1,-1,1)\}
# $$
# 
# that are points on a two-dimensional subspace $T$ of $\mathbb{R}^4$ that has a basis $(1,1,-1,-1)$ and $(-1,1,1,-1)$. It is easy to check that the vertex representation action of $D_4$ on $T$ is identical with the tautological representation of $D_4$ on this two-plane.
# 
# Finally, since the three subrepresentations described above span $V$, there is a direct sum decomposition of representations:
# 
# $$
# V\cong T\oplus \mathbb{R}(1,1,1,1)\oplus \mathbb{R} (1,-1,1,-1)
# $$
# 
# Importantly, none of these subrepresentations can be further decomposed.
