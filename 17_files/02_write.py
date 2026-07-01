# Write to a file called Muktar.txt It should contain data about Muktar.

f = open("Muktar.txt", "w")

string = '''
Muktar is a nice guy. He lives in Bangladesh and he works with Python. His favourite package is Pandas. He is interested in AI.
'''

f.write(string)

f.close()