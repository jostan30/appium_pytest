pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
        
        // SOLUTION: Override the build name at the pipeline level BEFORE the browserstack block.
        // This ensures the plugin, the publisher, and the SDK are all perfectly in sync.
        BROWSERSTACK_BUILD_NAME = "${PROJECT_NAME}-${COMPONENT_NAME}-${BUILD_NUMBER}"
    }

    stages {
        stage('Apply Fix for Build Name Mismatch') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    sh '''
                        # We removed the manual export here. 
                        # The SDK will now automatically pick up the BROWSERSTACK_BUILD_NAME from the pipeline environment.
                        echo "Running tests with pipeline build name: $BROWSERSTACK_BUILD_NAME"

                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                // The publisher will now successfully find the report because it is looking for 
                // the overridden BROWSERSTACK_BUILD_NAME instead of the default BUILD_TAG.
                browserStackReportPublisher 'app-automate'
            }
        }
    }
}