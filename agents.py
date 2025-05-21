from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set LITELLM_API_KEY globally so LiteLLM (used internally by CrewAI) picks it up
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["LITELLM_API_KEY"] = groq_api_key

# Set model name with provider format for LiteLLM compatibility
model_name = "groq/llama3-70b-8192"

# ✅ Blog Researcher Agent
blog_researcher = Agent(
    role="Blog Researcher From YouTube Videos",
    goal="Get the relevant video content for the topic {topic} from the YouTube channel",
    verbose=True,
    memory=True,
    tools=[yt_tool],  # Researcher does not use tools directly
    llm=model_name,
    allow_delegation=True,
    backstory=(
        "Expert in understanding videos on AI, Data Science, Machine Learning, and Gen AI. "
        "Provides insightful summaries and extracts key points from video content."
    )
)

# ✅ Blog Writer Agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from the YouTube channel",
    verbose=True,
    memory=True,
    tools=[yt_tool],  # Uses the YouTube tool to get content
    llm=model_name,
    allow_delegation=False,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, "
        "bringing new discoveries to light in an accessible and compelling manner."
    )
)
