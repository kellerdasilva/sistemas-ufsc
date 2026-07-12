"""
Classe base abstrata para Data Access Objects (DAOs) do sistema.

Este módulo implementa o padrão DAO, abstraindo a persistência de dados usando
pickle para serialização em arquivos. Todos os DAOs do sistema herdam desta
classe, que fornece operações CRUD básicas (Create, Read, Update, Delete) e
gerencia automaticamente o carregamento e salvamento dos dados.

A classe mantém um cache em memória (__cache) que é sincronizado automaticamente
com o arquivo de persistência sempre que há modificações. O carregamento inicial
ocorre no construtor, e se o arquivo não existir, um arquivo vazio é criado.

Responsabilidades:
- Gerenciar o ciclo de vida dos dados (carregar ao iniciar, salvar ao modificar)
- Fornecer interface unificada para operações de persistência
- Tratar erros de I/O e validações básicas de chaves
"""

import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        """
        Inicializa o DAO com o caminho do arquivo de persistência. Carrega
        automaticamente os dados existentes ou cria um arquivo vazio se não
        existir. O cache em memória é populado durante esta inicialização.
        """
        self.__datasource = datasource
        self.__cache = {}  # Cache em memória sincronizado com o arquivo
        try:
            self.__load()
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            self.__cache = {}
            self.__dump()

    def __dump(self):
        """
        Serializa o cache em memória para o arquivo usando pickle. Chamado
        automaticamente após cada operação de modificação (add, update, remove).
        """
        with open(self.__datasource, 'wb') as arquivo:
            pickle.dump(self.__cache, arquivo)

    def __load(self):
        """
        Carrega os dados do arquivo para o cache em memória usando pickle.
        Chamado automaticamente durante a inicialização do DAO.
        """
        with open(self.__datasource, 'rb') as arquivo:
            self.__cache = pickle.load(arquivo)

    def add(self, key, obj):
        """
        Adiciona um novo objeto ao cache usando a chave fornecida e persiste
        imediatamente no arquivo. Se já existir um objeto com a mesma chave,
        ele será sobrescrito.
        """
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        """
        Atualiza um objeto existente no cache. Lança KeyError se a chave não
        existir, garantindo que apenas registros existentes sejam modificados.
        """
        try:
            if self.__cache[key] is not None:
                self.__cache[key] = obj
                self.__dump()
        except KeyError:
            raise KeyError(
                f"Não existe registro com chave '{key}' para atualizar em {self.__datasource}.")

    def get(self, key):
        """
        Recupera um objeto do cache pela chave. Retorna None se a chave não
        existir, permitindo verificação de existência sem exceções.
        """
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        """
        Remove um objeto do cache pela chave e persiste a alteração. Lança
        KeyError se a chave não existir, garantindo que apenas registros
        existentes sejam removidos.
        """
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            raise KeyError(
                f"Não existe registro com chave '{key}' para remover em {self.__datasource}.")

    def get_all(self):
        """
        Retorna todos os valores armazenados no cache como uma view. Útil
        para operações que precisam iterar sobre todos os registros sem
        conhecer as chaves específicas.
        """
        return self.__cache.values()