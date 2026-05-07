"""Interface de linha de comando do Sistema de Monitoramento de Fake News.

Concentra a interação com o usuário: leitura de entradas, exibição do menu e
formatação da saída. A camada de apresentação não conhece detalhes da
classificação nem do armazenamento, delegando-os aos serviços.
"""

from typing import Callable, Dict

from modelo.noticia import Classificacao, Noticia
from servico.analisador import classificar_noticia
from servico.repositorio import RepositorioNoticias

SEPARADOR = "-" * 30

OPCAO_ADICIONAR_MANUAL = "1"
OPCAO_ADICIONAR_AUTOMATICO = "2"
OPCAO_LISTAR = "3"
OPCAO_SAIR = "4"


def _ler_texto_obrigatorio(prompt: str) -> str:
    """Lê do teclado um texto não-vazio, repetindo o pedido se necessário."""
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Entrada vazia. Por favor, digite algum texto.")


def _ler_classificacao_opcional() -> Classificacao:
    """Lê a classificação informada manualmente, com fallback para DUVIDOSA.

    Caso o usuário pressione Enter sem digitar nada, retorna DUVIDOSA,
    preservando o comportamento do código original.
    """
    entrada = input(
        "Digite a classificação (confiavel/duvidosa/falsa) "
        "[Enter = duvidosa]: "
    ).strip()
    if not entrada:
        return Classificacao.DUVIDOSA
    return Classificacao.a_partir_de_texto(entrada)


def adicionar_manualmente(repositorio: RepositorioNoticias) -> None:
    """Cadastra uma notícia informando texto e classificação manualmente."""
    texto = _ler_texto_obrigatorio("Digite o texto: ")
    try:
        classificacao = _ler_classificacao_opcional()
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    repositorio.adicionar(Noticia(texto=texto, classificacao=classificacao))
    print(f"Notícia adicionada como '{classificacao.value}'.")


def adicionar_automaticamente(repositorio: RepositorioNoticias) -> None:
    """Cadastra uma notícia classificada automaticamente pelo analisador."""
    texto = _ler_texto_obrigatorio("Digite o texto: ")
    classificacao = classificar_noticia(texto)
    repositorio.adicionar(Noticia(texto=texto, classificacao=classificacao))
    print(f"Notícia adicionada como '{classificacao.value}'.")


def listar(repositorio: RepositorioNoticias) -> None:
    """Imprime todas as notícias cadastradas no repositório."""
    if repositorio.esta_vazio():
        print("Nenhuma notícia cadastrada ainda.")
        return

    for noticia in repositorio.listar():
        print(f"Texto: {noticia.texto}")
        print(f"Classificacao: {noticia.classificacao.value}")
        print(SEPARADOR)


def _exibir_menu() -> None:
    """Imprime o menu principal de opções."""
    print()
    print("=== Sistema de Monitoramento de Fake News ===")
    print(f"{OPCAO_ADICIONAR_MANUAL} - adicionar manual")
    print(f"{OPCAO_ADICIONAR_AUTOMATICO} - adicionar automatico")
    print(f"{OPCAO_LISTAR} - listar")
    print(f"{OPCAO_SAIR} - sair")


# Mapeamento opção -> ação evita uma cadeia longa de if/elif.
AcaoMenu = Callable[[RepositorioNoticias], None]
ACOES_MENU: Dict[str, AcaoMenu] = {
    OPCAO_ADICIONAR_MANUAL: adicionar_manualmente,
    OPCAO_ADICIONAR_AUTOMATICO: adicionar_automaticamente,
    OPCAO_LISTAR: listar,
}


def executar() -> None:
    """Inicia o loop principal da interface de linha de comando."""
    repositorio = RepositorioNoticias()

    while True:
        _exibir_menu()
        try:
            opcao = input("opcao: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if opcao == OPCAO_SAIR:
            break

        acao = ACOES_MENU.get(opcao)
        if acao is None:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")
            continue

        try:
            acao(repositorio)
        except ValueError as erro:
            print(f"Erro: {erro}")
        except (EOFError, KeyboardInterrupt):
            print()
            break

    print("Encerrando o sistema.")
