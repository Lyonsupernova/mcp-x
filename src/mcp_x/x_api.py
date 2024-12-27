from .utils import setup_logger
import tweepy
import os
from pydantic import Field
from dotenv import load_dotenv


load_dotenv()  # create .env file providing with following credentials
API_KEY = os.getenv("X_API_KEY")
API_KEY_SECRET = os.getenv("X_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")


class ClientX:
    def __init__(self, logger):
        """
        Initializes the X API client
        """
        self.logger = logger
        self.logger.info("Initializing X API client")
        self.client = self.get_x_client()

    def create_tweet(self, tweet_content) -> tweepy.Response:
        """
        Post a tweet using the X API client
        """
        msg: str = Field(default=None, description="Message to be posted")
        try:
            # Post a tweet
            response: tweepy.Response = self.client.create_tweet(text=tweet_content)
            self.logger.info(f"Tweet successfully created: {response.data}.")
            msg = f"Tweet successfully created: {response.data}."
        except Exception as e:
            self.logger.error(f"Error posting tweets with content: {tweet_content}, exception: {e}", exc_info=True)
            msg = f"Error posting tweets with content: {tweet_content}, exception: {e}."
        return msg

    def get_x_client(self) -> tweepy.Client:
        """
        Get the X API client using v2
        """
        client: tweepy.Client = Field(default=None, description="Tweepy API client")
        try:
            client = tweepy.Client(
                bearer_token=BEARER_TOKEN,
                consumer_key=API_KEY,
                consumer_secret=API_KEY_SECRET,
                access_token=ACCESS_TOKEN,
                access_token_secret=ACCESS_TOKEN_SECRET,
                wait_on_rate_limit=False
            )
        except Exception:
            self.logger.error("Error getting X client API", exc_info=True)
        self.logger.info("Successfully created X API client")
        return client
