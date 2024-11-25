import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from utils import strip_comments

class LLM:
    def __init__(self, 
                 prompt_template: str,
                 model: str = "gpt-4o",
                 temperature: float = 0.4,
                 system_message: str = "You are an expert programming instructor who grades Python assignments.",
                 parser=None):
        """
        Initialize LLM with configuration and prompt template.
        
        Args:
            prompt_template: The template string to be used for prompts
            model: The OpenAI model to use
            temperature: The temperature parameter for generation
            system_message: The system message to set the AI's role
        """
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
            
        # Initialize OpenAI client
        self.client = AsyncOpenAI(api_key=api_key)
        
        # Store configuration
        self.prompt_template = prompt_template
        self.model = model
        self.temperature = temperature
        self.system_message = system_message
        self.parser = parser
        
    def prepare_prompt(self, solution: str) -> str:
        """
        Prepare the prompt using the template and solution.
        
        Args:
            solution: The solution to be inserted into the template
            
        Returns:
            str: The formatted prompt
        """
        return self.prompt_template.format(solution=solution)
        
    async def get_response(self, filename: str) -> str:
        """
        Get response from the LLM for a given solution.
        
        Args:
            filename: The path for the file
            
        Returns:
            str: The LLM's response
        """
        solution = strip_comments(filename)
        prompt = self.prepare_prompt(solution)
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature
        )
            
        if self.parser is not None:
            return self.parser(response.choices[0].message.content)
        return response.choices[0].message.content
        
    async def get_response_with_prompt(self, prompt: str) -> str:
        """
        Get response from the LLM for a custom prompt.
        
        Args:
            prompt: The custom prompt to send
            
        Returns:
            str: The LLM's response
        """
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature
        )
        if self.parser is not None:
            return self.parser(response.choices[0].message.content)
        return response.choices[0].message.content