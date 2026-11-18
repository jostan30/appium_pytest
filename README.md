# Wikipedia Android E2E Tests

Appium + pytest tests for the Wikipedia Android sample app, run on BrowserStack App Automate using the BrowserStack SDK.

Tests (run in order, sharing one session):

1. `test_01_onboarding.py`
2. `test_02_search.py`
3. `test_03_open_article.py`
4. `test_04_save_article.py`

## Prerequisites

- Python 3.9+
- A BrowserStack account (username + access key from https://www.browserstack.com/accounts/settings)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest appium-python-client selenium browserstack-sdk
```

Set your credentials as environment variables (never commit them):

```bash
export BROWSERSTACK_USERNAME="<your-username>"
export BROWSERSTACK_ACCESS_KEY="<your-access-key>"
```

Or put them in a git-ignored `.env` file and load with `set -a; source .env; set +a`.

## Upload the app to BrowserStack

The sample app is committed to this repo as `WikipediaSample.apk`. Upload it to get a `bs://` app id:

```bash
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@WikipediaSample.apk"
```

The response looks like:

```json
{"app_url": "bs://3b46f3a1c5a572949f20985149454d80494fa0c6"}
```

Copy the `app_url` value into the `app:` field of `browserstack.yml`.
(Uploaded apps are kept for 30 days; re-upload when it expires.)

## Run the tests

```bash
browserstack-sdk pytest
```

To run a single file:

```bash
browserstack-sdk pytest test_02_search.py
```

Results appear on the BrowserStack App Automate dashboard under project `Wikipedia-Android-E2E`.

## Configuration

`browserstack.yml` holds the device (Samsung Galaxy S23, Android 13.0), app id, project/build names, and logging options. `conftest.py` creates one Appium session shared by all tests; `locators.py` holds element locators.
