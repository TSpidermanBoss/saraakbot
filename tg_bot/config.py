from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 491634139 # my telegram ID
    OWNER_USERNAME = "Cricket9"  # my telegram username
    API_KEY = "511016924:AAHHmS_NafrmUawma9PpfRueQUEFAOY7BJw"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1001397779415' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    STRICT_GMUTE = True
    STRICT_GBAN = True
    SUDO_USERS = [491634139,705138975]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation', 'memes']
