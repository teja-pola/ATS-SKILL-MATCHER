
# 📄 *ATS Skill Checker*

*ATS Skill Checker* is a Flask-based web application designed to evaluate resumes against job descriptions using AI. It analyzes resumes, provides ATS match percentages, and suggests improvements to align resumes with job descriptions. The app uses Google Gemini AI to process and return structured insights, helping candidates tailor their resumes to specific roles effectively.

---

## 🚀 *Features*

1. *Analyze Resume*  
   - Provides an overview of the candidate’s strengths and weaknesses.  
   - Structured evaluation with key highlights.

2. *Suggest Skill Improvements*  
   - Offers actionable steps to improve missing skills.  
   - Recommends online courses, certifications, tools, and resources.

3. *Percentage Match*  
   - Calculates the ATS compatibility percentage.  
   - Lists matched and missing keywords/skills.  
   - Provides suggestions to increase match scores.

---

## 🛠 *Technologies Used*

- *Backend*: Flask (Python)
- *AI Integration*: Google Gemini API  
- *PDF Processing*: PyMuPDF (for extracting first-page content)  
- *Image Handling*: PIL (Pillow)  
- *Markdown Rendering*: \markdown\ Python library  
- *Environment Configuration*: \python-dotenv\

---

## 📦 *Project Structure*

```plaintext
ats-skill-checker/
│
├── templates/
│   └── index.html            # Front-end HTML file for the user interface
│
├── app.py                    # Flask backend logic
├── .env                      # Environment variables (API key)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

---

## ⚙ *Setup Instructions*

Follow these steps to set up the project locally:

### *1. Clone the Repository*
```bash
git clone <your-repository-url>
cd ats-skill-checker
```

### *2. Create a Virtual Environment*
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\\Scripts\\activate
```

### *3. Install Dependencies*
Install all required libraries using \requirements.txt\:
```bash
pip install -r requirements.txt
```

### *4. Set Up Environment Variables*
Create a \.env\ file in the project root and add your Google Gemini API key:

```plaintext
GOOGLE_API_KEY=your_gemini_api_key_here
```

### *5. Run the Application*
Start the Flask server:

```bash
python app.py
```

Access the application in your browser at:  
👉 *http://127.0.0.1:5000/*

---

## 📋 *Usage*

1. *Enter Job Description*: Paste the job description in the text area.  
2. *Upload Resume*: Upload your resume as a PDF file.  
3. *Select Task*: Choose from the following options:  
   - Analyze Resume  
   - Suggest Skill Improvements  
   - Percentage Match  
4. *View Results*:  
   - AI-generated analysis and suggestions will appear as formatted Markdown.  
   - Use the insights to improve and align your resume.  

---

## 🎨 *Screenshots*

### *Main Interface*
![Main UI](https://via.placeholder.com/600x400.png?text=UI+Image+Placeholder)

### *Response Example*
- Structured insights displayed in Markdown format.  

---

## 🧩 *Dependencies*

The following libraries are required:

| Dependency             | Description                              |
|------------------------|------------------------------------------|
| Flask                  | Web framework for Python                |
| python-dotenv          | Environment variable management         |
| google-generativeai    | Google Gemini AI client                 |
| PyMuPDF                | PDF extraction library                  |
| Pillow (PIL)           | Image processing for PDF pages          |
| Markdown               | Converts Markdown text to HTML          |

Install them using:
```bash
pip install -r requirements.txt
```

---

## 🤝 *Contributing*

Contributions are welcome! Follow these steps to contribute:  
1. Fork the repository.  
2. Create a feature branch: \git checkout -b new-feature\.  
3. Commit changes: \git commit -m "Add new feature"\.  
4. Push to the branch: \git push origin new-feature\.  
5. Open a pull request.  

---

## 🛡 *License*

This project is licensed under the *MIT License*.

---


