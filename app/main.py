import streamlit as st

# Sidebar
st.sidebar.title("Table of Contents")
st.sidebar.markdown("""
- [Introduction](#introduction)
    - [What is open-ended text generation?](#what-is-open-ended-text-generation)
    - [Why is evaluation of open-ended text generation important?](#why-is-evaluation-of-open-ended-text-generation-important)
    - [How is open-ended text generation currently evaluated?](#how-is-open-ended-text-generation-currently-evaluated)
- [The Problem](#the-problem)
- [MAUVE](#mauve)
    - [How to quantify quality and diversity?](#how-to-quantify-quality-and-diversity)

""")




# ------------------------- Title ------------------------- #

# Center the title and subtitles
st.markdown( """ <h1 style='text-align: center;'> Evaluation metrics for open-ended text generation: A review</h1> """, unsafe_allow_html=True)
st.markdown( """ <h4 style='text-align: center;'> <i> with a special focus on the state-of-the-art metric: MAUVE </i></h4> """, unsafe_allow_html=True)



# ---------------------------------------------------------  Introduction --------------------------------------------------------- #
st.header("Introduction")


# ------------------------- What is text generation? ------------------------- #

st.subheader("What is open-ended text generation?")
st.write("""
Open-ended text generation is a type of text generation that is designed to produce realistic and coherent text without any predefined constraints or rules. This is in contrast to other types of text generation, such as machine translation or summarization, where the generated text is required to conform to certain rules or constraints.
To generate text, a language model can produce the next word given a context by using the conditional probability of the next word on the previous words:
""")

st.latex(r'P(w_{t+1}|w_{t},...,w_{1})')

st.write("""
Open-ended text generation is a challenging task because it requires the model to generate text that is not only grammatically correct and coherent, but also interesting and engaging. This requires the model to have a deep understanding of the language and the ability to generate a wide range of possible outputs.
This is done by decoding the language model with various algorithms like **beam search**, **greedy search**, **top-k sampling** and **top-p (Nucleas) sampling**. 
""")

# ------------------------- Why is it important? ------------------------- #
st.subheader("Why is evaluation of open-ended text generation important?")
st.write("""
Evaluating the performance of text generation models is a crucial step in their development because it helps to determine how well the models are able to generate realistic and coherent text. Here are a few reasons:
- The quality of the generated text is one of the key factors that determines the usefulness of a text generation model. 
- Evaluating the generated text is important for comparing different text generation models.
- Rvaluating the generated text is also important for understanding the limitations of text generation models.
""")





# ------------------------- How to evaluate open-ended text generation? ------------------------- #
# Add a subheader
st.subheader("How is open-ended text generation currently evaluated?")

# Add a text
st.write(""" ***(an analysis of popular evaluation metrics)*** """)


st.markdown("""
#### Statistical

#####  Perplexity
    
Perplexity is a common metric for evaluating language models. It is defined as the inverse probability of the test data. Mathematically, it is the exponentiation of cross entropy.

**Pros**: 
- Easy to compute, widely used in NLP
**Cons**: 
- Generally, the lower the perplexity, the better the model. But, in the domain of open-ended text generation, the lower the perplexity, the more likely the model is to repeat itself. So, the model has to achieve similiar perplexity on both human and machine generated text so that a balance between generating new text and repeating itself. But the problem with using the perplexity metric is that it is not a good measure of the quality of the text generated by the model.
- Also, it assumes perfect history, which might not always be the case when using previously generated data to generate a new word.
- ***For example***, the model can generate a text with perplexity as same as the human generated text but the model generated text can be completely nonsensical.
    """)

# st.latex(r'Perplexity = e^{CE} = e^{-\frac{1}{N}\sum_{i=1}^N logP(x_i)}')

st.markdown("""
#####  Zipf's Law

The Zipf coefficient is calculated by comparing the observed frequency of words in a text to the expected frequency of those words based on the Zipf's law, which states that the frequency of a word in a text is inversely proportional to its rank in the frequency list. 
The Zipf coefficient is calculated as the ratio of the observed frequency to the expected frequency.

**Pros**:
- Unlike metrics like Self-BLEU, which only provide a relative measure of the diversity of the generated data, Zipf coefficient can provide a direct and interpretable measure of the regularity of the generated text. This can make it easier to compare the performance of different models, and it can provide more concrete guidance on how to improve the performance of a given model.
- it takes into account the frequencies of all words in the generated text, not just individual sentences. This can provide a more comprehensive evaluation of the quality of the generated text, and it can help to identify issues with the coherence or fluency of the text as a whole.

**Cons**:
- One potential issue with using the Zipf coefficient is that it is based on the assumption that the Zipf's law accurately describes the distribution of words in a text. However, this assumption may not always hold in practice, and the Zipf's law may not be a perfect model of the distribution of words in a text. In such cases, the Zipf coefficient may not accurately reflect the quality of the language model, and it may not provide a reliable measure of the model's performance.
- It does not provide an absolute measure of the quality of the language model as it only considers the frequency of the n-grams and exluding order of the n-grams, the coherence or grammatical correctness of the generated text. 
- Also, some decoding algorithms work by truncating the tail of the word distribution, which can lead to a lower n-gram frequency but a higher quality text.


#####  Generation Perplexity

Generation perplexity is a measure of the quality of a language model that is calculated by taking the exponential of the average cross-entropy of the model's predictions on a generated dataset, unlike the perplexity metric, which is calculated on a test dataset.

**Pros**:
- It is a more accurate measure of the quality of the language model than the perplexity metric, as it is calculated on a generated dataset rather than a test dataset.

**Cons**:
- Generation perplexity only provides a partial evaluation of the quality of the generated text. By calculating the average cross-entropy of the model's predictions on a generated dataset, generation perplexity only provides information about the accuracy of the model's predictions, and it does not take into account other aspects of the generated text such as its content or its relevance to a given prompt.
- Generation perplexity can be sensitive to the choice of generated dataset. The value of the generation perplexity metric can depend heavily on the specific dataset used to calculate it, and it can be affected by factors such as the length of the generated text, the diversity of the generated text, and the difficulty of the prompts used to generate the text. Even decoding algorithms that produce similar results can produce different values of the generation perplexity metric, depending on the specific dataset used to calculate it.

""")


st.markdown("""
#### Reference-based
##### Self-BLEU

BLEU(BiLingual Evaluation Understudy) that measures the similarity between the generated text and the reference text. BLEU(N) is the number of n-grams in the candidate summary that are also in the reference summary. Self-BLEU is a metric based on BLEU which calculates the  number of n-grams in the generated text that are also in the reference text [7].

**Pros**:
- One potential benefit of using Self-BLEU is that it is a simple and intuitive measure that is easy to calculate and interpret. It is based on the BLEU metric, which is a widely-used and well-established measure of sentence similarity, and it extends this metric in a straightforward way to evaluate the diversity of generated data. As a result, Self-BLEU can be an accessible and user-friendly metric for evaluating the performance of open-ended text generation models.
- Another potential advantage of Self-BLEU is that it provides a relative measure of the diversity of generated data. By comparing the similarity of individual sentences to the rest of the generated data, Self-BLEU can provide a sense of how well the generated text is able to capture the diversity of possible outputs that the language model is capable of generating. This can be useful for identifying instances of mode collapse, where the language model is only able to generate a limited range of outputs, and for evaluating the effectiveness of different techniques for improving the diversity of generated text.


**Cons**:
- One potential issue with using Self-BLEU is that it is based on the BLEU metric, which is designed to evaluate the similarity of two sentences or texts. While this metric can be useful for assessing the quality of machine translation systems, it may not be well-suited for evaluating open-ended text generation, where the goal is to generate diverse and creative text, rather than text that is similar to a given reference text.
- The higher the self-BLEU(N), the more similar the generated text is to the reference text. Note that it is possible to have a model with a high Self-BLEU(N) that is not a good model.
- For example, self-BLEU(N) = 1, it means that all n-grams in the generated text are also in the reference text, which implies reference = model and which also implies that there is no diversity in the generated text.
- Self-BLEU also suffers from its quadratic runtime complexity as for each sample text, we need to calculate a BLEU score between that sample and the whole reference text.

""")

# --------------------------------------------------------- The Problem ---------------------------------------------------------------------------------- 


st.header("The Problem")

st.markdown("""
Open-ended text generation involves the generation of novel and unpredictable text, it can be difficult to evaluate the performance of a given model using traditional metrics such as perplexity or BLEU score.
The fundamental problem in the evaluation of open-ended text generation is the lack of a clear, objective metric for evaluating both **quality** and **diversity** of the generated text.""")

# 

st.header("MAUVE")
st.markdown("""***Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers***""")

st.subheader("How to quantify quality and diversity?")
st.markdown(""" The authors of MAUVE quantify both diversity and quality of the generated text with the notion of Type I and Type II errors respectively.

Let $P$ be the probability distribution of the human text and $Q$ be the probability distribution of the generated text. 

|     | $P(x) << 1$ | $P(x) >> 0$ |
| --- | ------- | ------- |
| $Q(x) << 1$ | - | **Type II error (TN)** |
| $Q(x)>> 0$ | **Type I error (FP)** | - |



- **Type I error (FP)**: The model assigns a high probability to a sequence that has a low probability in the human generated text which is unlike written by humans. This is a false positive error.
- **Type II error (TN)**: The model assigns a low probability to a sequence that has a high probability in the human generated text. An indication that the model is not able to generate text like human text. This is a false negative error.

"""
)

st.markdown("""
#### KL Divergence

$$KL(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log \\frac{P(x)}{Q(x)}$$

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

**Solution**

*"Use a mixture distribution to ***softly*** measure the two errors"*
  
Authors define the mixture distribution is defined as follows:

$$R_{\lambda} = \lambda P + (1 - \lambda) Q$$


where $\lambda$ is a parameter that controls the relative weight of the two distributions and ranges from $0$ to $1$ **not inclusive.**

The not inclusive part is important because if $\lambda$ is $0$ or $1$, then the mixture distribution is just $P$ or $Q$ respectively. So by always keeping $\lambda$ in the range $(0, 1)$, we ensure that the mixture distribution does not have a zero probability at any point because we are always adding a non-zero probability to the mixture distribution (either $P$ or $Q$).

So the previous example would be:

$P = [0.22, 0.57, 0.12, 0.69]$

$Q = [0.31, 0.42, 0.12]$


$\lambda = 0.001$

$R_{\lambda} = 0.001 \\times [0.22, 0.57, 0.12, 0.69] + (1 - 0.001) \\times [0.31, 0.42, 0.12]$

$R_{\lambda = 0.001} = [0.3099, 0.4202, 0.12  , 0.0007]$

We see that the mixture distribution $R_{\lambda}$ has a non-zero probability at the fourth element, so the KL divergence between $P$ and $Q$ is no longer infinite.

---

> Just to point out that in the bigger scheme of things, the primary focus is to minimize both the Type I and Type II errors.

---

By exponetiating the two KL divergences and varying $\lambda$, we can get a curve that shows the trade-off between the two errors. 

"This yields a divergence curve." *(More on this later)*


$$C(P, Q) = \Big\{ \\big(\exp(-c\, KL(Q|R_\lambda)), \exp(-c\, KL(P|R_\lambda)) \\big) \Big\}_{\lambda \in [0, 1]}$$ 

where $c$ is a hyperparameter for scaling.

""")


