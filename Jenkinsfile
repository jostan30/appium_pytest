pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
    }

    stages {
        stage('Run BrowserStack Tests and Report') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    script {
                        // Name the SDK registers. It appends "  CI <BUILD_NUMBER>" to this.
                        def sdkBuildName =
                            "${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"
                        // Full name as stored on BrowserStack (exact match needed by the report lookup).
                        def storedBuildName = "${sdkBuildName}  CI ${env.BUILD_NUMBER}"

                        withEnv([
                            "BROWSERSTACK_BUILD=${sdkBuildName}",
                            "BROWSERSTACK_BUILD_NAME=${sdkBuildName}"
                        ]) {
                            echo "Build name sent by SDK: ${env.BROWSERSTACK_BUILD_NAME}"

                            sh '''
                                python3 -m venv .venv
                                . .venv/bin/activate
                                pip install --upgrade pip
                                pip install pytest appium-python-client selenium browserstack-sdk
                                browserstack-sdk pytest
                            '''
                        }

                        withEnv([
                            "BROWSERSTACK_BUILD=${storedBuildName}",
                            "BROWSERSTACK_BUILD_NAME=${storedBuildName}"
                        ]) {
                            echo "Build name used for report lookup: ${env.BROWSERSTACK_BUILD_NAME}"
                            browserStackReportAut 'app-automate'
                        }
                    }
                }
            }
        }
    }
}