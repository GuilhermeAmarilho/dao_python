from dao import DAO
from psycopg2 import connect
from trabalho import Trabalho
from autor import Autor
from autordao import autorDao
class trabalhoDao(DAO):
    def __init__(self):
        super().__init__()

    def salvar(self,trabalho):
        trabalhodao = trabalhoDao()

        if(trabalho.codigo == None):
            trabalhodao.inserir(trabalho)
        else:
            trabalhodao.alterar(trabalho)

    def alterar(self,trabalho):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE "Trabalho" SET conteudo = %s, nota = %s, titulo = %s, "dataEntrega" = %s, "dataHoraAtualizacao" = now() WHERE cod = %s and "dataHoraAtualizacao" = %s',[trabalho.conteudo,trabalho.nota,trabalho.titulo,trabalho.dataentrega,trabalho.codigo,trabalho.data])
            conn.commit()
            cur.close()

    def inserir(self,trabalho):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO "Trabalho" (conteudo,nota,titulo,"dataHoraAtualizacao") VALUES (%s,%s,%s,now()) RETURNING cod', [trabalho.conteudo,trabalho.nota,trabalho.titulo])
            linhaid = cur.fetchone()[0]
            trabalho.codigo = linhaid
            conn.commit()
            cur.close()

    def buscar(self,cod):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT  t.titulo, t.cod as cod_trabalho, t.nota,t.conteudo,t."dataEntrega",t."dataHoraAtualizacao", a.cod as cod_autor,a.nome, a.email FROM "Trabalho" as t LEFT JOIN "TrabalhoAutor"  as ta ON t.cod = ta."codTrabalho" LEFT JOIN "Autor" as a ON ta."codAutor"= a.cod WHERE t.cod = %s',[cod])
            linha = cur.fetchall()
            trabalho = Trabalho(linha[0][3],linha[0][2],linha[0][0])
            trabalho.codigo = linha[0][1]
            trabalho.dataentrega = linha[0][4]
            trabalho.data = linha[0][5]
            if(linha[0][7] == None):
                conn.commit()
                cur.close()
                return trabalho
            else:
                for l in linha:
                    autor = Autor(l[7],l[8])
                    autor.codigo = l[6]
                    trabalho.addAutor(autor)
                    conn.commit()
                    cur.close()
                return trabalho
    def vinculaAutores(self, trabalho):
       with connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('SELECT "codAutor" FROM "TrabalhoAutor" WHERE "codTrabalho"=%s', [trabalho.codigo])
            vet = []
            for linha in cur.fetchall():
                l = linha[0]
                vet.append(l)
            for a in trabalho.autores:
                if(not vet.__contains__(a.codigo)):
                    sql = cur.execute('INSERT INTO "TrabalhoAutor"("codAutor", "codTrabalho") VALUES (%s, %s)',[a.codigo, trabalho.codigo])
            

    def deletar(self,cod):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('DELETE FROM "Trabalho" WHERE cod = %s',[cod])
            conn.commit()
            cur.close()

    def listar(self):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('SELECT * FROM "Trabalho"')
            lista_trabalhos = []
            for linha in cur.fetchall():
                trabalho = Trabalho(linha[1],linha[2],linha[4])
                trabalho.codigo = linha[0]
                trabalho.dataentrega = linha[3]
                trabalho.data = linha[5]
                lista_trabalhos.append(trabalho)
            cur.close()
            conn.commit()
            return lista_trabalhos