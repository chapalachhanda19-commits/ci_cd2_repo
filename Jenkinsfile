pipeline {
    agent any
    stages{
        stage("checkout code") {
            steps{
                checkout scm
            }
            
        }
        stage("run the code") {
            steps{
                sh "python3 extract.py"
            }
            
        }
    }
}