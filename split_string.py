'''Split the string on a " " (space) delimiter and join using a - hyphen. '''
def split_and_join(line):
    string_split = line.split(' ')
    result = '-'.join(string_split)
    return result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)