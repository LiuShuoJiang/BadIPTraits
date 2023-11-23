#!/usr/bin/env python3
import database

def main():
    print("test")
    db = database.DataBase()
    
    f_paths = [
            #   "ipdata/reform_hosts_results.json",
            #   "ipdata/hosts_results_200.json",
              "ipdata/hosts_results_201400.json",
              "ipdata/hosts_results_401600.json",
              "ipdata/hosts_results_601800.json",
              "ipdata/hosts_results_8011000.json",
              "ipdata/hosts_results_10011200.json",
              "ipdata/hosts_results_12011400.json",
              "ipdata/hosts_results_14011600.json",
              "ipdata/hosts_results_16011800.json",
              "ipdata/hosts_results_18012000.json",
              ]
    
    characters = ["location.country", 
                  "location.province",
                  "location.city", 
                  "services.extended_service_name", 
                  "services.transport_protocol",
                  "services.tls.version_selected", 
                  "services.tls.cipher_selected", 
                  "services.tls.certificates.leaf_data.issuer_dn", 
                  "services.tls.certificates.leaf_data.issuer.common_name", 
                  "services.tls.certificates.leaf_data.issuer.organization", 
                  "services.tls.certificates.leaf_data.issuer.country", 
                  "services.http.response.headers.X_XSS_Protection", #xss_protect: enabled, disabled, none
                  "services.http.response.headers.Content_Security_Policy" #enabled, none
                  ]
    
    # reformate data
    # format_fpaths = ['format_ipdata/hosts_results_200.json', 
    #                  'format_ipdata/reform_hosts_results.json',
    #                 ]
    
    format_fpaths = ['format_ipdata/hosts_results_200.json', 
                     'format_ipdata/reform_hosts_results.json',
                     'format_ipdata/format_hosts_results_201400.json',
                     'format_ipdata/format_hosts_results_401600.json',
                     'format_ipdata/format_hosts_results_601800.json',
                     'format_ipdata/format_hosts_results_8011000.json',
                     'format_ipdata/format_hosts_results_10011200.json',
                     'format_ipdata/format_hosts_results_12011400.json',
                     'format_ipdata/format_hosts_results_14011600.json',
                     'format_ipdata/format_hosts_results_16011800.json',
                     'format_ipdata/format_hosts_results_18012000.json',
                    ]
    
    # for fp in f_paths:
    #     format_data = db.formatJson(fp)
    #     format_fp = 'format_ipdata/format_' + fp.split('/')[1]
    #     format_fpaths.append(format_fp)
    #     with open(format_fp, "w") as f:
    #         f.write(format_data)        

    
    for c in characters:
        result = {'char not found': []}
        for fpath in format_fpaths:         
            result = db.categorizeIPsByCharacter(fpath, c, result)
        jf_name = "output/" + c.replace(".", "_") + ".json"
        db.writeDictToJsonFile(result, jf_name)
    
    # c="services.extended_service_name"
    # result = {'char not found': []}
    # for fpath in format_fpaths:         
    #     result = db.categorizeIPsByCharacter(fpath, c, result)
    # jf_name = "output/" + c.replace(".", "_") + ".json"
    # db.writeDictToJsonFile(result, jf_name)

if __name__ == "__main__":
    main()