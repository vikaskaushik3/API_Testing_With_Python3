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
            checkout scmGit(
            branches: [[name: "*/master"]],
            extensions: [],
            userRemoteConfigs: [[url: 'https://github.com/vikaskaushik3/API_Testing_With_Python3.git']])
            }
        }

        stage('Setup Python Environment'){
            steps{
                sh '''
                    python3 -m venv $VENV_DIR && \
                    source $VENV_DIR/bin/activate && \
                    pip install --upgrade pip && \
                    pip install -r requirements.txt
                '''
                }
            }

        stage('Run API Tests'){
            steps{
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE'){
                    sh '''
                        source $VENV_DIR/bin/activate && \
                        mkdir -p $TEST_REPORT_DIR && \
                        pytest --alluredir=$TEST_REPORT_DIR/allure-results
                    '''
                  }
                script {
                    if (currentBuild.result == 'FAILURE') {
                        echo "Test execution failed. Marking current build as failed"
                        currentBuild.currentResult = 'FAILURE'
                        }
                    }
                }
            }

        stage('Publish Reports') {
            when {
                expression {
                    return currentBuild.currentResult == 'SUCCESS'
                }
            }
            steps {
                allure includeProperties: false,
                    jdk: '',
                    results: [[path: "${TEST_REPORT_DIR}/allure-results"]]
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
}
