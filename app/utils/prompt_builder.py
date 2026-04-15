from app.models.request_model import TravelRequest


def build_prompt(data: TravelRequest) -> str:
    """
    Builds a structured prompt for the LLM to generate a travel itinerary.
    """
    budget_map = {
        "budget": "economical (under ₹2000/day per person)",
        "medium": "moderate (₹2000–₹5000/day per person)",
        "luxury": "luxury (₹5000+/day per person)"
    }
    budget_desc = budget_map.get(data.budget.lower(), data.budget)

    prompt = f"""
You are an expert AI travel planner with deep knowledge of Indian and international destinations.

Create a detailed {data.days}-day travel itinerary for the following trip:

📍 Destination: {data.destination}
🎯 Preferences: {data.preferences}
👥 Travelers: {data.travelers} person(s)
💰 Budget Level: {budget_desc}

Please provide a comprehensive travel plan in the following structured format:

---
## ✈️ Trip Overview
Give a 2–3 line exciting intro about {data.destination}.

## 📅 Day-by-Day Itinerary
For each day, list:
- Morning, Afternoon, and Evening activities
- Key attractions to visit
- Local experiences to try

## 🏨 Hotel Suggestions
Provide 3 hotel options matching the {data.budget} budget:
- Hotel Name, approximate price per night (INR), and why it's recommended

## 🍽️ Food Suggestions
- 3–5 must-try local dishes or restaurants

## 💸 Estimated Total Cost (INR)
Break down cost for {data.travelers} traveler(s) for {data.days} days:
- Accommodation
- Food
- Transport
- Activities
- **Total Estimate**

## 💡 Pro Tips
3 quick tips specific to {data.destination} for a {data.preferences} traveler.
---

Be specific, enthusiastic, and practical. Use emojis to make it engaging!
"""
    return prompt.strip()
