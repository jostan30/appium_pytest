pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
    }

    stages {
        stage('Run BrowserStack Tests') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    withEnv(["BROWSERSTACK_BUILD_NAME=${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"]) {
                        sh '''
                            echo "Current BROWSERSTACK_BUILD_NAME is: $BROWSERSTACK_BUILD_NAME"

                            python3 -m venv .venv
                            . .venv/bin/activate
                            pip install --upgrade pip
                            pip install pytest appium-python-client selenium browserstack-sdk
                            browserstack-sdk pytest
                        '''

                        // Keep this inside withEnv so the report uses the same build name.
                        browserStackReportAut 'app-automate'
                    }
                }
            }
        }
    }
}