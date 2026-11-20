pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
    }

    stages {
        stage('Apply Fix using withEnv') {
            steps {
                script {
                    // Create the custom tag string
                    def customBuildTag = "${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"
                    
                    // Forcefully inject it into the environment for these specific steps
                    withEnv(["BUILD_TAG=${customBuildTag}", "BROWSERSTACK_BUILD_NAME=${customBuildTag}"]) {
                        
                        browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                            sh '''
                                echo "Injected BUILD_TAG: $BUILD_TAG"
                                echo "Injected BROWSERSTACK_BUILD_NAME: $BROWSERSTACK_BUILD_NAME"

                                python3 -m venv .venv
                                . .venv/bin/activate
                                pip install --upgrade pip
                                pip install pytest appium-python-client selenium browserstack-sdk
                                browserstack-sdk pytest
                            '''
                        }

                        // The publisher is also inside withEnv, so it looks for the custom tag
                        browserStackReportPublisher 'app-automate'
                    }
                }
            }
        }
    }
}