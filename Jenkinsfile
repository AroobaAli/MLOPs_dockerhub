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
                bat 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
