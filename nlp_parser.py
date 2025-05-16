import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_intent(user_input):
    prompt = f"""
You are a to-do list assistant. Convert this input into intent.

User: "{user_input}"

Return JSON:
{{
  "intent": "add_task/show_tasks/mark_done/delete_task",
  "task": "...",
  "time": "...",
  "index": ...
}}
Only include relevant keys.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return eval(response['choices'][0]['message']['content'])  # or use ast.literal_eval
