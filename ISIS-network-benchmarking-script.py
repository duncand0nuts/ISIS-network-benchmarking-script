def file_name_reader(input_file_path):
    # open file with list of filenames:
    input_file = open (input_file_path, 'r')
    #add filenames to a dictionary
    filenames = []
    for line in input_file:
        filenames.append(line)
    return filenames

filenames = file_name_reader('filename here')

def grab_files(filenames):
    times = []
    for file in filenames:
        start = time.clock()

        load_file = Load(Filename = file)

        elapsed = (time.clock() - start)
        times.append(elapsed)
    return(times)

test = grab_files(filenames)
print test
