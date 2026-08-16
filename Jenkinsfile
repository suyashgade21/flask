pipeline{
    agent any
    stages {
        stages('checkout scm') {
        steps {
            checkout scm
        }
    }
    stage('validate'){
        steps{
            sh 'python3 scripts/validate.py'
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

    