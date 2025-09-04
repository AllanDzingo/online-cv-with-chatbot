import PyPDF2

# --- Step 1: Extract text from PDF ---
def extract_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.lower()

# --- Step 2: Split into sections ---
def parse_cv_sections(cv_text):
    sections = {
        "skills": "",
        "experience": "",
        "education": ""
    }

    lines = cv_text.splitlines()
    current_section = None
    for line in lines:
        line_lower = line.strip().lower()
        if "skill" in line_lower:
            current_section = "skills"
        elif "experience" in line_lower or "work" in line_lower:
            current_section = "experience"
        elif "education" in line_lower or "degree" in line_lower:
            current_section = "education"
        elif current_section:
            sections[current_section] += line + " "
    return sections

# --- Step 3: Load CV sections ---
cv_text = extract_pdf_text("LinkedInCV.pdf")
cv_sections = parse_cv_sections(cv_text)

# --- Step 4: Chatbot response ---
def get_response(user_input):
    user_input = user_input.lower()
    if "skill" in user_input:
        return cv_sections["skills"] or "Skills info not found."
    elif "experience" in user_input or "work" in user_input:
        return cv_sections["experience"] or "Experience info not found."
    elif "education" in user_input or "degree" in user_input:
        return cv_sections["education"] or "Education info not found."
    else:
        return "I can answer questions about my skills, experience, or education."
