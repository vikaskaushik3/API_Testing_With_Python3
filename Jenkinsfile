pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        VENV_DIR = 'venv'
        TEST_REPORT_DIR = 'reports'

    }
    stages {
        stage('Checkout code'){
            steps {
            checkout scmGit(branches: [[name: "*/master"]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vikaskaushik3/API_Testing_With_Python3.git']])
            }
        }

        stage('Setup Python Environment'){
            steps{
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                }
            }

        stage('Run API Tests'){
            steps{
                sh '''
                    mkdir -p $TEST_REPORT_DIR
                    source $VENV_DIR/bin/activate
                    pytest --html=$TEST_REPORT_DIR/api_test_report.html --self-contained-html
                '''
                }
            }

        stage('Publish Reports'){
            steps{
                publishHTML(target: [
                    reportDir: "${TEST_REPORT_DIR}",
                    reportFiles: "api_test_report.html",
                    reportName: "API Test Reports"])
              }
            }
        }

        post {
            always {
                archiveArtifacts artifacts:"${TEST_REPORT_DIR}/*.html", fingerprint: true
            }
            failure {
                mail to: 'vikaskaushik166@gmail.com',
                subject: "Jenkins Build Failed: ${env.JOB_NAME}",
                body: "Check the build logs and report for details"
            }
        }

}