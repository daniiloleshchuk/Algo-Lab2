from IO import get_input_data, write_data


file_name = 'in/hamsters.in2'

data = get_input_data(file_name)
daily_food_supply = data['s']
total_hamsters = data['c']
hamsters = data['hamsters']

taken_hamsters = 0
available_daily_supply = daily_food_supply

previous_hamster_greediness = 0
checked_hamsters = 0
while available_daily_supply > 0 and checked_hamsters < total_hamsters:

    cur_hamster = hamsters.get_min_value()
    checked_hamsters += 1

    if taken_hamsters > 0:
        if checked_hamsters == 2:
            available_daily_supply -= previous_hamster_greediness

        if available_daily_supply >= (cur_hamster.daily_norm + cur_hamster.greediness):
            taken_hamsters += 1
            available_daily_supply -= (cur_hamster.daily_norm + cur_hamster.greediness)
            hamsters.remove_min_element()
        else:
            break
    else:
        if cur_hamster.daily_norm <= available_daily_supply:
            taken_hamsters += 1
            available_daily_supply -= cur_hamster.daily_norm
            previous_hamster_greediness = cur_hamster.greediness
            hamsters.remove_min_element()

print(taken_hamsters)
write_data(file_name, taken_hamsters)





