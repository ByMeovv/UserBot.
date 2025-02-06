from bot import TelethonBot
from handlers.id import ID
from handlers.tagger import Tagger


if __name__ == "__main__":
    UserBot_instance = TelethonBot()
    ID(UserBot_instance.client).id_handler()
    Tagger(UserBot_instance.client).tagger_handler()
    UserBot_instance.start()