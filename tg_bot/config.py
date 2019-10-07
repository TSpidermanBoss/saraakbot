from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 491634139 # my telegram ID
    OWNER_USERNAME = "Cricket9"  # my telegram username
    API_KEY = "840055105:AAGtoLBLJBj4xlnv2Y-ZLXMibDhKd0n6UeE"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://sures:9649335799@localhost:5432/minds'  # sample db credentials
    MESSAGE_DUMP = '-1001397779415' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    STRICT_GMUTE = True
    STRICT_GBAN = True
    SUDO_USERS = [491634139,705138975]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
