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
                sh """
                    . /var/jenkins_home/venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Testes') {
            steps {
                sh """
                    . /var/jenkins_home/venv/bin/activate
                    python jogo_termo/manage.py test
                """
            }
        }
    }

    post {
        failure {
            echo "A pipeline falhou."
        }
        success {
            echo "Pipeline concluída com sucesso!"
        }
    }
}
