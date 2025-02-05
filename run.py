from bot import TelethonBot
from handlers.id import ID
from handlers.tagger import Tagger


if __name__ == "__main__":
    UserBot_instance = TelethonBot()
    id_instance = ID(UserBot_instance.client)
    id_instance.id_handler()
    tagger_instance = Tagger(UserBot_instance.client)
    tagger_instance.tagger_handler()
    UserBot_instance.start()