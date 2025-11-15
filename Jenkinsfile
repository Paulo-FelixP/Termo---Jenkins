pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Baixando código do repositório...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Criando virtualenv e instalando dependências...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip

                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        pip install django
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Executando testes...'
                sh '''
                    . venv/bin/activate
                    cd jogo_termo
                    python manage.py test termo
                '''
            }
        }
    }

    post {
        success { echo '✓ Todos os testes passaram.' }
        failure { echo '✗ Algum teste falhou.' }
    }
}
