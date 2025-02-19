import openai
import json
import os
from typing import List, Dict
from config import OPENAI_API_KEY

# Ensure to set your OpenAI API key
openai.api_key = OPENAI_API_KEY  # Replace with your actual OpenAI API key

class  LLMService:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def generate_vocab(self, prompt: str) -> Dict:
        """
        Calls OpenAI's GPT API to generate vocabulary based on the prompt.

        Args:
            prompt (str): The prompt provided by the user to generate vocabulary.

        Returns:
            dict: A JSON-like dictionary containing the generated vocabulary.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # Assuming the response contains the generated vocabulary in a specific format
            generated_text = response['choices'][0]['message']['content']
            # You can choose to parse the generated text into a structured format here
            # For simplicity, we'll just return the raw text as is
            return {"vocab": generated_text}  # Return as a dictionary
        except Exception as e:
            print(f"Error generating vocabulary: {e}")
            return {}

    def store_vocab_json(self, vocab_data: Dict, file_path: str = 'vocab.json'):
        """
        Store the generated vocabulary JSON data in a file.

        Args:
            vocab_data (dict): The vocabulary data to store.
            file_path (str): The path to the JSON file where data should be saved.
        """
        try:
            # Ensure the parent directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Writing to the JSON file
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(vocab_data, f, ensure_ascii=False, indent=4)
            print(f"Vocabulary stored successfully at {file_path}")
        except Exception as e:
            print(f"Error storing vocabulary: {e}")


llm_service = LLMService()

# Example usage of the LLMService
# if __name__ == "__main__":
#     llm_service = LLMService()

#     # Example prompt
#     prompt = "Generate a list of 10 English words with their Japanese translations and example sentences."

#     # Generate vocabulary from OpenAI GPT API
#     vocab_data = llm_service.generate_vocab(prompt)

#     # If data is successfully generated, store it
#     if vocab_data:
#         llm_service.store_vocab_json(vocab_data)
