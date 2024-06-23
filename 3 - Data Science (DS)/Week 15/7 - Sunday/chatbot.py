import argparse
import logging
import sys
from typing import List, Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ImprovedHuggingFaceChatbot:
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium", device: str = "cpu"):
        self.device = device
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.logger = self._setup_logger()
        self.chat_history_ids = None

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        return logger

    def load_model(self) -> None:
        try:
            self.logger.info(f"Loading model: {self.model_name}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)
            self.logger.info("Model loaded successfully")
        except Exception as e:
            self.logger.error(f"Error loading model: {str(e)}")
            raise

    def generate_response(self, input_text: str, max_length: int = 1000) -> str:
        try:
            # Encode the new user input, add the eos_token and return a tensor in Pytorch
            new_user_input_ids = self.tokenizer.encode(input_text + self.tokenizer.eos_token, return_tensors='pt').to(self.device)

            # Append the new user input tokens to the chat history
            bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1) if self.chat_history_ids is not None else new_user_input_ids

            # Generate a response while limiting the total chat history to 1000 tokens
            self.chat_history_ids = self.model.generate(
                bot_input_ids, 
                max_length=max_length,
                pad_token_id=self.tokenizer.eos_token_id,  
                no_repeat_ngram_size=3,       
                do_sample=True, 
                top_k=100, 
                top_p=0.7,
                temperature=0.8
            )
            
            # Decode and return the model's response
            response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            return response
        except Exception as e:
            self.logger.error(f"Error generating response: {str(e)}")
            return "I'm sorry, I encountered an error while generating a response."

    def chat(self) -> None:
        self.logger.info("Starting chat session. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                self.logger.info("Ending chat session.")
                break
            response = self.generate_response(user_input)
            print(f"Chatbot: {response}")

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Improved Hugging Face Chatbot")
    parser.add_argument("--model", type=str, default="microsoft/DialoGPT-medium", help="Model name to use (default: microsoft/DialoGPT-medium)")
    parser.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda"], help="Device to use (default: cpu)")
    return parser.parse_args()

def main() -> None:
    args = parse_arguments()
    chatbot = ImprovedHuggingFaceChatbot(model_name=args.model, device=args.device)
    
    try:
        chatbot.load_model()
        chatbot.chat()
    except KeyboardInterrupt:
        chatbot.logger.info("Chat session interrupted by user.")
    except Exception as e:
        chatbot.logger.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()