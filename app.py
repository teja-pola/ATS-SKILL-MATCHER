from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai
import io
import base64
import markdown

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

# Function to get response from Gemini AI
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        return f"Error in generating response: {str(e)}"

# Function to process uploaded PDF and convert the first page to an image
def input_pdf_setup(uploaded_file):
    try:
        if uploaded_file:
            pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            first_page = pdf_document[0]
            pix = first_page.get_pixmap()
            
            img_byte_arr = io.BytesIO()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img.save(img_byte_arr, format="JPEG")
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [{"mime_type": "image/jpeg", "data": base64.b64encode(img_byte_arr).decode()}]
            return pdf_parts
    except Exception as e:
        return None

# Input Prompts
input_prompt1 = """You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.

Respond in an engaging, structured format as follows:
1. Overview: A brief summary of the candidate's suitability.
2. Strengths: Bullet points highlighting strong skills or experiences related to the job description.
3. Weaknesses: Bullet points where the resume lacks alignment with the job description.
4. Final Verdict: A short, one-sentence evaluation of whether the candidate is a good fit for the role.

Make sure the tone is professional, concise, and actionable.
give output in Markdown format
"""

input_prompt2 = """
You are a career advisor. Suggest actionable ways to improve the applicant's skills based on their resume and job description.

Respond in the following structured format:
1. Skills to Improve: List specific skills that the candidate should focus on.
2. How to Improve: Suggest clear, actionable steps such as:
   - Online courses
   - Certifications
   - Tools to practice
   - Real-world projects
3. Additional Resources: Recommend websites, platforms, or books where the candidate can learn these skills.

The tone should be encouraging, insightful, and tailored to the candidate's career growth.
give output in Markdown format
"""

input_prompt3 = """
You are an ATS (Applicant Tracking System) scanner evaluating the resume against the job description.

Respond in an engaging, structured format as follows:
1. Match Percentage: Provide a percentage score of how well the resume aligns with the job description.
2. Matched Keywords: List the keywords or skills from the job description that are present in the resume.
3. Missing Keywords: Highlight the important keywords or skills that are missing.
4. Suggestions: Briefly suggest ways to improve the match (e.g., add missing skills or tailor descriptions).

The tone should be analytical, clear, and encouraging.
give output in Markdown format
"""

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    error = None
    task = None

    if request.method == "POST":
        input_text = request.form.get("job_description")
        uploaded_file = request.files.get("resume_file")
        task = request.form.get("task")

        # Determine the prompt based on user action
        if task == "analyze_resume":
            input_prompt = input_prompt1
        elif task == "improve_skills":
            input_prompt = input_prompt2
        elif task == "percentage_match":
            input_prompt = input_prompt3
        else:
            error = "Invalid task selected."

        # Process PDF and get response
        if uploaded_file:
            pdf_content = input_pdf_setup(uploaded_file)
            if pdf_content:
                raw_response = get_gemini_response(input_text, pdf_content, input_prompt)
                response = markdown.markdown(raw_response)
            else:
                error = "Error processing the uploaded PDF file."
        else:
            error = "Please upload a valid resume PDF."

    return render_template("index.html", response=response, error=error, task=task)

if __name__ == "__main__":
    app.run(debug=True)
