list_me = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

counter = 0
while counter < len(list_me):
    if list_me[counter] > 0:
        print(list_me[counter])
        counter += 1

    if list_me[counter] == 0:
        counter += 1
      
    if list_me[counter] < 0:
        break

