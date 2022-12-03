
proposition
---
The proposition and proof provided describe a method for finding the best possible distribution $R_\lambda$ that minimizes the Kullback-Leibler (KL) divergence between two given distributions $P$ and $Q$. The proposition states that if $R_\lambda$ satisfies certain conditions, then it is the best possible solution to this optimization problem, and no other distribution can outperform it.

The proof of the proposition proceeds by first defining the Pareto frontier of the pair of objectives $\big(\kl(Q|\cdot), \kl(P | \cdot)\big)$. This is the set of all points in the space of possible solutions that are Pareto-optimal, meaning that they cannot be improved upon in one objective without deteriorating in the other.

Next, the proof uses the convexity of the KL divergence to show that the Pareto frontier can be computed exactly by minimizing linear combinations of the objectives. This allows us to find the distribution $R_\lambda$ that is Pareto-optimal for the pair of objectives $\big(\kl(Q|\cdot), \kl(P | \cdot)\big)$.

Finally, the proof invokes the next lemma to show that $R_\lambda^\star = \lambda P + (1-\lambda) Q$, which completes the proof. This result shows that the distribution $R_\lambda$ is the best possible solution to the optimization problem, and no other distribution can outperform it.

In the context of the proposition and proof provided, the Pareto frontier of the pair of objectives $\big(\kl(Q|\cdot), \kl(P | \cdot)\big)$ is the set of all points in the space of possible solutions that are Pareto-optimal.


pareto frontier
---
In other words, the Pareto frontier is the set of points that cannot be improved upon in one objective without deteriorating in the other. For example, if we were trying to find the distribution $R$ that minimizes the KL divergence between $P$ and $R$ and between $Q$ and $R$, then the Pareto frontier would be the set of all points in the space of possible solutions that cannot be improved upon in one objective (minimizing the KL divergence between $P$ and $R$ or between $Q$ and $R$) without deteriorating in the other.

In general, the Pareto frontier is a useful concept in optimization problems where we have multiple objectives that may conflict with each other. It allows us to identify the best possible solutions that cannot be improved upon in one objective without worsening in another.


Lemmma 2
---

The lemma provided is a useful mathematical result that relates the Kullback-Leibler (KL) divergence of two discrete distributions $P$ and $Q$ to the KL divergence of a third distribution $S$.

The lemma states that for any $\lambda \in [0, 1]$ and $\bar \lambda = 1- \lambda$, the following identity holds:

$$\lambda , \kl(P|S) + \bar \lambda , \kl(Q|S) = \lambda , \kl(P| R_\lambda) + \bar\lambda, \kl(Q|R_\lambda) + \kl(R_\lambda|S)$$

where $R_\lambda = \lambda P + \bar \lambda Q$. This identity shows that the KL divergence between $P$ and $Q$ on one side is related to the KL divergence between $P$ and $R_\lambda$, between $Q$ and $R_\lambda$, and between $R_\lambda$ and $S$ on the other side.

The lemma also states that as a consequence of this identity, we have that $R_\lambda \in \argmin_S \left{\lambda , \kl(P|S) + \bar \lambda, \kl(Q|S) \right}$. This means that the distribution $R_\lambda$ is the best possible solution to the optimization problem of minimizing the KL divergence between $P$ and $Q$ and between $P$ and $S$ or between $Q$ and $S$.

Overall, the lemma provides a useful mathematical result that relates the KL divergence of two discrete distributions to the KL divergence of a third distribution, and it can


Connection to Divergence Front
---


The paragraph provided explains the relationship between the Pareto frontier of the pair of objectives $\big(\kl(Q|\cdot), \kl(P | \cdot)\big)$ and the notion of the inclusive divergence frontier as defined by \citet{djolonga2020precision}.

The Pareto frontier is defined as the set of all points in the space of possible solutions that are Pareto-optimal, meaning that they cannot be improved upon in one objective without deteriorating in the other. In the context of the proposition and proof provided, the Pareto frontier of the pair of objectives $\big(\kl(Q|\cdot), \kl(P | \cdot)\big)$ is the set of all points in the space of possible solutions that cannot be improved upon in minimizing the KL divergence between $P$ and $Q$ or between $P$ and $R_\lambda$ or between $Q$ and $R_\lambda$ without deteriorating in the other.

The inclusive divergence frontier, as defined by \citet{djolonga2020precision}, is closely related to the Pareto frontier. It is defined as the set of all points in the space of possible solutions that cannot be improved upon in one objective without deteriorating in the other.

The paragraph states that the Pareto frontier of the pair of objectives $\big(\kl(Q|\cdot), \kl(P | \cdot)\big)$ coincides exactly with the inclusive divergence frontier. This means that the two concepts are essentially the same, and they both capture the notion of the set of points in the space of possible solutions that cannot be improved upon in one objective without deteriorating in the other.

Furthermore, the paragraph also provides an expression for the relationship between the inclusive KL divergence frontier and the divergence curve. It states that the inclusive KL divergence frontier is related to the divergence curve as follows:

$$\Fcal(P, Q) = \Big{ \left( c^{-1} \log t_1^{-1}, c^{-1} \log t_2^{-1} \right) , : , (t_1, t_2) \in \Ccal(P, Q) \Big}$$

This expression shows that the inclusive KL divergence frontier can be computed from the divergence curve by taking the inverse logarithm of the values in the set $\Ccal(P, Q)$ and then scaling by $c^{-1}$. This relationship provides a


## How is open-ended text generation currently evaluated?

***An analysis of popular evaluation metrics: Examples and Observations*** 

### Human

Human evaluation captures quality but not diversity, as it does not catch models that simply plagiarize from the training set. Hence, zero generalization ability and thus have inadequate diversity. Humans cannot quantify diversity. More often than not, they tend to not catch under diversity [3]. 

---

### Statistical

- **Perplexity**
    
    Perplexity is a common metric for evaluating language models. It is defined as the inverse probability of the test data. Mathematically, it is the exponentiation of cross entropy.
    
    $$
     Perplexity = e^{CE} = e^{-\frac{1}{N}\sum_{i=1}^N logP(x_i)}
    
    $$
    
    Observations
    
    - Generally, the lower the perplexity, the better the model. But, in the domain of open-ended text generation, the lower the perplexity, the more likely the model is to repeat itself.
    - So, the model has to achieve similiar perplexity on both human and machine generated text so that a balance between generating new text and repeating itself. But the problem with using the perplexity metric is that it is not a good measure of the quality of the text generated by the model.
    - The lowest possible perplexity is unknown (lower bound) since a perplexity of zero is impossible. If we don’t know the optimal value, we can't determine how effective our language model is.
    - Also, it assumes perfect history, which might not always be the case when using previously generated data to generate a new word.
    - For example, the model can generate a text with perplexity as same as the human generated text but the model generated text can be completely nonsensical.


----

The authors of MAUVE quantify both diversity and quality of the generated text with the notion of Type I and Type II errors respectively


|     | $P(x) \approx 0$ | $P(x) \approx 1$ |
| --- | ------- | ------- |
| $Q(x) \approx 0$ | - | **Type II error (TN)** |
| $Q(x) \approx 1$ | **Type I error (FP)** | - |


- **Type I error (FP)**: The model assigns a high probability to a sequence that has a low probability in the human generated text which is unlike written by humans. This is a false positive error.
- **Type II error (TN)**: The model assigns a low probability to a sequence that has a high probability in the human generated text. An indication that the model is not able to generate text like human text. This is a false negative error.


#### KL Divergence

$$KL(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log \frac{P(x)}{Q(x)}$$

Using KL divergence, the authors of MAUVE formalize the notion of Type I and Type II errors. 

$KL(Q||P)$ penalizes the model for assigning a high probability to a sequence that has a low probability in the human generated text. Conversely, $KL(P||Q)$ penalizes the model for assigning a low probability to a sequence that has a high probability in the human generated text.

**Problems with KL Divergences**

- *"KL divergence is infinite if the support of the distributions are not identical"*


Consider the following two distributions $P$ and $Q$:

$$P = [0.22, 0.57, 0.12, 0.69]$$

$$Q = [0.31, 0.42, 0.12]$$

In this example, the support of distribution $P$ is the set of four elements $\{1, 2, 3, 4\}$, while the support of distribution $Q$ is the set of three elements $\{1, 2, 3\}$. 

The support of a probability distribution is the set of all possible values that a random variable can take on. In other words, it is the range of values that the random variable can assume, and it is typically defined by the domain of the distribution's underlying probability density or mass function.

Since the two distributions do not have the same support, the KL divergence between them is infinite. This is because the value of $Q$ at the fourth element (which is not in the support of $Q$) is $0$, so the log of the ratio of $P$ and $Q$ at this point is infinite. Therefore, the KL divergence between $P$ and $Q$ is also infinite.

#### Solution

*"Use a mixture distribution to ***softly*** measure the two errors"*
  
Authors define the mixture distribution is defined as follows:

$$R_{\lambda} = \lambda P + (1 - \lambda) Q$$


where $\lambda$ is a parameter that controls the relative weight of the two distributions and ranges from $0$ to $1$ **not inclusive.**

The not inclusive part is important because if $\lambda$ is $0$ or $1$, then the mixture distribution is just $P$ or $Q$ respectively. So by always keeping $\lambda$ in the range $(0, 1)$, we ensure that the mixture distribution does not have a zero probability at any point because we are always adding a non-zero probability to the mixture distribution (either $P$ or $Q$).

So the previous example would be:

$P = [0.22, 0.57, 0.12, 0.69]$

$Q = [0.31, 0.42, 0.12]$


$\lambda = 0.001$

$R_{\lambda} = 0.001 \times [0.22, 0.57, 0.12, 0.69] + (1 - 0.001) \times [0.31, 0.42, 0.12]$

$R_{\lambda = 0.001} = [0.3099, 0.4202, 0.12  , 0.0007]$

We see that the mixture distribution $R_{\lambda}$ has a non-zero probability at the fourth element, so the KL divergence between $P$ and $Q$ is no longer infinite.

---

> Just to point out that in the bigger scheme of things, the primary focus is to minimize both the Type I and Type II errors.

---

By exponetiating the two KL divergences and varying $\lambda$, we can get a curve that shows the trade-off between the two errors. 

"This yields a divergence curve." *(More on this later)*


$$C(P, Q) = \Big\{ \big(\exp(-c\, KL(Q|R_\lambda)), \exp(-c\, KL(P|R_\lambda)) \big) \Big\}_{\lambda \in [0, 1]}$$ 

where $c$ is a hyperparameter for scaling.


