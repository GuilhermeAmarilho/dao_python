from datetime import datetime
from autor import Autor
class Trabalho:
    def __init__(self,conteudo,nota,titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._dataEntrega = None
        self._titulo = titulo
        self._data_atu = None
        self._codigo = None
        self._listaAutores = []

    def entregaTrabalho(self):
        self._dataEntrega = datetime.now()
    
    def _get_autores(self):
        return self._listaAutores
    
    def _set_autores(self,autor):
        self._listaAutores = autor

    def addAutor(self,autor):
        self._listaAutores.append(autor)

    def _get_conteudo(self):
        return self._conteudo

    def _set_conteudo(self,conteudo):
        self._conteudo = conteudo

    def _get_nota(self):
        return self._nota

    def _set_nota(self,nota):
        self._nota = nota

    def _get_data_entrega(self):
        return self._dataEntrega

    def _set_data_entrega(self,dataentrega):
        self._dataEntrega = dataentrega

    def _get_titulo(self):
        return self._titulo

    def _set_titulo(self,titulo):
        self._titulo = titulo
    
    def _get_dataAtu(self):
        return self._data_atu

    def _set_dataAtu(self,data):
        self._data_atu = data

    def _get_codigo(self):
        return self._codigo

    def _set_codigo(self,codigo):
        self._codigo = codigo

    def __str__(self):
        vet = []
        for a in self._listaAutores:
            print(a)
            autor = (a.nome,a.email)
            vet.append(autor)

        return "Conteudo: {}, Nota: {}, Data Entrega: {}, Titulo: {}, Data Atualização: {}, Codigo:{}, Autor(es):{} ".format(self._conteudo,self._nota, self._dataEntrega,self._titulo, self._data_atu,self._codigo,vet)
    

    conteudo = property(_get_conteudo, _set_conteudo)
    nota = property(_get_nota,_set_nota)
    dataentrega = property(_get_data_entrega,_set_data_entrega)
    titulo = property(_get_titulo,_set_titulo)
    data = property(_get_dataAtu,_set_dataAtu)
    codigo = property(_get_codigo,_set_codigo)
    autores = property(_get_autores,_set_autores)

