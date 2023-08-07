# LLM Numerical Bias Investigation

This is a repository for investigating the bias that LLMs appear to have when generating random numbers (see: [Link 1](https://gist.github.com/alonsosilvaallende/7551194ecb9b0a0a31cffb23b66c3919), [Link 2](https://twitter.com/RaphaelWimmer/status/1680290408541179906)).

![alt text](https://github.com/P-H-B-D/LLMNumericBias/blob/main/figures/1_10_n1001.csv.png)

Based off of the work of [https://gist.github.com/alonsosilvaallende/7551194ecb9b0a0a31cffb23b66c3919](https://gist.github.com/alonsosilvaallende/7551194ecb9b0a0a31cffb23b66c3919), I am looking into in-prompt "tricking" of the LLM into generating more truly random numbers without increasing temperature.

The main reason why I am doing this is that I am also planning to study downstream effects of numerical bias in LLMs, notably the possible effect of the type of numerical bias observed in RNG to the common implementation of using an LLM as a numerical rating or system (e.g. "Analyze the sentiment of this message from 0 to 10."). If a more generic technique to normalize RNG distributions is determined, I believe there is reason to believe that this could help alleviate any [intrinsic bias](https://twitter.com/Teknium1/status/1687983538996740097) in LLM rating systems.

While skewed distributions may be counteracted by measuring model outputs on a representative sample of the data and constructing an inverse normalization function, this process is 1) time consuming and 2) if data is insufficient to form a representative sample (as it often is with NLP), ineffectual. Better to do it with a prompt modification if possible. 

Follow along here or on my [Twitter](https://twitter.com/0xPHBD) and feel free to reach out if you would like to collaborate on this project or similar works. 

# Data

Data and figures of produced distributions may be found in the "datasets" and "figures" folders, labelled in the following format:

- <lower_bound>_<upper_bound>_n<sample_size>_<modifier>
- As of now, modifiers include: 
    - "nologit": not using logit biasing (useful for larger numbers which occupy multiple tokens and numerical encoding)
    - "inclusive": using the word "inclusive" after each bound in the prompt so as to see if any change is observed in the distribution (it is not as of now).

# Code

dataGenAsync.py and dataGenAsyncNoLogit.py are used to generate the data.

visualize.py is used to take the csv data and visualize it as a normalized distribution.

Standard prompt: 
- "generate a random number from {str(low)} to {(high)}"

Inclusive prompt: 
- "generate a random number from {str(low)} (inclusive) to {(high)} (inclusive)"

# TODO:
- More distributions + ranges. 
- Prompt techniques: Making LLM encode numbers as hex, give numbers as floats, make ranges (multi-token) big numbers, even more. 
