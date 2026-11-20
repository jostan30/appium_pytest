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
                    withEnv(["BROWSERSTACK_BUILD_NAME=${env.PROJECT_NAME}-${env.COMPONENT_NAME}-${env.BUILD_NUMBER}"]) {
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

                            echo '--- Direct BrowserStack API diagnostic ---'

                            int apiDiagnosticExitCode = sh(
                                returnStatus: true,
                                script: '''#!/bin/sh
set +x
python3 - <<'PY'
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
    print("DIAGNOSIS: BROWSERSTACK_BUILD_NAME is not set at the API check.")
    sys.exit(1)

if not username or not access_key:
    print("DIAGNOSIS: BrowserStack username/access key environment variables are missing.")
    sys.exit(1)

auth = (username, access_key)
response = requests.get(
    "https://api.browserstack.com/app-automate/builds.json",
    params={"limit": 100},
    auth=auth,
    timeout=30,
)
print("Build-list API HTTP status:", response.status_code)

if not response.ok:
    print("DIAGNOSIS: Could not list App Automate builds with the configured credentials.")
    sys.exit(1)

payload = response.json()
rows = payload if isinstance(payload, list) else payload.get("builds", [])

def build_data(row):
    if not isinstance(row, dict):
        return {}
    for key in ("automation_build", "build"):
        if isinstance(row.get(key), dict):
            return row[key]
    return row

matches = [
    build_data(row)
    for row in rows
    if build_data(row).get("name") == build_name
]

print("Exact-name build matches in the latest build list:", len(matches))

if not matches:
    print("DIAGNOSIS: The API did not return this exact build name for these credentials.")
    print("Check the BrowserStack account/credentials and the build name used by the test sessions.")
    sys.exit(0)

build = matches[0]
build_id = build.get("hashed_id") or build.get("build_id") or build.get("id")

if not build_id:
    print("DIAGNOSIS: Build matched, but the API response had no recognized build ID.")
    print("Build response fields:", ", ".join(sorted(build.keys())))
    sys.exit(1)

sessions_response = requests.get(
    "https://api.browserstack.com/app-automate/builds/"
    + quote(str(build_id), safe="")
    + "/sessions.json",
    auth=auth,
    timeout=30,
)
print("Sessions API HTTP status:", sessions_response.status_code)

if not sessions_response.ok:
    print("DIAGNOSIS: Build was found, but its sessions could not be fetched.")
    sys.exit(1)

sessions_payload = sessions_response.json()
sessions = (
    sessions_payload
    if isinstance(sessions_payload, list)
    else sessions_payload.get("sessions", [])
)
print("Sessions returned for the build:", len(sessions))

if not sessions:
    print("DIAGNOSIS: Build exists, but the App Automate API returned no sessions.")
else:
    print("DIAGNOSIS: Build and sessions are visible through the configured App Automate credentials.")
PY
'''
                            )

                            if (apiDiagnosticExitCode != 0) {
                                echo "The direct API check had an error (exit ${apiDiagnosticExitCode}); continuing to the plugin report step."
                            }

                            echo '--- BrowserStack Jenkins plugin report step ---'
                            browserStackReportAut 'app-automate'

                            if (testExitCode != 0) {
                                error("BrowserStack tests failed with exit code ${testExitCode}; report step was still run.")
                            }
                        }
                    }
                }
            }
        }
    }
}