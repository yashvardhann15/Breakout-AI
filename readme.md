# Data Analysis Application

A powerful tool for analyzing data from CSV files and Google Sheets, enhanced with AI-powered search and extraction capabilities using SerpAPI and Groq AI.

## Features

- **Data Input Options**
  - CSV file upload
  - Google Sheets integration
- **Search Integration**
  - Google search functionality based on data fields
  - Custom prompt support
- **AI-Powered Extraction**
  - Groq AI integration for intelligent data extraction
  - Customizable extraction parameters
- **User Interface**
  - Data preview functionality
  - Column selection tools
  - Export capabilities with CSV download

## Setup

1. Clone the repository
```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

2. Install dependencies
```bash
pip install pandas python-dotenv serpapi groq streamlit
```

3. Configure environment variables
Create a `.env` file in the project root:
```env
serpApi=your_serp_api_key_here
groqApi=your_groq_api_key_here
```

## Usage

### Starting the Application

Launch the Streamlit interface:
```bash
streamlit run app.py
```

### Dashboard Instructions

1. **Input Data**
   - Upload a CSV file, or
   - Provide a Google Sheets link (format: `https://docs.google.com/spreadsheets/d/<sheet_id>`)

2. **Data Selection**
   - Preview your dataset
   - Select relevant columns for analysis

3. **Search Configuration**
   - Enter a custom search prompt
   - Use `{}` as a placeholder for column values
   - Example: `Find contact details for {Company Name}`

4. **Extraction Settings**
   - Specify target information (emails, phone numbers, etc.)
   - Configure extraction parameters

5. **Process and Export**
   - Click "Fetch Information" to run analysis
   - Save results to CSV
   - Download processed data

### Google Sheets Integration

To use Google Sheets:
1. Open your sheet in Google Sheets
2. Copy the sheet URL
3. Paste into the application
4. The app will automatically process the data

## Requirements

- Python 3.7+
- Valid SerpAPI key
- Valid Groq API key

## Environment Variables

Required API keys:
```env
serpApi=your_serp_api_key_here
groqApi=your_groq_api_key_here
```

## Optional Features

- **Export Options**
  - CSV file export
  - Direct download functionality
  - Custom file naming

## Support

For support:
- Open an issue in the GitHub repository
- Include relevant error messages
- Provide steps to reproduce any issues

---

For more detailed documentation or to report issues, please visit the GitHub repository.
