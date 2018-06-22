from .color import Color
import logging
from django.utils.timezone import now

# TODO: implement the routine for making actual log file.
class Log:
    logger = logging.getLogger('Codebrick')

    @classmethod
    def warning(self, msg):
        rv = Log.logger.findCaller()
        last_segment_of_path = rv[0].split('/')[-1:][0]
        print(Color.fg.yellow + str(now()), ' W '  + msg + Color.reset + ' @' + last_segment_of_path + ':' + str(rv[1]), sep='')
    
    @classmethod
    def error(self, msg):
        rv = Log.logger.findCaller()
        last_segment_of_path = rv[0].split('/')[-1:][0]
        print(Color.fg.yellow + str(now()), ' E '  + msg + Color.reset + ' @' + last_segment_of_path + ':' + str(rv[1]), sep='')

    @classmethod
    def debug(self, msg):
        rv = Log.logger.findCaller()
        last_segment_of_path = rv[0].split('/')[-1:][0]
        print(Color.fg.yellow + str(now()), ' D '  + msg + Color.reset + ' @' + last_segment_of_path + ':' + str(rv[1]), sep='')