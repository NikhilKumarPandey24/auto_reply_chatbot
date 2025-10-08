import google.generativeai as genai

genai.configure(api_key="")

# Debug list models (optional - comment out after verification)
# for m in genai.list_models():
#     print("-", m.name)

# Use a valid model from the available list
# Options: gemini-2.0-flash, gemini-2.5-flash, gemini-flash-latest
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Reply like Nikhil, an Indian coder mixing Hindi and English casually."
response = model.generate_content(prompt)

print(response.text)
