import os

path = ["C:", ""]

def display(directories):
    print(f"|------------|")
    for i, file in enumerate(directories):
        print(f"{i+1}_{file}")
    
    print(f"|------------|")
    
def getDirectories(path):
    return [dir for dir in os.listdir("/".join(path)) if os.path.isdir("/".join(path) + dir + "/")]
def getFiles(path):
    return [dir for dir in os.listdir("/".join(path)) if not(os.path.isdir("/".join(path) + dir + "/"))]

def search(target, currentPath):
    try:
        files = getFiles(currentPath)
        directories = getDirectories(currentPath)
    except:
        return []
    results = []
    for file in files:
        if target in file.lower():
            results.append({"Name": file, "Type": "File", "Path": "/".join(currentPath)})
    for dir in directories:
        if target in dir.lower():
            results.append({"Name": dir, "Type": "Folder", "Path": "/".join(currentPath)})
        nextPath = currentPath
        nextPath.insert(len(nextPath)-1, dir)
        results.extend(search(target, nextPath))
        currentPath.pop(len(currentPath)-2)
    return results

def displaySearchResults(results):
    for result in results:
        print(f"Type: {result['Type']}; Name: {result['Name']}; Path: {result['Path']}")
    
def main():
    global path
        
    while True:
        directories = getDirectories(path)
        userInput = input(f"{'/'.join(path)}>")
        userInput = userInput.split(" ")
        if userInput[0] == "":
            pass
        elif len(userInput) == 1:
            if userInput[0].lower() == "quit":
                return False
            elif userInput[0].lower() == "dir":
                display(directories)
            elif userInput[0].lower() == "search":
                print("ERROR: Search [File Name]")
            elif userInput[0].lower() == "cd":
                if len(path) > 2:
                        path.pop(len(path)-2)
                else:
                    print("ERROR: Cannot Go Back")
            else:
                print("ERROR: Unknown Command")
            
        elif len(userInput) == 2 and userInput[0].lower() == "cd":
            if userInput[1].isdigit():
                selectedDirNumber = int(userInput[1])
                if 0 < selectedDirNumber <= len(directories):
                    selectedDir = directories[selectedDirNumber-1]
                    path.insert(len(path)-1, selectedDir)
                else:
                    print("ERROR: Unknown ID")
            else:
                print("ERROR: CD [ID]")
        elif len(userInput) >= 2 and userInput[0].lower() == "search":
            target = " ".join(userInput[1:]).lower()
            print(f"Searching For \"{target}\"...")
            results = search(target, path)
            displaySearchResults(results)
                
        
if __name__ == "__main__":
    main()