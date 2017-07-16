import logging
import logging.config
import roger

def load_configs(environment):
    global logger
    if environment == 'desenv':
        logging.config.fileConfig('./configs/log.conf')
        logger = logging.getLogger('roger_app')

def main():
    load_configs('desenv')
    roger.start()

if __name__ == '__main__':
    main()
