node_parent = {0: None}
node_data = {0: "root"}
node_position = {0: None}
tree_length =  len((node_data))
tree_depth = 0
unique_parents = []
# 0 is the identifier number of the root node

def getDepth():
    listOfValues = list(node_parent.values())
    for value in listOfValues:
        if value not in unique_parents:
            unique_parents.append(value)
    tree_depth = len(unique_parents)

def getKeysByValue(dictOfElements, valueToFind): # This should be ignored, it is just a function that creates a list of all key names that contain a searched value in a dict (for parent max)
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys

def createNode(position, parent, value): # For position: 0 = Root, 1 = Left and 2 = Right
    listOfKeys = getKeysByValue(node_parent, parent)
    totalChilds = len(listOfKeys)
    if(totalChilds==2):
        print("Error! Parent can't have more than two childs in a binary tree!")
    else:
        temp_identifier = tree_length + 1
        node_parent[temp_identifier] = parent
        node_data[temp_identifier] = value
        node_position[temp_identifier] = position
        tree_length =  len((node_data))
        getDepth()


