pipeline {
    agent any
    stages{
        stage("checkout code") {
            steps{
                checkout scm
            }
        }
        stage("setup environment") {
            steps{
                sh "pip install -r requirements.txt"
            }
            
        }
        stage("run the code") {
            steps{
                sh "python3 extract.py"
            }
            
        }
    }
}