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
                        def customBuildName =
                            "${env.PROJECT_NAME}-${env.COMPONENT_NAME}"

                        withEnv([
                            "BROWSERSTACK_BUILD=${customBuildName}",
                            "BROWSERSTACK_BUILD_NAME=${customBuildName}"
                        ]) {
                            echo "BROWSERSTACK_BUILD_NAME for tests and report: ${env.BROWSERSTACK_BUILD_NAME}"

                            sh '''
                                python3 -m venv .venv
                                . .venv/bin/activate
                                pip install --upgrade pip
                                pip install pytest appium-python-client selenium browserstack-sdk
                                browserstack-sdk pytest
                            '''

                            browserStackReportAut 'app-automate'
                        }
                    }
                }
            }
        }
    }
}