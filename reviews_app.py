import streamlit as st
import scraper
import summaryllm
import os

model = "meta/meta-llama-3-70b-instruct"

tab1, tab2 = st.tabs(['Home', "More Info"])

key = os.environ["REPLICATE_API_TOKEN"]

with tab1:
    st.title("Amazon Reviews Summarizer")
    st.write("🚀 Instead of scouring reviews yourself, let this LLM pipeline do it for you!")

    instructions = "Instructions:\n 1. Once you're on a product's website on Amazon, scroll down to where you see the reviews. \n 2. Filter the reviews by clicking on the 1, 2, 3, 4, or 5 star reviews (seen on the left hand side of the Amazon webpage).\n 3. Copy this url and paste it into the box below to get your summary!"

    st.write(instructions)

    # Input control for filtering by partial name
    url = st.text_input("Copy and paste the url here", "")

    if st.button("Get Reviews Summary"):
        reviews = scraper.scrape(url)
        summary = summaryllm.get_summary(reviews, model, key)
        summary

with tab2:
    "# How it works"

    "The LLM being employed is Meta's llama-3-70b-instruct. This LLM pipeline works by scraping reviews from the Amazon url and passing them to the LLM to distill each one down to a principal complaint or praise. Then, it passes these distilled versions back into the LLM again where it consolidates similar reviews and provides an overarching summary."
