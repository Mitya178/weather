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
                   echo "Line1"
                   echo "Line2"
                   #git clone git@github.com:Mitya178/weather.git
                   docker build -t my_flask_app:v0.1 .
                '''
            }
        }
    }
}
