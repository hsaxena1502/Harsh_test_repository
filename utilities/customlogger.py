import logging

class LogGen:
    logging.basicConfig(filename= ".\\logs\\automation.log",format = '%(asctime)s:%(levelname)s: %(message)s', datefmt= '$m%d%y %I:%S:%S %p')
    logger =logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


