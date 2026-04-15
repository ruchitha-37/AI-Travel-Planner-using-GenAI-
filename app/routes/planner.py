from fastapi import APIRouter, HTTPException
from app.models.request_model import TravelRequest
from app.services.llm_service import generate_plan
from app.utils.prompt_builder import build_prompt

router = APIRouter()


@router.post("/plan-trip", summary="Generate AI Travel Itinerary")
def plan_trip(request: TravelRequest):
    """
    Generate a complete AI-powered travel itinerary including:
    - Day-wise plan
    - Hotel suggestions
    - Food suggestions
    - Estimated cost in INR
    - Pro tips
    """
    try:
        prompt = build_prompt(request)
        result = generate_plan(prompt)
        return {
            "success": True,
            "destination": request.destination,
            "days": request.days,
            "itinerary": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")


@router.get("/destinations", summary="Popular Destinations")
def get_destinations():
    """Returns a list of popular travel destinations for quick selection."""
    return {
        "popular": [
            {"name": "Goa", "emoji": "🏖️", "tags": ["beach", "party", "nightlife"]},
            {"name": "Manali", "emoji": "🏔️", "tags": ["mountains", "snow", "adventure"]},
            {"name": "Jaipur", "emoji": "🏰", "tags": ["culture", "history", "heritage"]},
            {"name": "Kerala", "emoji": "🌴", "tags": ["backwaters", "nature", "ayurveda"]},
            {"name": "Ladakh", "emoji": "⛰️", "tags": ["adventure", "biking", "landscapes"]},
            {"name": "Mumbai", "emoji": "🌆", "tags": ["city", "food", "nightlife"]},
            {"name": "Rishikesh", "emoji": "🕉️", "tags": ["yoga", "rafting", "spiritual"]},
            {"name": "Andaman Islands", "emoji": "🐠", "tags": ["scuba", "beach", "island"]},
        ]
    }
