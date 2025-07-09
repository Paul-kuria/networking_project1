import requests
from config.config import configuration
from config.custom_logging import logger

class NgrokAPIs:
    def __init__(self):
        self.base_url = "https://api.ngrok.com"
        self.headers={
                "Authorization": f"Bearer {configuration.NGROK_API_KEY1}",
                "Ngrok-Version": "2",
            }

    def get_all_endpoints(self):
        """Get all endpoints for the ngrok account in question.
        """
        
        logger.info("Fetch all started logs")

        res = requests.get(
            url=f"{self.base_url}/api_keys",
            headers=self.headers
        )
        status_code = res.status_code
        res.raise_for_status()

        if status_code == 200:
            logger.success("Successfully fetched data from ngrok. \n")
            logger.info(res.json()) 
        else:
            logger.error(f"Error fetching data, response code: {status_code}")



def main():
    ngrok = NgrokAPIs()
    ngrok.get_all_endpoints()

if __name__ == "__main__":
    main()

