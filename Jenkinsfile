pipeline {
    agent { 
        node {
            label 'docker-agent-food'
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
                python3 test.py
               
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