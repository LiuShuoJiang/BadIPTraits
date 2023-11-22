#!/usr/bin/env python3
import database

def main():
    print("test")
    db = database.DataBase()
    
    f_path = "reform_hosts_results.json"
    characters = ["location.country", 
                  "location.province",
                  "location.city", 
                #   "services", # traffic on record or no record
                  "services.extended_service_name", 
                  "services.tls.version_selected", 
                  "services.tls.cipher_selected", 
                  "services.tls.certificates.leaf_data.issuer_dn", 
                  "services.tls.certificates.leaf_data.issuer.common_name", 
                  "services.tls.certificates.leaf_data.issuer.organization", 
                  "services.tls.certificates.leaf_data.issuer.country", 
                  "services.http.response.headers.X_XSS_Protection", #xss_protect: enabled, disabled, none
                  "services.http.response.headers.Content_Security_Policy" #enabled, none
                  ]
    
    for c in characters:
        result = db.categorizeIPsByCharacter(f_path, c)
        jf_name = c.replace(".", "_") + ".json"
        db.writeDictToJsonFile(result, jf_name)
    
    # c = 'services.tls.certificates.leaf_data.issuer.common_name'
    # result = db.categorizeIPsByCharacter(f_path, c)
    # jf_name = c.replace(".", "_") + ".json"
    # db.writeDictToJsonFile(result, jf_name)
    

if __name__ == "__main__":
    main()