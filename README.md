# SupplySentinel

**SupplySentinel** is an AI-powered platform that proactively monitors real-time risks across fulfillment centers by analyzing weather disruptions, political unrest, labor strikes, and public sentiment.  
It uses FastAPI, MongoDB Atlas, and Google's Gemini AI model to calculate risk scores and recommend mitigation strategies for supply chain resilience.

## 🌟 Features

- Live weather, news, and sentiment risk analysis
- AI-driven risk scoring for each fulfillment center
- Custom Gemini recommendations for at-risk facilities
- MongoDB Atlas integration for real-time data storage
- Fully automated agent running every 5 minutes

## 🏗️ Tech Stack

- Python 3.10+
- FastAPI
- NiceGUI (for future dashboard)
- MongoDB Atlas (Cloud NoSQL Database)
- Gemini AI API (Google Generative AI)
- Hugging Face Transformers
- OpenWeatherMap API, NewsAPI

## 🚀 How It Works

1. Fetch live weather, news headlines, and public sentiment data.
2. Calculate individual risk scores per fulfillment center.
3. Trigger Gemini AI to generate risk mitigation advice for facilities at high risk (>70%).
4. Update MongoDB collections with live scores and recommendations.
5. Repeat every 5 minutes.

## 📦 Project Structure
supplysentinel/ 
├── app/ 
│ ├── agent/ # Background agent that fetches risks and updates scores 
│ ├── services/ # Weather, News, Sentiment, Database, Gemini AI service handlers 
│ ├── core/ # Core utility functions and future logic (placeholder) 
├── .env # Environment variables (MongoDB URI, API keys) 
├── requirements.txt # Python dependencies 
├── README.md # Project documentation


## 📜 License

MIT License. Feel free to use, fork, and build upon SupplySentinel.

---

# 📣 Want to Learn More?

SupplySentinel is built for modern supply chain risk management using AI agents and real-time data processing.  
Stay tuned for dashboard and alerting system updates! 🚀
