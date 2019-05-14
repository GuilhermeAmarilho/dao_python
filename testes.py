import psycopg2
from trabalhodao import trabalhoDao
from trabalho import Trabalho
from autor import Autor
from autordao import autorDao
if __name__ == '__main__':
    #TESTES DE AUTOR
    autordao = autorDao()
    autor = Autor('Vinicius De Freitas','viniciusdefreitas@gmail.com')
    autor1 = Autor('Vinicius Goularte','viniciusgoularte@gmail.com')
    #try:
        #autordao.salvar(autor)
        #autordao.salvar(autor1)
    #except psycopg2.errors.UniqueViolation:
        #print("Email duplicado")
    #try:
        #autorbusca = autordao.buscar(1)
        #autorbusca.email = "viniciusfreitas@hotmail.com"
        #autordao.salvar(autorbusca)
    #except IndexError:
        #print("Código errado ou não existe no banco")
    #except psycopg2.errors.InvalidTextRepresentation:
        #print("O código não pode ser string")
    #autordao.deletar(1)
    #lista_autor = autordao.listar()
    #for a in lista_autor:
        #print(a)
    #print(autordao.buscar(2))
    #TESTES DE TRABALHO
    trabalhodao = trabalhoDao()
    #trabalho = Trabalho('Trabalho de desenvolvimento de sistemas 1 sobre msqli',8, 'msql1')
    #trabalho1 = Trabalho('Trabalho de portugues sobre poemas e poesias',3, 'Poemas')
    #trabalhodao.salvar(trabalho1)
    #trabalhodao.salvar(trabalho)
    #try:
        #trabalhobusca = trabalhodao.buscar(1)
        #trabalhobusca.nota = 2
        #trabalhodao.salvar(trabalhobusca)
    #except IndexError:
        #print("Código errado ou não existe no banco")
    #except psycopg2.errors.InvalidTextRepresentation:
        #print("O código não pode ser string")
    #print(trabalhodao.buscar(1))
    #lista_trabalho = trabalhodao.listar()
    #for t in lista_trabalho:
        #print(t)
    #autor = autordao.buscar(2)
    #trabalho = trabalhodao.buscar(2)
    #trabalho.addAutor(autor)
    #trabalhodao.vinculaAutores(trabalho)
    #trabalhodao.deletar(2)
    #trabalho4 = trabalhodao.buscar(1)
    #trabalho4.entregaTrabalho()
    #trabalhodao.salvar(trabalho4)
    

    