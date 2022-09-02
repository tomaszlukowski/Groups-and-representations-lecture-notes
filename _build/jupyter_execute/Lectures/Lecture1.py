#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import HTML as Center

Center(""" <style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style> """)


# # Linear algebra - crash course
# 
# We will start by recalling from linear algebra the definition of a vector space and a linear map. These notion will be crucial in the definition and interpretation of group representations that we will introduce in the following lectures.
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
# We will be dealing mostly with finite dimensional vector spaces in these lectures. In such case, we can introduce the definition of a basis of a vector space. 
# 
# ```{admonition} Definition (Linearly independent vectors)
# :class: definition
# 
# Let $V$ be an $n$-dimensional vector space and let $v_1,v_2,\ldots,v_k\in V$ be vectors. Then we say that these vectors are linearly independent if the vector equation
# $$
# \alpha_1 v_1+\alpha_2 v_2+\ldots \alpha_k v_k=0
# $$
# has only the trivial solution $\alpha_1=\alpha_2=\ldots=\alpha_k$.
# ```
# 
# ```{admonition} Example (Linearly independent vectors)
# :class: example
# 
# Let us take $V=\mathbb{R}^2$ and $v_1=\begin{pmatrix}2\\3\end{pmatrix}$
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

# In[ ]:




