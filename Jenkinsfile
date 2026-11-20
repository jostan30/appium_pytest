pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
        
        // SOLUTION: Override Jenkins' native BUILD_TAG. 
        // The BrowserStack plugin will read this and automatically set 
        // BROWSERSTACK_BUILD_NAME to match our custom format.
        BUILD_TAG = "${PROJECT_NAME}-${COMPONENT_NAME}-${BUILD_NUMBER}"
    }

    stages {
        stage('Apply Fix for Build Name Mismatch') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    sh '''
                        # Let's verify what the plugin actually injects now
                        echo "Running tests with injected build name: $BROWSERSTACK_BUILD_NAME"

                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                // The publisher will now look for our custom BUILD_TAG and succeed!
                browserStackReportPublisher 'app-automate'
            }
        }
    }
}