pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python app.py'
            }
        }
    }
}