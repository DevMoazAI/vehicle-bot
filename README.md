<!-- Banner Image -->
<p align="center">
  <img src="images/demo_screenshot.png" alt="Vehicle Diagnostic Bot UI" width="800"/>
</p>

<h1 align="center">🚘 Vehicle Diagnostic Assistant Bot</h1>

<p align="center">
  AI-powered assistant for diagnosing car, bike, and scooter issues in real-time.<br>
  Built using Gradio + LLM API with a modern, responsive UI.
</p>

---

## 🚀 Features

- Accepts user queries in English or Roman Urdu
- Diagnoses car, bike, and scooter issues based on symptoms
- Returns structured and professional vehicle advice:
  - Problem analysis
  - Possible causes
  - Immediate safety actions
  - Recommended fixes
  - Prevention tips
- Handles buying suggestions for budget vehicles
- Clean, responsive Gradio UI styled with custom CSS & Font Awesome icons

---

## 🖼️ UI Preview

<p align="center">
  <img src="images/mobile_view.png" alt="Mobile View" width="320"/>
  <img src="images/desktop_view.png" alt="Desktop View" width="500"/>
</p>

---

## 📦 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/vehicle-diagnostic-bot.git
cd vehicle-diagnostic-bot

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your .env file
# Add your LLM API key and model info:
# GROQ_API_KEY=your_key_here
# MODEL_NAME=llama3-70b-8192

# 5. Run the app
python app.py
💬 Sample Questions to Ask the Bot
"My car makes a knocking sound after 10 minutes."

"Bike is not starting in the morning, battery is fine."

"Which 125cc bike is best under 100k?"

"My scooter heats up in traffic."

"There’s a metallic sound under the car when I accelerate."

🛠️ Tech Stack
Python 3.10+

Gradio – UI framework

Font Awesome – Icons

LLM API – For natural language understanding

.env – Environment config for secrets

Responsive CSS – Mobile-friendly layout

🤝 Credits
Built by Moaz Ahmad Khalid
Inspired by real-world automotive diagnostics and AI chat UX best practices.

📄 License
This project is open-source and available under the MIT License.

---