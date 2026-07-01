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
                }
            }
            steps {
                echo "Iniciando a execução dos testes..."
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    sh 'python3 test_temperatura.py -v'
                }
            }
        }
    }
}
