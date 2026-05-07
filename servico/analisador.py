"""Análise automática de notícias com base em indícios de baixa qualidade.

A heurística reproduz o critério do código original, agora com nomes claros,
constantes e responsabilidades bem definidas. Cada indício soma um ponto e a
pontuação final determina a classificação.
"""

from modelo.noticia import Classificacao

# Termo que, presente no texto, é interpretado como declaração de fonte.
PALAVRA_FONTE = "FONTE"

# Marcadores de linguagem sensacionalista (mantidos como no código original).
MARCADOR_EXCLAMACAO = "!!!"
MARCADOR_URGENCIA = "URGENTE"

# Tamanho mínimo (em caracteres) considerado adequado para uma notícia.
TAMANHO_MINIMO_TEXTO = 10

# Limites de pontuação usados na decisão final.
LIMITE_CONFIAVEL = 0
LIMITE_DUVIDOSA = 1


def classificar_noticia(texto: str) -> Classificacao:
    """Classifica uma notícia avaliando indícios de baixa qualidade.

    Args:
        texto: Conteúdo da notícia a ser analisada.

    Returns:
        A classificação resultante: CONFIAVEL, DUVIDOSA ou FALSA.

    Raises:
        ValueError: Quando o texto é vazio ou contém apenas espaços.
    """
    if texto is None or not texto.strip():
        raise ValueError("Texto da notícia não pode ser vazio.")

    indicios = _contar_indicios(texto)

    if indicios <= LIMITE_CONFIAVEL:
        return Classificacao.CONFIAVEL
    if indicios <= LIMITE_DUVIDOSA:
        return Classificacao.DUVIDOSA
    return Classificacao.FALSA


def _contar_indicios(texto: str) -> int:
    """Conta quantos indícios de baixa qualidade o texto apresenta."""
    indicios = 0
    if PALAVRA_FONTE not in texto:
        indicios += 1
    if MARCADOR_EXCLAMACAO in texto:
        indicios += 1
    if MARCADOR_URGENCIA in texto:
        indicios += 1
    if len(texto) < TAMANHO_MINIMO_TEXTO:
        indicios += 1
    return indicios
