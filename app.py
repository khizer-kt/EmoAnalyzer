import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    st.title("Sentiment Analysis Tool")
    text = st.text_area("Enter text for sentiment analysis")

    # Perform sentiment analysis
    if st.button("Analyze"):
        # Create a TextBlob object for the input text
        blob = TextBlob(text)

        # Get the sentiment polarity (-1 to 1) and subjectivity (0 to 1)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity

        # Define sentiment labels based on polarity
        if sentiment_polarity > 0:
            sentiment_label = "Positive"
        elif sentiment_polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        # Display the sentiment scores and labels
        st.write("Sentiment Polarity:", sentiment_polarity)
        st.write("Sentiment Subjectivity:", sentiment_subjectivity)
        st.write("Sentiment Label:", sentiment_label)

        # Generate sentiment distribution visualization
        sentiment_distribution = {"Positive": 0, "Neutral": 0, "Negative": 0}
        sentiment_distribution[sentiment_label] += 1

        fig, ax = plt.subplots()
        ax.bar(sentiment_distribution.keys(), sentiment_distribution.values())
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        ax.set_title("Sentiment Distribution")

        st.pyplot(fig)

        # Generate word cloud visualization
        wordcloud = WordCloud().generate(text)

        plt.figure(figsize=(8, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Word Cloud")

        st.pyplot(plt)

# Run the Streamlit app
if __name__ == "__main__":
    main()
