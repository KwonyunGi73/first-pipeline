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
                    // **여기서 $(pwd) 앞의 $에 \를 붙여서 이스케이프합니다.**
                    sh "docker run --rm -v ${DOCKER_HOST_SOCKET}:${DOCKER_HOST_SOCKET} -v \$(pwd):/app -w /app python:3.9-slim-bullseye python3 -m unittest test_app.py"
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