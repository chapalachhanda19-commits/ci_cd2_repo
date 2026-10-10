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
                sh "python3 -m pip install -r requirement.txt"
            }
            
        }
        stage("run the code") {
            steps{
                sh "python3 extract.py"
            }
            
        }
    }
}