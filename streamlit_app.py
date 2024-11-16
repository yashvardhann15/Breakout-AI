import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
from groq import Groq
import re

load_dotenv()
serpApi = os.getenv("serpApi")
GroqAPi = os.getenv("groqApi")

client = Groq(api_key=GroqAPi)

chat_history = [
    {
        "role": "system",
        "content": "You are an assistant specialized in extracting specific information from web pages based on a query. Provide only the requested information. If no relevant data is available, respond with 'Result not found' only and only."
    }
]

if 'mapping' not in st.session_state:
    st.session_state.mapping = {}

def searchGoogle(prompt):
    match = re.search(r'\{(.+?)\}', prompt)
    if not match:
        return "No value found in curly braces in the prompt."

    selected_value = match.group(1)
    search_query = prompt.replace(f"For {{{selected_value}}}", str(df[selected_attribute].iloc[0]))

    params = {
        "engine": "google",
        "q": search_query,
        "api_key": serpApi
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" not in results or not results["organic_results"]:
        return "No search results found."

    formatted_results = []
    for result in results.get("organic_results", []):
        title = result.get("title", "No Title")
        link = result.get("link", "No Link")
        snippet = result.get("snippet", "No Snippet")
        formatted_results.append({
            "title": title.strip(),
            "link": link.strip(),
            "snippet": snippet.strip()
        })

    return formatted_results

def getResult(results, backPrompt, chat_history):
    MAX_HISTORY_LENGTH = 5
    chat_history = chat_history[-MAX_HISTORY_LENGTH:]
    all_responses = []
    organic_results = results

    for batch in organic_results:
        chat_history.append({
            "role": "user",
            "content": f"""
            I have a search result. Please extract the requested details:

            Search Result:
            Title: {batch['title']}
            Link: {batch['link']}
            Snippet: {batch['snippet']}

            Extraction Task:
            {backPrompt}

            Provide only the requested information.
            """
        })

        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=chat_history
        )

        ai_response = completion.choices[0].message.content
        chat_history.append({
            "role": "assistant",
            "content": ai_response
        })

        if "result not found" not in ai_response.lower():
            all_responses.append(ai_response)

    if not all_responses:
        return "Result not found."

    return combineResponses(all_responses)

def combineResponses(responses):
    unique_responses = set(responses)
    combined_response = "\n".join(unique_responses)
    result = f"**Extracted Information:**\n{combined_response}"
    return result.strip()

st.title("AI Helper")

st.header("Data Input")
input_method = st.radio("Choose input method:", ["Upload CSV", "Google Sheets Link"])

df = None
if input_method == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
else:
    sheet_url = st.text_input("Enter Google Sheets link:")
    if sheet_url:
        try:
            sheet_id = re.search('/spreadsheets/d/([a-zA-Z0-9-_]+)', sheet_url).group(1)
            csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
            df = pd.read_csv(csv_url)
        except (AttributeError, IndexError):
            st.error("Error: Invalid Google Sheets URL format.")

if df is not None:
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    st.subheader("Column Selection")
    selected_attribute = st.selectbox("Select a column:", df.columns)
    
    if selected_attribute:
        prompt = st.text_input("Enter a prompt (enclose column value in curly brackets{}):")
        
        if prompt:
            backPrompt = st.text_input("Enter the details you want to fetch about the selected attribute:")
            
            if st.button("Fetch Information"):
                search_results = searchGoogle(prompt)
                aiResponse = getResult(search_results, backPrompt, chat_history)
                st.session_state.mapping[backPrompt] = aiResponse
                
                st.subheader("Extracted Information")
                st.write(aiResponse)
    
    if st.session_state.mapping:
        if st.button("Save Results"):
            # Prepare data for saving
            data = {"User Query": [], "AI Response": []}
            for query, response in st.session_state.mapping.items():
                data["User Query"].append(query)
                data["AI Response"].append(response)
            
            results_df = pd.DataFrame(data)
            
            results_df.to_csv("results.csv", index=False)
            st.success("Results saved to results.csv")
            
            st.download_button(
                label="Download Results",
                data=results_df.to_csv(index=False).encode('utf-8'),
                file_name='results.csv',
                mime='text/csv'
            )