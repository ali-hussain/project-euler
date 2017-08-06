import logging
import argparse
import os

def initialize(parse_custom_args=None):
    """This method is used to parse and handle arguments """
    parser = argparse.ArgumentParser(description='CloudFormation Template Generator')
    parser.add_argument(
        '--log',
        '-l',
        nargs='?',
        default='WARN',
        help='Yaml file defining logging configurations or just log level'
    )
    if parse_custom_args is not None:
        parse_custom_args(parser)
    args, unknown = parser.parse_known_args()
    # handle standard arguments, ignore unknown arguments
    setup_logging(args.log)
    return args

def setup_logging(log_specification):
    """Setup logging configuration
    """
    if log_specification and os.path.exists(log_specification):
        with open(log_specification, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        numeric_level = getattr(logging, log_specification.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % log_specification)
        _format = "%(asctime)s - %(filename)s - %(levelname)s - %(lineno)s: %(message)s"
        logging.basicConfig(format=_format, level=numeric_level)
