
""""MY FIRST ATTEMPT OF SOLUTION"""
# def is_there_a_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config):
#     seats_per_subgroup = num_of_chars // num_of_subgroups
#     slots = seat_config.split('|')
#     goal_slots = [seats_per_subgroup]
#     goal_slots *= num_of_subgroups
#     empty_seats_per_slot = []
#     for slot in slots:
#         empty_seats = 0
#         for i in slot:
#             if i == "O":
#                 empty_seats += 1
#         empty_seats_per_slot.append(empty_seats)
#     empty_seats_per_slot = sorted(empty_seats_per_slot)
#     empty_seats_per_slot = empty_seats_per_slot[::-1]
#     for i in range(len(empty_seats_per_slot)-num_of_subgroups):
#         empty_seats_per_slot.pop()
#     print(empty_seats_per_slot,goal_slots)
#
#     if empty_seats_per_slot >= goal_slots:
#         return "YES"
#     else:
#         return "NO"


"""
    #     slot = slot.replace("O", "S", seats_per_subgroup)
    #     last_slots.append(slot)
    # 
    # return last_slots
    #     for i in range(len(slot)):
    #         if slot[i] == "S":
    #             slot_counter += 1
    #             print(slot_counter)
    # if slot_counter == num_of_chars:
    #     return "YES"
    # else:
    #     return "NO" """

# def is_there_a_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config):
#     num_people_per_subgroup = num_of_chars // num_of_subgroups
#     slots = seat_config.split("|")
#     empty_seats = 0
#     last_slots = []
#     for slot in slots:
#         for i in range(len(slot)):
#             if slot[i] == "O":
#                 empty_seats += 1
#         if empty_seats >= num_people_per_subgroup:
#             for i in range(len(slot)):
#                 slot = slot.replace("O","S", num_people_per_subgroup)
#     return slots
def is_there_a_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config):
    seats_per_subgroup = num_of_chars // num_of_subgroups
    slots = seat_config.split('|')
    last_seat_config = ""
    reserved_seats = 0
    for slot in slots:
        empty_seats = 0
        for i in range(len(slot)):
            if slot[i] == "O":
                empty_seats += 1
        solution = slot
        while empty_seats >= seats_per_subgroup:
            solution = solution.replace("O", "S", seats_per_subgroup)
            empty_seats = 0

            for i in range(len(solution)):
                if solution[i] == "O":
                    empty_seats += 1


        last_seat_config = last_seat_config + solution + "|"
    last_seat_config = last_seat_config[:len(last_seat_config)-1:]
    for i in range(len(last_seat_config)):
        if last_seat_config[i] == "S":
            reserved_seats += 1
    print(last_seat_config)
    if reserved_seats == num_of_chars:
        return "YES"
    else:
        return "NO"













print(is_there_a_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO'))
print(is_there_a_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO'))
print(is_there_a_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO'))