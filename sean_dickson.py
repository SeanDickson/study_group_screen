import yaml
myDict = {'first_name':'Sean',
        'last_name':'Dickson',
        'company':'Boeing',
        'github_username':'SeanDickson',
        'email_address':'sean.m.dickson@boeing.com'
        }

myList = [myDict]
print(myList)

with open('sean_dickson.yml', 'w') as outfile:
    yaml.dump(myList, outfile, default_flow_style=False)
