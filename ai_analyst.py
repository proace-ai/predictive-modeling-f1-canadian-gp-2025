# ai_analyst.py

import pandas as pd
import google.generativeai as genai

# CONFIGURE API
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

# LOAD DATA
gp_data = pd.read_csv("canadian_gp_history.csv")
driver_data = pd.read_csv("driver_profiles.csv")

# FORMAT
gp_table = gp_data.to_markdown(index=False)
driver_table = driver_data.to_markdown(index=False)

# PROMPT
prompt = f"""
You are an AI sports strategist with deep expertise in Formula 1 analytics.

🎯 Objective:
Predict the top 3 podium finishers for the 2025 Canadian Grand Prix at Circuit Gilles Villeneuve.

Here is all the available data:

---
📊 **Past Canadian GP results:**
{gp_table}

---
🏎️ **Driver Profiles:**
{driver_table}

---
🏟️ **Track Insights**:
- Semi-street circuit with fast straights and heavy braking zones.
- Low downforce setups are optimal.
- High chance of safety cars.
- Braking efficiency and traction out of corners is key.

🌧️ **Race Day Weather Forecast**:
- 21°C temperature
- 40% chance of rain
- Slightly cloudy with humidity expected

🧠 Use all this data to predict:
1. Top 3 podium finishers.
2. Reasoning behind each selection.
3. Highlight any driver whose performance might surprise or disappoint based on this analysis.

Format:
1st: [Driver]  
2nd: [Driver]  
3rd: [Driver]  

Reasoning:
...
"""

# GENERATE
response = model.generate_content(prompt)
print("🔮 Gemini Prediction:\n")
print(response.text)
