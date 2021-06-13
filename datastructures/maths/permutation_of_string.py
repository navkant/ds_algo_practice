def get_permutations(string):
    print('called')
    hash_map = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                24: 'x', 25: 'y', 26: 'z'}
    starting_alph = sorted([s for s in string])
    start_range = [str(list(hash_map.keys())[list(hash_map.values()).index(x)]) for x in starting_alph]
    rev_str = start_range[::-1]
    special_dict = {}
    for i in range(int(''.join(start_range)), int(''.join(rev_str))+1):
        digit_list = [x for x in str(i)]
        if not set(str(list(hash_map.keys())[list(hash_map.values()).index(x)]) for x in starting_alph).issubset(set(digit_list)):
            # import pdb; pdb.set_trace()
            continue
        alph_list = [hash_map[int(j)] for j in str(i)]
        unique_string = ''.join(alph_list)
        if unique_string not in special_dict:
            print(unique_string)
            special_dict[unique_string] = 1
        # import pdb; pdb.set_trace()
