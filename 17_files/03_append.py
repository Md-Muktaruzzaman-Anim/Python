# Append to an existing file called Muktar.txt It should add data about Muktar's hometown.

f = open("Muktar.txt", "a")

string = '''
Muktar initially lived in Bangladesh. He is a very nice guy.
'''

f.write(string)

f.close()