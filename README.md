# Web Monitor

The Web Monitor is a Python-based application that allows you to monitor the availability of web pages and report their status, including connection-level and content-related issues.

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ChanhNguyen17/web-monitor.git
   ```

2. Navigate to the project directory:

   ```
   cd web-monitor
   ```

3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

## Configuration

Before you can start monitoring websites, you need to configure the application using the `config.json` file. Here's how to configure it:

1. Open the `config.json` file in a text editor.

2. Add the websites you want to monitor in the following format:

   ```json
   {
    "websites": [
        {
            "url": "http://www.foobar.com/login",
            "content_requirement": "Please login:"
        },
        {
            "url": "https://company.f-secure.com/en",
            "content_requirement": "Making every digital moment secure, for everyone"
        },
        {
            "url": "https://wiki.python.org/moin/BeginnersGuide",
            "content_requirement": "Hacking with Python"
        }
    ],
    "checking_period_seconds": 5
    }
   ```

   - `"url"`: The URL of the website you want to monitor.
   - `"content_requirement"`: The content requirement that must be present in the response. Leave it empty (`""`) if you don't want to check for specific content.

3. Set the `"checking_period_seconds"` to specify how often the tool should check the websites (in seconds).

## Running the Application

To start monitoring the configured websites, run the following command:

```
python web_monitor.py
```

The application will periodically make HTTP requests to the specified websites, check for content requirements, and log the results.

## Viewing Monitoring Results

The monitoring results are logged in the `monitoring.log` file. You can view the log to see the status and response times of each checked website.

To view the log, you can use a text editor or run the following command:

```
cat monitoring.log
```

The log file contains entries like this:

```
INFO:root:URL: http://www.foobar.com/login, Status: Connection error: 403, Response Time: 0.326521635055542 seconds
INFO:root:URL: https://company.f-secure.com/en, Status: Content requirement met, Response Time: 0.2340555191040039 seconds
INFO:root:URL: https://wiki.python.org/moin/BeginnersGuide, Status: Content requirement not met, Response Time: 0.9651226997375488 seconds
```

The "Status" field indicates whether the content requirement was met or not or Connection error.

## Running Unit Tests

To run unit tests for the Web Monitoring Tool, use the following command:

```
python -m unittest tests/test_web_monitor.py
```

This command will execute the unit tests, and you'll see the test results in the terminal.
