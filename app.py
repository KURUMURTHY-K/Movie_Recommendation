import streamlit as st
import pandas as pd

# Sample dataset
movies = pd.DataFrame({
    'Movie Name': ['Inception', 'Interstellar', 'The Dark Knight', 'Tenet', 'Gravity', 'Arrival', 'The Martian'],
    'Genre': ['Sci-Fi', 'Sci-Fi', 'Action', 'Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Sci-Fi'],
    'Duration': [148, 169, 152, 150, 91, 116, 144]
})

# Streamlit UI
st.title("🎬 Movie Recommendation System")

# User input
input_name = st.text_input("Enter a Movie Name")
input_genre = st.selectbox("Select Genre", movies['Genre'].unique())
input_duration = st.slider("Select Duration (in minutes)", 60, 200, 120)

if st.button("Get Recommendations"):
    # Filter by genre
    genre_filtered = movies[movies['Genre'] == input_genre]

    # Filter by duration range (+/-10 mins)
    duration_filtered = genre_filtered[
        (genre_filtered['Duration'] >= input_duration - 10) &
        (genre_filtered['Duration'] <= input_duration + 10)
    ]

    # Exclude the movie with exact same name (if found)
    final_recommendations = duration_filtered[duration_filtered['Movie Name'] != input_name]

    if not final_recommendations.empty:
        st.subheader("📽️ Recommended Movies:")
        st.table(final_recommendations)
    else:
        st.warning("No similar movies found. Try changing the filters.")
