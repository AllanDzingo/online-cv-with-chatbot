import json
import random

# --- Step 1: Load CV data from JSON ---
with open("cv_data.json", "r") as f:
    cv_data = json.load(f)

# --- Helper: make responses sound natural ---
def natural_response(options):
    """Pick a random phrasing so replies don't feel repetitive."""
    return random.choice(options)

# --- Step 2: Chatbot response function ---
def get_response(user_input):
    user_input = user_input.lower()

    if "skill" in user_input:
        skills = ", ".join(cv_data["skills"])
        return natural_response([
            f"I’d say my strongest skills are {skills}.",
            f"My main strengths include {skills}, which I’ve built over time.",
            f"Some of the skills I rely on most are {skills}."
        ])

    elif any(word in user_input for word in ["experience", "work", "job", "career"]):
        jobs = [
            f"{job['role']} at {job['company']} ({job['dates']})"
            for job in cv_data["experience"]
        ]
        job_summary = "; ".join(jobs)
        return natural_response([
            f"I’ve gained experience through roles such as {job_summary}.",
            f"My career so far includes positions like {job_summary}.",
            f"I’ve worked in roles including {job_summary}, which gave me valuable experience."
        ])

    elif any(word in user_input for word in ["education", "degree", "study", "school", "university"]):
        edu = [
            f"{e['qualification']} from {e['institution']} ({e['dates']})"
            for e in cv_data["education"]
        ]
        edu_summary = "; ".join(edu)
        return natural_response([
            f"My academic background includes {edu_summary}.",
            f"I studied {edu_summary}, which shaped my knowledge and skills.",
            f"My qualifications include {edu_summary}."
        ])

    elif any(word in user_input for word in ["summary", "about", "intro", "yourself", "profile"]):
        return natural_response([
            f"Here’s a quick summary about me: {cv_data['profile']['summary']}",
            f"In short: {cv_data['profile']['summary']}",
            cv_data['profile']['summary']
        ])

    elif any(word in user_input for word in ["contact", "reach", "email", "linkedin"]):
        contact = cv_data["profile"]["contact"]
        return natural_response([
            f"You can reach me via email at {contact['email']} or on LinkedIn: {contact['linkedin']}.",
            f"My contact details are: Email - {contact['email']}, LinkedIn - {contact['linkedin']}.",
            f"Feel free to connect with me at {contact['email']} or on LinkedIn: {contact['linkedin']}."
        ])

    else:
        return natural_response([
            "I can tell you about my skills, work experience, education, or a short profile. What would you like to know?",
            "Would you like to hear about my skills, my background, or my work history?",
            "I’ve got info on my education, experience, skills, and a short bio. Which one interests you?"
        ])
