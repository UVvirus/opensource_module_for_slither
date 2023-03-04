from web3 import  Web3

def read_contract(filename: str):
    with open(filename,'r') as read_smart_contract:
       list_of_lines = read_smart_contract.readlines()
    print(list_of_lines)
    i =0
    variable_list=[]
    for lines in list_of_lines:
        i +=1
        if "public" in lines:
            if ";" or "=" in lines:
                if not "{" in lines:  #
                    print("index and content:", i-1)
                    print(lines)
                    variable_list.append(lines.strip())
                    print("variable list:", variable_list)

    datatype= parse_datatype(variable_list)
    write_contract("TestConstant.sol",datatype,"BYTES")

# Now list_of_lines variable is like this
#   [ bytes32 public constant BYTES =\n', '\n', uint256 public someUint256 = 3;\n', ]
# we need datatype(bytes32), so we are extracting it from here
def parse_datatype(list_of_lines:list):
    datatype_list=[]
    for elements in list_of_lines:
        split=elements.split(' ')
        if len(split) > 1:
            datatype_list.append(split[0])
    print("datatype list:",datatype_list)
    return datatype_list

def parse_variable_name():
    pass

def write_contract(filename: str, datatype: list, variable_name: str):
    with open(filename, 'a') as write_smart_contract:
        getter_method = f'function read_private_variable() public view returns({datatype})' \
                        f'{{return {variable_name}; ' \
                        f'}}'
        write_smart_contract.write(getter_method)
    write_smart_contract.close()



if __name__ == "__main__":
    read_contract("TestConstant.sol")
    #write_contract("TestConstant.sol","bytes32","BYTES")
    #parse_datatype([ "bytes32 public constant BYTES =\n'", "'\n'", "uint256 public someUint256 = 3;\n'" ])
