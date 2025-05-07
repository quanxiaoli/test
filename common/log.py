import  logging,time
import function
from common.function import project_path


class FrameLog:
    def __init__(self,logger=None):
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #创建一个handler
        self.log_time=time.strftime('%Y-%m-%d')
        self.log_path=project_path()+"/common/"
        self.log_name=self.log_path+self.log_time+"log.log"