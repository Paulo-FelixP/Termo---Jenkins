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
                sh """
                    . /var/jenkins_home/venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                """
            }
        }

        stage('Testes') {
            steps {
                echo "Executando testes..."
                sh """
                    . /var/jenkins_home/venv/bin/activate
                    python manage.py test
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline concluída com sucesso!"
        }
        failure {
            echo "A pipeline falhou."
        }
    }
}
