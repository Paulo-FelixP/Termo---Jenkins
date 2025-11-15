pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Paulo-FelixP/Termo---Jenkins'
            }
        }

        stage('Instalar dependências') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install django
                '''
            }
        }

        stage('Rodar testes') {
            steps {
                sh '''
                . venv/bin/activate
                python jogo_termo/manage.py test
                '''
            }
        }
    }
}
