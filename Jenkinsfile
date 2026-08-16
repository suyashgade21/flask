pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Validate') {
            steps {
                sh 'python3 scripts/validate.py'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/pytest'
            }
        }
        stage('Docker build'){
            steps {
                sh  '''
                pwd
                docker build -t devops-demo-api:${BUILD_NUMBER} .'''
            }
        }
        stage('load to minikube'){
            steps{
                sh 'minikube image load devops-demo-api:${BUILD_NUMBER}'
            }


        }
        stage('deployment'){
            steps{
                sh 'kubectl apply -f k8s'
            }
        }
        stage('minikube url '){
            steps{
                sh 'minikube svc devops-demo-api -n devops-demo --url '
            }
        }
       
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }

        failure {
            echo 'CI pipeline failed!'
        }
    }
}