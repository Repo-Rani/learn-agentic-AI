from agents import Runner, RunConfig, Agent, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY= os.environ.get("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    # model="openai/gpt-3.5-turbo",
    # model="mistralai/mistral-7b-instruct",
    model="meta-llama/llama-3-8b-instruct",
    openai_client=client
)

config = RunConfig(
    model=model,
    tracing_disabled=True,
    model_provider=client)

agent = Agent(
    name="AI Assistant",
    instructions="You're AI Assistant!",
)

user_input = input("Enter Here your questions!")
result = Runner.run_sync(agent, user_input, run_config=config)
print(result.final_output)