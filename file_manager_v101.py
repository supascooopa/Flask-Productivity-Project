import os


def get_file_name(**kwargs):
    """ Returns files of your choosing from your current working directory """
    list_of_file = []
    file_extension = kwargs.get("file_extension", None)
    num = 1
    if file_extension is not None:
        for files in os.listdir(os.curdir):
            if os.path.isfile(files) and files.endswith(file_extension):
                print(num, files)
                list_of_file.append(files)
                num += 1
    else:
        for index, files in enumerate(os.listdir(os.curdir)):
            if os.path.isfile(files):
                print(index, files)
                list_of_file.append(files)
    question = int(input("Please enter the corresponding number of the file: "))
    try:
        return list_of_file[question - 1]
    except IndexError:
        input("Please enter only from the numbers you see")
        get_file_name(file_extension=file_extension)



def show_inside_directory(directory):
    """ Returns all files inside a directory you specify"""
    list_of_files = [file for file in os.listdir(directory)]
    return list_of_files


def show_path_wfl(file_name):
    """ Returns the path of the current working directory with the file you specify """
    return os.path.abspath(file_name)


def show_path_wdr():
    """ Returns the path of the current working directory you specify """
    lst_of_files = []
    for number, folder in enumerate(os.listdir(os.curdir), 1):
        print(f"{number}. {folder}")
        lst_of_files.append(folder)
    question = int(input("which file do you like the path of, please enter their corresponding number: "))
    return os.path.abspath(lst_of_files[question - 1])


def new_file_name(file_extension):
    """ Lets the user enter a new file name"""
    return f"{input('please enter a file name ')}.{file_extension}"
