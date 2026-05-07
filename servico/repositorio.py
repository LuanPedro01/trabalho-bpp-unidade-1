"""Repositório em memória das notícias cadastradas no sistema."""

from typing import List

from modelo.noticia import Noticia


class RepositorioNoticias:
    """Armazena, em memória, as notícias adicionadas pelo usuário.

    Encapsula o acesso à coleção interna para que as demais camadas não
    dependam diretamente de uma estrutura de dados específica.
    """

    def __init__(self) -> None:
        self._noticias: List[Noticia] = []

    def adicionar(self, noticia: Noticia) -> None:
        """Adiciona uma notícia ao repositório.

        Raises:
            TypeError: Se o objeto recebido não for uma Noticia.
        """
        if not isinstance(noticia, Noticia):
            raise TypeError("Apenas instâncias de Noticia podem ser adicionadas.")
        self._noticias.append(noticia)

    def listar(self) -> List[Noticia]:
        """Retorna uma cópia da lista de notícias cadastradas."""
        return list(self._noticias)

    def esta_vazio(self) -> bool:
        """Indica se ainda não há notícias cadastradas."""
        return not self._noticias

    def quantidade(self) -> int:
        """Quantidade de notícias atualmente armazenadas."""
        return len(self._noticias)
