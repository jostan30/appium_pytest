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
                        // Name sent to the SDK. The SDK may append its own suffix (e.g. "  CI <n>").
                        def sdkBuildName =
                            "${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"

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

                        // Resolve the exact name BrowserStack stored (the report lookup needs an exact match)
                        // by taking the newest build whose name starts with the SDK build name.
                        def storedBuildName = ''
                        withEnv(["SDK_BUILD_NAME=${sdkBuildName}"]) {
                            storedBuildName = sh(
                                returnStdout: true,
                                script: '''
                                    curl -s -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
                                        "https://api-cloud.browserstack.com/app-automate/builds.json?limit=20" \
                                    | python3 -c "
import sys, json, os
prefix = os.environ['SDK_BUILD_NAME']
names = [b['automation_build']['name'] for b in json.load(sys.stdin)]
match = next((n for n in names if n == prefix or n.startswith(prefix + ' ')), '')
sys.stdout.write(match)
"
                                '''
                            ).trim()
                        }

                        if (!storedBuildName) {
                            echo "No stored build found starting with '${sdkBuildName}'; falling back to SDK name"
                            storedBuildName = sdkBuildName
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