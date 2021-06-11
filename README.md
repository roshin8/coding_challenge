# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:

You can use a virtual environment (conda, venv, etc):
```
python3 -m venv /coding_challenge
source /coding_challenge/bin/activate
```

Or just pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running the code
```
python -m run
```

### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests

```
curl -i "http://127.0.0.1:5000/health-check"
```
```
curl -i "http://127.0.0.1:5000/org-stats-agg?github_org={ORG}&bitbucket_team={TEAM}"
```

## What'd I'd like to improve on...
Will mention it while discussing the code
