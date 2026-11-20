pipeline {
    agent any

    stages {
        stage('Setup & Run Wikipedia Android E2E Tests') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
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