# File for utilities

# Function to make sure that the list contains only integers
# Returns true if list only contains integers, otherwise false
def checkList(list) -> bool:
    for i in list:
        if type(i) is not int:
            return False
    
    return True