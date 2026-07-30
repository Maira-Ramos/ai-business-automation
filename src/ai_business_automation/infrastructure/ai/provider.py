from abc import ABC, abstractmethod

from .response import AIResponse

class AIProvider(ABC):
    
    @abstractmethod
    def generate(self, prompt: str) -> AIResponse:
        """Gera uma resposta utilizando um modelo de IA."""