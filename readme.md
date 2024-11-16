# Data Analysis Application

A web application that analyzes data from CSV files or Google Sheets and extracts specific information using Google Search and Groq AI. Features both command-line and Streamlit interfaces.

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install pandas python-dotenv serpapi-python groq streamlit
```

3. Create `.env` file with your API keys:
```env
serpApi=your_serp_api_key_here
groqApi=your_groq_api_key_here
```

## Running the Application

### Streamlit Interface:
```bash
streamlit run app.py
```

### Command Line:
```bash
python script.py
```

## Features

- CSV file upload
- Google Sheets integration
- Custom search prompts
- AI-powered information extraction
- Results export to CSV
- User-friendly interface

## Usage

1. Choose input method (CSV/Google Sheets)
2. Select a column from your dataset
3. Enter prompt using {} for column values
4. Enter your query
5. View and download results

## Requirements

- Python 3.7+
- SerpAPI key
- Groq API key

## Support

For support, please raise an issue in the repository.
