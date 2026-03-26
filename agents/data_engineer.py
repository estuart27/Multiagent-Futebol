from .base import SportsAgent

_SYSTEM_PROMPT = """Você é um Engenheiro e Analista de Dados Esportivos.
Sua função: Receber o nome de um confronto e levantar dados estatísticos recentes
(média de gols, posse de bola, desfalques importantes, histórico de confrontos).
Como este é um MVP, você pode simular dados realistas caso não tenha o dado exato
em tempo real, mas deve estruturá-los de forma extremamente analítica em formato
de tópicos ou JSON para o próximo agente."""


def create() -> SportsAgent:
    """
    O Engenheiro/Analista de Dados - É o motor da operação. Responsável por consumir APIs de estatísticas,
    criar scripts de automação (em Python ou JavaScript, por exemplo) e estruturar bancos de dados.
    Ele cruza métricas como Expected Goals (xG), posse de bola em áreas perigosas e histórico de confrontos para criar modelos preditivos 
    e identificar padrões invisíveis a olho nu
    """
    return SportsAgent(
        name="Engenheiro de Dados",
        role="Dados",
        system_prompt=_SYSTEM_PROMPT,
    )