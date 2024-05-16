import openai as ai

# Set your API key
ai.api_key = ""

prompt = """
Classify the following animals into categories, negative, positive, neutral:
1. Unbelievably good! 
2. Shoes fell apart on the second use. 
3. The shoes look nice, but hey aren't very comfortable. 
4. Can't wait to show them off! 
"""



# Create a request to the Completion endpoint
response = ai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=100
)

print(response['choices'][0]['text'])