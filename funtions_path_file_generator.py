import os


# curve generated
def path_file(path_file_without_prefix, prefix):  # генерирование название соответствующего файла
    path_file_prefix_def = path_file_without_prefix + '_' + str(prefix) + '.csv'

    return path_file_prefix_def


def path_file_without_prefix(folder_name, file_name, experiment, ticker):  # генерирование название соответствующего файла
    path_folder_ticker = path_folder(folder_name, experiment, ticker)

    path_file_without_prefix = path_folder_ticker + file_name

    return path_file_without_prefix


def path_folder(folder_name, experiment, ticker):  # создание папки, если еще не существует
    path_folder_ticker = folder_name + '/' + ticker + '/' + experiment + '/'
    folder_check(folder_name)

    return path_folder_ticker


def folder_check(dirName):
    try:
        os.makedirs(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    return dirName


def create_folder_or_check_existence(dirName):
    try:
        os.makedirs(dirName)
        print('Новая папка ', dirName, ' создана')
    except Exception:
        print('Папка ', dirName, ' уже существует')


def file_clear(file):
    try:
        os.remove(file)
    except Exception:
        pass

    return file


# history
def path_file_history(folder_name, history_ticker, prefix):  # генерирование название файла из history ticker
    path_file_history_def = folder_name + '/' + str(history_ticker[prefix]) + '.csv'
    print(path_file_history_def)

    return path_file_history_def
