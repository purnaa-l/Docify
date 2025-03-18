import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS
from io import BytesIO
from fpdf import FPDF

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page Configuration
st.set_page_config(page_title="DOCIFY: AI Code Documentor", layout="wide")
st.title("📜 DOCIFY: Your AI-Powered Code Documentor")

st.markdown("""
    **🚀 Upload your code and generate detailed documentation instantly!**
    - **AI-Powered Code Analysis**
    - **Generate PDF Documentation** 📄
    - **Listen to Your Docs** 🔊
""")

# Helper Function to Generate Documentation
def generate_documentation(code_input):
    prompt = f"""
    You are a professional technical writer. Generate detailed documentation for the following code.
    Include:
    - Overview of what the code does
    - Function descriptions
    - Code structure explanation
    - Usage examples (if applicable)
    
    Code:
    ```python
    {code_input}
    ```
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text

# PDF Generation Function
def create_pdf(documentation):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    
    # Remove emojis & unsupported characters
    doc_cleaned = documentation.encode("ascii", "ignore").decode()
    pdf.multi_cell(0, 10, doc_cleaned)
    
    # Get PDF as a string (binary) and store in BytesIO
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # Correct encoding
    pdf_stream = BytesIO(pdf_bytes)  # Convert string to BytesIO
    pdf_stream.seek(0)  # Move pointer to start
    
    return pdf_stream

# Text-to-Speech Function
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)  # ✅ Corrected method
    audio_bytes.seek(0)  # Move pointer to start
    return audio_bytes

# UI Components
code_input = st.text_area("📝 Paste your code here:", height=250)

if st.button("📄 Generate Documentation"):
    if code_input.strip():
        with st.spinner("Generating documentation..."):
            doc_text = generate_documentation(code_input)
            st.subheader("📑 Generated Documentation")
            st.write(doc_text)
            
            # PDF Download
            pdf_file = create_pdf(doc_text)
            st.download_button(label="📥 Download as PDF", data=pdf_file, file_name="documentation.pdf", mime="application/pdf")
            
            # Text-to-Speech (Audio)
            audio_file = text_to_speech(doc_text)
            
            # 🔊 Play Audio Button
            st.audio(audio_file, format='audio/mp3', start_time=0)

            # 📥 Download Audio Button - FIXED
            st.download_button(label="🔊 Download Audio", data=audio_file.getvalue(), file_name="documentation.mp3", mime="audio/mp3")

    else:
        st.warning("⚠️ Please enter code before generating documentation!")

# Custom Styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextArea textarea {
        font-size: 14px;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)
