from utils.config import config


class history():
    def __init__(self,path):
        self.config=config(path)
        self.list_type=[{'type': '', 'data':""},{'type': '', 'data':""},{'type': '', 'data':""}]#先加一点，外边防止list out of range
        self.history_list={
            "id_list":[],
            "id":[]
        }

    def store_content(self,id,content):
        if id not in self.history_list["id_list"]:
            self.history_list["id_list"].append(id)
            self.history_list[str(id)]=self.list_type.copy()
            self.history_list[str(id)].append(content)
        else:
            self.history_list[str(id)].append(content)


