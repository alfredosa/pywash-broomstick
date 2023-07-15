import random

import streamlit as st

# Generate a random number
random_number = random.randint(1, 100)

# Display the random number using Streamlit
st.write("Random Number:", random_number)