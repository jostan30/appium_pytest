pipeline {
    agent any

    stages {
        stage('Setup & Run Wikipedia Android E2E Tests') {
            steps {
                browserstack(credentialsId: 'YOUR_ACTUAL_CREDENTIAL_ID') {
                    sh '''
                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                browserStackReportPublisher 'app-automate'
            }
        }
    }
}