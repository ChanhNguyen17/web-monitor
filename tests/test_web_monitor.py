import unittest
from unittest.mock import patch
from web_monitor import WebMonitor


class TestWebMonitor(unittest.TestCase):
    def setUp(self):
        self.monitoring_log_file = 'tests/monitoring_test.log'
        self.monitor = WebMonitor('config.json', self.monitoring_log_file)
        self.url = "https://mock_site.com"

    def tearDown(self):
        open(self.monitoring_log_file, 'w').close()

    def get_last_log_entry(self):
        # Helper method to get the last log entry from the log file
        with open(self.monitoring_log_file, 'r') as log_file:
            log_entries = log_file.readlines()
            if log_entries:
                return log_entries[-1]
            else:
                return ""

    @patch('web_monitor.requests.get')
    def test_check_website_content_met(self, mock_get):
        mock_get.return_value.text = "mock response"
        mock_get.return_value.status_code = 200

        website = {
            "url": self.url,
            "content_requirement": "mock response"
        }
        self.monitor.check_website(website)

        # Assert that the log contains the expected status and response time
        expected_log_entry = f"URL: {self.url}, Status: Content requirement met, Response Time: "
        self.assertIn(expected_log_entry, self.get_last_log_entry())

    @patch('web_monitor.requests.get')
    def test_check_website_content_not_met(self, mock_get):
        mock_get.return_value.text = "invalid content"
        mock_get.return_value.status_code = 200

        website = {"url": self.url, "content_requirement": "mock response"}
        self.monitor.check_website(website)

        # Assert that the log contains the expected status
        expected_log_entry = f"URL: {self.url}, Status: Content requirement not met, Response Time: "
        self.assertIn(expected_log_entry, self.get_last_log_entry())


if __name__ == "__main__":
    unittest.main()
