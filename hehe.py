iclient = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "$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"
)

completion = client.chat.completions.create(
  model="snowflake/arctic",
  messages=[{"role":"user","content":""}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

