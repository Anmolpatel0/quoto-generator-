import random
import streamlit as st

# Page Configuration for a clean look
st.set_page_config(
    page_title="Random Quote Generator", page_icon="✨", layout="centered"
)

# Initialize session state with a default list of quotes
if "quotes" not in st.session_state:
  st.session_state.quotes = [
      {
          "text": (
              "The best way to get started is to quit talking and begin doing."
          ),
          "author": "Walt Disney",
      },
      {
          "text": (
              "The pessimist sees difficulty in every opportunity. The optimist"
              " sees opportunity in every difficulty."
          ),
          "author": "Winston Churchill",
      },
      {
          "text": (
              "Don't let yesterday take up too much of today."
          ),
          "author": "Will Rogers",
      },
      {
          "text": (
              "It's not whether you get knocked down, it's whether you get up."
          ),
          "author": "Vince Lombardi",
      },
      {
          "text": (
              "If you are working on something that you really care about, you"
              " don't have to be pushed. The vision pulls you."
          ),
          "author": "Steve Jobs",
      },
      {
          "text": (
              "People who are crazy enough to think they can change the world,"
              " usually do."
          ),
          "author": "Rob Siltanen",
      },
  ]

# Initialize current random quote in session state so it persists on rerun
if "current_quote" not in st.session_state:
  st.session_state.current_quote = random.choice(
      st.session_state.quotes
  )

# App Header
st.title("✨ Random Quote Generator")
st.write("Discover inspiring words and wisdom with a single click.")
st.markdown("---")

# Display the current quote inside a clean container/card style
st.markdown("<br>", unsafe_allow_html=True)

quote_container = st.container()
with quote_container:
  st.markdown(
      f"<h3 style='text-align: center; color: #4A90E2;'>“{st.session_state.current_quote['text']}”</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<p style='text-align: right; font-style: italic; color: #666;'>—"
      f" {st.session_state.current_quote['author']}</p>",
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# Button to generate a new random quote
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  if st.button("🔄 New Quote", use_container_width=True):
    # Ensure we pick a different quote if possible
    available_quotes = [
        q
        for q in st.session_state.quotes
        if q != st.session_state.current_quote
    ]
    if not available_quotes:
      available_quotes = st.session_state.quotes
    st.session_state.current_quote = random.choice(
        available_quotes
    )
    st.rerun()

st.markdown("---")

# Sidebar for adding custom quotes
st.sidebar.header("🛠️ Customize")
with st.sidebar.expander("Add a New Quote"):
  new_text = st.text_area("Quote Text")
  new_author = st.text_input("Author Name")

  if st.button("Add to Collection"):
    if new_text and new_author:
      st.session_state.quotes.append(
          {"text": new_text, "author": new_author}
      )
      st.success("New quote added successfully!")
    else:
      st.warning("Please fill in both fields.")
