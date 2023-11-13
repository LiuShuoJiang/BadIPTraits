#!/usr/bin/env python3
import database

def main():
    print("test")
    db = database.DataBase()
    
    result = db.categorizeIPsByCharacter(f_path="reform_hosts_results.json", character="location.country")
    db.writeDictToJsonFile(d=result, f_name="country.json")
    

if __name__ == "__main__":
    main()