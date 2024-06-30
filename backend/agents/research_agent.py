import openai

class ResearchAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def perform_task(self, document_content, question):
        prompt = f"Perform research and gather more information based on the following content and question:\n\nContent: {document_content}\n\nQuestion: {question}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500
        )
        return response.choices[0].text.strip()
