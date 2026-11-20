pipeline {
    agent any

    environment {
        PROJECT_NAME = 'WikipediaApp'
        COMPONENT_NAME = 'AndroidE2E'
    }

    stages {
        stage('Diagnose BrowserStack report') {
            steps {
                browserstack(credentialsId: '2c59e499-cef3-4b55-af61-590ae34b4d50') {
                    withEnv([
                        "BROWSERSTACK_BUILD_NAME=${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"
                    ]) {
                        script {
                            echo "Expected BrowserStack build name: ${env.BROWSERSTACK_BUILD_NAME}"

                            int testExitCode = sh(
                                returnStatus: true,
                                script: '''#!/bin/sh
set +x
set -e

python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install pytest appium-python-client selenium browserstack-sdk
browserstack-sdk pytest
'''
                            )

                            echo '--- Direct App Automate API diagnostic ---'

                            int diagnosticExitCode = sh(
                                returnStatus: true,
                                script: '''#!/bin/sh
set +x

.venv/bin/python - <<'PY'
import os
import sys
from urllib.parse import quote

import requests

build_name = os.environ.get("BROWSERSTACK_BUILD_NAME")
username = os.environ.get("BROWSERSTACK_USERNAME")
access_key = (
    os.environ.get("BROWSERSTACK_ACCESS_KEY")
    or os.environ.get("BROWSERSTACK_ACCESSKEY")
)

if not build_name:
    print("DIAGNOSIS: BROWSERSTACK_BUILD_NAME is missing.")
    sys.exit(1)

if not username or not access_key:
    print("DIAGNOSIS: BrowserStack credential environment variables are missing.")
    sys.exit(1)

try:
    response = requests.get(
        "https://api-cloud.browserstack.com/app-automate/builds.json",
        params={"limit": 100},
        auth=(username, access_key),
        timeout=30,
    )
    print("Build-list API HTTP status:", response.status_code)

    if not response.ok:
        print("DIAGNOSIS: The build list could not be fetched with these credentials.")
        sys.exit(1)

    payload = response.json()
    rows = payload if isinstance(payload, list) else payload.get("builds", [])

    def build_data(row):
        if not isinstance(row, dict):
            return {}
        nested = row.get("automation_build")
        return nested if isinstance(nested, dict) else row

    matches = [
        build_data(row)
        for row in rows
        if build_data(row).get("name") == build_name
    ]

    print("Exact-name build matches:", len(matches))

    if not matches:
        print("DIAGNOSIS: No exact-name build was returned by this account's API.")
        sys.exit(0)

    build_id = (
        matches[0].get("hashed_id")
        or matches[0].get("build_id")
        or matches[0].get("id")
    )

    if not build_id:
        print("DIAGNOSIS: A matching build was found, but its ID was missing.")
        sys.exit(1)

    sessions_response = requests.get(
        "https://api-cloud.browserstack.com/app-automate/builds/"
        + quote(str(build_id), safe="")
        + "/sessions.json",
        auth=(username, access_key),
        timeout=30,
    )
    print("Sessions API HTTP status:", sessions_response.status_code)

    if not sessions_response.ok:
        print("DIAGNOSIS: The build was found, but its sessions could not be fetched.")
        sys.exit(1)

    sessions_payload = sessions_response.json()
    sessions = (
        sessions_payload
        if isinstance(sessions_payload, list)
        else sessions_payload.get("sessions", [])
    )
    print("Sessions returned:", len(sessions))

except requests.RequestException as exc:
    print("DIAGNOSIS: API request failed:", type(exc).__name__)
    sys.exit(1)
except ValueError:
    print("DIAGNOSIS: BrowserStack returned an unexpected response format.")
    sys.exit(1)
PY
'''
                            )

                            if (diagnosticExitCode != 0) {
                                echo "API diagnostic exited with status ${diagnosticExitCode}; continuing to the Jenkins report step."
                            }

                            echo '--- BrowserStack Jenkins report step ---'
                            browserStackReportAut 'app-automate'

                            if (testExitCode != 0) {
                                error("BrowserStack tests failed with exit code ${testExitCode}.")
                            }
                        }
                    }
                }
            }
        }
    }
}