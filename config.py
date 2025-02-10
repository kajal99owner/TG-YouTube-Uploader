import os


class Config(object):
    """
    Configuration class for the Telegram bot.

    Retrieves configuration values from environment variables.
    Provides default values if environment variables are not set.
    """

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7286429810:AAHBzO7SFy6AjYv8avTRKWQg53CJpD2KEbM")
    """
    Telegram bot token.  Required.
    """

    APP_ID = int(os.environ.get("APP_ID", 26489431))
    """
    Telegram API ID.  Required.  Defaults to 12345 if not set.
    """

    API_HASH = os.environ.get("API_HASH", "9a2fce85339bb79254a55368a61ab92f")
    """
    Telegram API hash.  Required.
    """

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://graph.org/file/b7e8484f6395a180b6380.jpg")
    """
    Path to the default audio thumbnail image.  Optional.
    """

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://t.me/kajal_developer/7")
    """
    Path to the default video thumbnail image.  Optional.
    """

    # Add any new configuration options here
    # For example:
    # OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Bot owner's user ID
    # DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///mydatabase.db")
    # COMMAND_PREFIX = os.environ.get("COMMAND_PREFIX", "/")
    # Use a more robust default value or raise an exception
    # if a required setting is missing.  For example, for APP_ID
    # you can replace 12345 with 0 and then add:
    # if Config.APP_ID == 0:
    #   raise ValueError("APP_ID must be set in the environment.")
    # This can be implemented at the end of the Config class.

# Example usage:
# from config import Config
# print(f"Bot Token: {Config.TG_BOT_TOKEN[:10]}...") # Print the first 10 chars
# print(f"App ID: {Config.APP_ID}")
# print(f"API Hash: {Config.API_HASH[:10]}...") # Print the first 10 chars
# print(f"Audio Thumbnail: {Config.AUDIO_THUMBNAIL}")
# print(f"Video Thumbnail: {Config.VIDEO_THUMBNAIL}")
