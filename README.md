# 💼 Gemini Interview Chatbot

An AI-powered technical interview simulator built with Streamlit and Google Gemini API. Candidates submit their code, get dynamically generated interview questions, receive follow-up questions based on their answers, and get a detailed performance report with scores and skill analysis.

---

## 🚀 Features

- 📋 Candidate Info Collection — Name, qualification, and self-introduction
- 🎲 Random Coding Topics — Assigned per language (Python, JavaScript, Java, C++)
- 💻 Code Submission — Upload a file or paste code directly
- 🤖 AI Question Generation — Gemini generates 5 technical questions based on submitted code
- 🔁 Follow-up Questions — AI asks deeper follow-up questions based on each answer
- 📊 Score & Feedback — Each answer is scored (0–5) with constructive feedback
- 📈 Skill Analysis — Identifies strengths and weaknesses across 6 skill categories
- 💾 Save Results — Exports interview results as a JSON file

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Google Gemini API (gemma-3-1b-it) | AI question generation & evaluation |
| JSON | Result storage |

---

## 📁 Project Structure

InterviewBot/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── run_streamlit.bat         # Windows run script
└── candidate_gemma.json      # Sample interview result output

---

## ⚙️ Setup & Installation

1. Clone the Repository
   git clone https://github.com/yourusername/InterviewBot.git
   cd InterviewBot

2. Install Dependencies
   pip install -r requirements.txt

3. Set Your Gemini API Key
   Get your free API key from Google AI Studio and set it as an environment variable:

   # Windows
   set GEMINI_API_KEY=your_api_key_here

   # Mac/Linux
   export GEMINI_API_KEY=your_api_key_here

4. Run the App
   streamlit run app.py

   Or on Windows, double-click run_streamlit.bat

---

## 🖥️ How It Works

1. Enter Name & Qualification
        ↓
2. Select Language → Get Random Coding Topic
        ↓
3. Submit Code (upload file or paste)
        ↓
4. AI Generates 5 Technical Questions
        ↓
5. Answer Each Question
        ↓
6. AI Asks Follow-up Questions
        ↓
7. Get Score, Feedback & Skill Analysis
        ↓
8. Save Results as JSON

---

## 📊 Skill Categories Evaluated

- ✅ Algorithmic Thinking
- ✅ Code Efficiency
- ✅ Syntax Accuracy
- ✅ Problem Understanding
- ✅ Communication
- ✅ Edge Case Handling

---

## 📦 Requirements

streamlit>=1.28.0
google-generativeai>=0.3.0

---

## 📄 Sample Output

After completing an interview, results are saved as a JSON file:

{
  "name": "John Doe",
  "qualification": "B.Tech",
  "final_score": 7.5,
  "strengths": ["Algorithmic Thinking", "Syntax Accuracy"],
  "weaknesses": ["Edge Case Handling"]
}

---

## 🙋 Author

Your Name
LinkedIn: # 💼 Gemini Interview Chatbot

An AI-powered technical interview simulator built with Streamlit and Google Gemini API. Candidates submit their code, get dynamically generated interview questions, receive follow-up questions based on their answers, and get a detailed performance report with scores and skill analysis.

---

## 🚀 Features

- 📋 Candidate Info Collection — Name, qualification, and self-introduction
- 🎲 Random Coding Topics — Assigned per language (Python, JavaScript, Java, C++)
- 💻 Code Submission — Upload a file or paste code directly
- 🤖 AI Question Generation — Gemini generates 5 technical questions based on submitted code
- 🔁 Follow-up Questions — AI asks deeper follow-up questions based on each answer
- 📊 Score & Feedback — Each answer is scored (0–5) with constructive feedback
- 📈 Skill Analysis — Identifies strengths and weaknesses across 6 skill categories
- 💾 Save Results — Exports interview results as a JSON file

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Google Gemini API (gemma-3-1b-it) | AI question generation & evaluation |
| JSON | Result storage |

---

## 📁 Project Structure

InterviewBot/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── run_streamlit.bat         # Windows run script
└── candidate_gemma.json      # Sample interview result output

---

## ⚙️ Setup & Installation

1. Clone the Repository
   git clone https://github.com/yourusername/InterviewBot.git
   cd InterviewBot

2. Install Dependencies
   pip install -r requirements.txt

3. Set Your Gemini API Key
   Get your free API key from Google AI Studio and set it as an environment variable:

   # Windows
   set GEMINI_API_KEY=your_api_key_here

   # Mac/Linux
   export GEMINI_API_KEY=your_api_key_here

4. Run the App
   streamlit run app.py

   Or on Windows, double-click run_streamlit.bat

---

## 🖥️ How It Works

1. Enter Name & Qualification
        ↓
2. Select Language → Get Random Coding Topic
        ↓
3. Submit Code (upload file or paste)
        ↓
4. AI Generates 5 Technical Questions
        ↓
5. Answer Each Question
        ↓
6. AI Asks Follow-up Questions
        ↓
7. Get Score, Feedback & Skill Analysis
        ↓
8. Save Results as JSON

---

## 📊 Skill Categories Evaluated

- ✅ Algorithmic Thinking
- ✅ Code Efficiency
- ✅ Syntax Accuracy
- ✅ Problem Understanding
- ✅ Communication
- ✅ Edge Case Handling

---

## 📦 Requirements

streamlit>=1.28.0
google-generativeai>=0.3.0

---

## 📄 Sample Output

After completing an interview, results are saved as a JSON file:

{
  "name": "John Doe",
  "qualification": "B.Tech",
  "final_score": 7.5,
  "strengths": ["Algorithmic Thinking", "Syntax Accuracy"],
  "weaknesses": ["Edge Case Handling"]
}

---

## 🙋 Author

Your Name
LinkedIn:# 💼 Gemini Interview Chatbot

An AI-powered technical interview simulator built with Streamlit and Google Gemini API. Candidates submit their code, get dynamically generated interview questions, receive follow-up questions based on their answers, and get a detailed performance report with scores and skill analysis.

---

## 🚀 Features

- 📋 Candidate Info Collection — Name, qualification, and self-introduction
- 🎲 Random Coding Topics — Assigned per language (Python, JavaScript, Java, C++)
- 💻 Code Submission — Upload a file or paste code directly
- 🤖 AI Question Generation — Gemini generates 5 technical questions based on submitted code
- 🔁 Follow-up Questions — AI asks deeper follow-up questions based on each answer
- 📊 Score & Feedback — Each answer is scored (0–5) with constructive feedback
- 📈 Skill Analysis — Identifies strengths and weaknesses across 6 skill categories
- 💾 Save Results — Exports interview results as a JSON file

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Google Gemini API (gemma-3-1b-it) | AI question generation & evaluation |
| JSON | Result storage |

---

## 📁 Project Structure

InterviewBot/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── run_streamlit.bat         # Windows run script
└── candidate_gemma.json      # Sample interview result output

---

## ⚙️ Setup & Installation

1. Clone the Repository
   git clone https://github.com/yourusername/InterviewBot.git
   cd InterviewBot

2. Install Dependencies
   pip install -r requirements.txt

3. Set Your Gemini API Key
   Get your free API key from Google AI Studio and set it as an environment variable:

   # Windows
   set GEMINI_API_KEY=your_api_key_here

   # Mac/Linux
   export GEMINI_API_KEY=your_api_key_here

4. Run the App
   streamlit run app.py

   Or on Windows, double-click run_streamlit.bat

---

## 🖥️ How It Works

1. Enter Name & Qualification
        ↓
2. Select Language → Get Random Coding Topic
        ↓
3. Submit Code (upload file or paste)
        ↓
4. AI Generates 5 Technical Questions
        ↓
5. Answer Each Question
        ↓
6. AI Asks Follow-up Questions
        ↓
7. Get Score, Feedback & Skill Analysis
        ↓
8. Save Results as JSON

---

## 📊 Skill Categories Evaluated

- ✅ Algorithmic Thinking
- ✅ Code Efficiency
- ✅ Syntax Accuracy
- ✅ Problem Understanding
- ✅ Communication
- ✅ Edge Case Handling

---

## 📦 Requirements

streamlit>=1.28.0
google-generativeai>=0.3.0

---

## 📄 Sample Output

After completing an interview, results are saved as a JSON file:

{
  "name": "Prem Ramole",
  "qualification": "B.Tech",
  "final_score": 7.5,
  "strengths": ["Algorithmic Thinking", "Syntax Accuracy"],
  "weaknesses": ["Edge Case Handling"]
}

---

## 🙋 Author

Your Name  Prem Ramole
LinkedIn:https://in.linkedin.com/in/prem-ramole-779088298?utm_source=share&utm_medium=member_mweb&utm_campaign=share_via&utm_content=profile
GitHub:(https://github.com/premramole)

---

## 📜 License

This project is open source and available under the MIT License.
GitHub: https://github.com/yourusername

---

## 📜 License

This project is open source and available under the MIT License.
GitHub: https://github.com/yourusername

---

## 📜 License

This project is open source and available under the MIT License.
