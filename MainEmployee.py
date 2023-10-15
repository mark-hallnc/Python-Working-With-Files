import pickle
import emp
#import os.path

def main():

    #Open the file
    employeeDictionary = openFile()
      
    #display the menu.
    menu()
    #Get the menu choice.
    menuChoice = int(input('Enter your choice: '))
    #while choice is valid...
    while menuChoice >= 1 or menuChoice <= 5:
        # choice 1 calls method to look up employee, passing the dict to it.
        if menuChoice == 1:
            lookup(employeeDictionary)            
        # choice 2 calls method to add employee, passing the dict to it.    
        elif menuChoice == 2:
            addEmployee(employeeDictionary)    
        # choice 3 calls method to modify employee, passing the dict to it.    
        elif menuChoice == 3:
            modifyEmployee(employeeDictionary)
        # choice 4 calls method to remove employee, passing the dict to it.    
        elif menuChoice == 4:
            removeEmployee(employeeDictionary)
        # choice 5 displays exit message and exits the program.
        elif menuChoice == 5:
            print("Exiting program.")
            exit()
        else:
            #Display error message if choice is out of range
            print("Invalid entry.")
            #Prompt again for the choice.
            menu()
            menuChoice = int(input('Enter your choice: '))
                 
    #pickle and close file.
    saveFile(employeeDictionary)      

def openFile():
    #Try to open the file and if it does not exist,
    #Create it.
    try:
        fileToOpen = open('employee.dat' , 'rb')
        data = pickle.load(fileToOpen)
        fileToOpen.close()
    except IOError:
        openNewFile = open('employee.dat', 'wb')
        data = {}
    return data

def saveFile(employeeDictionary):
    #fileToSave = open('employee.dat', 'wb')
    pickle.dump(employeeDictionary, fileToSave)
    fileToSave.close()
    
def lookup(employeeDictionary):
    
        #Get the name to search.
        nameToLookup = input("Name to search: ")
        #See if name is in dictionary.
        if nameToLookup in employeeDictionary:        
            nameFound = employeeDictionary.get(nameToLookup)
            #Show result.  
            if nameFound:
                print(nameFound, " was located in the dictionary")
                return
                
        else:
            print("Name not found.")
            return
        
def addEmployee(employeeDictionary):

    #Get the employee's info.
    name = input("Enter employee name: ")
    id_number = input("Enter the ID number: ")
    department = input("Enter Department: ")
    title = input("Enter Job title: ")
    #Make sure the employee is not already in dictionary.
    if name not in employeeDictionary:
        #Add new employee to dictionary.
        newEmp = emp.Employee(name, id_number, department, title)
        employeeDictionary[newEmp] = newEmp
        #Show the results.
        print (name, " has been added.")
    else:
        print (name, " already exists.")

    return employeeDictionary

    #Return to the menu.
    menu()


def modifyEmployee(employeeDictionary):

    #Get name to look up.
    search = input("Enter the name you want to modify: ")
    #See if name is in the dictionary.
    if search in employeeDictionary:
        #Get new infor for employee.
        name = input("Enter employee name: ")
        id_number = input("Enter new the ID number: ")
        department = input("Enter new Department: ")
        title = input("Enter new Job title: ")
        #Add new info to dictionary.
        choice = emp.Employee(name ,id_number, department, title)
        employeeDictionary[name] = choice
        #Show result.
        print (name, "has been modified.")
    else:
        print ("Name not found")

    return employeeDictionary

def removeEmployee(employeeDictionary):

    #Get the name to remove.
    nameToRemove = input("Enter employee to remove: ")
    #Check if the name is in the dictionary.
    if nameToRemove in employeeDictionary:
        #Delete the name from the dictionary.
        del employeeDictionary[nameToRemove]
        #Display result.
        print (nameToRemove, " has been removed.")
    else:
        print ("Name not found.")
    return employeeDictionary
        
def menu():

    #Menu items.
    print("______: Employee Data Structure :______")
    print("______:        Main Menu        :______")
    print("1. Look up an employee in the dictionary")
    print("2. Add a new employee to the dictionary")
    print("3. Modify employee's name, department, and job title in the dictionary")
    print("4. Delete an employee from the dictionary")
    print("5. Quit the program")

main()








