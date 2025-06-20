// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Run Python Test') {
            steps {
                echo '파이썬 계산기 테스트를 시작합니다...'
                
                // 터미널에서 python으로 test_calculator.py 파일을 실행하라는 명령어
                sh 'python test_calculator.py'
            }
        }
    }
}