from neo4j import GraphDatabase

class SchoolManagementSystem:
    """Sistema de Gerenciamento Escolar utilizando Neo4j"""
    def __init__(self, uri, auth):
        """Inicializa a conexão com o banco de dados"""
        self._driver = GraphDatabase.driver(uri, auth=auth)

    def close(self):
        """Fecha a conexão com o banco de dados"""
        self._driver.close()

    def create_sample_data(self):
        """Cria dados de exemplo no banco de dados Neo4j"""
        try:
            with self._driver.session() as session:
                # Criar professores
                session.run("CREATE (:Professor {name: 'Alex'})")
                session.run("CREATE (:Professor {name: 'Paulo'})")
                print("Professores Criados!!")

                # Criar cursos
                session.run("CREATE (:Curso {name: 'Matematica'})")
                session.run("CREATE (:Curso {name: 'Historia'})")
                print("Cursos Criados!!")

                # Criar turmas
                session.run("CREATE (:Turma {name: 'Turma 1'})")
                session.run("CREATE (:Turma {name: 'Turma 2'})")
                print("Turmas Criadas!!")

                # Criar alunos
                session.run("CREATE (:Aluno {name: 'Caio'})")
                session.run("CREATE (:Aluno {name: 'Sandra'})")
                print("Alunos Criados!!")

                # Criar relações entre professores e cursos
                session.run("""
                    MATCH (prof:Professor {name: 'Alex'})
                    MATCH (curso:Curso {name: 'Matematica'})
                    CREATE (prof)-[:ENSINA]->(curso)
                """)
                print("Relações criadas primeira parte!!")
                session.run("""
                    MATCH (prof:Professor {name: 'Paulo'})
                    MATCH (curso:Curso {name: 'Historia'})
                    CREATE (prof)-[:ENSINA]->(curso)
                """)
                print("Relações criadas segunda parte!!")

                # Criar relações entre turmas e cursos
                session.run("""
                    MATCH (turma:Turma {name: 'Turma 1'})
                    MATCH (curso:Curso {name: 'Matematica'})
                    CREATE (turma)-[:PERTENCE_A]->(curso)
                """)
                session.run("""
                    MATCH (turma:Turma {name: 'Turma 2'})
                    MATCH (curso:Curso {name: 'Historia'})
                    CREATE (turma)-[:PERTENCE_A]->(curso)
                """)

                # Criar relações entre alunos e turmas
                session.run("""
                    MATCH (aluno:Aluno {name: 'Caio'})
                    MATCH (turma:Turma {name: 'Turma 1'})
                    CREATE (aluno)-[:FAZ_PARTE]->(turma)
                """)
                session.run("""
                    MATCH (aluno:Aluno {name: 'Sandra'})
                    MATCH (turma:Turma {name: 'Turma 2'})
                    CREATE (aluno)-[:FAZ_PARTE]->(turma)
                """)
        except Exception as e:
            print("An error occurred while creating sample data: {}".format(e))

if __name__ == "__main__":
    URI = "ip"  # URI do seu banco de dados Neo4j Aura
    AUTH = ("user", "password")  # Seu nome de usuário e senha

    # Criar instância do sistema de gerenciamento escolar
    system = SchoolManagementSystem(URI, AUTH)

    # Criar dados de exemplo no banco de dados Neo4j Aura
    system.create_sample_data()

    # Verificar conectividade com o banco de dados Neo4j Aura
    try:
            with GraphDatabase.driver(URI, auth=AUTH) as driver:
            driver.verify_connectivity()
            print("Conexão bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar: {}".format(e))

    # Fechar conexão
    system.close()
