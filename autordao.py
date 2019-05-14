from dao import DAO
from psycopg2 import connect
from autor import Autor

class autorDao(DAO):
    def __init__(self):
        super().__init__()

    def salvar(self,autor):
        autordao = autorDao()

        if(autor.codigo == None):
            autordao.inserir(autor)
        else:
            autordao.alterar(autor)

    def inserir(self,autor):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO "Autor" (nome, email) VALUES (%s,%s) RETURNING cod',[autor.nome,autor.email])
            linhaid = cur.fetchone()[0]
            autor.codigo = linhaid
            conn.commit()
            cur.close()

    def deletar(self,cod):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('DELETE FROM "Autor" WHERE cod = %s',[cod])
            conn.commit()
            cur.close()

    def listar(self):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "Autor"')
            lista_autores = []
            for linha in cur.fetchall():
                autor = Autor(linha[1],linha[2])
                autor.codigo = linha[0]
                lista_autores.append(autor)
            conn.commit()
            cur.close()
            return lista_autores

    def buscar(self,cod):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "Autor" WHERE cod=%s',[cod])
            linha = cur.fetchall()
            autor = Autor(linha[0][1],linha[0][2])
            autor.codigo = linha[0][0]
            conn.commit()
            cur.close()
            return autor

    def alterar(self,autor):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE "Autor" SET nome = %s,email = %s WHERE cod = %s',[autor.nome,autor.email,autor.codigo])
            conn.commit()
            cur.close()

