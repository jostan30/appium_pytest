pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root'
        }
    }

    stages {
        stage('Setup & Run Wikipedia Android E2E Tests') {
            steps {
                // Replace '<credential_id>' with your actual BrowserStack Credential ID
                browserstack(credentialsId: '<credential_id>') {
                    sh '''
                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                // Embeds the BrowserStack App Automate test report in Jenkins
                browserStackReportPublisher 'automate'
            }
        }
    }
}