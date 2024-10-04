import json
class config:
    def __init__(self,path):
        with open(path,"r",encoding="utf-8") as f:
            self.config_json=json.load(f)

    def get(self,ele_list):
        ele=ele_list[0]
        back=self.config_json[ele]
        for ele in ele_list[1:]:
            back=back[ele]
        return back