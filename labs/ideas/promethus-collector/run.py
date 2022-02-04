import registry
from pollster import Pollster
from producer import ProducerThread
from producer_conf import producers


def mock():
    producer = ProducerThread(producers)
    producer.start()
    plugins = registry.setup_check_plugin()
    pollster = Pollster(plugins, 15)
    pollster.run()


if __name__ == "__main__":
    mock()