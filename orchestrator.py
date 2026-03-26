"""
Orquestrador do Comitê Esportivo.

Coordena os quatro agentes em sequência e devolve o histórico
completo da análise como uma lista de dicionários.
"""

from server import data_engineer, oddsmaker, scout, tipster

# ── Instâncias únicas (criadas uma vez ao importar o módulo) ──────────────────
_agente_dados = data_engineer.create()
_agente_scout = scout.create()
_agente_oddsmaker = oddsmaker.create()
_agente_tipster = tipster.create()


def executar_comite_esportivo(confronto: str) -> list[dict]:
    """
    Orquestra os quatro agentes e retorna o histórico completo.

    Args:
        confronto: String descrevendo o jogo, ex: "Flamengo x Palmeiras".

    Returns:
        Lista de dicts com chaves 'agente' e 'mensagem'.
    """
    historico: list[dict] = []

    # 1 — Engenheiro de Dados
    print(f"[1/4] {_agente_dados.name} analisando...")
    dados_out = _agente_dados.analyze(f"Levante os dados para o jogo: {confronto}")
    historico.append({"agente": _agente_dados.name, "mensagem": dados_out})

    # 2 — Scout Tático
    print(f"[2/4] {_agente_scout.name} analisando...")
    scout_out = _agente_scout.analyze(
        f"Confronto: {confronto}\nDados levantados:\n{dados_out}\nFaça sua análise tática."
    )
    historico.append({"agente": _agente_scout.name, "mensagem": scout_out})

    # 3 — Oddsmaker
    print(f"[3/4] {_agente_oddsmaker.name} analisando...")
    odds_out = _agente_oddsmaker.analyze(
        f"Confronto: {confronto}\n"
        f"Dados:\n{dados_out}\n"
        f"Análise Tática:\n{scout_out}\n"
        "Faça sua precificação e encontre valor."
    )
    historico.append({"agente": _agente_oddsmaker.name, "mensagem": odds_out})

    # 4 — Tipster Principal
    print(f"[4/4] {_agente_tipster.name} deliberando...")
    tipster_out = _agente_tipster.analyze(
        f"Confronto: {confronto}\n"
        f"Dados:\n{dados_out}\n"
        f"Tática:\n{scout_out}\n"
        f"Mercado:\n{odds_out}\n"
        "Dê o veredito final e a tip."
    )
    historico.append({"agente": _agente_tipster.name, "mensagem": tipster_out})

    return historico