import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load AI Artist Discovery Data
df_sorted = pd.DataFrame({
    "Artist Name": ["Artist A", "Artist B", "Artist C", "Artist D", "Artist E"],
    "Spotify Monthly Listeners": [95940, 64402, 95203, 79487, 67148],
    "TikTok Engagement Rate (%)": [20.0, 17.0, 23.0, 17.0, 18.0],
    "YouTube Views (Last 30 Days)": [100000, 250000, 75000, 180000, 140000],
    "Song Completion Rate (%)": [80, 85, 75, 78, 82],
    "Playlist Adds (Spotify)": [3940, 7402, 3203, 7487, 5148],
    "Instagram Engagement Rate (%)": [10.2, 18.5, 9.7, 15.3, 12.9],
    "SoundCloud Streams": [120000, 300000, 90000, 200000, 150000],
    "AI Artist Score": [100, 100, 100, 100, 100],
})

# Streamlit Dashboard
def main():
    st.title("AI Artist Discovery Dashboard")
    st.subheader("Real-Time AI-Powered A&R System")
    
    # Display DataFrame
    st.dataframe(df_sorted)
    
    # Plot AI Artist Score Rankings
    st.subheader("Top AI-Discovered Artists")
    plt.figure(figsize=(10, 6))
    plt.bar(df_sorted["Artist Name"], df_sorted["AI Artist Score"], color='blue')
    plt.xlabel("Artist Name")
    plt.ylabel("AI Artist Score (0-100)")
    plt.title("AI Artist Ranking by Commercial Potential")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(plt)

if __name__ == "__main__":
    main()
