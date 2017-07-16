import logging
from roger import Roger

def load_configs(environment):
    global logger
    if environment == 'desenv':
        logging.basicConfig(filename='section.log',level=logging.DEBUG)


def main():
    load_configs('desenv')

    roger_instance = Roger()
    roger_instance.start()

if __name__ == '__main__':
    main()
