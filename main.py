"""
Entry point do Projeto Mensageiro.

Uso:
    python main.py "Flamengo x Palmeiras"
    python main.py  # usa o confronto padrão de exemplo
"""

import sys
from orchestrator import executar_comite_esportivo

_SEPARADOR = "=" * 60


def _imprimir_historico(historico: list[dict]) -> None:
    print(f"\n{_SEPARADOR}")
    print("       RELATÓRIO DO COMITÊ ESPORTIVO")
    print(_SEPARADOR)
    for entrada in historico:
        print(f"\n>>> {entrada['agente'].upper()}")
        print("-" * 40)
        print(entrada["mensagem"])
    print(f"\n{_SEPARADOR}\n")


def main() -> None:
    confronto = sys.argv[1] if len(sys.argv) > 1 else "Flamengo x Palmeiras"
    print(f"\nIniciando análise: {confronto}\n")
    historico = executar_comite_esportivo(confronto)
    _imprimir_historico(historico)


if __name__ == "__main__":
    main()