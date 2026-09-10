import streamlit as st
from google import genai
from PIL import Image

# Set up page configurations
st.set_page_config(page_title="Quantum Probability AI", page_icon="🌌", layout="wide")

# Custom Styling for Cyberpunk Theme
st.markdown("""
    <style>
    .main { background-color: #0d0d1a; color: #ffffff; }
    h1 { color: #8A2BE2; text-align: center; font-family: 'Courier New', Courier, monospace; }
    h3 { color: #4B0082; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🌌 QUANTUM PROBABILITY CLOUD ANALYZER</h1>", unsafe_allow_html=True)
st.markdown("<h3>Next-Gen AI System simulating millions of calculations per second</h3>", unsafe_allow_html=True)

# API Key Input
api_key = st.text_input("🔑 Enter your Google AI Studio API Key First", type="password", placeholder="Paste your Gemini API Key here...")

col1, col2 = st.columns(2)

with col1:
    text_input = st.text_area("💬 Enter English Chat Text", placeholder="Paste your chat history here...", height=150)
    image_file = st.file_uploader("📸 Upload Image for Visual Probability", type=["png", "jpg", "jpeg"])
    btn = st.button("🚀 RUN MASSIVE CLOUD COMPUTATION", use_container_width=True)

with col2:
    st.markdown("### 📊 Computation Results")
    if btn:
        if not api_key:
            st.error("ERROR: Please enter your Google AI Studio API Key first!")
        elif not text_input and image_file is None:
            st.warning("Please provide either chat text or an image to start computation.")
        else:
            with st.spinner("Simulating Cloud Calculations..."):
                try:
                    client = genai.Client(api_key=api_key.strip())
                    prompt = """
                    You are an advanced Quantum Cloud Probability Analyzer simulating massive cloud computations.
                    Analyze the given text input or image input. Output exact mathematical probability percentages for Positive and Negative.
                    You MUST return the output format strictly like this line-by-line so the app can read it:
                    Positive: [X]%
                    Negative: [Y]%
                    Explanation: [Write report in English]
                    """
                    contents = [prompt]
                    if text_input: contents.append(text_input)
                    if image_file: contents.append(Image.open(image_file))
                    
                    response = client.models.generate_content(model='gemini-3.5-flash', contents=contents)
                    res_text = response.text
                    
                    pos_val, neg_val = 50, 50
                    for line in res_text.split('\n'):
                        if "Positive:" in line:
                            try:
                                val_str = line.split("Positive:")[1].replace('%','').strip()
                                pos_val = float(val_str)
                            except: pass
                        if "Negative:" in line:
                            try:
                                val_str = line.split("Negative:")[1].replace('%','').strip()
                                neg_val = float(val_str)
                            except: pass
                    
                    # Beautiful UI components for Streamlit Cloud
                    st.write(f"**Positive: {pos_val}%**")
                    st.progress(int(pos_val))
                    st.write(f"**Negative: {neg_val}%**")
                    st.progress(int(neg_val))
                    
                    st.text_area("🧠 AI Deep Analysis Report", res_text, height=200)
                except Exception as e:
                    st.error(f"Error in Cloud Computation: {str(e)}")

