import json
import time
import requests
import logging


class WebMonitor:
    def __init__(self, config_file, logging_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        logging.basicConfig(filename=logging_file, level=logging.INFO)

    def monitor(self):
        while True:
            for website in self.config["websites"]:
                self.check_website(website)
            time.sleep(self.config["checking_period_seconds"])

    @staticmethod
    def check_website(website):
        url = website["url"]
        content_requirement = website["content_requirement"]

        try:
            start_time = time.time()
            response = requests.get(url)
            elapsed_time = time.time() - start_time

            if response.status_code == 200:  # Successful connection
                if content_requirement in response.text:
                    status = "Content requirement met"
                else:
                    status = "Content requirement not met"
            else:
                status = f"Connection error: {response.status_code}"

            result = f"URL: {url}, Status: {status}, Response Time: {elapsed_time} seconds"
            print(result)
            logging.info(result)
        except requests.exceptions.RequestException as e:
            logging.error(f"URL: {url}, Error: {str(e)}")


if __name__ == "__main__":
    monitor = WebMonitor('config.json', 'monitoring.log')
    monitor.monitor()
