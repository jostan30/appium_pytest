pipeline {
    agent any

    environment {
        // Simulating the customer's custom project/component variables
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
    }

    stages {
        stage('Reproduce Build Name Mismatch') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    script {
                        // Customer overrides BROWSERSTACK_BUILD_NAME with custom metadata
                        // Note: The plugin's publisher step still looks at the original BUILD_TAG
                        env.BROWSERSTACK_BUILD_NAME = "${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"
                    }

                    sh '''
                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                // This step will still look for the default BUILD_TAG instead of the custom name above
                browserStackReportPublisher 'app-automate'
            }
        }
    }
}