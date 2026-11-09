class Estado:
    def __init__(self):
        self.__nome = ""
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome

class Cidade:
    def __init__(self):
        self.__nome = ""
        self.__estado = None
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_estado(self, estado):
        self.__estado = estado
    def get_estado(self):
        return self.__estado
    def get_nome_estado(self):
        if self.__estado is None:
            return "Cidade sem estado"
        else:
            return self.__estado.get_nome()

class Escolaridade:
    def __init__(self):
        self.__nome = ""
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__escolaridade = None
        self.__naturalidade = None
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_escolaridade(self):
        return self.__escolaridade
    def set_escolaridade(self, escolaridade):
        self.__escolaridade = escolaridade
    def get_naturalidade(self):
        return self.__naturalidade
    def set_naturalidade(self, naturalidade):
        self.__naturalidade = naturalidade
    def get_nome_escolaridade(self):
        if self.__escolaridade is None:
            return "Pessoa sem escolaridade"
        else:
            return self.__escolaridade.get_nome()
    def get_nome_estado_naturalidade(self):
        if self.__naturalidade is None:
            return "Pessoa sem estado naturalidade"
        else:
            return self.__naturalidade.get_nome_estado()
    def get_nome_cidade_naturalidade(self):
        if self.__naturalidade is None:
            return "Pessoa sem naturalidade"
        else:
            return self.__naturalidade.get_nome()

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__curso = None
    def set_curso(self, curso):
        self.__curso = curso
    def get_curso(self):
        return self.__curso
    def get_nome_coordenador(self):
        if self.__curso is None:
            return "Professor sem curso"
        else:
            return self.__curso.get_nome_coordenador()

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__curso = None  # começa sem curso (relaçao opcional)
    def set_curso(self, curso):
        self.__curso = curso
    def get_curso(self):
        return self.__curso
    def get_nome_coordenador(self):
        if self.__curso is None:
            return "Aluno sem curso"
        else:
            return self.__curso.get_nome_coordenador()

class Curso:
    def __init__(self):
        self.__coordenador = None
    def set_coordenador(self, coordenador):
        self.__coordenador = coordenador
    def get_coordenador(self):
        return self.__coordenador
    def get_nome_coordenador(self):
        if self.__coordenador is None:
            return "Curso sem coordenador"
        else:
            return self.__coordenador.get_nome()
    def get_nome_escolaridade_coordenador(self):
        if self.__coordenador is None:
            return "Curso sem coordenador"
        else:
            return self.__coordenador.get_nome_escolaridade()

class Escola:
    def __init__(self):
        self.__diretor = None  # comeca sem diretor (relacao opcional)
    def set_diretor(self, diretor):
        self.__diretor = diretor
    def get_diretor(self):
        return self.__diretor
    def get_nome_escolaridade_diretor(self):
        if self.__diretor is None:
            return "Escola sem diretor"  # se nao tem diretor avisa sem vez de dar erro
        else:
            return self.__diretor.get_nome_escolaridade()