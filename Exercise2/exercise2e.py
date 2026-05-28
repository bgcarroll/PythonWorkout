
def sum_objects(objects):

    total = 0

    for object in objects:
        try:
            total += int(object)
        except TypeError as ex:
            # end up in here for list, tuple, dict
            print(f"Error Message: {ex}")
            try:
                if type(object) in (list, tuple):
                    for element in object:
                        try:
                            total += int(element)
                        except ValueError as ex:
                            print(f"Error Message: {ex}")
                if type(object) == dict:
                    for element in object.values():
                        try:
                            total += int(element)
                        except ValueError as ex:
                            print(f"Error Message: {ex}")
            except:
                print('blew up here')
        except ValueError as ex:
            print(f"Error Message: {ex}")

    return total



print(sum_objects([{1: 55, 2: 45}, '13', 'foo', [1,2,3], 4.5, [1,2,'foo', 50], (1,1,2)]))
