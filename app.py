import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    error = None

    if request.method == "POST":
        topic = request.form.get("topic", "python oops, function")
        
        client = get_groq_client()
        if not client:
            error = "Error: GROQ_API_KEY is not set in environment variables. Please check your Vercel settings."
        else:
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Generate 10 MCQ questions on {topic}. Please strictly follow this format for each question:\n\n**Question [Number]:** [Question Text]\n* A) [Option A]\n* B) [Option B]\n* C) [Option C]\n* D) [Option D]\n\n**Correct Answer:** [Answer Text]\n\nDo not add any greeting, intro or outro text."
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                )
                result = chat_completion.choices[0].message.content
            except Exception as e:
                error = f"AI Error: {str(e)}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host="0.0.0.0", port=port)