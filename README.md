# 📈 WealthFlow AI

**WealthFlow AI** is a Python and Django-based AI financial assistant dashboard that helps users ask finance-related questions, understand investment concepts, and calculate basic investment growth projections.

The project uses **Django** for the backend, **SQLite** for storing chat sessions and messages, and **OpenRouter API** with a Gemini model for AI-generated responses.

> ⚠️ This project is built for learning and portfolio purposes only. It does not provide professional financial advice or real-time stock market recommendations.

---

## 🚀 Key Features

### 🤖 AI-Powered Financial Assistant

Users can ask finance-related questions about investments, stocks, mutual funds, bonds, and basic financial planning.

### 💬 Chat Session Management

The application stores chat sessions and messages, allowing users to view previous conversations.

### 📊 Investment Growth Projection

Includes a custom compound-interest calculation tool to estimate future investment value based on amount, return percentage, and duration.

### 🔗 OpenRouter API Integration

Uses OpenRouter API to connect with an AI model and generate intelligent financial explanations.

### 🧠 AI Response Handling

The backend sends user input and chat history to the AI model, receives the response, stores it, and displays it on the dashboard.

### 🖥️ Interactive Local Dashboard

A clean web dashboard where users can type questions and receive AI-generated responses.

---

## 🛠️ Tech Stack

| Category    | Technology                              |
| ----------- | --------------------------------------- |
| Backend     | Python, Django                          |
| Database    | SQLite                                  |
| AI / LLM    | OpenRouter API, Gemini Model            |
| Frontend    | HTML, CSS, JavaScript, Django Templates |
| Tools       | Git, GitHub, VS Code                    |
| Environment | python-dotenv                           |

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/magaavelan/Wealth-Flow-AI.git
```

### 2️⃣ Move into the Project Folder

```bash
cd Wealth-Flow-AI/Wealth-Flow
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5️⃣ Install Required Packages

```bash
pip install django python-dotenv openai
```

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

### 6️⃣ Create a `.env` File

Create a `.env` file inside the project folder and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 7️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8️⃣ Start the Development Server

```bash
python manage.py runserver
```

### 9️⃣ Open in Browser

```text
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

```text
Wealth-Flow-AI/
│
├── Wealth-Flow/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── core/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── agent.py
│   │   ├── templates/
│   │   │   └── core/
│   │   │       └── dashboard.html
│   │   └── migrations/
│   │
│   └── manage.py
│
└── README.md
```

---

## 🗃️ Database Models

### 💬 ChatSession

Stores each chat conversation.

**Main fields:**

* title
* user
* created_at

### 📝 ChatMessage

Stores messages inside each chat session.

**Main fields:**

* session
* role
* content
* timestamp

The `role` field identifies whether the message is from the **user** or the **assistant**.

---

## 🔄 Application Flow

1. User opens the WealthFlow AI dashboard.
2. User creates or selects a chat session.
3. User enters a finance-related question.
4. Django stores the user message in SQLite.
5. The backend sends the user message and chat history to OpenRouter API.
6. The AI model generates a response.
7. Django stores the AI response in the database.
8. The frontend displays the response in the chat dashboard.

---

## 💡 Example Questions

Users can ask questions like:

```text
What is a mutual fund?
```

```text
Explain stocks and bonds in simple words.
```

```text
If I invest ₹10,000 for 5 years at 12% return, what will be the future value?
```

```text
How should a beginner understand asset allocation?
```

---

## 📚 What I Learned

Through this project, I practiced:

* Django project structure
* Django models and database handling
* Chat session and message storage
* POST request handling
* JSON response handling
* OpenRouter API integration
* AI response processing
* Environment variable usage
* Basic compound-interest calculation
* Building an AI-powered dashboard

---

## ⚠️ Disclaimer

WealthFlow AI is created for educational and portfolio purposes only.

It does not provide real-time market data, guaranteed investment returns, professional financial advice, or buy/sell stock recommendations.

Users should consult a certified financial advisor before making real investment decisions.

---

## 👨‍💻 Author

**Magaavelan S**
Python Developer Fresher

🔗 GitHub: https://github.com/magaavelan
