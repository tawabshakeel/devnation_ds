def concat_lst(list_1, list_2):
    final_list = []
    for element in list_2:
        list_1.append(element)
    for element in list_1:
        if element not in final_list:
            final_list.append(element)
    return final_list


