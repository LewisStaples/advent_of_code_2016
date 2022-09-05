# adventOfCode 2016 day 7
# https://adventofcode.com/2016/day/7


def has_an_abba(in_string):
    for i in range(1, len(in_string) - 2):    
        # "fail" if there isn't a middle repeat (example: "bb" in "abba")
        if in_string[i] != in_string[i+1]:
            continue
        # fail if char one i there isn't an "ab" in "abba"
        if in_string[i-1] == in_string[i]:
            continue
        # fail if the first and last letters in "abba" are different
        if in_string[i-1] != in_string[i+2]:
            continue
        # all tests above have passed, so it has an "abba"
        return True
    # No "abba" has been founded anywhere in the string
    return False

def find_all_aba_s(in_string, reverse = False):
    ret_val = set()
    for i in range(1, len(in_string) - 1):    
        # "fail" if i-1 and i+1 are different
        if in_string[i-1] != in_string[i+1]:
            continue
        # "fail" if i and i+1 are identical
        if in_string[i] == in_string[i+1]:
            continue
        # all tests above have passed, so it has an "aba"
        if reverse:
            ret_val.add((in_string[i], in_string[i-1]))
        else:
            ret_val.add((in_string[i-1], in_string[i]))
    return ret_val

def supports_tls(hypernet_strings, supernet_strings):
        # for each hypernet string:
        for hypernet_string in hypernet_strings:
            if has_an_abba(hypernet_string):
                return False
        # for each supernet string:
        for supernet_string in supernet_strings:
            if has_an_abba(supernet_string):
                return True
        return False

def supports_ssl(hypernet_strings, supernet_strings):
    # traverse all supernet strings, get (a,b) pair for all "ABA"s:
    all_abas = set()
    for supernet_string in supernet_strings:
        all_abas.update(find_all_aba_s(supernet_string))
    # traverse all hypernet strings, if any "BAB" matches any "ABA" from supernet
    for hypernet_string in hypernet_strings:
        # the True reverses the returned pair to reflect ABA vs. BAB
        all_babs = (find_all_aba_s(hypernet_string, True))
        for bab in all_babs:
            if bab in all_abas:
                return True
    return False

count_ip_supporting_tls = 0
count_ip_supporting_ssl = 0

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # positions of left and right bracket characters
        i_left = [i for i,ch in enumerate(in_string) if ch == '[']
        i_right = [i for i,ch in enumerate(in_string) if ch == ']']

        # Test 1 ... len(i_left) should == len(i_right)
        assert(len(i_left) == len(i_right))
        # Test 2 ... i_left should be smallest, then an i_right should be next smallest, and so on
        for i in range(len(i_left)):
            assert(i_left[i] < i_right[i])
        for i in range(1, len(i_left)):
            assert(i_left[i] > i_right[i-1])
        # Above tests show that all brackets are in pairs with left followed by right bracket
        # without any nested brackets (this eliminates some nasty edge cases)
        
        i_all = i_left + i_right + [-1] + [len(in_string)] # combine i_left and i_right, plus start and end of the string
        i_all.sort()
        
        hypernet_strings = []
        supernet_strings = []

        for counter, i in enumerate(range(1, len(i_all))):
            new_string = in_string[i_all[i-1] + 1: i_all[i]]
            if counter%2 == 0:
                supernet_strings.append(new_string)
            else:
                hypernet_strings.append(new_string)

        if supports_tls(hypernet_strings, supernet_strings):
            count_ip_supporting_tls += 1

        if supports_ssl(hypernet_strings, supernet_strings):
            count_ip_supporting_ssl += 1

print(f'The answer to part A is {count_ip_supporting_tls}\n')
print(f'The answer to part B is {count_ip_supporting_ssl}\n')

