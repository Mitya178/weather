pipeline {
    agent any

    stages {
        //def ci
        stage('pipeline-test1') {
            //container('docker') {
            //  ci.build()
            //}
            steps {
                //container('docker')
                sh '''
                   docker build -t my_flask_app:v0.1 .
                '''
            }
        }
    }
}
