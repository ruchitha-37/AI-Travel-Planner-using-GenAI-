# 🌍 AI Travel Planner — GenAI Portfolio Project

A full-stack AI-powered travel planner that generates day-wise itineraries, hotel suggestions, food picks, and cost breakdowns using **OpenAI GPT** + **LangChain** + **FastAPI**.

---

## 🧠 Tech Stack

| Layer      | Technology              |
|------------|------------------------|
| AI/LLM     | OpenAI GPT-3.5 Turbo   |
| AI Framework | LangChain             |
| Backend    | FastAPI + Uvicorn       |
| Frontend   | HTML5 + CSS3 + Vanilla JS |
| Notebook   | Jupyter (AI testing)    |

---

## 🏗️ Project Structure

```
ai-travel-planner/
├── notebook/
│   └── travel_planner.ipynb     # AI concept testing
├── app/
│   ├── main.py                  # FastAPI app entry
│   ├── routes/planner.py        # API endpoints
│   ├── services/llm_service.py  # LLM integration
│   ├── models/request_model.py  # Input schema
│   └── utils/prompt_builder.py  # Prompt engineering
├── frontend/
│   ├── index.html               # Main UI
│   ├── style.css                # Dark mode styling
│   └── script.js                # API integration
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone / Navigate to Project

```bash
cd ai-travel-planner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set OpenAI API Key

```powershell
# Windows PowerShell
$env:OPENAI_API_KEY = "sk-your-api-key-here"
```
r
```bash
# Linux / Mac
export OPENAI_API_KEY="sk-your-api-key-here"
```

> Get your key at https://platform.openai.com/api-keys

### 4. Run the Backend

```bash
uvicorn app.main:app --reload
```

API will be available at: http://127.0.0.1:8000
Interactive docs: http://127.0.0.1:8000/docs

### 5. Open the Frontend

Simply open `frontend/index.html` in your browser — no build step needed!

---

## 📡 API Endpoints

| Method | Endpoint              | Description                   |
|--------|-----------------------|-------------------------------|
| GET    | `/`                   | Health check                  |
| POST   | `/api/plan-trip`      | Generate travel itinerary     |
| GET    | `/api/destinations`   | Get popular destinations list |

### Sample Request

```json
POST /api/plan-trip
{
  "destination": "Goa",
  "preferences": "beach, nightlife, budget food",
  "days": 3,
  "budget": "budget",
  "travelers": 2
}
```

---

## 🎯 What the AI Generates

- ✅ Day-by-day activity plan (Morning / Afternoon / Evening)
- ✅ 3 hotel suggestions with pricing (in INR)
- ✅ Local food & restaurant picks
- ✅ Full cost breakdown for the trip
- ✅ Pro travel tips specific to the destination
