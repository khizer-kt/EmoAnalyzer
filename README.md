# EmoAnalyzer
## Overview
The Sentiment Analysis Tool is a web application that performs sentiment analysis on text input provided by the user. It leverages natural language processing techniques to determine the sentiment polarity and subjectivity of the text, providing valuable insights into the emotional tone of the content.
## Features
- **Sentiment Analysis:** The tool analyzes the sentiment of the text input and provides sentiment polarity, subjectivity, and sentiment labels (positive, negative, or neutral).
- **Sentiment Distribution Visualization:** It generates a bar chart that displays the distribution of sentiment labels within the analyzed text, providing an overview of the sentiment composition.
- **Word Cloud Visualization:** The tool generates a word cloud visualization to showcase the most frequent words in the analyzed text, giving an at-a-glance representation of the prominent themes or sentiments.

## Dependencies
**1. Streamlit:** Streamlit is a Python library used for building interactive web applications. It provides an intuitive and straightforward way to create user interfaces for data analysis and visualization.

**2. TextBlob:** TextBlob is a Python library that simplifies natural language processing tasks, including sentiment analysis. It offers a high-level API for sentiment analysis, tokenization, part-of-speech tagging, and more. In this tool, TextBlob is used for sentiment analysis.

**3. Matplotlib:** Matplotlib is a popular plotting library in Python. It provides a wide range of functionalities for creating visualizations, such as bar charts. In this tool, Matplotlib is used to visualize the sentiment distribution.

**4. Wordcloud:** Wordcloud is a Python library for generating word clouds, which are visual representations of word frequency in a text corpus. It helps visualize the most frequently occurring words in the analyzed text.
## Installation and Setup
To use the **EmoAnalyzer** tool, follow these steps:
- Ensure you have Python and pip installed on your machine.
- Clone the project repository from https://github.com/khizer-kt/EmoAnalyzer
- Navigate to the project directory and create a virtual environment (optional but recommended).
- Install the required dependencies by running the following command:
```
pip install -r requirements.txt

```
Run the Streamlit app using the following command:
```
streamlit run app.py

```
