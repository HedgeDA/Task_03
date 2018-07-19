def people(documents):
    number = input('введите номер документа:')
    if number == '':
        return 'не указан номер документа'
    print('выполняется поиск владельца по номеру документа:', number)

    result = 'документ не найден'
    for document in documents:
        if document['number'] == number:
            result = 'владелец документа: ' + document['name']
            break

    return result


def doclist(documents):
    print('формируем список документов...')

    result = list()
    for document in documents:
        name = document['type'] + ' "' + document['number'] + '" "' + document['name'] + '"'
        result.append(name)

    return result


def shelf(directories):
    number = input('введите номер документа:')
    if number == '':
        return 'не указан номер документа'
    print('выполняется поиск полки по номеру документа:', number)

    result = 'документ не найден'
    for shelf_num, doc_list in directories.items():
        if number in doc_list:
            result = 'номер полки: ' + shelf_num
            break

    return result


def add_document(documents, directories):
    number = input('введите номер документа:')
    if number == '':
        return 'нельзя добавить документ без указания номера'

    for index, document in enumerate(documents):
        if document['number'] == number:
            result = 'документ с номером ' + number + ' уже существует, нельзя добавить ещё один'
            return result

    type_doc = input('введите тип документа:')
    if type_doc == '':
        return 'нельзя добавить документ без указания типа'

    name = input('введите имя владельца документа:')
    if name == '':
        return 'нельзя добавить документ без указания владельца'

    shelf_num = input('введите номер полки хранения документа:')
    if shelf_num == '':
        return 'нельзя добавить документ без указания номера полки хранения'
    print('добавляем новый документ...')

    documents.append({"type": type_doc, "number": number, "name": name})
    if directories.get(shelf_num) == None:
        directories[shelf_num] = list()
        print('добавлена полка с номером:', shelf_num)
    directories[shelf_num].append(number)

    return 'добавлен документ с номером: ' + number


def delete_document(documents, directories):
    number = input('введите номер документа:')
    if number == '':
        return 'нельзя удалить документ без указания номера'
    print('выполняется поиск документа:', number)

    result = 'документ не найден'
    for index, document in enumerate(documents):
        if document['number'] == number:
            result = 'удален документ с номером: ' + number
            del documents[index]
            break

    for shelf_num, doc_list in directories.items():
        if number in doc_list:
            del doc_list[doc_list.index(number)]
            break

    return result


def move(directories):
    number = input('введите номер документа:')
    if number == '':
        return 'не указан номер документа'

    new_shelf_num = input('введите номер целевой полки:')
    if new_shelf_num == '':
        return 'не указан номер целевой полки'
    print('выполняется поиск документа:', number)

    result = 'документ не найден'
    for shelf_num, doc_list in directories.items():
        if number in doc_list:
            if shelf_num == new_shelf_num:
                result = 'документ уже находится на указанной полке'
                return

            del doc_list[doc_list.index(number)]

            if directories.get(new_shelf_num) == None:
                directories[new_shelf_num] = list()
                print('добавлена полка с номером:', new_shelf_num)
            directories[new_shelf_num].append(number)
            result = 'документ с номером ' + number + ' перемешен на полку ' + new_shelf_num

            break

    return result


def add_shelf(directories):
    shelf_num = input('введите номер полки:')
    if shelf_num == '':
        return 'нельзя добавить полку без указания номера'
    print('добавляем новую полку...')

    if directories.get(shelf_num) == None:
        directories[shelf_num] = list()
        result = 'добавлена полка с номером: ' + shelf_num
    else:
        result = 'полка с номером ' + shelf_num + ' уже существует'

    return result


def main():
    # инициализация данных
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    print('команды:')
    print('    p - поиск владельца по номеру документа')
    print('    l - список документов')
    print('    ls - список размещения документов на полоках')
    print('    s - поиск полки по номеру документа')
    print('    a - добавить документ')
    print('    d - удалить документ')
    print('    m - переместить документ')
    print('    as - добавить новую полку')
    print('    q - выход')

    while True:
        print()
        command = input('введите команду: ')

        if command.lower() == 'q':
            break
        elif command.lower() == 'p':
            print(people(documents))
        elif command.lower() == 'l':
            print(doclist(documents))
        elif command.lower() == 'ls':
            print(directories)
        elif command.lower() == 's':
            print(shelf(directories))
        elif command.lower() == 'a':
            print(add_document(documents, directories))
        elif command.lower() == 'd':
            print(delete_document(documents, directories))
        elif command.lower() == 'm':
            print(move(directories))
        elif command.lower() == 'as':
            print(add_shelf(directories))

    print()
    print('работа завершена.')


main()