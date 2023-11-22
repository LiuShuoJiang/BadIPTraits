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
        
        count = 0
        result = {'char not found': []}
        character_list = character.split(".")
        with open(f_path, "r") as f:
            j_data = json.load(f)
        
        for ip_group in j_data["data"]:
            for ip_tuple in ip_group.items():
                # check if current ip item has character, if not, continue to next ip_item
                ip_addr = ip_tuple[0]
                ip_item = ip_tuple[1]
                
                c_vals = ['char not found'] # default
                
                # if desired character is service
                if "services" in character_list[0] and 'services' in ip_item.keys(): 
                    serv_list = ip_item['services']
                    for serv in serv_list:
                        serv_name = character_list[1]
                        if serv_name == 'http':
                            if ('http' not in serv.keys()): continue
                            http_dict = serv['http']
                            if('response' not in http_dict.keys() or 'headers' not in http_dict['response'].keys()): continue
                            headers_dict = http_dict['response']['headers']
                            if ('X_XSS_Protection' in character_list[4]):
                                if ('X_XSS_Protection' in headers_dict.keys()):
                                    if '0' in headers_dict['X_XSS_Protection'][0]:
                                        c_vals[0] = 'X_XSS_Protection OFF'
                                    elif '1' in headers_dict['X_XSS_Protection'][0]:
                                        c_vals[0] = 'X_XSS_Protection ON'
                                    else:
                                        c_vals[0] = 'X_XSS_Protection UNKNOWN'
                                elif ('X_Xss_Protection' in headers_dict.keys()):
                                    if '0' in headers_dict['X_Xss_Protection'][0]:
                                        c_vals[0] = 'X_XSS_Protection OFF'
                                    elif '1' in headers_dict['X_Xss_Protection'][0]:
                                        c_vals[0] = 'X_XSS_Protection ON'
                                    else:
                                        c_vals[0] = 'X_XSS_Protection UNKNOWN'
                                else:
                                    continue
                                # if('X_XSS_Protection' not in headers_dict.keys() and 'X_Xss_Protection' not in headers_dict.keys()):
                                #     continue
                                # else:
                                #     if '0' in headers_dict['X_XSS_Protection'][0]:
                                #         c_val = 'X_XSS_Protection OFF'
                                #     elif '1' in headers_dict['X_XSS_Protection'][0]:
                                #         c_val = 'X_XSS_Protection ON'
                                #     else:
                                #         c_val = 'X_XSS_Protection UNKNOWN'
                            elif ('Content_Security_Policy' in character_list[4]):
                                if('Content_Security_Policy' not in headers_dict.keys()):
                                    continue
                                else:
                                    c_vals[0] = 'Content_Security_Policy ON'
                        elif serv_name == 'tls':
                            if ('tls' not in serv.keys()): continue
                            tls_dict = serv['tls']
                            if ('version_selected' in character_list[2]):
                                if ('version_selected' not in tls_dict.keys()): continue
                                if (tls_dict['version_selected'] in c_vals): continue
                                c_vals.append(tls_dict['version_selected'])
                            elif ('cipher_selected' in character_list[2]):
                                if ('cipher_selected' not in tls_dict.keys()): continue
                                if (tls_dict['cipher_selected'] in c_vals): continue
                                c_vals.append(tls_dict['cipher_selected'])
                            elif ('certificates' in character_list[2]):
                                if ('certificates' not in tls_dict.keys()): continue
                                leaf_dict = tls_dict['certificates']['leaf_data']
                                if ('issuer_dn' in character_list[4]):
                                    if ('issuer_dn' not in leaf_dict.keys()): continue
                                    if (leaf_dict['issuer_dn'] in c_vals): continue
                                    c_vals.append(leaf_dict['issuer_dn'])
                                elif ('common_name' in character_list[5]):
                                    if ('common_name' not in leaf_dict['issuer'].keys()): continue
                                    if (leaf_dict['issuer']['common_name'][0] in c_vals): continue
                                    c_vals.append(leaf_dict['issuer']['common_name'][0])
                                elif ('organization' in character_list[5]):
                                    if ('organization' not in leaf_dict['issuer'].keys()): continue
                                    if (leaf_dict['issuer']['organization'][0] in c_vals): continue
                                    c_vals.append(leaf_dict['issuer']['organization'][0])
                                elif ('country' in character_list[5]):
                                    if ('country' not in leaf_dict['issuer'].keys()): continue
                                    if (leaf_dict['issuer']['country'][0] in c_vals): continue
                                    c_vals.append(leaf_dict['issuer']['country'][0])
                        elif serv_name == 'extended_service_name':
                            if ('extended_service_name' not in serv.keys()): continue
                            if (serv['extended_service_name'] in c_vals): continue
                            c_vals.append(serv['extended_service_name'])
                            #an ip can have multiple services
                elif 'location' in character_list[0] and 'services' in ip_item.keys():
                    loc_dict = ip_item['location']
                    if ('country' in character_list[1]):
                        if ('country' not in loc_dict.keys()): continue
                        c_vals[0] = loc_dict['country']
                    elif ('province' in character_list[1]):
                        if ('province' not in loc_dict.keys()): continue
                        c_vals[0] = loc_dict['province']
                    elif ('city' in character_list[1]):
                        if ('city' not in loc_dict.keys()): continue
                        c_vals[0] = loc_dict['city']
                
                for c in c_vals:
                    if c not in result.keys():
                        result[c] = []
                    result[c].append(ip_addr)
                count += 1
        
        print("count: " + str(count))
        return result
    
    def writeDictToJsonFile(self, d: dict, f_name: str):
        j = json.dumps(d, indent=4)
        with open(f_name, 'w') as f:
            print(j, file=f)