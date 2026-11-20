 pipeline {
    agent any

    stages {
        stage('Setup & Run Wikipedia Android E2E Tests') {
            steps {
                // Replace '<credential_id>' with your BrowserStack Credential ID from Jenkins
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