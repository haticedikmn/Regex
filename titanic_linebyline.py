import re

regex = r".*(?<=d, )([\w\.]+ [\w\.]+ [\w\.]+)\D,([\w\.]+),(\d*)"
f = open('new_titanic.csv', 'w')

with open('Regex/titanic.csv') as file:
    while line := file.readline():
       #print(line)
        matches = re.search(regex, line)

        if matches:
            print(matches.group(1) + "," + matches.group(2) + "," + matches.group(3))
            new_line = matches.group(1) + "," + matches.group(2) + "," + matches.group(3)
            f.write(new_line + '\n')
f.close()