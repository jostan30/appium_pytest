pipeline {
    agent any

    stages {
        stage('Set Custom Tag') {
            steps {
                script {
                    // Trick the plugin by overriding the actual JOB_NAME it uses to build the string
                    env.JOB_NAME = "WikipediaApp-AndroidE2E"
                    echo "Forced JOB_NAME to: ${env.JOB_NAME}"
                }
            }
        }

        stage('Run BrowserStack Tests') {
            steps {
                // Let's see if the plugin picks up the fake JOB_NAME
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    sh '''
                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest appium-python-client selenium browserstack-sdk
                        browserstack-sdk pytest
                    '''
                }

                browserStackReportPublisher 'app-automate'
            }
        }
    }
}