# QuizMaster AI - Intelligent Quiz Generator 🧠⚡

An AI-powered web application that generates 10 high-quality MCQ questions for any given topic using the **Groq Llama 3** model.

## 🚀 Features
- **Instant Quiz Generation**: Enter a topic and get 10 MCQs in seconds.
- **AI Powered**: Utilizes Groq's `llama-3.3-70b-versatile` model for high-quality content.
- **Clean UI/UX**: Minimalist and responsive design built with Flask & CSS.
- **Dynamic Content**: Each quiz is unique and formatted precisely.

## 🛠️ Technology Stack
- **Backend**: Python (Flask)
- **AI Integration**: Groq Llama-3 API
- **Frontend**: HTML5, CSS3
- **Environment Management**: Python-Dotenv

## 📂 Project Structure
```text
.
├── app.py              # Main Flask application
├── static/             # Static files
│   └── style.css       # Custom CSS styling
├── templates/          # HTML templates
│   └── index.html      # Main application interface
├── .env                # Environment variables (Excluded from git)
├── .env.example        # Example environment variables
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment configuration
└── .gitignore          # Files ignored by git
```

## ⚙️ Setup & Installation

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/singhneha139222-desig/ai_quiz_app.git
cd ai_quiz_app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
python app.py
```
Wait for the server to start, then open your browser and visit: `http://127.0.0.1:5001`

## 💡 How it Works
1. Enter any topic (e.g., "Python OOPS", "Deep Learning", etc.) in the input field.
2. The app sends a structured prompt to the Groq API.
3. The AI generates 10 MCQs with 4 options and the correct answer.
4. The quiz is instantly displayed on the web page.
---

## 🚀 Vercel Deployment

This project is configured for easy deployment on **Vercel**.

### Steps to Deploy:
1. **Push to GitHub**: Make sure your code is on GitHub.
2. **Import to Vercel**: Connect your repository to Vercel.
3. **Set Environment Variables**: In the Vercel dashboard, go to *Settings > Environment Variables* and add:
   - `GROQ_API_KEY`: Your Groq Cloud API Key.
4. **Deploy**: Vercel will automatically detect the `vercel.json` and deploy your Flask app.

> [!NOTE]
> Ensure that your `.git` folder is in the root directory (where `app.py` is) before pushing.

