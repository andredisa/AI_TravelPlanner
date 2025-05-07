# 🌍✈️ AI Travel Planner

>**Plan your next trip smartly with the AI Travel Planner!**  
An interactive Streamlit app that leverages LLMs (GPT-4o or Llama 3.2) and search engines to create personalized travel itineraries.

---

## 🚀 Features

- 🧠 **AI Researcher**: Finds top-rated activities and accommodations
- 📅 **AI Planner**: Builds a detailed, customized itinerary
- 🔍 **Web Search Integration**: Powered by [SerpAPI](https://serpapi.com/)
- 🧩 Support for **Llama 3.2 (Ollama)** and **GPT-4o (OpenAI)**

---

## 🗂️ Project Structure

```bash
AI_WebScraper/
├── agents/
│   ├── gpt_agent.py      # Agent logic using GPT-4o
│   └── llama_agent.py    # Agent logic using Llama 3.2
├── app/
│   ├── main_gpt.py       # Streamlit interface with GPT-4o
│   └── main_llama.py     # Streamlit interface with Llama
├── requirements.txt      # Dependencies
└── README.md
```

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/andredisa/AI_TravelPlanner.git
cd AI_TravelPlanner
```

2. **Install the requirements:**

```bash
pip install -r requirements.txt
```

3. **Launch the app with your preferred model:**
> ▶️ GPT-4o:
```bash
streamlit run app/main_gpt.py
```

>🦙 Llama 3.2 (Ollama):
```bash
streamlit run app/main_llama.py
```

---

## 🔑 Required API Keys

| Service  | API Key Name      | Where to Get It                     |
|----------|-------------------|-------------------------------------|
| OpenAI   | `OPENAI_API_KEY`  | [openai.com](https://openai.com)    |
| SerpAPI  | `SERP_API_KEY`    | [serpapi.com](https://serpapi.com)  |

> 🛡️ API keys are entered securely via the Streamlit interface. No keys are stored locally.

---

## 💡 Example Use Case
🔎 Enter your destination and number of days  
🧳 Let the AI agent research activities and places  
📜 Receive a tailored itinerary with tips, suggestions, and details

---

## 🎯 Goal
A travel assistant powered by AI that helps you from the initial research all the way to full itinerary planning, using generative intelligence and real-world web data.

---

## 📌 TODO / Future Ideas

- 🌐 Export trip itineraries as PDF
- 🗺️ Interactive map with trip route and stops
- 🔁 User memory and saved trips functionality
- 📆 Calendar integration (Google Calendar, iCal)

---

## ✨ Contributing

🎉 **Contributions are more than welcome!**

If you find a bug 🐞, have a feature request ✨, or want to improve the code 💻:

- Open an [Issue](https://github.com/andredisa/AI_TravelPlanner/issues)  
- Submit a [Pull Request](https://github.com/andredisa/AI_TravelPlanner/pulls) 🚀  

>💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

Let’s build this together!

---

## 📜 License

📄 This project is released under the **MIT License**.  
Please refer to the [LICENSE](LICENSE) file for full details.

---

### 🧑‍💻✨ Happy coding
