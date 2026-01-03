import streamlit as st
import json
import random
import os
import re
import google.generativeai as genai
from collections import Counter

# --- Configure Gemini API ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDPBAnNlNU3KmvRVAS6aRTfdbRvlxRcLWE")
genai.configure(api_key=GEMINI_API_KEY)

# --- Custom CSS for enhanced UI ---
st.markdown('''
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="stApp"] {
        background: linear-gradient(135deg, #e0e7ff 0%, #f0fdfa 100%);
        font-family: 'Inter', sans-serif !important;
    }
    .big-font {
        font-size: 2.5rem !important;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.7em;
        letter-spacing: -1px;
        text-shadow: 0 2px 8px rgba(44,62,80,0.08);
        display: flex;
        align-items: center;
        gap: 0.5em;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(90deg, #6366f1, #38bdf8);
        border-radius: 12px;
        height: 18px;
        box-shadow: 0 2px 8px rgba(56,189,248,0.12);
    }
    .stProgress > div > div {
        border-radius: 12px;
        background: #e0e7ff;
        height: 18px;
    }
    .card {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        box-shadow: 0 4px 32px rgba(44,62,80,0.10);
        padding: 2.5rem 2rem 2rem 2rem;
        margin-bottom: 2.5rem;
        border: 1.5px solid #e0e7ff;
        transition: box-shadow 0.2s, transform 0.2s;
        animation: fadeInCard 0.7s cubic-bezier(.4,0,.2,1);
    }
    .card:hover {
        box-shadow: 0 8px 40px rgba(56,189,248,0.18);
        transform: translateY(-2px) scale(1.01);
    }
    @keyframes fadeInCard {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: none; }
    }
    .question {
        font-size: 1.25rem;
        font-weight: 600;
        color: #2563eb;
        margin-bottom: 0.7em;
        display: flex;
        align-items: center;
        gap: 0.4em;
    }
    .stTextArea textarea {
        background: #f1f5f9;
        border-radius: 10px;
        font-size: 1.08rem;
        border: 1.5px solid #e0e7ff;
        transition: border 0.2s;
    }
    .stTextArea textarea:focus {
        border: 1.5px solid #38bdf8;
        outline: none;
    }
    .stButton > button {
        background: linear-gradient(90deg, #6366f1, #38bdf8);
        color: white;
        border-radius: 10px;
        font-weight: 600;
        border: none;
        padding: 0.6em 1.7em;
        margin: 0.2em 0.2em 0.2em 0;
        transition: background 0.2s, transform 0.15s;
        box-shadow: 0 2px 8px rgba(56,189,248,0.10);
        font-size: 1.08rem;
    }
    .stButton > button:disabled {
        background: #cbd5e1 !important;
        color: #64748b !important;
        box-shadow: none;
    }
    .stButton > button:hover:enabled {
        background: linear-gradient(90deg, #38bdf8, #6366f1);
        color: #fff;
        transform: translateY(-2px) scale(1.03);
        box-shadow: 0 4px 16px rgba(56,189,248,0.18);
    }
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 1.5px solid #e0e7ff;
        background: #f1f5f9;
    }
    .stFileUploader > div {
        border-radius: 10px;
        background: #f1f5f9;
        border: 1.5px solid #e0e7ff;
    }
    .stInfo {
        border-radius: 10px;
        background: #e0f2fe;
        color: #2563eb;
        border: 1.5px solid #bae6fd;
        font-size: 1.08rem;
    }
    .stSuccess {
        border-radius: 10px;
        background: #d1fae5;
        color: #047857;
        border: 1.5px solid #6ee7b7;
        font-size: 1.08rem;
    }
    .stMarkdown hr {
        border: 0;
        border-top: 1.5px solid #e0e7ff;
        margin: 1.5em 0;
    }
    .stTextInput > div > input {
        border-radius: 10px;
        border: 1.5px solid #e0e7ff;
        background: #f1f5f9;
        font-size: 1.08rem;
        transition: border 0.2s;
    }
    .stTextInput > div > input:focus {
        border: 1.5px solid #38bdf8;
        outline: none;
    }
    .stSelectbox label, .stTextInput label, .stTextArea label, .stFileUploader label {
        font-weight: 600;
        color: #1e293b;
        font-size: 1.08rem;
    }
    </style>
''', unsafe_allow_html=True)
# --- Gemini API Wrapper ---
def ask_gemini(prompt: str, model_name: str = "gemma-3-1b-it", max_output_tokens: int = 1024, temperature: float = 0.7) -> str:
    try:
        model = genai.GenerativeModel(model_name)
        generation_config = {
            "max_output_tokens": max_output_tokens,
            "temperature": temperature
        }
        response = model.generate_content(prompt, generation_config=generation_config)
        return response.text
    except Exception as e:
        return f"Error from Gemini: {e}"
# --- Language & Topic Selection Stage ---
if st.session_state.get("stage") == "language_topic":
    languages = ["Python", "JavaScript", "Java", "C++"]
    language = st.selectbox("Select the programming language:", languages, key="language_select")
    language_topics = {
        "Python": ["Reverse a string", "Find factorial of a number", "Check for palindrome", "Fibonacci sequence", "Sort a list", "Find prime numbers", "File I/O operations", "Class and object example"],
        "JavaScript": ["Reverse an array", "Debounce a function", "Find max in array", "FizzBuzz", "DOM manipulation", "Promise example", "Event handling"],
        "Java": ["Binary search", "Reverse a linked list", "Inheritance example", "File reading/writing", "Exception handling", "Multithreading"],
        "C++": ["Bubble sort", "Stack using class", "Pointer arithmetic", "File streams", "Operator overloading", "Template function"]
    }
    if 'last_language' not in st.session_state or st.session_state['last_language'] != language:
        st.session_state['last_language'] = language
        st.session_state['random_topic'] = random.choice(language_topics[language])
    topic = st.session_state['random_topic']
    st.info(f"Write code for the following topic in {language}: **{topic}**")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Back", key="back_to_info", use_container_width=True):
            st.session_state["stage"] = "candidate_info"
            st.rerun()
    with col2:
        if st.button("Next", key="to_code", use_container_width=True):
            st.session_state["stage"] = "code_submission"
            st.rerun()

# --- Gemini Question Generation ---
def get_gemma_questions(code_text: str, num_questions: int = 5) -> list:
    prompt = (
        f"Analyze the following code and generate {num_questions} technical, interview-style questions about it. "
        "Be specific and do not ask generic questions.\n\n"
        f"Code:\n{code_text}\n"
    )
    response = ask_gemini(prompt)
    questions = []
    for line in response.splitlines():
        line = line.strip()
        if not line:
            continue
        if line[0].isdigit() and (line[1:2] == "." or line[1:2] == ")"):
            line = line[2:].strip()
        elif line.startswith("-"):
            line = line[1:].strip()
        if "?" in line:
            questions.append(line)
    if len(questions) < 2:
        questions = [q.strip() + "?" for q in response.split("?") if q.strip()]
    return questions[:num_questions]

# --- Gemini Follow-up Question Generation ---
def get_followup_question(q: str, a: str) -> str:
    prompt = (
        "Based on the interview question and the candidate’s answer below, generate 1 targeted follow-up question.\n"
        "If the answer is incomplete or vague, ask for clarification or deeper reasoning.\n"
        "If the answer is strong, push for deeper insight, optimizations, or edge cases.\n"
        "Return only the follow-up question without explanation or formatting.\n\n"
        f"Question: {q}\nAnswer: {a}"
    )
    return ask_gemini(prompt).strip()

# --- Gemini Review Feedback Generation ---
def get_review_feedback(q: str, a: str) -> dict:
    prompt = (
        "Evaluate the candidate’s answer to the technical question below using this rubric:\n"
        "5 = Excellent (complete, precise, insightful)\n"
        "4 = Good (mostly correct, some depth)\n"
        "3 = Fair (partially correct, some gaps)\n"
        "2 = Poor (mostly incorrect or shallow)\n"
        "1 = Very poor (barely relevant)\n"
        "0 = Incorrect (wrong or irrelevant)\n\n"
        "Respond with ONLY a single valid JSON object, no extra text, no markdown, no explanation:\n"
        '{"feedback": <short constructive feedback>, "score": <0–5>}\n\n'
        f"Question: {q}\nAnswer: {a}"
    )
    try:
        response = ask_gemini(prompt)
        json_match = re.search(r'{.*}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
    except Exception:
        pass
    return {"feedback": "Could not parse feedback", "score": 0}

# --- Gemini Strengths & Weaknesses Analysis ---
def get_strengths_weaknesses(q: str, a: str) -> dict:
    prompt = (
        "Analyze the following technical interview question and the candidate's answer.\n"
        "Classify the answer across these skill categories: "
        "Algorithmic Thinking, Code Efficiency, Syntax Accuracy, "
        "Problem Understanding, Communication, and Edge Case Handling.\n\n"
        "Return a JSON object with two fields:\n"
        "- 'strengths': a list of categories the candidate performed well in\n"
        "- 'weaknesses': a list of categories the candidate needs to improve\n\n"
        "Respond only in this format:\n"
        "{\n  \"strengths\": [...],\n  \"weaknesses\": [...]\n}\n\n"
        f"Question: {q}\nAnswer: {a}"
    )
    try:
        response = ask_gemini(prompt)
        json_match = re.search(r'{.*}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
    except Exception:
        pass
    return {"strengths": [], "weaknesses": []}

# --- Utility: JSON Extract ---
def extract_json(text):
    match = re.search(r'{.*}', text, re.DOTALL)
    if match:
        return match.group(0)
    return None

# --- Streamlit App Logic (Candidate Info, Code Input, Q&A Flow) ---

st.title("💼 Gemini Interview Chatbot")

# Session states
if "stage" not in st.session_state:
    st.session_state.stage = "info"

if st.session_state.stage == "info":
    st.subheader("Candidate Information")
    st.session_state.name = st.text_input("Your Name:")
    st.session_state.qual = st.selectbox("Your Qualification:", ["B.Tech", "M.Tech", "BCA", "MCA", "Diploma"])
    st.session_state.intro = st.text_area("Introduce Yourself:")
    if st.button("Next ➡️") and st.session_state.name.strip() and st.session_state.intro.strip():
        st.session_state.stage = "topic"

elif st.session_state.stage == "topic":
    st.subheader("Random Coding Topic")
    languages = ["Python", "JavaScript", "Java", "C++"]
    language = st.selectbox("Select the programming language:", languages, key="language_select")
    language_topics = {
        "Python": ["Reverse a string", "Find factorial of a number", "Check for palindrome", "Fibonacci sequence", "Sort a list", "Find prime numbers", "File I/O operations", "Class and object example"],
        "JavaScript": ["Reverse an array", "Debounce a function", "Find max in array", "FizzBuzz", "DOM manipulation", "Promise example", "Event handling"],
        "Java": ["Binary search", "Reverse a linked list", "Inheritance example", "File reading/writing", "Exception handling", "Multithreading"],
        "C++": ["Bubble sort", "Stack using class", "Pointer arithmetic", "File streams", "Operator overloading", "Template function"]
    }
    if 'last_language' not in st.session_state or st.session_state['last_language'] != language or st.button("New Random Topic"):
        st.session_state['last_language'] = language
        st.session_state['random_topic'] = random.choice(language_topics[language])
    topic = st.session_state['random_topic']
    st.info(f"Write code for the following topic in {language}: **{topic}**")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Back", key="back_to_info", use_container_width=True):
            st.session_state["stage"] = "info"
            st.rerun()
    with col2:
        if st.button("Next", key="to_code", use_container_width=True):
            st.session_state["stage"] = "code"
            st.session_state["language"] = language
            st.session_state["topic"] = topic
            st.rerun()

elif st.session_state.stage == "code":
    st.subheader("💻 Submit Your Code")
    lang = st.session_state.get("language", "Python")
    topic = st.session_state.get("topic", "")
    st.info(f"Write code for the following topic in {lang}: **{topic}**")
    uploaded = st.file_uploader("Upload Code File", type=["py", "java", "js", "cpp"])
    if uploaded:
        st.session_state.code = uploaded.read().decode("utf-8")
    else:
        st.session_state.code = st.text_area("Or Paste Your Code Below:", height=300)
    if st.session_state.code.strip():
        if st.button("Generate Questions"):
            st.session_state.questions = get_gemma_questions(st.session_state.code)
            if not st.session_state.questions:
                st.error("No questions could be generated for your code. Please check your code and try again.")
            else:
                st.session_state.answers = {}
                st.session_state.current_q_idx = 0
                st.session_state.stage = "questions"

elif st.session_state.stage == "questions":
    if not st.session_state.questions:
        st.error("No questions available. Please go back and try again.")
        if st.button("Back", key="back_to_code_empty_questions"):
            st.session_state.stage = "code"
            st.rerun()
    else:
        st.subheader("🧠 Answer Interview Questions")
        idx = st.session_state.current_q_idx
        q = st.session_state.questions[idx]
        st.markdown(f"**Q{idx+1}:** {q}")
        ans = st.text_area(f"Your Answer to Q{idx+1}", key=f"ans_{idx}", value=st.session_state.answers.get(q, ""))
        st.session_state.answers[q] = ans
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Previous", key="prev_q", use_container_width=True, disabled=idx==0):
                st.session_state.current_q_idx = max(0, idx-1)
                st.rerun()
        with col2:
            if idx < len(st.session_state.questions)-1:
                if st.button("Next", key="next_q", use_container_width=True, disabled=not ans.strip()):
                    st.session_state.current_q_idx = idx+1
                    st.rerun()
            else:
                if st.button("Submit Answers", key="submit_ans", use_container_width=True, disabled=not ans.strip()):
                    st.session_state.followups = [
                        {
                            "main_q": q,
                            "main_a": st.session_state.answers[q],
                            "followup_q": get_followup_question(q, st.session_state.answers[q]),
                            "followup_a": ""
                        } for q in st.session_state.questions
                    ]
                    st.session_state.current_fup_idx = 0
                    st.session_state.stage = "followups"
                    st.rerun()

elif st.session_state.stage == "followups":
    st.subheader("🔁 Follow-up Questions")
    idx = st.session_state.current_fup_idx
    f = st.session_state.followups[idx]
    st.markdown(f"**Follow-up Q{idx+1}:** {f['followup_q']}")
    f["followup_a"] = st.text_area(f"Your Answer to Follow-up Q{idx+1}", key=f"follow_ans_{idx}", value=f.get("followup_a", ""))
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Previous", key="prev_fup", use_container_width=True, disabled=idx==0):
            st.session_state.current_fup_idx = max(0, idx-1)
            st.rerun()
    with col2:
        if idx < len(st.session_state.followups)-1:
            if st.button("Next", key="next_fup", use_container_width=True, disabled=not f["followup_a"].strip()):
                st.session_state.current_fup_idx = idx+1
                st.rerun()
        else:
            if st.button("Finish & Review", key="finish_review", use_container_width=True, disabled=not f["followup_a"].strip()):
                st.session_state.reviews = []
                for qa in st.session_state.questions:
                    fb = get_review_feedback(qa, st.session_state.answers[qa])
                    st.session_state.reviews.append({"q": qa, "a": st.session_state.answers[qa], **fb})
                for fup in st.session_state.followups:
                    fb = get_review_feedback(fup["followup_q"], fup["followup_a"])
                    st.session_state.reviews.append({"q": fup["followup_q"], "a": fup["followup_a"], **fb})
                st.session_state.stage = "summary"
                st.rerun()

elif st.session_state.stage == "summary":
    st.subheader("📋 Summary & Score")
    total = 0
    all_strengths = []
    all_weaknesses = []
    strengths_weaknesses = []
    for i, r in enumerate(st.session_state.reviews):
        st.markdown(f"**Q{i+1}:** {r['q']}")
        st.markdown(f"**Your Answer:** {r['a']}")
        st.markdown(f"**Feedback:** {r['feedback']}")
        st.markdown(f"**Score:** {r['score']} / 5")
        sw = get_strengths_weaknesses(r['q'], r['a'])
        strengths_weaknesses.append(sw)
        all_strengths.extend(sw['strengths'])
        all_weaknesses.extend(sw['weaknesses'])
        total += r['score']
        st.markdown("---")
    final_score = round(total * 10 / (len(st.session_state.reviews) * 5), 2)
    st.success(f"🎯 Final Score: {final_score} / 10")

    # Skill frequency analysis
    strength_counts = Counter(all_strengths)
    weakness_counts = Counter(all_weaknesses)
    # Remove overlap: if a skill is a strength, do not show as weakness
    overlap = set(strength_counts) & set(weakness_counts)
    for skill in overlap:
        del weakness_counts[skill]
    st.subheader("📈 Candidate Skill Analysis")
    st.markdown("**Top Strengths:**")
    if strength_counts:
        for skill, count in strength_counts.most_common():
            st.markdown(f"- {skill}: {count} ✔️")
    else:
        st.markdown("- None")
    st.markdown("**Top Weaknesses:**")
    if weakness_counts:
        for skill, count in weakness_counts.most_common():
            st.markdown(f"- {skill}: {count} ⚠️")
    else:
        st.markdown("- None")

    if st.button("💾 Save Result"):
        data = {
            "name": st.session_state.name,
            "qualification": st.session_state.qual,
            "introduction": st.session_state.intro,
            "code": st.session_state.code,
            "review": st.session_state.reviews,
            "strengths_weaknesses": strengths_weaknesses,
            "final_score": final_score
        }
        filename = f"{st.session_state.name.replace(' ', '_')}_interview.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        st.success(f"Saved as {filename}")
