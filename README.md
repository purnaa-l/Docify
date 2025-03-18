# Docify

(Generated From the Project)

DOCIFY: AI-Powered Code Documentor - Documentation

# Overview
DOCIFY is a Streamlit application that leverages Google's Gemini AI model to generate detailed documentation for Python code. Users paste their code into a text area, and DOCIFY produces a comprehensive documentation that includes an overview, function descriptions, code structure explanation, and usage examples. The generated documentation can be downloaded as a PDF file and listened to as an audio file. The application utilizes the google.generativeai, streamlit, fpdf, and gTTS libraries.

# Code Structure
The code is organized into several functions and utilizes Streamlit for the user interface.

Environment Setup: The code begins by loading environment variables (including the Google API key) using dotenv and configuring the Google Generative AI client.

Streamlit UI Configuration: st.set_page_config sets up the Streamlit page title and layout. The main title and a descriptive markdown section explain the application's functionality.

generate_documentation(code_input) Function: This function forms the core of the documentation generation process. It constructs a prompt instructing the Gemini AI model to generate documentation based on the provided code. The prompt explicitly requests an overview, function descriptions, code structure explanation, and usage examples. The response from the Gemini API is then returned as text.

create_pdf(documentation) Function: This function takes the generated documentation text and creates a PDF file using the fpdf library. It handles potential encoding issues by removing unsupported characters before adding the text to the PDF. The function returns the PDF as a BytesIO object for easy download. Crucially, it addresses encoding issues by using .encode('latin1') on the PDF output before converting it to a BytesIO object.

text_to_speech(text) Function: This function converts the documentation text into an audio file using the gTTS library. It returns the audio as a BytesIO object. The method for writing to audio_bytes is corrected to use tts.write_to_fp().

User Interface (UI) Components: Streamlit components (st.text_area, st.button, st.spinner, st.subheader, st.write, st.download_button, st.audio) are used to create the interactive user interface. The st.text_area allows users to paste their code. The st.button triggers the documentation generation process. Progress is indicated with st.spinner. The generated documentation is displayed using st.write. Download buttons are provided for both PDF and audio outputs. Error handling ensures a warning message is displayed if no code is entered.

Custom Styling: Custom CSS styling is applied to enhance the visual appearance of the buttons and text area using st.markdown with the unsafe_allow_html=True parameter.

# Function Descriptions
generate_documentation(code_input): Takes Python code as input, constructs a prompt for the Gemini AI model, sends the request, and returns the generated documentation as a string.

create_pdf(documentation): Takes documentation text as input, creates a PDF document containing this text, and returns the PDF as a BytesIO object. Handles encoding issues to ensure compatibility.

text_to_speech(text): Takes text as input, generates an audio file using gTTS, and returns the audio as a BytesIO object.

# Usage Examples
Run the application: Ensure you have the required libraries installed (streamlit, google-generativeai, python-dotenv, gTTS, fpdf). Set your Google API key as the environment variable GOOGLE_API_KEY. Run the script using streamlit run your_script_name.py.

Paste code: Paste your Python code into the text area provided by the application.

Generate documentation: Click the "Generate Documentation" button. The application will communicate with the Gemini AI model and display the generated documentation.

Download PDF: Click the "Download as PDF" button to download the documentation as a PDF file.

Listen to/Download Audio: Listen to the documentation audio using the built-in player and/or download it as an MP3 file.

# Error Handling
- The application includes basic error handling. If the user tries to generate documentation without entering any code, a warning message is displayed. The create_pdf function incorporates error handling for encoding issues.

# Dependencies
streamlit
google-generativeai
python-dotenv
gTTS
fpdf

Remember to install these packages using pip install streamlit google-generativeai python-dotenv gTTS fpdf. You will also need a Google Cloud project with the Gemini API enabled and an API key.
