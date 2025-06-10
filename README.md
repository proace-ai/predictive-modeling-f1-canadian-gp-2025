# F1 Canadian Grand Prix Predictor 🏎️

An AI-powered Formula 1 race prediction system that analyzes historical data and driver profiles to predict podium finishers for the Canadian Grand Prix at Circuit Gilles Villeneuve.

## 🎯 Project Overview

This project combines historical F1 race data with AI analysis to make informed predictions about race outcomes. It uses Google's Gemini AI model to analyze patterns from past Canadian GP results (2019-2024) and current driver performance profiles.

## 🏗️ Project Structure

```
f1-canadian-gp-predictor/
├── ai_analyst.py           # Main prediction engine using Gemini AI
├── data_collector.py       # Data collection and processing scripts
├── canadian_gp_history.csv # Historical race results (2019-2024)
├── driver_profiles.csv     # Current driver performance metrics
├── cache/                  # FastF1 data cache directory
└── README.md              # Project documentation
```

## 📊 Data Sources

### Historical Race Data
- **Years Covered**: 2019, 2022, 2023, 2024
- **Data Points**: Driver positions, lap times, race status, team performance
- **Source**: FastF1 API for official F1 timing data

### Driver Profiles
- **Metrics**: Consistency rating, aggressiveness, wet weather skill
- **Attributes**: Strengths, weaknesses, preferred circuit types
- **Coverage**: All 20 drivers from the 2025 F1 season

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Required Libraries
```bash
pip install pandas
pip install fastf1
pip install google-generativeai
```

### Setup
1. Clone the repository
2. Install dependencies
3. Configure your Google Gemini API key in `ai_analyst.py`:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

## 🚀 Usage

### 1. Collect Data (Optional)
If you want to refresh the historical data:
```bash
python data_collector.py
```
This will:
- Fetch fresh race results from FastF1
- Generate updated driver profiles
- Save data to CSV files

### 2. Generate Predictions
Run the main prediction script:
```bash
python ai_analyst.py
```

The AI will analyze:
- Historical performance patterns at Montreal
- Track-specific requirements (low downforce, braking zones)
- Weather conditions and their impact
- Driver strengths/weaknesses alignment with track characteristics

## 📈 Prediction Methodology

### Data Analysis Factors
1. **Historical Performance**: Past results at Circuit Gilles Villeneuve
2. **Track Characteristics**: Semi-street circuit with long straights and heavy braking
3. **Weather Impact**: Rain probability and temperature effects
4. **Driver Profiles**: Skill ratings and circuit preferences
5. **Team Performance**: Recent form and car characteristics

### AI Processing
- Uses Google Gemini 2.5 Flash model for analysis
- Processes structured data in markdown format
- Applies F1 domain expertise through specialized prompting
- Generates reasoned predictions with explanations

## 🏁 Circuit Gilles Villeneuve Specifics

### Track Characteristics
- **Type**: Semi-street circuit
- **Key Features**: Fast straights, heavy braking zones
- **Setup**: Low downforce optimal
- **Challenges**: High safety car probability, wall proximity

### Historical Patterns
- **Recent Winners**: Max Verstappen (2022, 2023, 2024), Lewis Hamilton (2019)
- **Successful Teams**: Red Bull, Mercedes dominance
- **Weather Impact**: Rain can significantly shuffle the order

## 📋 Output Format

The prediction provides:
1. **Top 3 Podium Predictions**
   - 1st, 2nd, 3rd place finishers
2. **Detailed Reasoning**
   - Why each driver was selected
   - Track-specific advantages
3. **Surprise/Disappointment Analysis**
   - Drivers who might over/under-perform expectations

## 🔧 Customization

### Modifying Driver Profiles
Edit `driver_profiles.csv` to update:
- Consistency ratings (0-10)
- Aggressiveness levels (0-10)
- Wet weather skills (Poor/Average/Good/Strong/Excellent/Master)
- Strengths and weaknesses

### Adding More Historical Data
Modify the `years` list in `data_collector.py`:
```python
get_canadian_gp_results([2019, 2020, 2021, 2022, 2023, 2024])
```

### Adjusting AI Prompts
Customize the prediction criteria in `ai_analyst.py` by modifying the prompt template.

## 🤖 AI Model Details

- **Model**: Google Gemini 2.5 Flash Preview
- **Capabilities**: Multi-modal analysis, reasoning, sports analytics
- **Input**: Structured data + natural language context
- **Output**: Formatted predictions with explanations

## 📊 Sample Output

```
🔮 Gemini Prediction:

1st: Max Verstappen
2nd: Lando Norris  
3rd: Lewis Hamilton

Reasoning:
Verstappen's dominance at Montreal continues with his superior
high-speed stability and tire management. Norris benefits from
McLaren's low-drag setup and his wet weather expertise given
the 40% rain chance. Hamilton's experience and wet weather
mastery secure the final podium spot...
```

## 🔮 Limitations

- Predictions are based on historical patterns and may not account for:
  - Mechanical failures
  - Strategic surprises
  - Unexpected weather changes
  - Driver/team form fluctuations
- AI analysis is probabilistic, not deterministic
- Data limited to available FastF1 coverage

## 🚧 Future Enhancements

- Real-time telemetry integration
- Qualifying performance weighting
- Car performance correlation analysis
- Multi-race prediction accuracy tracking
- Interactive web interface

## 📝 License

This project is for educational and entertainment purposes. F1 data is used under fair use for analysis.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues or questions:
- Check existing GitHub issues
- Create a new issue with detailed description
- Include error messages and system information

---

**Disclaimer**: This is a prediction tool for entertainment purposes. Actual race results may vary significantly from predictions.