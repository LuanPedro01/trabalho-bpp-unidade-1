"""Ponto de entrada do Sistema de Monitoramento de Fake News.

Executa a interface de linha de comando definida em ``interface.cli``.
Esse arquivo intencionalmente concentra apenas a inicialização, deixando
as responsabilidades de domínio, lógica e apresentação em seus pacotes.
"""

from interface.cli import executar


if __name__ == "__main__":
    executar()
