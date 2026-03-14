from flask import Flask, render_template, request
from resume_reader import extract_text
from skills import skills

app = Flask(__name__)

required_skills = [
    "python", "java", "sql", "machine learning",
    "html", "css", "javascript", "communication",
    "teamwork", "problem solving", "dsa"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    
    if file:
        text = extract_text(file)

        detected = []
        missing = []

        for skill in required_skills:
            if skill in text:
                detected.append(skill)
            else:
                missing.append(skill)

        score = int((len(detected) / len(required_skills)) * 100)

        return render_template('index.html',
                               detected=detected,
                               missing=missing,
                               score=score)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)