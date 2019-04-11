contact_id = 0
contact_list = {}
exit = True
while exit:

    print('\n======================== Меню ====================================')
    action = int(input('1-Добавить, 2-Просмотр, 3-Удалить, 4-Обновить, 0-Выход - Выбор: '))

    # Добавление контакта
    if action == 1:
        contact = input('Имя: ')
        phone = input('Телефон: ')
        company = input('Организация: ')
        course = int(input('Курс: '))
        contact_id_key = 'Контакт_' + str(contact_id)
        contact_list[contact_id_key] = list()
        contact_list[contact_id_key].append(dict(name=contact, mobile_phone=phone, organization=company, courses=course))
        contact_id += 1

    # Просмотр контактов
    if action == 2:
        for contact_key in contact_list:
            print('Ключ =>', contact_key)
            contact_values = contact_list.get(contact_key)[0]
            print('\tИмя: ', contact_values.get('name'))
            print('\tТелефон: ', contact_values.get('mobile_phone'))
            print('\tОрганизация: ', contact_values.get('organization'))
            print('\tКурс: ', contact_values.get('courses'))

    # Удаление контакта по ключу
    if action == 3:
        delete_key = input('Введить ключ контакта: ')
        contact_list.pop(delete_key)
        print('Контакт с ключом =>', delete_key, ' удален')

    # Обновление контакта
    if action == 4:
        update_key = input('Введите ключ контакта для обновление: ')
        update_item = contact_list.get(update_key)[0]
        update_contact = input('Имя: ' + update_item.get('name') + ' => ')
        update_phone = input('Телефон: ' + update_item.get('mobile_phone') + ' => ')
        update_company = input('Организация: ' + update_item.get('organization') + ' => ')
        update_course = int(input('Курс: ' + str(update_item.get('courses')) + ' => '))
        update_item.update(dict(name=update_contact, mobile_phone=update_phone, organization=update_company, courses=update_course))
        print('Контакт с ключом =>', update_key, ' обнавлен')

    # Выход
    if action == 0:
        print('\nДо свидания !')
        exit = False

