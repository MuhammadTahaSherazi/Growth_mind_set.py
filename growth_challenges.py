import streamlit as st
import random
from growth_challenges import challenges

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🌱 Growth Mindset Challenge")
st.write("Click the button to get a challenge that boosts your growth mindset!")

if st.button("Give me a challenge!"):
    challenge = random.choice(challenges)
    st.success(challenge)
else:
    st.info("Click the button above to get started.")
