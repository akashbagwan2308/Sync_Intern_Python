# Url Shortner

import streamlit as st
import pyshorteners
import clipboard

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

# Streamlit app
st.title("URL Shortener")
url_to_shorten = st.text_input("Enter the URL to shorten")

# Button to shorten the URL
if st.button("Shorten"):
    if url_to_shorten:
        shortened_url = shorten_url(url_to_shorten)
        clipboard.copy(shortened_url)
        st.success("Shortened URL:")
        st.write(shortened_url)
        st.info("The shortened URL has been copied to the clipboard.")
    else:
        st.warning("Please enter a URL to shorten.")

