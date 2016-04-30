from collections import defaultdict

def unique_chars(s):
    return len(s) == len(set(s))

def no_structs(s):
    for char in s:
        if s.count(char) > 1:
            return False
    return True

def check_perm(s1, s2):
    d1 = char_count_dict(s1)
    d2 = char_count_dict(s2)
    for key in d1:
        if (not (key in d2)) or d1[key] != d2[key]:
            return False
    return True

def char_count_dict(str_):
	count_dict = defaultdict(int)
	for char in str_:
		count_dict[char] += 1
	return dict(count_dict)


def compress(s):
    if s == '':
        return s
    count_list = []
    current_char = s[0]
    current_count = 0
    for char in s:
        if char == current_char:
            current_count += 1
        else:
            count_list.append((current_char, current_count))
            current_char = char
            current_count = 1
    count_list.append((current_char, current_count))
    return s if len(s) == len(convert_to_str(count_list)) else convert_to_str(count_list)

def convert_to_str(counts):
    compressed_str = ''
    for char, count in counts:
        compressed_str += char + str(count)
    return compressed_str

print(compress('aabbcc'))