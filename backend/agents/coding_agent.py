import openai

class CodingAgent:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.model = "code-davinci-002"  # OpenAI's Codex model optimized for code generation

    def perform_task(self, document_content, question):
        prompt = (
            f"Document Content: {document_content}\n\n"
            f"Question: {question}\n\n"
            "Develop the necessary code to address the question based on the document content:"
        )
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=1500
        )
        return response.choices[0].text.strip()
