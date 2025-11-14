pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Baixando o código do GitHub..."
                checkout scm
            }
        }

        stage('Instalar dependências') {
            steps {
                echo "Instalando dependências..."
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Testes') {
            steps {
                echo "Executando testes Django..."
                sh '''
                    python manage.py test
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou.'
        }
    }
}