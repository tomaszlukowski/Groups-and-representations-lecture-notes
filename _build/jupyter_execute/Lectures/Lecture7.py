#!/usr/bin/env python
# coding: utf-8

# # Character Theory
# 
# To provide the complete classification for $S_n$ we will study the character theory.
# 
# In the analysis of the representations of $S_3$, the key thing was to study the eigenvalues of the actions of individual elements of $S_3$. Finding individual eigenvalues is howwever quite difficult. Luckily, it is sufficient to consider their sum, the trace of a matrix, which is much easier to calculate.
# 
# ```{admonition} Definition (Trace)
# :class: definition
# 
# Let $\phi:V\to V$ be a linear map of a finite dimensional vector space. The trace of $\phi$ is the sume of diagonal entries $a_{11}+a_{22}+\ldots +a_{nn}$ of a matrix representing $\phi$ in any fixed basis for $V$. This is independent of the choice of basis.
# 
# ```
# 
# ```{admonition} Definition (Character)
# :class: definition
# 
# Let $V$ be a finite dimensional representation of a group $G$. The character of the representation is the function:
# 
# $$
# \begin{align*}
# &\chi_V:G\to \mathbb{F}\\
# &g\mapsto \mbox{ trace of } g\mbox{ acting } V
# \end{align*}
# $$
# 
# ```
# 
# 
# ```{admonition} Example (Character)
# :class: example
# 
# Character of $S_3$: let us compute the characters of the three irreducible representations of $S_3$:
# - the trivial representation $T$ of $S_3$ is one-dimensional and take the value $(1)$ for all elements in $S_3$. Its character is
# 
# $$
# \chi_T=(\chi_T(e),\chi_T((12)),\chi_T((13)),\chi_T((23)),\chi_T((123)),\chi_T((132)))=(1,1,1,1,1,1)
# $$
# 
# - the alternating representation $A$ of $S_3$ is one-dimensional and takes the value $(1)$ on all even permutations, and $(-1)$ on all odd permutations
# 
# $$
# \chi_A=(\chi_A(e),\chi_A((12)),\chi_A((13)),\chi_A((23)),\chi_A((123)),\chi_A((132)))=(1,-1,-1,-1,1,1)
# $$
# 
# - the standard representation $S$ characters could be found by writing the matrices for the action of each of the six elements in $S_3$. However, we can find it using the following fact:
# 
# > Let $V$ and $W$ be finite dimensional representations of a group $G$. Then
# >
# >$$
# \chi_{V\oplus W}=\chi_V+\chi_W
# $$
# >
# >as functions on $G$.
# 
# Now, because the permutation representation $P$ of $S_3$ decomposes as a sum of the trivial representation and the standard representation, we can compute the character of the standard representation using the fact above to get:
# 
# $$
# \chi_P=(3,1,1,1,0,0)=\chi_{T\oplus S}=\chi_T+\chi_S
# $$
# 
# that implies that
# 
# $$
# \chi_S=(3,1,1,1,0,0)-(1,1,1,1,1,1)=(2,0,0,0,-1,-1)
# $$
# 
# All characters of $S_3$ are summarized in the table below
# 
# $$
# \begin{array}{c|c|c|c|c|c|c}
# &e&(12)&(13)&(23)&(123)&(132)\\
# \hline
# \mbox{trivial}&1&1&1&1&1&1\\
# \hline
# \mbox{alternating}&1&-1&-1&-1&1&1\\
# \hline
# \mbox{standard}&2&0&0&0&-1&-1
# \end{array}
# $$
# 
# The characters of any representation $V$ of $S_3$ can be obtained from these three by decomposing into irreducibles:
# 
# $$
# V=T^{a}\oplus A^b\oplus S^c
# $$
# 
# and using 
# 
# $$
# \chi_V=a \chi_T+b\chi_A+c\chi_S
# $$
# 
# ```
# 
# Isomorphic representations have the same character, but also the converse is true: the character completely determines the representation up to an isomorphism. Much stronger statement is true: the rows of the character table are orthonormal to each other. This means that if $\chi_V$ and $\chi_W$ are characters of irreducible representations of $G$ then their scalar product is either $1$ or $0$, depending on whether $V\cong W$ or not.
# 
# This implies that the number of different irreducible representations of $G$ must be smaller than $|G|$. In fact, there is a better bound on the number of irreducible representations of a finite group. Notice that each character takes the same valus on elements with the same cycle structure. This comes from a property of traces that implies that
# 
# $$
# \chi_V(hgh^{-1})=\chi_V(g)
# $$
# 
# In other words, if $g'=h gh^{-1}$ then $\chi_V(g')=\chi_V(g)$. We call such elements conjugate to each other and for symmetric groups there is a general statement that two permutations are conjugated if they have the same cycle structure. To avoid redundancy, we can therefore write a simplified character table for $S_3$:
# 
# $$
# \begin{array}{c|c|c|c}
# g&e&(12)&(123)\\
# \hline
# \#&1&3&2\\
# \hline
# \mbox{trivial}&1&1&1\\
# \hline
# \mbox{alternating}&1&-1&1\\
# \hline
# \mbox{standard}&2&0&-1
# \end{array}
# $$
# 
# where in the second row we indicated the number of elements in each conjugacy class.
# 
# To summarize, we have the following useful statement: for finite-dimensional representations of a finite group $G$ we have:
# - there are at most $t$ irreducible representations of $G$, where $t$ is the number of conjugacy classes of $G$.
# -each representation is determined (up to an isomorphism) by its character
# - a complex representation $V$ is irreducible if and only if $\langle\chi_V,\chi_V\rangle=1$
# - the multiplicity of a complex irreducible representation $W$ in a representation $V$ is given by $\langle \chi_V,\chi_W\rangle$,
# 
# where we defined 
# 
# $$
# \langle\chi_W,\chi_V\rangle =\frac{1}{|G|}\sum_{g\in G}\chi_W(g)\overline{\chi_V(g)} 
# $$
# where the overline indicates the complex conjugate.
# 
# This provides us with a powerful tool for analysing complex representaions of finite groups. In particular, we can take any representation and decompose it into irreducible representations using the character theory. Let us take the regular representation $R$ of $S_3$. It is a six-dimensional representation obtained by left multiplication by group elements. We already showed that there are only three representation of $S_3$: trivial $T$, alternating $A$ and standard $S$. Therefore, we have a decomposition
# 
# $$
# R\cong T^{a}\oplus A^b\oplus S^c
# $$
# 
# for some non-negative integers $a,b,c$. This produces the following relation on characters:
# 
# $$
# \chi_V=a \chi_T+b\chi_A+c\chi_S
# $$
# 
# The character of the regular representation is $(6,0,0)$. This leads to a system of linear equations:
# 
# $$
# (6,0,0)=a(1,1,1)+b(1,-1,1)+c(2,0,-1)
# $$
# 
# which is solved by: $(a,b,c)=(1,1,2)$. therefore, the regular representation of $S_3$ decomposes as:
# 
# $$
# R\cong T\oplus A\oplus S^2
# $$
# 
# This statement can be generalised to any finite group:
# 
# ```{admonition} Proposition 
# :class: proposition
# 
# The regular representation $R$ of any finite group $G$ decomposes (over $\mathbb{C}$) as
# 
# $$
# R\cong W_1^{\dim W_1}\oplus W_2^{\dim W_2}\oplus \ldots \oplus W_t^{\dim W_t}
# $$
# 
# with every irreducible representation $W_i$ appearing exactly $\dim W_i$ times
# ```
# 
# This proposition leads to a useful relation:
# 
# $$
# |G|=\sum_i(\dim W_i)^2
# $$
# 
# where the sum is taken over all irreducible complex representations of $G$.
# 
# ```{admonition} Example (Complete classification of irreducible representations of $D_4$)
# :class: example
# 
# For $D_4$ we have $5$ conjugacy classes of elements:
# 
# $$
# C_1=\{e\}\quad C_2=\{A,A^3\}\quad C_3=\{A^2\}\quad C_4=\{B,A^2 B\}\quad C_5=\{AB,A^3 B\}
# $$
# 
# This means that there are $5$ irreducible complex representations of $D_4$. Moreover, we found $2$ of them already:
# 
# $$
# \begin{array}{c|c|c|c|c|c}
# g&C_1&C_2&C_3&C_4&C_5\\
# \hline
# \# &1&2&1&2&2\\
# \hline
# \mbox{trivial}&1&1&1&1&1\\
# \hline
# \mbox{tautological}&2&0&-2&0&0
# \end{array}
# $$
# 
# Let $W_3$, $W_4$ and $W_5$ be the remaining irreducible representation, with dimensions $w_3,w_4$ and $w_5$. Then 
# 
# $$
# |D_4|=8=1^2+2^2+w_1^2+w_4^2+w_5^2
# $$
# 
# that implies that $w_3=w_4=w_5=1$. All remaining representaions are one-dimensional. They have the following characters:
# 
# 
# $$
# \begin{array}{c|c|c|c|c|c}
# g&C_1&C_2&c_3&C_4&C_5\\
# \hline
# \#&1&2&1&2&2\\
# \hline
# \mbox{trivial}&1&1&1&1&1\\
# \hline
# \mbox{tautological}&2&0&-2&0&0\\
# \hline
# W_3&1&1&1&-1&-1\\
# \hline
# W_4&1&-1&1&1&-1\\
# \hline
# W_5&1&-1&1&-1&1
# \end{array}
# $$
# 
# It is easy to checj that they are orthonormal. For example
# 
# $$
# \langle \chi_{W_1},\chi_{W_3}\rangle=\frac{1}{8}(1\cdot 1\cdot 1+2\cdot 1\cdot 1+1\cdot 1\cdot 1+2\cdot 1\cdot (-1)+1\cdot 1\cdot (-1))=0
# $$
# 
# Also
# 
# $$
# \langle \chi_{W_3},\chi_{W_3}\rangle=\frac{1}{8}(1\cdot 1\cdot 1+2\cdot 1\cdot 1+1\cdot 1\cdot 1+2\cdot (-1)\cdot (-1)+1\cdot (-1)\cdot (-1))=1
# $$
# 
# ```

# In[ ]:




