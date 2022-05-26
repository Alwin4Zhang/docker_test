pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    // image 'qnib/pytest' 
                }
            }
            steps {
                // sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python app.py'
                sh 'docker build -t myimage . && docker run -d -p 5000:5000 myimage'
            }
        }
    }
}