"""Entidades de domínio: a notícia cadastrada e sua classificação."""

from dataclasses import dataclass
from enum import Enum


class Classificacao(Enum):
    """Classificações possíveis para uma notícia analisada pelo sistema."""

    CONFIAVEL = "confiavel"
    DUVIDOSA = "duvidosa"
    FALSA = "falsa"

    @classmethod
    def a_partir_de_texto(cls, valor: str) -> "Classificacao":
        """Converte uma string informada pelo usuário em uma Classificacao.

        A comparação ignora espaços nas extremidades e diferenças de caixa,
        para tornar a entrada manual mais tolerante.

        Args:
            valor: Texto informado pelo usuário.

        Returns:
            A Classificacao correspondente ao valor.

        Raises:
            ValueError: Quando o valor não corresponde a nenhuma
                classificação válida.
        """
        normalizado = valor.strip().lower()
        for classificacao in cls:
            if classificacao.value == normalizado:
                return classificacao
        opcoes = ", ".join(c.value for c in cls)
        raise ValueError(
            f"Classificação inválida: '{valor}'. Opções válidas: {opcoes}."
        )


@dataclass(frozen=True)
class Noticia:
    """Notícia cadastrada no sistema com sua classificação atribuída.

    Atributos:
        texto: Conteúdo textual da notícia.
        classificacao: Resultado da análise (manual ou automática).
    """

    texto: str
    classificacao: Classificacao
