import streamlit as st
from datetime import datetime
from backend.database import init_db, save_entry, get_entries
from backend.ai import analyze_text
import pandas as pd
import plotly.express as px
import datetime as dt

def main():
    init_db()  # Ensure DB exists

    st.title("📝 AI Journal App")
    st.write("Log your thoughts and let AI analyze your emotions!")

    # Journal Entry
    text = st.text_area("Write your journal entry:")

    if st.button("Save Entry"):
        if text.strip():
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            emotion, scores = analyze_text(text)
            save_entry(date, text, emotion, scores)
            st.success(f"Saved! Detected emotion: **{emotion}**")
        else:
            st.warning("Please write something before saving.")

    # Past Entries
    st.subheader("📅 Past Entries")
    entries = get_entries()

    if entries:
        df = pd.DataFrame(entries, columns=[
            "id", "date", "text", "emotion",
            "joy", "sadness", "anger", "fear", "surprise", "disgust", "neutral"
        ])

        st.dataframe(df[["date", "emotion", "text"]])

        st.subheader("📊 Emotion Distribution per Entry")

        emotion_cols = ["joy", "sadness", "anger", "fear", "surprise", "disgust", "neutral"]

        chart_data = df.melt(
            id_vars=["date"],
            value_vars=emotion_cols,
            var_name="emotion",
            value_name="score"
        )

        fig = px.bar(
            chart_data,
            x="date",
            y="score",
            color="emotion",
            barmode="group",   # can switch to "stack" if you prefer stacked bars
            title="Emotions for Each Entry"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("No entries yet. Write your first journal entry above!")


    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

# Filter last 7 days
    one_week_ago = dt.datetime.now() - dt.timedelta(days=7)
    weekly_data = df[df["date"] >= one_week_ago]

    if not weekly_data.empty:
        # Average scores of the last 7 days
        weekly_avg = weekly_data[emotion_cols].mean().reset_index()
        weekly_avg.columns = ["emotion", "score"]

        # Create pie chart
        pie_fig = px.pie(
            weekly_avg,
            names="emotion",
            values="score",
            title="Weekly Emotion Distribution (Last 7 Days)"
        )
        st.plotly_chart(pie_fig, use_container_width=True)
    else:
        st.info("No entries in the last 7 days to show weekly emotion distribution.")

if __name__ == "__main__":
    main()
