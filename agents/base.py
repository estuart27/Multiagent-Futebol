import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


class SportsAgent:
    """Classe base para todos os agentes do comitê esportivo."""

    def __init__(self, name: str, role: str, system_prompt: str, model_name: str = "gemini-2.0-flash"):
        self.name = name
        self.role = role
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_prompt,
        )

    def analyze(self, input_context: str) -> str:
        """Envia o contexto para o agente e retorna a resposta."""
        try:
            response = self.model.generate_content(input_context)
            return response.text
        except Exception as e:
            return f"[Erro no agente {self.name}]: {str(e)}"

    def __repr__(self) -> str:
        return f"<SportsAgent name={self.name!r} role={self.role!r}>"