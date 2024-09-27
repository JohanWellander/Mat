pipeline {
    agent {
        docker {
            image 'python:3.9-alpine' // Assuming you're using an Alpine-based Python image
            args '-u root' // Run as root to avoid permission issues with package installs
        }
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
