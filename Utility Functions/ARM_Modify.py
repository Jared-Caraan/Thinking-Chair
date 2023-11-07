import json

def segmentParams(data):

    counter = 1
    param_obj = {}
    for ind, val in enumerate(data['parameters']):
        if (ind % 255 == 0 and ind != 0):
            param_obj[val] = data['parameters'][val]

            json_dict = {
                "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
                "contentVersion": "1.0.0.0",
                "parameters": param_obj
            }
            json_object = json.dumps(json_dict, indent=4)
            with open(r"C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\General\Scripts\arm_template\parameters_{}.json".format(counter), 'w' ) as f:
                f.write(json_object)
            param_obj = {}
            counter += 1
        else:
            param_obj[val] = data['parameters'][val]
    
    if param_obj:
        json_dict = {
            "parameters": param_obj
        }
        json_object = json.dumps(json_dict, indent=4)
        with open(r"C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\General\Scripts\arm_template\parameters_{}.json".format(counter), 'w' ) as f:
            f.write(json_object)

def extractResource(data):
    variable_obj = data['variables']
    resource_obj = data['resources']

    json_dict = {
        "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "variables": variable_obj,
        "resources": resource_obj
    }

    json_object = json.dumps(json_dict, indent=4)
    with open(r"C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\General\Scripts\arm_template\resources.json", 'w' ) as f:
        f.write(json_object)

def showResourceCategory(data):
    resource_set = set()

    for i in data['resources']:
        resource_set.add(i['type'])
    
    return resource_set

def main():
    f = open(r'C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\General\Scripts\arm_template\ARMTemplateForFactory.json')

    data = json.load(f)
    
    option = 'resources'

    if option == 'parameters':
        segmentParams(data)
    elif option == 'resources':
        extractResource(data)
    elif option == 'show_resources':
        showResourceCategory(data)

if __name__ == "__main__":
    main()