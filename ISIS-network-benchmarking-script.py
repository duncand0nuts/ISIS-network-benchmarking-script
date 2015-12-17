def file_name_reader(input_file_path):
    # open file with list of filenames:
    input_file = open (input_file_path, 'r')
    #add filenames to a dictionary
    filenames = []
    for line in input_file:
        filenames.append(line)
    return filenames

filenames = file_name_reader('files.txt')

def grab_files(filenames):
    for file in filenames:
        load_file = Load(Filename = file)

test = grab_files(filenames)
