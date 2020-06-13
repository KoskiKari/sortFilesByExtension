import shutil, os, glob, itertools, pyautogui

def getFilenames():
    files = []
    split_files = []
    for filename in glob.glob('*.*'):
        files.append(filename)
    for filename in files:
        split_files.append(filename.split('.'))

    #sort by file extension (last element)
    split_files.sort(key = lambda x: x[-1])
    
    return split_files

def createDict(split_files):
    dict_filenames = {}
    #group by file extensions
    for key, group in itertools.groupby(split_files, lambda x: x[-1]):
        for item in group:
            #create a key if not in dict - item in brackets to convert it in list format
            if key not in dict_filenames:
                dict_filenames[key] = [item]
            else:
                dict_filenames[key].append(item)

    return dict_filenames

def makeDirs(dict_filenames):
    for key, value in dict_filenames.items():
        #is this outer try/except redundant?
        try:
            if not os.path.exists(key):
                os.makedirs(key)
            for filename in value:
                #prevent sorting the script itself
                if filename[0] == 'sortFiles':
                    continue
                try:
                    shutil.move('.'.join(filename), key)
                except Exception as e:
                    print('Error in shutil.move:',e)
        except Exception as e:
            print(value,key)
            print('Error in makedirs:',e)

def confirmExecute():
    #get the path to the script
    scriptpath = os.path.realpath(__file__)

    #console confirmation
    #print('Current directory is: '+ scriptpath)
    #selection = input('Confirm sorting (y/n)')

    #confimation via message box ( OK / Cancel )
    selection = pyautogui.confirm(f'Current location to sort:\n{scriptpath}')

    if selection.lower() == 'ok':
        return True
    else:
        return False

if confirmExecute(): #confirm execution
    split_files = getFilenames()
    dict_filenames = createDict(split_files)
    makeDirs(dict_filenames)