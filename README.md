# Tech Career Field Chatbot

## Overview
A chatbot designed to help individuals from non-tech backgrounds choose the best tech career field based on their interests and aptitudes. The chatbot utilizes a survey to gather user responses and provides personalized recommendations.

## Features
- **Survey-based Career Matching:** The chatbot guides users through a survey that collects relevant data about their interests, skills, and preferences.
- **Recommendation Engine:** Based on the survey results, the chatbot suggests the most suitable tech career paths.
- **FastAPI Microservices:** The application backend is powered by FastAPI, ensuring high performance and easy scalability.
- **Groq AI Models:** The recommendation logic is powered by Groq AI models, delivering intelligent and precise career suggestions.

- **Swarmauri SDK Integration:** The chatbot integrates the Swarmauri SDK .

## Tech Stack
- **Backend:** FastAPI
- **Machine Learning and AI:** Groq AI Models
- **SDKs** Swarmauri SDK
- **Frontend:** (to be defined but html templates for now, possibly React, Vue, or another framework)

## Future Enhancements
- **Multiple Language Support**
- **Integration with LinkedIn for career suggestions based on user profiles**
- **Real-time feedback and improvement on career suggestions through AI learning**

## How It Works
1. Users interact with the chatbot, which initiates a survey.
2. The survey responses are processed using the Swarmauri SDK.
3. FastAPI microservices handle requests and pass data to Groq AI models.
4. Based on the analysis, the chatbot recommends career fields in tech that match the user's profile.

## Goals
- Help people with non-technical backgrounds discover tech career opportunities.
- Provide accurate and personalized career advice powered by AI.
