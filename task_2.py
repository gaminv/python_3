# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, delimiter = ","):
    participants_1 = participants_1.split(delimiter)
    participants_1_res = set(participants_1)

    participants_2 = participants_2.split(delimiter)

    general_participants = participants_1_res.intersection(participants_2)
    general_participants = sorted(list(general_participants))

    return general_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter = "|"))
