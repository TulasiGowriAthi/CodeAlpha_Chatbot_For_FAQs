# 🤖 Conversational NLP FAQ Chatbot

An intelligent, context-aware conversational AI assistant designed to handle technical troubleshooting, system optimizations, and content creation guidance. Instead of using rigid, outdated `if/else` matching strings, this agent utilizes **Natural Language Processing (NLP)** models to vectorize user sentences and mathematically predict user intent in real-time.

Developed as part of the **CodeAlpha Artificial Intelligence Internship**.

---

## 🧠 Architectural & NLP Workflow
To deliver human-like, flexible responses, the chatbot utilizes a mature data processing pipeline:
1. **Tokenization & Stop-Word Filtering:** Text queries are broken down into tokens, and meaningless functional filler words (e.g., 'and', 'the', 'is') are stripped using an English corpora dictionary.
2. **TF-IDF Vectorization:** Words are transformed into numerical feature matrices using `TfidfVectorizer`, weighting vocabulary based on domain-specific importance rather than raw frequency.
3. **Cosine Similarity Metric:** User inputs are mapped against the master FAQ database as geometric vectors. The assistant calculates the cosine angle between vectors to identify the single best matching answer.
4. **Fallback Thresholding:** Includes a strict mathematical constraint threshold (0.25). If a user question does not align sufficiently with any known technical topic, the chatbot handles the query gracefully without breaking context.

---

## 🎯 Key Features
- **Modern Messaging UI:** Built with Streamlit’s native `st.chat_message` framework, closely mirroring premium conversational platforms like ChatGPT.
- **Session State Preservation:** Implements dynamic cache tracking (`st.session_state`) to retain scrolling conversation history smoothly across application redraws.
- **Niche Domain Specialization:** Fully equipped to answer queries on Windows God Mode, local drive space management, performance boosting, and faceless AI video creation workflows.

---

## 🖥️ Application Preview
[FAQ_Chatbot](Chatbot_Interface.png)

## 🚀 Tech Stack & Core Libraries
- **UI Architecture:** Streamlit
- **Machine Learning / NLP:** Scikit-Learn (`TfidfVectorizer`, `cosine_similarity`)
- **Language Core:** Python 3.9+

---

📊 Core Analytical Methodology

The backend engine processes textual context mathematically to identify structural alignment:Term Frequency-Inverse Document Frequency (TF-IDF): Reflects how important a word is to a document in a collection. It scores common words lower and rare topical terms higher.Cosine Similarity: Measures the cosine of the angle between two multi-dimensional vectors projected in a multi-variable vector space. It calculates alignment directional patterns regardless of exact phrase length:
$$\text{Similarity}(A, B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

## 🛠️ Installation & Local Setup
1. . **Download the Project:**
   Download the zip file of this repository and extract it, or open this project folder directly in VS Code.


2. **Install Dependencies:**
   pip install -r requirements.txt

3. **Launch the Chatbot:**

   streamlit run app.py

## 📂 Project Structure
 
 CodeAlpha_FAQ_Chatbot/
├── app.py              # Core NLP processing pipelines and Chat room UI
├── requirements.txt    # Project package dependencies
└── README.md           # Professional project documentation

## 🎬 Project Demonstration
Watch the real-time intent-matching process and video breakdown of this chatbot on LinkedIn:

👉 Click Here to Watch the Project Video on LinkedIn

Developed with 💙 by Tulasi Gowri during the CodeAlpha AI Internship.
