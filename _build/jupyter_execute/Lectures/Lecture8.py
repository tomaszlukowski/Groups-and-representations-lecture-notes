#!/usr/bin/env python
# coding: utf-8

# # Classification of representations for symmetric groups
# 
# For the symmetric group $S_n$, all irreducible representations have been classified and they can be constructed using the so-called Young symmetrisers and Frobenius's formula for their characters.
# 
# ## Young diagrams
# 
# First, we observe that all conjugacy classes in $S_n$ are determined by their cycle structure. All elements of a class have the same cycle structure. The cycle struscture is described by a set of non-negative integers $\{\nu_r\}$, where $r=1,2,\ldots,n$, and $\nu_r$ is the number of $r$-cycles.
# 
# ```{admonition} Example (Conjugacy classes in $S_n$)
# :class: example
# 
# In $S_6$, the permutation $\sigma=(12)(456)$ has the cycle structure $(1,1,1,0,0,0)$.
# 
# ```
# 
# An alternative characterisation of the classes is in terms of the non-negative integers $\{\mu_r\}$ where 
# 
# $$
# \mu_s=\sum_{r=s}^n\nu_r
# $$
# 
# In this case $\mu_1\leq \mu_2\leq\ldots\leq \mu_n\leq 0$ and $\{\mu_r\}$ is a partition of $n$. The classes can be labelled by partitions of $n$ and there is as many classes as partitions of $n$. A useful way to keep track of the partitions os to introduce a pictorial notation in terms of Young diagrams. The Young diagram corresponding to the partition $\{\mu_r\}$ of $n$ consists of left-justified rows of $\mu_r$ boxes stacked in decreasing order of length.
# 
# ```{admonition} Example (Young diagrams)
# :class: example
# 
# For $S_5$ we have
# 
# $$
# \begin{array}{c|c|c|c|c}
# \mbox{cycle structure } \nu_r&\mbox{partition }\mu_r&\mbox{Young diagram}&\mbox{number of elements} &\mbox{example}\\
# \hline
# (5,0,0,0,0)&(5,0,0,0,0)&\begin{array}{l}\Box\Box\Box\Box\Box\end{array}&1&e\\
# \hline
# (3,1,0,0,0)&(4,1,0,0,0)&\begin{array}{l}\Box\Box\Box\Box\\[-5cm]\Box\end{array}&10&(12)\\
# \hline
# (1,2,0,0,0)&(3,2,0,0,0)&\begin{array}{l}\Box\Box\Box\\[-5cm]\Box\Box\end{array}
# &15&(12)(34)\\
# \hline
# (2,0,1,0,0)&(3,1,1,0,0)&\begin{array}{l}\Box\Box\Box\\[-5cm]\Box\\[-5cm]\Box\end{array}
# &20&(123)\\
# \hline
# (0,1,1,0,0)&(2,2,1,0,0)&\begin{array}{l}\Box\Box\\[-5cm]\Box\Box\\[-5cm]\Box\end{array}
# &20&(12)(345)\\
# \hline
# (1,0,0,1,0)&(2,1,1,1,0)&\begin{array}{l}\Box\Box\\[-5cm]\Box\\[-5cm]\Box\\[-5cm]\Box\end{array}
# &30&(1234)\\
# \hline
# (0,0,0,0,1)&(1,1,1,1,1)&\begin{array}{l}\Box\\[-5cm]\Box\\[-5cm]\Box\\[-5cm]\Box\\[-5cm]\Box\end{array}
# &24&(12345)\\
# \hline
# \end{array}
# $$
# ```
# 
# The number of elements in a class of cycle structure $\{\nu_r\}$ is $\frac{n!}{\prod_r r^{\nu_r}\nu_r!}$.
# 
# ## Irreducible representations of $S_n$
# 
# Young diagrams plat a more significant role in defining the irreducible representations of the symmetric group. There is a Young diagram for every partition of $n$, but there is also an irreducible representation of $S_n$ for every Young diagram.
# 
# Given a Young diagram, one produces a Young tableaux by filling the $n$ boxes of the diagram with the numbers $1$ through $n$, in such a way that the numbers always increase from left to right along each row and from top to bottom in any column.
# 
# The dimension of the irreducible representation is the number of different Young tableaux that can be produced this way. This can be easily calculated using the so-called hook-length formula.
# 
# ### Hook-length formula
# 
# In a Young diagram place a hook pointing to the right and down in the center of each box. The hook length of the box is the number of boxes lying along the hook in both directions.
# 
# Now, in each box of a Young diagram enter its hook length. The number of distinct Young tableaux, and therefore the dimension of the corresponding representation, in $n!$ divided by the product of all hook lengths.
# 
# ### Young symmetriser
# 
# To each Young tableau there is a symmetriser that projects out of any vector on which it acts the part belonging to the irreducible representation associated to this tableau. To construct it, we need to identify among all $n!$ permutations, those which leave the labels in their rows (denoted $R$) and those which leave the labels in the columns (denoted $C$).
# 
# Define the following combination of permutations
# 
# $$
# \rho=\sum_{r\in R}e_r\quad\quad \kappa=\sum_{c\in C}\mathrm{sign}(c)e_c
# $$
# 
# Then the Young symmetriser is defined as:
# 
# $$
# P=\rho\circ \kappa
# $$
# 
# ## Frobenius's formula for characters
# 
# The Frobenius's formula will allow us to find all characters for irreducible representations of $S_n$. Take a representation given by a Young diagram $Y$.
# - Introduce independent variables $x_1,x_2,\ldots,x_k$, where $k$ is the number of rows of $Y$
# - Define power sums $P_j=x_1^j+x_2^j+\ldots +x_k^j$ for $1\leq j\leq n$
# - Define the discriminant $\Delta=\prod_{i<j}(x_i-x_j)$.
# 
# Then 
# 
# $$
# \chi_\mu(\nu)=\left[\Delta\prod_{j=1^n}P_j^{\nu_j}\right]_{\mbox{coeff of }x_1^{l_1}\cdot\ldots\cdot x_k^{l_k}}
# $$
# 
# where $l_j=\mu_j+k-j$ (we are not interested in $l_j$ for $j>k$; in other words we remove all $0$s from $\mu$).
# 
# ```{admonition} Example
# :class: example
# 
# In $S_3$, take the irreducible representation given by $Y=\begin{array}{l}\Box\Box\\[-5cm]\Box\end{array}$. Then $k=2$. there are two variables: $x_1$ and $x_2$. Here $\mu=(2,1,0)$ and therefore $l_1=2+2-1=3$ and $l_2=1+2-2=1$.
# 
# Let us take the class of $e$ with the cycle structure $(3,0,0)$. Then
# 
# $$
# \chi_{(2,1,0)}((3,0,0))=\left[\Delta P_1^3 P_2^0 P_3^0\right]_{\mbox{coeff of }x_1^3x_2}=\left[(x_1-x_2)(x_1+x_2)^3\right]_{\mbox{coeff of }x_1^3x_2}=2
# $$
# 
# Similarly for other conjugacy classes:
# 
# $$
# \chi_{(2,1,0)}((1,1,0))=\left[\Delta P_1^1 P_2^1 P_3^0\right]_{\mbox{coeff of }x_1^3x_2}=\left[(x_1-x_2)(x_1+x_2)(x_1^2+x_2^2)\right]_{\mbox{coeff of }x_1^3x_2}=0
# $$
# 
# $$
# \chi_{(2,1,0)}((0,0,1))=\left[\Delta P_1^0 P_2^0 P_3^1\right]_{\mbox{coeff of }x_1^3x_2}=\left[(x_1-x_2)(x_1^3+x_2^3)\right]_{\mbox{coeff of }x_1^3x_2}=-1
# $$
# ```
# 

# In[ ]:




