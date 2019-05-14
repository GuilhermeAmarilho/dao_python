class Autor:
    def __init__(self,nome,email):
        self._nome = nome
        self._email = email
        self._codigo = None

    def _get_codigo(self):
        return self._codigo

    def _set_codigo(self,codigo):
        self._codigo = codigo

    def _get_nome(self):
        return self._nome

    def _set_nome(self,nome):
        self._nome = nome
    
    def _get_email(self):
        return self._email

    def _set_email(self,email):
        self._email = email
    
    def __str__(self):
        return "Código: {}, Nome: {}, Email: {}".format(self._codigo,self._nome,self._email)

    codigo = property(_get_codigo,_set_codigo)
    nome = property(_get_nome,_set_nome)
    email = property(_get_email,_set_email)