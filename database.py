import json

class DataBase(object):
    # def __init__(self):
        
        
    def getIPs(self, file_path: str) -> list[str]:
        ip_list = []
        with open(file_path, "r") as file:
            for line in file:
                if ("#" in line): 
                    line = line.split('#', 1)[0]
                    if(len(line) == 0): continue
                ip_list.append(line.strip())
        
        print(str(ip_list))
        
    def formatJson(self, f_path: str):
        # TODO: read data as string, then modify
        # find all "}{"
        #{
            # "foo": [
            #   {},  
            # ]
        #}
        
        # with open(f_path, "r+") as f:
        #     for 
        return 0
        
    def categorizeIPsByCharacter(self, f_path: str, character: str):
        
        result = {}
        character_list = character.split(".")
        with open(f_path, "r") as f:
            j_data = json.load(f)
        
        for ip_group in j_data["data"]:
            for ip_item in ip_group.items():
                # check if current ip item has character, if not, continue to next ip_item
                try:
                    ip_addr = ip_item[0]
                    c_val = ip_item[1]
                    for c in character_list:
                        c_val = c_val[c]
                except KeyError:
                    continue # skip if current ip item does not have requested character
                
                if c_val not in result.keys():
                    result[c_val] = []
                
                result[c_val].append(ip_addr)
                
        return result
    
    def writeDictToJsonFile(self, d: dict, f_name: str):
        j = json.dumps(d, indent=4)
        with open(f_name, 'w') as f:
            print(j, file=f)