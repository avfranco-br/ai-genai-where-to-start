# --- Gaia Agent Definition ---
from smolagents import CodeAgent, DuckDuckGoSearchTool, VisitWebpageTool
from tools.gaiatool import fetch_questions
from smolagents import LiteLLMModel, InferenceClientModel
import os
from smolagents import HfApiModel
#from smolagents import OpenAIServerModel #uncoment in case of using OpenAI API, or Hugging Face API

# ----- THIS IS WERE YOU CAN BUILD WHAT YOU WANT ------
# (Keep Constants as is)
# --- Constants ---
DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"

api_url = DEFAULT_API_URL

class GaiaAgent:
    def __init__(self):
        print("GaiaAgent initialized.")

        self.questions_url = f"{api_url}/questions"

        if not os.getenv("SPACE_ID"):
            # Initialize local model
            model_id = "ollama/qwen2.5:14b"
            self.model = LiteLLMModel(
                model_id=model_id, 
                api_base="http://localhost:11434"
                #api_key=os.getenv("GEMINI_API_KEY")
            )
        else: # Run with Hugging Face Inference API
            #model_id = "meta-llama/Llama-3.3-70B-Instruct"
            #self.model = InferenceClientModel(model_id=model_id)

            self.model = HfApiModel(
                provider="novita", 
                temperature=0.0,
                api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
            )

            """self.model = OpenAIServerModel(
                model_id="gpt-4o-mini",
                api_base="https://api.openai.com/v1",
                api_key=os.environ["OPENAI_API_KEY"],
                temperature=0.0
            )"""

        search= DuckDuckGoSearchTool()
        web_browser = VisitWebpageTool()

        self.agent = CodeAgent(
            model=self.model,
            tools=[search, web_browser],
            add_base_tools=True,
            additional_authorized_imports=["pandas", "re"]
        )

        system_prompt = """You are a general AI assistant. I will ask you a question. Report your thoughts, and
finish your answer with the following template: FINAL ANSWER: [YOUR FINAL ANSWER].
YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated
list of numbers and/or strings. If you are asked for a number, don’t use comma to write your number neither use units such as $ or
percent sign unless specified otherwise. If you are asked for a string, don’t use articles, neither abbreviations (e.g. for cities), and write the
digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element
to be put in the list is a number or a string."""

        self.agent.prompt_templates["system_prompt"] = self.agent.prompt_templates["system_prompt"] + system_prompt

        self.questions_data = fetch_questions(self.questions_url)


    def get_questions(self):
        return self.questions_data

    def __call__(self, question: str) -> str:
        print(f"Agent received question (first 50 chars): {question[:50]}...")
        answer = self.agent.run(question)
        print(f"Agent returning answer: {answer}")
        return answer
