pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            args '-u root' 
            }
      }
    triggers {
        pollSCM 'H * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                # Install build dependencies in Alpine Linux
                apk update
                apk add --no-cache gcc musl-dev python3-dev libffi-dev
                apk add --no-cache tesseract-ocr tesseract-ocr-dev
                apk add --no-cache make

                # Install Python dependencies
                pip install --upgrade pip
                pip install pytesseract
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                cd Mat
                python3 main.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Delivering...'
                sh '''
                echo "doing delivery stuff..."
                '''
            }
        }
    }
}