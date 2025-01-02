from food_personality_bot import FoodPersonalityBot
from config import *
import sys

def run_bot():
    try:
        print("Starting Food Personality Bot...")
        bot = FoodPersonalityBot(
            api_key=TWITTER_API_KEY,
            api_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
        )
        print("Bot initialized successfully!")
        bot.listen_for_mentions()
    except KeyboardInterrupt:
        print("\nBot stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error running bot: {str(e)}")

if __name__ == "__main__":
    run_bot()
