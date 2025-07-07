// Jenkinsfile
pipeline {
    agent {
        // 테스트를 실행할 도커 이미지 지정. Python 3.9 버전의 경량 이미지 사용.
        // 젠킨스 에이전트가 이 도커 컨테이너 안에서 작업을 수행합니다.
        docker {
            image 'python:3.9-slim-bullseye'
            // 컨테이너가 특정 포트를 필요로 하거나 추가 볼륨 마운트가 필요할 경우 여기에 옵션 추가 가능
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                // GitHub 저장소에서 코드 가져오기
                git url: 'https://github.com/KwonyunGi73/first-pipeline.git', // 당신의 GitHub 저장소 URL
                    branch: 'main' // 혹은 'master', 당신의 기본 브랜치 이름 확인
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // 도커 컨테이너 내부에서 파이썬 테스트 실행
                    // 'python -m unittest test_app.py' 명령어를 컨테이너 안에서 실행
                    sh 'python3 -m unittest test_app.py'
                }
            }
        }
    }

    post {
        // 빌드 성공 여부에 관계없이 항상 실행되는 부분
        always {
            echo 'Pipeline finished!'
        }
        // 빌드가 성공했을 때 실행되는 부분
        success {
            echo 'Unit tests passed successfully! Code is good.'
        }
        // 빌드가 실패했을 때 실행되는 부분
        failure {
            echo 'Unit tests failed! Please check the code and logs.'
        }
    }
}