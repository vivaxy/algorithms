from common.assert_list_node_equal import assertListNodeEqual

def assertListNodeArrayEqual(array1, array2):
    if (len(array1) != len(array2)):
        print(str(len(array1)) + ' len != ' + str(len(array2)))
        return False
    return all(assertListNodeEqual(array1[i], array2[i]) for i in range(len(array1)))
