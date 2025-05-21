# 🎥➡️📝 Video2Blog: AI-Driven Video-to-Blog Converter

**Video2Blog** is a multi-agent AI system built on **CrewAI** that transforms any public video URL into a polished, SEO-optimized blog post. It’s perfect for content creators, marketers, and educators who want to repurpose video content into written format with minimal effort.

---

## 🚀 How It Works

1. **User Input**  
   - Provide a video URL (e.g., YouTube).

2. **Agent 1 – Blog Researcher**  
   - Uses `crewai_tools.youtubechannelsearchtools` to fetch video metadata (title, description, tags).  
   - Extracts key topics, timestamps, and external references.  
   - Outputs an **outline** and **research notes**.

3. **Agent 2 – Blog Writer**  
   - Takes the outline/notes from Agent 1.  
   - Leverages a CrewAI-powered LLM to draft a full **blog post**:  
     - Engaging introduction  
     - Sectioned body with headings  
     - Conclusion and call-to-action  
   - Ensures SEO best practices (keywords, meta description).

4. **Behind the Scenes**  
   - Both agents are driven by pre-built LLM “brains” via CrewAI.  
   - Agents communicate sequentially within a CrewAI orchestration pipeline.

---

## 🔧 Tech Stack & Tools

| Component         | Technology / Library               |
|-------------------|------------------------------------|
| Orchestration     | CrewAI                             |
| Agents’ Brains    | OpenAI-style LLMs via CrewAI APIs  |
| Video Metadata    | `crewai_tools.youtubechannelsearchtools` |
| Web Framework     | (Optional) Flask / Streamlit       |
| Environment       | Python 3.10+, `venv`               |

---

## 📋 Prerequisites
1. **Clone this repo**  
   ```bash
   git clone https://github.com/TSujal/Video2Blog.git
   cd Video2Blog

2. **Create & activate virtual env**
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. **Install Dependencies**
pip install -r requirements.txt

4) **Usage**
# From project root
streamlit run app.py     


## 🤝 Contributing

Pull requests are welcome. Please open an issue first to discuss what you would like to change or add.

---

## 📫 Contact

Built by **Sujal Thakkar**  
📧 thakkar.su@northeastern.edu  
🔗 [LinkedIn](https://www.linkedin.com/in/sujal-thakkar/) • [GitHub](https://github.com/TSujal)

---
