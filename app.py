import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    st.set_page_config(
        page_title="EmoAnalyzer🥺",
        page_icon=":smiley:",
        layout="centered",
        initial_sidebar_state="auto"
    )
    st.title("EmoAnalyzer🥺")
    text = st.text_area("Enter Text For Emotion Testing")

    if st.button("Analyze"):
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity
        if sentiment_polarity > 0:
            sentiment_label = "Positive"
        elif sentiment_polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        st.write("Sentiment Polarity:", sentiment_polarity)
        st.write("Sentiment Subjectivity:", sentiment_subjectivity)
        st.write("Sentiment Label:", sentiment_label)

        sentiment_distribution = {"Positive": 0, "Neutral": 0, "Negative": 0}
        sentiment_distribution[sentiment_label] += 1
        fig, ax = plt.subplots()
        ax.bar(sentiment_distribution.keys(), sentiment_distribution.values())
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        ax.set_title("Sentiment Distribution")
        st.pyplot(fig)
        wordcloud = WordCloud().generate(text)
        plt.figure(figsize=(8, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Word Cloud")
        st.pyplot(plt)

if __name__ == "__main__":
    main()
