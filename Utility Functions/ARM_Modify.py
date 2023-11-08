import json
import os

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
            "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.0",
            "parameters": param_obj
        }
        json_object = json.dumps(json_dict, indent=4)
        with open(r"C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\General\Scripts\arm_template\parameters_{}.json".format(counter), 'w' ) as f:
            f.write(json_object)

def extractResource(data):
    variable_obj = data['variables']
    resource_obj = data['resources']

    dataflows_obj = [ele for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/dataflows']
    triggers_obj = [ele for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/triggers']
    pipelines_obj = [ele for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/pipelines']
    datasets_obj = [ele for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/datasets']
    ir_obj = [ele for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/datasets']

    json_dict = {
        "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
            "factoryName": {
                "type": "string",
                "metadata": "Data Factory name",
                "defaultValue": "ARF-EUN-AXERIA-PROD-ADF01"
            }
        },
        "variables": variable_obj,
        "resources": triggers_obj
    }

    json_object = json.dumps(json_dict, indent=4)
    with open(r"C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\Migration\ADF\arm_template\triggers_resources.json", 'w' ) as f:
        f.write(json_object)

def showResourceCategory(data):
    resource_set = set()

    for i in data['resources']:
        resource_set.add(i['type'])
    
    return resource_set

def linked_compare_params(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_param_set = set()

    linked_param_set = set()

    for _, val in enumerate(basis_data['parameters']):
                basis_param_set.add(val)

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            for _, val in enumerate(data['parameters']):
                linked_param_set.add(val)
    
    return sorted(linked_param_set) == sorted(basis_param_set)

def linked_compare_dataflows(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_dataflow_set = set()

    linked_dataflow_set = set()
    linked_dataflows_obj = []

    resource_obj = basis_data['resources']
    dataflows_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/dataflows']
    for i in dataflows_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_dataflow_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_dataflows_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/dataflows'])
    
    for i in linked_dataflows_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_dataflow_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    return sorted(basis_dataflow_set) == sorted(linked_dataflow_set)

def linked_compare_pipelines(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_pipeline_set = set()

    linked_pipeline_set = set()
    linked_pipeline_obj = []

    resource_obj = basis_data['resources']
    pipeline_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/pipelines']
    for i in pipeline_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_pipeline_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_pipeline_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/pipelines'])
    
    for i in linked_pipeline_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_pipeline_set.add(i[opening_quote_ind + 2 : closing_quote_ind])
    
    return sorted(basis_pipeline_set) == sorted(linked_pipeline_set)

def linked_compare_datasets(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_dataset_set = set()

    linked_dataset_set = set()
    linked_dataset_obj = []

    resource_obj = basis_data['resources']
    dataset_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/datasets']
    for i in dataset_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_dataset_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_dataset_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/datasets'])
    
    for i in linked_dataset_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_dataset_set.add(i[opening_quote_ind + 2 : closing_quote_ind])
    
    return sorted(basis_dataset_set) == sorted(linked_dataset_set)

def linked_compare_ls(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_ls_set = set()

    linked_ls_set = set()
    linked_ls_obj = []

    resource_obj = basis_data['resources']
    ls_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/linkedServices']
    for i in ls_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_ls_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_ls_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/linkedServices'])
    
    for i in linked_ls_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_ls_set.add(i[opening_quote_ind + 2 : closing_quote_ind])
    
    return sorted(basis_ls_set) == sorted(linked_ls_set)

def linked_compare_trigger(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_trigger_set = set()

    linked_trigger_set = set()
    linked_trigger_obj = []

    resource_obj = basis_data['resources']
    trigger_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/triggers']
    for i in trigger_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_trigger_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_trigger_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/triggers'])
    
    for i in linked_trigger_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_trigger_set.add(i[opening_quote_ind + 2 : closing_quote_ind])
    
    return sorted(basis_trigger_set) == sorted(linked_trigger_set)

def linked_compare_ir(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_ir_set = set()

    linked_ir_set = set()
    linked_ir_obj = []

    resource_obj = basis_data['resources']
    ir_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/integrationRuntimes']
    for i in ir_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_ir_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_ir_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/integrationRuntimes'])
    
    for i in linked_ir_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_ir_set.add(i[opening_quote_ind + 2 : closing_quote_ind])
    
    return sorted(basis_ir_set) == sorted(linked_ir_set)

def linked_compare_mvn(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_mvn_set = set()

    linked_mvn_set = set()
    linked_mvn_obj = []

    resource_obj = basis_data['resources']
    mvn_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/managedVirtualNetworks']
    for i in mvn_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_mvn_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_mvn_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/managedVirtualNetworks'])
    
    for i in linked_mvn_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_mvn_set.add(i[opening_quote_ind + 2 : closing_quote_ind])
    
    return sorted(basis_mvn_set) == sorted(linked_mvn_set)

def linked_compare_mpe(basis_dir, linked_dir):
    basis_f = open(basis_dir)
    basis_data = json.load(basis_f)
    basis_mpe_set = set()

    linked_mpe_set = set()
    linked_mpe_obj = []

    resource_obj = basis_data['resources']
    mpe_obj = [ele['name'].split(',')[1] for ele in resource_obj if ele['type'] == 'Microsoft.DataFactory/factories/managedVirtualNetworks/managedPrivateEndpoints']
    for i in mpe_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        basis_mpe_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    for filename in os.listdir(linked_dir):
        f = os.path.join(linked_dir, filename)
        if f.find('master') == -1:
            f_open = open(f)
            data = json.load(f_open)
            linked_data = data['resources']
            linked_mpe_obj.extend([ele['name'].split(',')[1] for ele in linked_data if ele['type'] == 'Microsoft.DataFactory/factories/managedVirtualNetworks/managedPrivateEndpoints'])
    
    for i in linked_mpe_obj:
        opening_quote_ind = i.find("'")
        closing_quote_ind = i.find("'", opening_quote_ind + 1)
        linked_mpe_set.add(i[opening_quote_ind + 2 : closing_quote_ind])

    return sorted(basis_mpe_set) == sorted(linked_mpe_set)

def main():
    basis_dir = r'C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\Migration\ADF\arm_template\ARMTemplateForFactory.json'
    linked_dir = r'C:\Users\Jared\Documents\Files\Jared\Work\Arch\Classified\Migration\ADF\arm_template\linkedTemplates'

    
    print(linked_compare_params(basis_dir, linked_dir))
    print(linked_compare_dataflows(basis_dir,linked_dir))
    print(linked_compare_pipelines(basis_dir, linked_dir))
    print(linked_compare_datasets(basis_dir, linked_dir))
    print(linked_compare_ls(basis_dir, linked_dir))
    print(linked_compare_trigger(basis_dir, linked_dir))
    print(linked_compare_ir(basis_dir, linked_dir))
    print(linked_compare_mvn(basis_dir, linked_dir))
    print(linked_compare_mpe(basis_dir, linked_dir))
    
    # option = 'resources'

    # if option == 'parameters':
    #     segmentParams(data)
    # elif option == 'resources':
    #     extractResource(data)
    # elif option == 'show_resources':
    #     print(showResourceCategory(data))

if __name__ == "__main__":
    main()