#!/usr/bin/env python
# coding: utf-8

# # Lecture 4 - Linear representations
# 
# ## Matrix groups
# 
# Let $M_n$ be the set of all $n\times n$ matrices $A=(a_{ij})$, $i,j=1,2,\ldots,n$. The identity matrix $\mathbb{I}_n$ is the matrix with all diagonal entries equal to 1 and the remaining entries equal to 0:
# 
# $$
# \mathbb{I}_n=\begin{pmatrix}1&0&\ldots&0\\0&1&\ldots&0\\\vdots&\vdots&\ddots&\vdots\\
# 0&0&\ldots&1\end{pmatrix}
# $$
# 
# Multiplication of two matrices $A=(a_{ij})$ and $B=(b_{ij})$ in $M_n$ produces a matrix
# 
# $$
# A\cdot B=(\sum_{l=1}^n a_{il}b_{lj})\in M_n
# $$
# 
# The multiplication can be considered as a map
# 
# $$
# M_n\times M_n\to M_n
# $$
# 
# It is therefore a binary operation.
# 
# ```{admonition}
# :class: proposition
# 
# We have the following multiplication rules
# - $A=\mathbb{I}\cdot A=A\cdot \mathbb{I}_n$
# - $A\cdot(B\cdot C)=(A\cdot B)\cdot C$ for any three matrices $A,B,C\in M_n$
# 
# 
# ```
# 
# A matrix $A\in M_n$ is called invertible, or non-singular, if there exists a matrix $B$ such that 
# 
# $$
# A\cdot B=B\cdot A=\mathbb{I}_n
# $$
# 
# ```{admonition} Definition (Linear group)
# :class: definition
# 
# The subset of $M_n$ consisting of invertible matrices is denoted by $GL_n$ and called the general linear group.
# 
# ```
# 
# ```{admonition} Proposition 
# :class: proposition
# 
# The general linear group $GL_n$ is a group with matrix multiplication as the binary operation
# ```
# 
# We can consider different linear groups by specyfying the domain of the matrix elements, e.g.:
# - $GL_n(\mathbb{C})$ -- invertible matrices with complex entries
# - $GL_n(\mathbb{R})$ -- invertible matrices with real entries
# - $GL_n(\mathbb{Z})$ -- invertible matrices with integer entries
# 
# ```{admonition} Example (Linear group)
# 
# $GL_2(\mathbb{R})=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:a,b,c,d\in\mathbb{R}, ad-bc\neq 0\right\}$
# 
# ```
# 
# There are various subgroups of $GL_n$:
# - $SL_n=\{A\in GL_n:\det A=1\}$
# - $O_n=\{A\in GL_n(\mathbb{R}):A\cdot A^T=\mathbb{I}_n\}$
# - $SO_n=\{A\in O_n:\det A=1\}$
# - The matrices $D=\{\mathbb{I}_2,A,A^2,A^3,B,AB,A^2B,A^3B\}$ where $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ is a subgroup of $GL_2$. We encountered this group already when we studied the subgroups of $S_n$, namely $D$ has the same multiplication table as the group of symmetries of a square: $D_4$.
# - Lorentz group: let $\eta$ be the following matrix
# 
# $$
# \eta=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
# $$
# 
# Then the Lorentz group is defined as:
# 
# $$
# Lor=\{A\in GL_4(\mathbb{R}):A^T\eta A=\eta\}\subset GL_4(\mathbb{R})
# $$
# 
# ## Linear representations
# 
# Before defining linear representations of groups, let us recall from linear algebra the definition of a vector space and a linear map.
# 
# ```{admonition} Definition (Vector space)
# :class: definition
# 
# A vector space over a field $\mathbb{F}$ ($\mathbb{R}$ or $\mathbb{C}$), is a set $V$ together with two operations: vector addition and multiplication by scalar, that satisfy the following axioms:
# - addition is commutative, associative, has an identity element and inverses (therefore $V$ is an abelian group with +)
# - $\lambda(\mu v)=(\lambda\mu)v$ for all $\lambda,\mu\in\mathbb{F}$ and $v\in  V$
# - $\lambda(v+u)=\lambda v+\lambda u$ for all $\lambda\in\mathbb{F}$ and $v,u\in  V$
# - $(\lambda+\mu) v)=\lambda v+\mu v$ for all $\lambda,\mu\in\mathbb{F}$ and $v\in  V$
# ```
# 
# ```{admonition} Examples (Vector space)
# :class: example
# 
# - $\mathbb{F}=\mathbb{R}$, $V=\mathbb{R}^n$ is a vector space over real numbers
# - $\mathbb{F}=\mathbb{C}$, $V=\mathbb{C}^n$ is a vector space over complex numbers
# - the set $M_{n\times m}(\mathbb{R})$ of all $n\times m$ matrices is a vector space
# 
# ```
# 
# ```{admonition} Definition (Linear map)
# :class: definition
# 
# Let $U$ and $V$ be vector spaces over $\mathbb{F}$. Then $f:U\to V$ is called a linear map if
# - $f(u+v)=f(u)+f(v)$ for all $u,v\in U$
# - $f(\lambda u)=\lambda f(u)$ for all $\lambda\in \mathbb{F}$ and $u\in U$
# 
# ```
# 
# ```{admonition} Examples (Linear map)
# :class: example
# 
# - The identity map $id_U:U\to U$ is a linear map
# - For an $n\times m$ real matrix $A$, we can define a map: $T_A:\mathbb{R}^n\to\mathbb{R}^m$ as $T_A(v)=A\cdot v$. Then $T_A$ is a linear map.
# 
# ```
# 
# Our goal is to define a mathematical structure that facilitates the action of groups on vector spaces. The first step is to observe that the set $GL(V)$ of invertible linear maps $V\to V$ on an $n$-dimensional vector space $V$ over a field $\mathbb{F}$ forms a group, called the general linear group of $V$.The group multiplication is composition of maps, the identity element is the identity map and the iverse is the map inverse.
# 
# For $V=\mathbb{F}^n$ the general linear group reduces to the previously mentioned group of invertible matrices:
# 
# $$
# GL(\mathbb{F}^n)=GL_n(\mathbb{F})
# $$
# 
# In a general case, the general linear group $GL(V)$ acts linearly on the vector space $V$. For an arbitrary group $G$ we can find an action on a vector space by assigning to each group element in $G$ a linear transformation in $GL(V)$. This assignment should preserve the group structure of $G$, which means that it should be a group homomorphism $G\to GL(V)$. This motivates the following definition:
# 
# ```{admonition} Definition (Representation)
# :class: definition
# 
# A representation $R$ of a group $G$ is a group homomorphism $R:G\to GL(V)$, where $V$ is a vector space over $\mathbb{F}$. The dimension of the representation $R$ is defined by $\dim(R)=\dim_\mathbb{F}(V)$.
# 
# ```
# 
# ```{admonition} Examples (Representation)
# :class: example
# 
# - Trivial representation: let $V$ be any vector space. The trivial representation of $G$ on $V$ is the group homomorphism $G\to GL(V)$ sending every element of $G$ to the identity transformation. That is, the elements of $G$ all act on $V$ trivially by doing nothing.
# - Permutation represtation of $S_n$: Consider the $n$-dimensional vector space $V$ with basis elements $e_i$, $i=1,2,\ldots,n$. Then the symmetric group $S_n$ acts on %V% by permuting basis elements, namely for $\sigma\in  S_n$, the action is:
# 
# $$
# \sigma.e_i=e_{\sigma(i)}
# $$
# 
# For example, for $S_3$ this leads to the following three-dimensional representation $S_3\to GL(\mathbb{R}^3)$:
# 
# $$
# \begin{align*}
# e\mapsto \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}, \qquad (12)\mapsto \begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}, \qquad (13)\mapsto \begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}\\
# (23)\mapsto \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}, \qquad (123)\mapsto \begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}, \qquad (132)\mapsto \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}
# \end{align*}
# $$
# 
# There is an analogous representation of $S_n$ on $\mathbb{R}^n$ for all $n$.
# 
# - Alternating representation of $S-n$: For every symmetric group $S_n$
# for any $n$, there exists a one-dimensional representation defined by the homomorphism: for $\sigma\in S_n$ we have $\sigma\mapsto (1)$ if $\sigma$ is an even permutation; and $\sigma\mapsto (-1)$ if $\sigma$ is an odd permutation.
# 
# - Tautological representation of $D_n$: The tautological representation of $D_n$ is given by the action of $D_n$ on  regular $n$-gon. For example, for $D_4$ we have a homomorphism
# 
# $$
# \rho:D_4\to GL(\mathbb{R}^2)
# $$
# 
# that takes the rotation by $90^\circ$ element $A$ to $\rho(A)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$; and the reflection with respect to the $x$-axis $B$ to $\rho(B)=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$. The tautological representation of $D_n$ is always two-dimensional.
# 
# ```
# 
# 

# In[ ]:




