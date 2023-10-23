pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Requirements') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip --user' 
                bat 'pip install --user -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
