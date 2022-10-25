#!/usr/bin/env python
# coding: utf-8

# # Groups
# 
# ## Definition of a group
# 
# We start our adventure with groups and representations by defining what we mean by a group. There are two main ingredients in this definition: a group is a set with a (binary) operation defined on it. This means if we take two elements of the set, we can 'multiply' them and obtain another element of the same set. Not all sets with binary operations define groups, the operation needs to satisfy additional conditions. In particular, we often want to define more than two elements, and therefore we need to define what we mean by this, for example introducing appropriate brackets, such that at any stage we multiply only two elements at the time. For a binary operation to be a group multiplication, we demand that the operation is associative, which means that the result of multiplying more than two things does not depend on the way in which we put the brackets. Moreover, we demand that there is an identity element of the binary operation, which is an element that does not change the value of other elements when multiplied. Finally, every element should have an inverse element. A formal definition is given below:
# 
# ```{admonition} Definition (Group)
# :class: definition
# 
# A **group** $(G,\star)$ is a set $G$ tohether with a binary operation
# 
# $$ \star:G\times G\to G$$
# 
# satisfying:
# - <u>*Closure*</u>: For all $a,b\in G$, the result of the operation $a\star b$ is also in $G$
# 
# - <u>*Associativity*</u>: For all $a,b,c\in G$
# 
# $$a\star (b\star c)=(a \star b)\star c$$
# 
# - <u>*Identity element*</u>: There exists an element $e\in G$ such that for every element $a\in G$ the following holds:
# 
# $$e\star a=a\star e=a$$
# 
# Such element is unique and it is called the *identity element*.
# 
# - <u>*Inverse element*</u>: For each $a\in G$ there exists an element $b\in G$, commonly denoted $a^{-1}$, such that
# 
# $$a\star b=b\star a=e$$
# 
# ```
# 
# In the definition of a group we do not assume that the binary operation $\star$ is commutative, and it is important to realise that there are many groups that are not commutative. It is, however, useful to define a special class of groups, called *Abelian groups*, for which the order in which we multiply elements is not important.
# 
# ```{admonition} Definition (Abelian group)
# :class: definition
# 
# A group $G$ is called an **Abelian group** if in addition to the conditions above it satisfies:
# 
# - <u>*Commutativity*</u>: For all $a,b\in G$ we have
# 
# $$a\star b=b\star a$$
# ```
# 
# There are many examples of groups that you already know from your previous studies. We give some examples of the ones that might be new to you below.
# 
# 
# ```{admonition} Examples (Group)
# :class: example
# 
# - $(\mathbb{Z},+)$ - integer numbers with addition (identity element: $e=0$, inverse element: $a^{-1}=-a$, it is *Abelian*)
# 
# - $(\mathbb{R},+)$ - real numbers with addition (identity element: $e=0$, inverse element: $a^{-1}=-a$, it is *Abelian*)
# 
# - $(\mathbb{R}^+,\cdot)$ - poitive real numbers with multiplication (identity element: $e=1$, inverse element: $a^{-1}=\frac{1}{a}$, it is *Abelian*)
# 
# - *Symmetric group*: Let $X$ be any non-empty set. A **permutation** on $X$ is a function $f:X\to X$ such that $f$ is one-to-one. If $X$ is a finite set with $n$ elements then we call the set of all permutations on $X$ with composition, a symmetric group $S_n$.
# 
# For $n=3$, if $X=\{1,2,3\}$ then we have six permutations on $X$:
# 
# $$
# \begin{align*}
# &e=\left(\begin{matrix}1&2&3\\1&2&3\end{matrix}\right)\qquad &(12)=\left(\begin{matrix}1&2&3\\2&1&3\end{matrix}\right)\qquad
# &(13)=\left(\begin{matrix}1&2&3\\3&2&1\end{matrix}\right)\\
# &(23)=\left(\begin{matrix}1&2&3\\1&3&2\end{matrix}\right)\qquad &(123)=\left(\begin{matrix}1&2&3\\2&3&1\end{matrix}\right)\qquad
# &(132)=\left(\begin{matrix}1&2&3\\3&1&2\end{matrix}\right)
# \end{align*}
# $$
# 
# The symmetric group $S_n$ for $n\leq 3$ is not Abelian, for example
# 
# $$(132)\circ(12)=\left(\begin{matrix}1&2&3\\3&1&2\end{matrix}\right)\circ\left(\begin{matrix}1&2&3\\2&1&3\end{matrix}\right)=\left(\begin{matrix}1&2&3\\1&3&2\end{matrix}\right)=(23)$$
# 
# $$(12)\circ(132)=\left(\begin{matrix}1&2&3\\2&1&3\end{matrix}\right)\circ \left(\begin{matrix}1&2&3\\3&1&2\end{matrix}\right)=\left(\begin{matrix}1&2&3\\3&2&1\end{matrix}\right)=(13)$$
# 
# and therefore $(132)\circ(12)\neq(12)\circ(132)$.
# 
# - *Alternating group*: if the permutation $f$ on the set $X$ interchanges just two elements of $X$, leaving all the other fixed, then $f$ is called a **transposition**. Every permutation can be expressed as a product of transpositions. We say that a permutation $f$ is even (odd) if $f$ can be expressed as a product of an even (odd) number of transpositions. The set of all even permutations on $X$ forms a group called the alternating group $A_n$.
# 
# For $n=3$:
# 
# $$
# \begin{align*}
# &e - \mathrm{zero \,\,transpositions}\\
# &(12), (13),(23) - \mathrm{one \,\,transposition}\\
# &(123)=(13)\circ (12), (132)=(13)\circ(23) - \mathrm{two\,\, transpositions}
# \end{align*}
# $$
# 
# Then $A_3=\{e,(123),(132)\}$.
# 
# - *Cyclic group*: for any $n$ consider the set $\mathbb{Z}_n=\{0,1,2,\ldots,n-1\}$ and define a binary operation $+\,(\textrm{mod}\,\, n)$ which is defined as: to compute $a+b\,(\mathrm{mod}\,\,n)$, add the integers $a$ and $b$, divide the result by $n$, and take the remainder. Then $(\mathbb{Z}_n,+\,(\mathrm{mod}\,\,n))$ is a group. Cyclic groups are abelian
# 
# For example, $\mathbb{Z}_4=\{0,1,2,3\}$ with the following multiplication table
# 
# $$
# \begin{array}{c|c|c|c|c}
# +\,(\mathrm{mod}\,\, 4)&0&1&2&3\\
# \hline
# 0&0&1&2&3\\
# \hline
# 1&1&2&3&0\\
# \hline
# 2&2&3&0&1\\
# \hline
# 3&3&0&1&2
# \end{array}
# $$
# ```
# 
# ## Subgroups
# 
# Some of the subsets of groups are themselves groups.
# 
# ```{admonition} Definition (Subgroup)
# :class: definition
# 
# Given a group $(G,\star)$, a subset $H$ of $G$ is called a **subgroup** of $G$, if $H$ also forms a group under the operation $\star$. We denote it by $H\leq G$.
# ```
# 
# ```{admonition} Proposition
# :class: proposition
# 
# A subset $H$ of a group $(G,\star)$ is a subgroup if $H$ is closed under $\star$ and it contains inverses.
# ```
# 
# ```{admonition} Examples (Subgroup)
# :class: example
# 
# - For every group $G$, the *trivial group* $\{e\}$ and the full group $G$ are subgroups of $G$.
# 
# - The set containing all even numbers $2\mathbb{Z}=\{2n:n\in \mathbb{Z}\}$ with addition is a subgroup of $(\mathbb{Z},+)$
# 
# - $(\{0,2\},+\,(\mathrm{mod}\,\,4))$ is a subgroup of $(\mathbb{Z}_4,+\,(\mathrm{mod}\,\,4))$ 
# 
# - $\{e,(12)\}$ is a subgroup of $S_3$
# 
# - *Center of a group*: the set
# 
# $$
# Z(G)=\{x\in G:g\star x=x\star g \mbox{ for all }g\in G\}
# $$
# 
# is a subgroup of $G$
# ```
# 
# ## Order of an element
# 
# ```{admonition} Definition (Order of an element)
# :class: definition
# 
# The **order of an element** $g\in G$ is the smallest positive integer $m$ such that
# 
# $$
# a^m=e
# $$
# 
# We denote the order of $g$ by $|g|$.
# ```
# 
# 
# ```{admonition} Example (Order of an element)
# :class: example
# 
# - In $S_3$ the element $(12)$ has order 2 since $(12)\circ(12)=e$. Similarly, the element $(123)$ has order 3 since $(123)\circ(123)\circ(123)=e$.
# 
# - In $\mathbb{Z}$ all elements apart from 0 have infinite order since there is no $m$ such that $a+a+\ldots+a=0$ ($m$ times) for any $a\in \mathbb{Z}\setminus \{0\}$.
# 
# ```
# 
# ## Order of a group
# 
# ```{admonition} Definition (Order of a group)
# :class: definition
# 
# The **order of a group** $G$ is its cardinality. We denote the order of $G$ by $|G|$.
# 
# ```
# 
# ```{admonition} Examples (Order of a group)
# :class: example
# 
# - $(\mathbb{Z},+)$ has an infinite order
# - the cyclic group group $(\mathbb{Z}_n,+\,\mathrm{mod}\,\, n)$ has order $n$
# - the symmetric group $S_n$ has order $n!$, while the alternating group $A_n$ has order $\frac{n!}{2}$
# 
# ```
# 
# ## Subgroups generated by elements
# 
# ```{admonition} Definition (Subgroup generated by an element)
# :class: definition
# 
# Let $g\in G$. Then the **subgroup generated by $g$** is
# 
# $$
# \langle g\rangle= \{g^k:k\in \mathbb{Z}\}
# $$
# 
# ```
# 
# ```{admonition} Example (Subgroup generated by an element)
# :class: example
# 
# - In $S_3$: $\langle (123) \rangle=\{(123),(123)^2=(132),(123)^3=e\}$
# 
# - In $S_4$: $\langle(12)(34)\rangle=\{(12)(34),((12)(34))^2=e\}$
# 
# ```
# 
# ```{admonition} Proposition
# :class: proposition
# 
# Let $g\in G$ and $H=\langle g\rangle$. Then $|H|=|g|$.
# 
# ```
# 
# ```{admonition} Definition (Subgroup generated by a set)
# :class: definition
# 
# Let $S$ be a subset containing elements from a group $G$. Then the **subgroup generated by $S$** is
# 
# $$
# \langle S\rangle=\{s_1^{k_1}\star s_2^{k_2} \star \ldots \star s_l^{k_l}:l\in\mathbb{N},s_i\in S,k_i\in \mathbb{Z}\}
# $$
# ```
# 
# ```{admonition} Example (Subgroup generated by a set)
# :class: example
# 
# - In $S_4$: the subgroup generated by the set containing $(12)$ and $(34)$ is: $\langle \{(12),(34)\} \rangle=\{e,(12),(34),(12)(34)\}$. This subgroup is not cyclic, namely it cannot be generated by a single element in $S_4$.
# 
# ```

# In[ ]:




