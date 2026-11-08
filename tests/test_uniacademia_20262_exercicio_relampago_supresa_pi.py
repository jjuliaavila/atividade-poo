from codigo.uniacademia_20262_exercicio_relampago_supresa_pi import *

def test_deve_retornar_nome_escolaridade_professor():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    professor = Professor()
    professor.set_escolaridade(escolaridade)
    assert professor.get_nome_escolaridade() == "Doutorado"

def test_deve_retornar_pessoa_sem_escolaridade():
    professor = Professor()
    assert professor.get_nome_escolaridade() == "Pessoa sem escolaridade"

def test_deve_retornar_nome_estado_cidade():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    assert cidade.get_nome_estado() == "RJ"

def test_deve_retornar_cidade_sem_estado():
    cidade = Cidade()
    assert cidade.get_nome_estado() == "Cidade sem estado"

def test_deve_retornar_nome_estado_naturalidade_aluno():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    aluno = Aluno()
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "RJ"

def test_deve_retornar_aluno_sem_estado_naturalidade():
    aluno = Aluno()
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem estado naturalidade"

def test_deve_retornar_curso_sem_coordenador():
    curso = Curso()
    assert curso.get_nome_coordenador() == "Curso sem coordenador"

def test_deve_retornar_nome_coordenador_curso():
    coordenador = Professor()
    coordenador.set_nome("Marco")
    curso = Curso()
    curso.set_coordenador(coordenador)
    assert curso.get_nome_coordenador() == "Marco"

def test_deve_retornar_professor_sem_curso():
    professor = Professor()
    assert professor.get_nome_coordenador() == "Professor sem curso"

def test_deve_retornar_nome_coordenador_professor():
    coordenador = Professor()
    coordenador.set_nome("Marco")
    curso = Curso()
    curso.set_coordenador(coordenador)
    professor = Professor()
    professor.set_curso(curso)
    assert professor.get_nome_coordenador() == "Marco"

def test_deve_retornar_nome_escolaridade_coordenador_curso():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Mestrado")
    coordenador = Professor()
    coordenador.set_escolaridade(escolaridade)
    curso = Curso()
    curso.set_coordenador(coordenador)
    assert curso.get_nome_escolaridade_coordenador() == "Mestrado"

def test_deve_retornar_curso_sem_coordenador_ao_pedir_escolaridade():
    curso = Curso()
    assert curso.get_nome_escolaridade_coordenador() == "Curso sem coordenador"

def test_deve_retornar_pessoa_sem_escolaridade_coordenador_curso():
    coordenador = Professor()
    curso = Curso()
    curso.set_coordenador(coordenador)
    assert curso.get_nome_escolaridade_coordenador() == "Pessoa sem escolaridade"

def test_deve_retornar_nome_escolaridade_diretor_escola():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    diretor = Professor()
    diretor.set_escolaridade(escolaridade)
    escola = Escola()
    escola.set_diretor(diretor)
    assert escola.get_nome_escolaridade_diretor() == "Doutorado"

def test_deve_retornar_escola_sem_diretor():
    escola = Escola()
    assert escola.get_nome_escolaridade_diretor() == "Escola sem diretor"

def test_deve_retornar_pessoa_sem_escolaridade_diretor_escola():
    diretor = Professor()  # escolaridade começa None (não defini nenhuma)
    escola = Escola()
    escola.set_diretor(diretor)
    assert escola.get_nome_escolaridade_diretor() == "Pessoa sem escolaridade"

def test_deve_retornar_nome_cidade_naturalidade_professor():
    cidade = Cidade()
    cidade.set_nome("Leopoldina")
    professor = Professor()
    professor.set_naturalidade(cidade)
    assert professor.get_nome_cidade_naturalidade() == "Leopoldina"

def test_deve_retornar_professor_sem_naturalidade():
    professor = Professor()
    assert professor.get_nome_cidade_naturalidade() == "Pessoa sem naturalidade"