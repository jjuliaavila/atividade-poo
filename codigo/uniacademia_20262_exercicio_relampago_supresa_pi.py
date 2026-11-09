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
    def get_nome_tipo_ensino(self):
        if self.__curso is None:
            return "Professor sem curso"
        else:
            return self.__curso.get_nome_tipo_ensino()
    def get_nome_diretor(self):
        if self.__curso is None:
            return "Professor sem curso"
        else:
            # pergunta pro curso quem é o diretor da escola
            return self.__curso.get_nome_diretor_escola()

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
    def get_nome_estado_escola(self):
        if self.__curso is None:
            return "Aluno sem curso"
        else:
            return self.__curso.get_nome_estado_escola()

class Curso:
    def __init__(self):
        self.__coordenador = None
        self.__tipo_ensino = None
        self.__escola = None
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
    def set_tipo_ensino(self, tipo_ensino):
        self.__tipo_ensino = tipo_ensino
    def get_tipo_ensino(self):
        return self.__tipo_ensino
    def get_nome_tipo_ensino(self):
        if self.__tipo_ensino is None:
            return "Curso sem tipo de ensino"
        else:
            return self.__tipo_ensino.get_nome()
    def set_escola(self, escola):
        self.__escola = escola
    def get_escola(self):
        return self.__escola
    def get_nome_estado_escola(self):
        if self.__escola is None:
            return "Curso sem escola"
        else:
            return self.__escola.get_nome_estado()
    def get_nome_diretor_escola(self):
        if self.__escola is None:
            return "Curso sem escola"
        else:
            # pergunta pra escola quem é o diretor
            return self.__escola.get_nome_diretor()

class Escola:
    def __init__(self):
        self.__diretor = None  # comeca sem diretor (relacao opcional)
        self.__cidade = None
    def set_diretor(self, diretor):
        self.__diretor = diretor
    def get_diretor(self):
        return self.__diretor
    def get_nome_escolaridade_diretor(self):
        if self.__diretor is None:
            return "Escola sem diretor"  # se nao tem diretor avisa sem vez de dar erro
        else:
            return self.__diretor.get_nome_escolaridade()
    def set_cidade(self, cidade):
        self.__cidade = cidade
    def get_cidade(self):
        return self.__cidade
    def get_nome_estado(self):
        if self.__cidade is None:
            return "Escola sem cidade"
        else:
            return self.__cidade.get_nome_estado()
    def get_nome_diretor(self):
        if self.__diretor is None:
            return "Escola sem diretor"
        else:
            return self.__diretor.get_nome()

class TipoEnsino:
    def __init__(self):
        self.__nome = ""  # nome do tipo de ensino (fundamental, medio, superior)
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome