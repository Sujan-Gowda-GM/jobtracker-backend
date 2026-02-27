from pypdf import PdfReader
import google.generativeai as genai
import os
import json

def pdf_extract(file):
    reader=PdfReader(file)
    text=""
    
    for page in reader.pages:
        content=page.extract_text()
        if content:
            text+=content+"\n"
            
    return text

def gemini_feedback(resume_text,job_description):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model=genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    You are an expert ATS (Applicant Tracking System) analyzer.
    Compare the following Resume with the Job Description.
    
    Resume Text: {resume_text}
    Job Description: {job_description}
    
    Task: Provide an ATS score (0-100) and specific feedback.
    Format: You MUST return ONLY a valid JSON object. Do not explain.
    JSON Structure:
    {{
        "score": 85,
        "feedback": "Your summary of improvements here."
    }}
    """
    
    response=model.generate_content(prompt)
    
    raw_response=response.text.strip().replace('```json', '').replace('```', '')
    
    try:
        return json.loads(raw_response)
    except Exception as e:
        return {"score": 0, "feedback": "AI processing error. Please try again."}

