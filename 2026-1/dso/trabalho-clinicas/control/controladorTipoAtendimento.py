from model.tipo_atendimento import TipoAtendimento
from Exceptions.tipoAtendimentoException import TipoAtendimentoException
from DAOs.tipo_atendimento_dao import TipoAtendimentoDAO

class ControladorTipoAtendimento:
    def __init__(self):
        self.__tipo_dao = TipoAtendimentoDAO()

    def cadastrar(self, nome, descricao, valor_base):
        if self.buscar(nome) is not None:
            raise TipoAtendimentoException(f"Já existe um tipo de atendimento com o nome '{nome}'.")
        
        tipo = TipoAtendimento(nome, descricao, valor_base)
        self.__tipo_dao.add(tipo)

    def remover(self, nome):
        tipo = self.buscar(nome)
        if tipo is None:
            raise TipoAtendimentoException(f"Tipo de atendimento '{nome}' não encontrado.")
        self.__tipo_dao.remove(nome)

    def alterar(self, nome, novo_nome=None, descricao=None, valor_base=None):
        tipo = self.buscar(nome)
        if tipo is None:
            raise TipoAtendimentoException(f"Tipo de atendimento '{nome}' não encontrado.")
        
        mudou_chave = (novo_nome is not None and novo_nome != nome)
        if mudou_chave:
            self.__tipo_dao.remove(nome)
            
        if novo_nome:
            tipo.nome = novo_nome
        if descricao:
            tipo.descricao = descricao
        if valor_base is not None:
            tipo.atualizar_valor_base(valor_base)
            
        if mudou_chave:
            self.__tipo_dao.add(tipo)
        else:
            self.__tipo_dao.update(tipo)

    def listar(self):
        tipos = self.__tipo_dao.get_all()
        if not tipos:
            raise TipoAtendimentoException("Nenhum tipo de atendimento cadastrado.")
        
        return [
            {
                "nome": t.nome,
                "descricao": t.descricao,
                "valor_base": t.valor_base
            }
            for t in tipos
        ]

    def buscar(self, nome):
        return self.__tipo_dao.get(nome)
