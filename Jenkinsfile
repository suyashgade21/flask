pipeline{
    agent any
    stages {
        stage('checkout scm') {
        steps {
            checkout scm
        }
    }
    stage('validate'){
        steps{
            sh 'python3 scripts/validate.py'
        }
    }
    stage('install Dependecies'){
        steps{
            sh ''' 
                python3 -m venv venv 
                ./venv/bin/pip install --upgrade pip 
                ./venv/bin/pip install -r requirements.txt
                '''
        }
    }
    stage('test'){
        steps{
            sh 'pytest'
        }
        
    } 
}
post {
    success{
        echo 'CI pipeline completed successfully!'
    }
    failure{
        echo 'CI pipeline failed !'
    }
} }

    