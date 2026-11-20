def common_friends(list1, list2):
    result = []

    for name in list1:
        if name in list2:
            result.append(name)

    result.sort()
    return result

def only_first(list1, list2):
    result = []

    for name in list1:
        if name not in list2:
            result.append(name)

    return result   

ali = ["Aysel", "Murad", "Leyla", "Elvin"]
vali =["Leyla", "Nigar", "Aysel", "Kamal"]
print("Ortaq dostlar:", common_friends(ali, vali))
print("Yalniz birinci siyahi:", only_first(ali, vali))