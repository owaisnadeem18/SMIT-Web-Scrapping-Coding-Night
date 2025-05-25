import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Real-Time Job Data Analyzer", layout="wide")

# Title
st.title("📊 Real-Time Job Data Analyzer")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('./rozee_selenium_jobs.csv', on_bad_lines='skip', encoding='utf-8')

df = load_data()

# Show Data
st.subheader("Dataset Preview")
st.dataframe(df.head(10))

# Total Jobs
st.metric("📌 Total Jobs Found", len(df))

# Jobs by Company
if 'Company' in df.columns:
    st.subheader("🏢 Jobs by Company")
    company_counts = df['Company'].value_counts().head(10)
    fig1, ax1 = plt.subplots()
    company_counts.plot(kind='barh', ax=ax1, color='skyblue')
    ax1.set_xlabel("Number of Jobs")
    st.pyplot(fig1)
else:
    st.warning("⚠️ 'Company' column not found in dataset.")

# Jobs by Title
if 'Title' in df.columns:
    st.subheader("💼 Top Job Titles")
    title_counts = df['Title'].value_counts().head(10)
    st.bar_chart(title_counts)
else:
    st.warning("⚠️ 'Title' column not found in dataset.")

# Location Wise Jobs
if 'Location' in df.columns:
    st.subheader("🌍 Jobs by Location")
    location_counts = df['Location'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    location_counts.plot(kind='bar', ax=ax2, color='orange')
    ax2.set_ylabel("Jobs Count")
    st.pyplot(fig2)
else:
    st.warning("⚠️ 'Location' column not found in dataset.")

# Remote Jobs Count
if 'Location' in df.columns:
    remote_jobs = df[df['Location'].str.contains('Remote', na=False)]
    st.metric("🧑‍💻 Remote Jobs", len(remote_jobs))

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by a passionate developer.")
