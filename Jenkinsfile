pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.6' 
                }
            }
            steps {
                sh 'sudo pip install -r requirements.txt'
                sh 'python app.py' 
            }
        }
    }
}