from bot import TelethonBot
from handlers.id import ID
from handlers.tagger import Tagger
from handlers.fox_handler import FoxHandler


if __name__ == "__main__":
    UserBot_instance = TelethonBot()
    ID(UserBot_instance.client).id_handler()
    Tagger(UserBot_instance.client).tagger_handler()
    FoxHandler(UserBot_instance.client).fox_handler()
    UserBot_instance.start()