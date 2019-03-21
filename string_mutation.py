'''We all know that string is immutatable, write a logic to add a character to a string
Task 
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string, . 
The next line contains an integer , denoting the index location and a character  separated by a space.

Output Format 
Using any of the methods explained above, replace the character at index  with character .'''

def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    result =''.join(l)
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)