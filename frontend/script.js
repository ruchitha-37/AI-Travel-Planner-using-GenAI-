// ==========================================
// AI Travel Planner — Frontend Script
// ==========================================

// In production (Render), window.BACKEND_URL is injected via config.js
// In local dev, it falls back to localhost
const API_BASE = (window.BACKEND_URL || "http://127.0.0.1:8000") + "/api";
let selectedBudget = "budget";

// ---- Load Popular Destinations ----
async function loadDestinations() {
    try {
        const res = await fetch(`${API_BASE}/destinations`);
        if (!res.ok) return;
        const data = await res.json();
        const container = document.getElementById("destinationChips");

        data.popular.forEach(dest => {
            const chip = document.createElement("button");
            chip.className = "dest-chip";
            chip.id = `dest-chip-${dest.name.toLowerCase().replace(/\s+/g, '-')}`;
            chip.innerHTML = `<span class="chip-emoji">${dest.emoji}</span>${dest.name}`;
            chip.onclick = () => {
                document.getElementById("destination").value = dest.name;
                document.getElementById("preferences").value = dest.tags.join(", ");
                // Highlight selected chip
                document.querySelectorAll(".dest-chip").forEach(c => c.classList.remove("active"));
                chip.classList.add("active");
            };
            container.appendChild(chip);
        });
    } catch (err) {
        // Backend not running yet — silent fail for destinations
        console.warn("Destinations endpoint not available:", err.message);
    }
}

// ---- Budget Selector ----
function selectBudget(level) {
    selectedBudget = level;
    document.querySelectorAll(".budget-btn").forEach(btn => btn.classList.remove("active"));
    document.getElementById(`budget-${level}`).classList.add("active");
}

// ---- Add Tag to Preferences ----
function addTag(tag) {
    const prefInput = document.getElementById("preferences");
    const current = prefInput.value.trim();
    if (current === "") {
        prefInput.value = tag;
    } else if (!current.toLowerCase().includes(tag.toLowerCase())) {
        prefInput.value = current + ", " + tag;
    }
    prefInput.focus();
}

// ---- Main: Plan Trip ----
async function planTrip() {
    const destination = document.getElementById("destination").value.trim();
    const preferences = document.getElementById("preferences").value.trim();
    const days = parseInt(document.getElementById("days").value);
    const travelers = parseInt(document.getElementById("travelers").value);

    // Validation
    if (!destination) return showError("Please enter a destination 📍");
    if (!preferences) return showError("Please add at least one preference 🎯");
    if (!days || days < 1 || days > 30) return showError("Days must be between 1 and 30 📅");
    if (!travelers || travelers < 1) return showError("Number of travelers must be at least 1 👥");

    // Hide previous results/errors
    hideResult();
    hideError();

    // Show loading state
    setLoading(true);

    const payload = {
        destination,
        preferences,
        days,
        travelers,
        budget: selectedBudget
    };

    try {
        const res = await fetch(`${API_BASE}/plan-trip`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Something went wrong on the server.");
        }

        // Display result
        showResult(data);

    } catch (err) {
        if (err.message.includes("Failed to fetch") || err.message.includes("NetworkError")) {
            showError("❌ Cannot connect to backend. Make sure FastAPI is running:\n\n  uvicorn app.main:app --reload");
        } else {
            showError(`❌ ${err.message}`);
        }
    } finally {
        setLoading(false);
    }
}

// ---- UI Helpers ----

function setLoading(isLoading) {
    const btn = document.getElementById("generateBtn");
    const btnText = document.getElementById("btnText");
    const loader = document.getElementById("btnLoader");

    btn.disabled = isLoading;
    btnText.textContent = isLoading ? "Generating your itinerary..." : "🚀 Generate My Itinerary";

    if (isLoading) {
        loader.classList.remove("hidden");
    } else {
        loader.classList.add("hidden");
    }
}

function showResult(data) {
    const resultCard = document.getElementById("resultCard");
    const resultTitle = document.getElementById("resultTitle");
    const resultEl = document.getElementById("result");

    resultTitle.textContent = `🗺️ ${data.destination} — ${data.days}-Day Travel Plan`;
    resultEl.textContent = data.itinerary;
    resultCard.classList.remove("hidden");

    // Smooth scroll to result
    resultCard.scrollIntoView({ behavior: "smooth", block: "start" });
}

function hideResult() {
    document.getElementById("resultCard").classList.add("hidden");
    document.getElementById("result").textContent = "";
}

function showError(msg) {
    const errorCard = document.getElementById("errorCard");
    document.getElementById("errorMsg").textContent = msg;
    errorCard.classList.remove("hidden");
    errorCard.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function hideError() {
    document.getElementById("errorCard").classList.add("hidden");
}

async function copyItinerary() {
    const text = document.getElementById("result").textContent;
    if (!text) return;

    try {
        await navigator.clipboard.writeText(text);
        const btn = document.getElementById("copyBtn");
        btn.textContent = "✅ Copied!";
        setTimeout(() => (btn.textContent = "📋 Copy"), 2000);
    } catch {
        // Fallback
        const ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
    }
}

// Allow pressing Enter to submit
document.addEventListener("DOMContentLoaded", () => {
    loadDestinations();

    ["destination", "preferences", "days", "travelers"].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener("keydown", e => {
                if (e.key === "Enter") planTrip();
            });
        }
    });
});
