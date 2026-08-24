import json

from pathlib import Path

RULES = Path("rules.json")

'''
Load categories from the rules.json file
'''

def load_categories():
    with RULES.open("r", encoding='utf-8') as file:
        rules = json.load(file)
    
    return rules["categories"]



# categories = load_categories()

# for category, extensions in categories.items():
#     print(category, "=>", extensions)
    
    
    


