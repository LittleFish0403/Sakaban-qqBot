from utils.config import config
from utils.audio import audio
from utils.history import history
from utils.sd import sd
from utils.youki import youki


class handle:
    def __init__(self,path):
        self.config=config(path)
        self.history=history(path)
        if self.config.get(["enable","audio"]):
            self.audio=audio(path)
        else:
            self.audio=None
        if self.config.get(["enable","sd"]):
            self.sd=sd(path)
        else:
            self.sd=None
        if self.config.get(["enable","youki"]):
            self.youki=youki(path)
        else:
            self.youki=None
        self.user_inf=self.config.get(["user_inf"])



        
