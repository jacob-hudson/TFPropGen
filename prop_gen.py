import json

variable_items = [] 

with open("ansible_facts.json") as json_file:
    json_data = json.load(json_file)
    for key in json_data.keys():
        if key.startswith("terraform_ec2_"):
            variable_items.append(json.dumps(key).replace('"', '') + " = " + json.dumps(json_data[key]))

with open('external_vars.tfvars', 'w') as tfvars:
    for var_item in variable_items:
        tfvars.write(var_item + '\n')
            