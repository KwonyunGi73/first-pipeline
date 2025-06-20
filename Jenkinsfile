// Jenkinsfile
pipeline {
    // 'agent any' 대신, 'python:3.9-slim' 도커 이미지를 작업 공간으로 사용하라고 지정
    agent {
        docker { image 'python:3.9-slim' }
    }
    stages {
        stage('Run Python Test') {
            steps {
                echo '파이썬 컨테이너 안에서 테스트를 시작합니다...'
                
                // 파이썬이 잘 설치되었는지 버전을 확인하는 로그를 추가 (좋은 습관입니다)
                sh 'python --version'
                
                // 우리의 테스트 코드를 실행
                sh 'python test_calculator.py'
            }
        }
    }
}