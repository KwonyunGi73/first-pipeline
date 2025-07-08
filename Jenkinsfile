// Jenkinsfile
pipeline {
    // 이제 Jenkins 컨트롤러 자체가 Docker 명령을 수행할 수 있도록 설정
    // Docker CLI와 권한이 컨테이너 이미지 자체에 내장되었으므로 'any' 사용
    agent any

    environment {
        // 호스트의 Docker 소켓을 컨테이너 내부로 마운트할 때 필요
        // 이 경로는 Docker Desktop이 사용하는 리눅스 가상머신 경로
        DOCKER_HOST_SOCKET = '/var/run/docker.sock'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // GitHub 저장소에서 코드 가져오기 (Jenkinsfile이 SCM에서 읽히므로 현재 디렉토리가 저장소 루트가 됨)
                git url: 'https://github.com/KwonyunGi73/first-pipeline.git', // 당신의 GitHub 저장소 URL
                    branch: 'main' // 혹은 'master', 당신의 기본 브랜치 이름 확인
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // 호스트의 Docker 데몬을 사용하여 파이썬 테스트를 실행하는 컨테이너를 띄움
                    // -v ${DOCKER_HOST_SOCKET}:${DOCKER_HOST_SOCKET}: Jenkins 컨테이너 내부의 Docker CLI가 호스트 Docker 데몬과 통신
                    // -v $(pwd):/app: 현재 Jenkins 작업 디렉토리(GitHub 코드)를 테스트 컨테이너 내부로 마운트
                    sh "docker run --rm -v ${DOCKER_HOST_SOCKET}:${DOCKER_HOST_SOCKET} -v $(pwd):/app -w /app python:3.9-slim-bullseye python3 -m unittest test_app.py"
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