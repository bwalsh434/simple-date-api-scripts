# simple-date-api-scripts
A set of scripts used with the simple-date-api application.

## bootstrap.sh
Bootstrap script for the simple-date-api application. Installs OS dependencies, pulls down the simple-date-api app,
and starts the simple-date-api app. <br>

For the designed use case, the Google Compute Engine servers pull down this script from a Google Cloud Storage bucket on
VM boot and use it as the startup-script.

## api_test.sh
Simple script written for Python 3 that sends GET requests to the supplied URL (CLI argument) indefinitely. <br> <br>
To run the script:
```
python3 --url http://34.95.112.0/date
```

