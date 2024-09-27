pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM 'H * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                ls
                cat /etc/*-release
                cd Mat
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd Mat
                python3 main.py
               
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}