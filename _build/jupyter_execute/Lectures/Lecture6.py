#!/usr/bin/env python
# coding: utf-8

# # Irreducible representations
# 
# We define a class of representations that will provide us with building blocks for all possible representations. 
# 
# ```{admonition} Definition (Irreducible representation)
# :class: definition
# 
# A representation of a group on a vector space is irreducible if it has no proper non-zero subrepresentations
# ```
# 
# ```{admonition} Examples (Irreducible representation)
# :class: example
# 
# - All one-dimensional representations are irreducible.
# - The tautological representation $T$ of $D_4$ is irreducible over real numbers. If there was some proper, non-zero subrepresentation, it would have to be on-dimensional, but no line in the place is left invariant under the action of the symmetry group of the square.
# ```
# 
# ```{admonition} Counterexample (Irreducible representation)
# :class: warning
# 
# The vertex permutation representation of $D_4$ is not irreducible since the line spanned by the vector $(1,1,1,1)$ is a non-zero proper subrepresentation. 
# ```
# 
# ## Complete reducibility
# 
# One of the most important statements in this lecture concern reducibility of finite representations of finite groups.
# 
# ```{admonition} Proposition
# :class: proposition
# 
# Every finite-dimensional representation of a finite group over the real or complex numbers decomposes into a direct sum of irreducible subrepresentations.
# 
# ```
# 
# The key statement for the above proposition is that every subrepresentation of a real or complex representation of a finite group has a representation complement. That is, if $W$ is a subrepresentation of $V$, then there exists another subrepresentation $W'$ of $V$ such that $V\cong W\oplus W'$ as representations of $G$.
# 
# We will not prove this proposition in full generality, but instead we provide an algorithm on how to find the representation complement: 
# 1. Let $W$ be a subrepresentation of $G$ inside a representation $V$.
# > As an example, let us take $V=\mathbb{R}^4$ to be the vertex permutation representation of $D_4$, and $W$ to be the subrepresentation spanned by $(-1,1,-1,1)$.
# 2. Fix any vector space complement $U$ of $W$ inside $V$, and decompose $V$ as the direct sum of vector spaces $V\cong W\oplus U$.
# > Let us take $U$ to be the subspace in $\mathbb{R^4}$ consisting of all vectors whose last coordinate is zero. Then any element $(x_1,x_2,x_3,x_4)\in \mathbb{R}^4$ can be decomposed as
# >
# >$$
# (x_1,x_2,x_3,x_4)=(-x_4,x_4,-x_4,x_4)+(x_1+x_4,x_2-x_4,x_3+x_4,0)\in W\oplus U
# $$
# 3. The decomposition allows us to define a projection $\Pi:V\to W$ onto the first factor: for all $v\in V$ we can write $v=w+u$ for some $w\in W$ and $u\in U$. Then $\pi(v)=w$.
# > In our case
# >
# >$$
# \Pi((x_1,x_2,x_3,x_4))=(-x_4,x_4,-x_4,x_4)
# $$
# 4. Define a new linear map $\phi:V\to W$ obtained by averaging $\Pi$ over all elements in $G$:
# 
# $$
# \phi(v)=\frac{1}{|G|}\sum_{g\in G}g.\Pi(g^{-1}.v)
# $$
# >$$
# \begin{array}{c|c|c|c|c|c|c|c|c|c}
# \hline
# g&e&(1234)&(13)(24)&(1432)&(13)&(24)&(12)(34)&(14)(23)\\
# \hline
# g^{-1}.(x_1,x_2,x_3,x_4)&(x_1,x_2,x_3,x_4)&(x_2,x_3,x_4,x_1)&(x_3,x_4,x_1,x_2)&(x_4,x_1,x_2,x_3)&(x_3,x_2,x_1,x_4)&(x_1,x_4,x_3,x_2)&(x_2,x_1,x_4,x_3)&(x_4,x_3,x_2,x_1)\\
# \hline
# \Pi(g^{-1}.x)&(-x_4,x_4,-x_4,x_4)&(-x_1,x_1,-x_1,x_1)&(-x_2,x_2,-x_2,x_2)&(-x_3,x_3,-x_3,x_3)&(-x_4,x_4,-x_4,x_4)&(-x_2,x_2,-x_2,x_2)&(-x_3,x_3,-x_3,x_3)&(-x_1,x_1,-x_1,x_1)\\
# \hline
# g.\Pi(g^{-1}.x)&(-x_4,x_4,-x_4,x_4)&(x_1,-x_1,x_1,-x_1)&(-x_2,x_2,-x_2,x_2)&(x_3,-x_3,x_3,-x_3)&(-x_4,x_4,-x_4,x_4)&(-x_2,x_2,-x_2,x_2)&(x_3,-x_3,x_3,-x_3)&(x_1,-x_1,x_1,-x_1)\\
# \hline
# \end{array}
# $$
# >Summing over all 8 elements we get:
# >
# >$$
# \phi((x_1,x_2,x_3,x_4))=\frac{1}{8}(2x_1-2x_2+2x_3-2x_4)(1,-1,1,-1)
# $$
# 5. Find the kernel of $\phi$ and set $W'=\mathrm{ker}\phi$. Then $W'$ is the representation complement we look for, and $V\cong W\oplus W'$
# > The kernel of $\phi$ consists of all vectors that are mapped to $0$. Therefore
# >
# >$$
# \mathrm{ker}\phi=\{(x_1,x_2,x_3,x_4):x_1-x_2+x_3-x_4=0\}=W'
# $$
# Then $W'$ is the representation complement of $W$.
# 
# This algorithm allows is to find a complete decomposition for any finite dimensional representation $V$ by following these three steps:
# 1. Find an invariant subspace $W$ of $V$
# 2. Find the representation complement $W$'of $W$ in $V$
# 3. Repeat steps 1. and 2. for $W$ and $W'$ until you end up with irreducible representations.
# 
# The decomposition into irreducible subrepresentations is not uniques in general. It is however unique up to an isomorphism in the following way:
# 
# ```{admonition} Proposition
# :class: proposition
# 
# Let $V$ be a finite-dimensional real or complex representation of a finite group $G$. Then $V$ has a decomposition into subrepresentations
# 
# $$
# V=V_1\oplus V_2\oplus\ldots\oplus V_t
# $$
# where each $V_i$ is isomorphic to a direct sum of some number of copies of some fixed irreducible representation $W_i$, with $W_i\neq W_j$ unles $i=j$. That is, given two different decompositions of $V$ into non-isomorphic irreducible subrepresentations
# 
# $$
# W_1^{a_1}\oplus \ldots\oplus W_t^{a_t}=U_1^{b_1}\oplus \ldots\oplus U_r^{b_r}
# $$
# 
# where the $W_i$ (respectively $U_i$) are all irreducible and non-isomorphic, then after relabelling $t=r$, $a_i=b_i$, the subrepresentations $W_i^{a_u}$ equal the $U_i^{b_i}$ for all $i$, and the corresponding $W_i$ are isomorphic to $U_i$ for all $i$.
# ```
# 
# ## Classification of irreducible representations of finite groups
# 
# In this part of the module we want to find all irreducible representaions for finite groups, with special emphasis on symmetric groups $S_n$.
# 
# As the starting point, let us try to classify all representations of $S_2$ over complex numbers. Suppose that $V$ is a complex representation of $S_2$. The group $S_2$ is generated by one element $\sigma=(12)$ and therefore to find subrepresentations of $V$ it is sufficient to find subspaces of $V$ that are invariant under the action of $\sigma$. First considedr the action of $\sigma$ on $V$. Let $v$ be an eigenvector of this action, with the eigenvalue $\theta$. Then the subspace spanned by $v$ is invariant under the action of $S_2$, and therefore all representations of $S_2$ must be one-dimensional. Moreover, since $\sigma^2$ is the identity element of $A_2$, then $\theta^2=1$ which imples that $\theta=\pm 1$. There are only two irreducible complex representations of $S_2$:
# - when $\theta=1$ then we get the trivial representation
# - when $\theta=-1$ then we get the alternating representation
# 
# We can perform a similar calculation for $S_3$. The group $S_3$ is generated by $\sigma=(123)$ and $\tau=(12)$. Let $V$ be a complex representation of $S_3$, then we need to find all subspaces of $V$ invariant under the action of both $\sigma$ and $\tau$. Let $v$ be the eigenvector for the action of $\sigma$, with the eigenvalue $\theta$. Let $w-\tau.v$. Because we know that $\tau \sigma\tau=\sigma^2$ in $S_3$ then
# 
# $$
# \sigma.w=\sigma\tau.v=\tau\sigma^2v=\tau.(\theta^2)v=\theta^2\tau.v=\theta^2w
# $$
# 
# and therefore $w$ is also an eigenvector of $\sigma$ with the eigenvalue $\theta^2$. It follows that the subspace generated by $v$ and $w$ is invariant under $\sigma$ and $\tau$, hence under all of $S_3$. In particular, an irreducible complex representation of $S_3$ over the complex numbers can have dimension no hogher than two.
# 
# Now suppose that $V$ is irreducible. Since $\sigma^2$ is the identity element of $S_3$, the eigenvalue $\theta$ must satisfy $\theta^3=1$. There are two cases to consider:
# - $\theta=1$. Then $w=v$ because otherwise the subspace spanned by $v+w$ would be a one-dimensional invariant subspace of $V$, and therefore $V$ would not be irreducible. Then $V$ is one-dimensional and we know that $\sigma$ acts triviall on it. Now, since $\tau^=e$ we have only two options:
#  - $\tau$ acts trivially: $V$ is the trivial representation
#  - $\tau$ acts as $-1$: $V$ is the alternating representation
# - $\theta\neq 1$. In this case $\theta\neq \theta^2$, so the vectors $v$ and $w$ have distinct eigenvalues $\theta$ and $\theta^2$. Moreover, since $\theta^3=1$ ther $\theta^2+\theta+1=0$. Then, the map
# 
# $$
# \begin{align*}
# &V\to W=\{(x_1,x_2,x_3):\sum x_i=0\}\subset \mathbb{C}^3\\
# &v\mapsto (1,\theta,\theta^2),\qquad w\mapsto (\theta,1,\theta^2)
# \end{align*}
# $$
# 
# defines an isomorphism from $V$ to the standard representation of $S_3$.
# 
# To conclude, there are only 3 complex irreducible representations of $S_3$:
# - trivial (one-dimensional) representation
# - alternating (one-dimensional) representation
# - standard (two-dimensional) representation

# In[ ]:




