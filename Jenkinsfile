pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
        // Override the core Jenkins BUILD_TAG which the plugin relies on
        BUILD_TAG = "${PROJECT_NAME}-${COMPONENT_NAME}-${BUILD_NUMBER}"
    }

    stages {
        stage('Reproduce Build Name Mismatch') {
            steps {
                // The plugin initializes here, reading the overridden BUILD_TAG
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    sh '''
                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                // The publisher will now fail because the plugin's internal tracking
                // and the SDK's payload are out of sync due to the overridden core variable.
                browserStackReportPublisher 'app-automate'
            }
        }
    }
}