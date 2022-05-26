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
                sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python app.py'
            }
        }
    }
}