import shutil, os, glob, itertools

def getFilenames():
    files = []
    split_files = []
    for filename in glob.glob('*.*'):
        files.append(filename)
    for filename in files:
        split_files.append(filename.split('.'))
    #sort by file extension (second element)
    split_files.sort(key = lambda x: x[-1])
    
    return split_files

def createDict(split_files):
    dict_filenames = {}
    #group by extension 
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
        try:
            if not os.path.exists(key):
                os.makedirs(key)
            for filename in value:
                shutil.move('.'.join(filename), key)
                #shutil.move(filename[0]+'.'+filename[1], key)
        except:
            print(key)
            print('Error in makeDirs()')

def confirmExecute():
    #get path of file
    scriptpath = os.path.realpath(__file__)
    print('Current directory is: '+ scriptpath)
    selection = input('Confirm sorting (y/n)')
    if selection.lower() == 'y':
        return True
    else:
        return False

if confirmExecute(): #confirm execution
    split_files = getFilenames()
    dict_filenames = createDict(split_files)
    makeDirs(dict_filenames)