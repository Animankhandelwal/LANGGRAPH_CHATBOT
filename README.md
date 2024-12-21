# Car Recommendation Chatbot

## Overview
The **Car Recommendation Chatbot** is an interactive Python application designed to assist users in finding the perfect car based on their preferences. It leverages the **Tavily API** to provide personalized car recommendations. Users can specify their preferences such as car type, budget, desired features, brand, and fuel type, and receive tailored suggestions.


## Features
- **Interactive Chatbot**: Guides users step-by-step to input their car preferences.
- **Custom Recommendations**: Suggests cars based on user-provided criteria.
- **Tavily API Integration**: Fetches real-time car data and recommendations.
- **Stateful Conversation Flow**: Uses `langgraph` to maintain a structured flow.
- **User-Friendly Design**: Designed to be intuitive and adaptable for various use cases.


## How It Works
1. The chatbot begins by greeting the user and asking for their car preferences (e.g., type, budget, features).
2. The user's inputs are processed, and a query is sent to the **Tavily API**.
3. The chatbot displays a list of recommended cars based on the user's preferences.
4. The session concludes with a friendly thank-you message.


## Prerequisites
- Python 3.8 or later
- Tavily API Key (set as `TAVILY_API_KEY` in your environment variables)
- Required Python libraries:
  - `langgraph`
  - `tavily-python`
  - `typing-extensions`
