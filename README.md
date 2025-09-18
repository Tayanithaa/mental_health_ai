# Mental Health AI Journal

A Streamlit-powered journal app that uses AI to analyze the emotional content of your daily entries. Entries are stored in a local SQLite database and visualized with interactive charts.

## Features
- Write daily journal entries and save them securely.
- Automatic emotion analysis using a Hugging Face transformer model.
- View past entries and emotion scores.
- Interactive charts for emotion trends and weekly summaries.

## Folder Structure
```
mental_health_ai/
├── app.py                # Streamlit app UI and logic
├── backend/
│   ├── ai.py             # AI emotion analysis (Hugging Face pipeline)
│   └── database.py       # SQLite database helpers
├── journal.db            # SQLite database file
├── requirements.txt      # Python dependencies
├── test_model.py         # Quick test for model predictions
└── README.md             # Project documentation
```

## Quick Start
1. **Clone the repository:**
   ```powershell
   git clone <repo-url>
   cd mental_health_ai
   ```
2. **Set up Python environment:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```powershell
   .venv\Scripts\python.exe -m streamlit run app.py
   ```
   The app will open at http://localhost:8501

## Usage
- Write your journal entry in the text area and click "Save Entry".
- The app will analyze your text and display detected emotions.
- View past entries and emotion distribution charts.

## Testing
- To test the AI model directly, run:
   ```powershell
   .venv\Scripts\python.exe test_model.py
   ```

## Dependencies
- Python 3.10+
- streamlit
- transformers
- torch
- pandas
- plotly
- sqlite3 (built-in)

See `requirements.txt` for full list.

## Contributing
Pull requests and issues are welcome! Please follow standard Python code style and add tests for new features.


## Maintainer
Tayanithaa N S
