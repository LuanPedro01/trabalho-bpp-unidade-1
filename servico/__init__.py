"""Pacote com a lógica de negócio do sistema (análise e armazenamento)."""

from servico.analisador import classificar_noticia
from servico.repositorio import RepositorioNoticias

__all__ = ["classificar_noticia", "RepositorioNoticias"]
