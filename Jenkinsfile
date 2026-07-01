pipeline {
    agent none // Garante que nada vai rodar no host do Jenkins
    
    stages {
        stage('Build em Container') {
            agent {
                docker { 
                    image 'python:3.9-slim' 
                    // Traz o container de Python leve para o build
                }
            }
            steps {
                echo "Iniciando processo de compilação/validação..."
                sh 'python3 -m py_compile temperatura.py'
            }
        }
        
        stage('Testes em Container') {
            agent {
                docker { 
                    image 'python:3.9-slim'
                    // Levanta um container totalmente novo e limpo para o teste
                }
            }
            steps {
                echo "Iniciando a execução dos testes..."
                // Roda o unittest que você já criou
                sh 'python3 test_temperatura.py -v'
            }
        }
    }
}