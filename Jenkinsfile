pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
    }

    stages {
        stage('Reproduce Build Name Mismatch') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    sh '''
                        # Force-override the build name inside the shell right before the SDK runs
                        export BROWSERSTACK_BUILD_NAME="${PROJECT_NAME}-${COMPONENT_NAME}-${BUILD_NUMBER}"
                        echo "Running tests with custom build name: $BROWSERSTACK_BUILD_NAME"

                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                // This step runs outside the shell and still looks up Jenkins' default BUILD_TAG
                browserStackReportPublisher 'app-automate'
            }
        }
    }
}