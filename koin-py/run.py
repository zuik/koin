# Runner for the app
from koin.twitter import main
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s [ %(threadName)s ][ %(levelname)s ]: \n%(message)s'")

    main()
