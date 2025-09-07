import streamlit as st
from backend.database import init_db, save_entry, get_entries

def main():
    init_db()   # Make sure DB exists

    st.title("AI Journal App")
    st.write("Welcome! Add your daily entry below:")

    text = st.text_area("Your journal entry")
    if st.button("Save"):
        save_entry("2025-09-06", text, "neutral", 0.0)  # placeholder
        st.success("Saved!")

    st.subheader("Past Entries")
    entries = get_entries()
    for e in entries:
        st.write(f"📅 {e[1]} | Sentiment: {e[3]} | Score: {e[4]}")
        st.write(e[2])
        st.markdown("---")

if __name__ == "__main__":
    main()
