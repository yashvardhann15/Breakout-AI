# AI Helper

A powerful tool for analyzing data from CSV files and Google Sheets, enhanced with AI-powered search and extraction capabilities using SerpAPI and Groq AI.

The project is live at: https://breakout-ai.streamlit.app/

This is the link to project's video: https://www.youtube.com/watch?v=wW1IsssTxoE

<!-- <video controls src="BreakoutAI.mp4" title="Assignment Video"></video> -->



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
git clone https://github.com/yashvardhann15/Breakout-AI.git
cd Breakout-AI
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
   - Provide a Google Sheets link (Remember to give viewer access to everyone with the link)

2. **Data Selection**
   - Preview your dataset
   - Select relevant column for analysis

3. **Search Configuration**
   - Enter a custom search prompt
   - Use `{}` as a placeholder for column values
   - Example: `Find contact details for {Company Name}`


4. **Process and Export**
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
  - Direct download and update functionality
  - Model searches all possible links to get the responses, combines all the results to give output.
  - Reponse is kept to be precise.

## Support

For support:
- Open an issue in the GitHub repository
- Include relevant error messages
- Provide steps to reproduce any issues


---

For more detailed documentation or to report issues, please visit the GitHub repository.
