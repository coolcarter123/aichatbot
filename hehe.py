import openai
client = openai.OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key="YOUR_NVIDIA_API_KEY"
)
chat_completion = client.chat.completions.create(
model="mistralai/mixtral-8x7b-instruct-v0.1",
messages=[{"role" : "user" , "content" : "Write me a love song" }],
temperature=0.7
)
