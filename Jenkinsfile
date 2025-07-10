// Jenkinsfile
pipeline {
    agent any

    environment {
        DOCKER_HOST_SOCKET = '/var/run/docker.sock'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/KwonyunGi73/first-pipeline.git',
                    branch: 'main' // 혹은 'master', 당신의 기본 브랜치 이름 확인
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh "sudo chmod 666 ${DOCKER_HOST_SOCKET}"
                    // **여기서 python3 -m unittest test_app.py 부분을 수정합니다.**
                    sh "docker run --rm -v ${DOCKER_HOST_SOCKET}:${DOCKER_HOST_SOCKET} -v \$(pwd):/app -w /app python:3.9-slim-bullseye python3 -m unittest discover -s /app -p 'test_*.py'"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Unit tests passed successfully! Code is good.'
        }
        failure {
            echo 'Unit tests failed! Please check the code and logs.'
        }
    }
}