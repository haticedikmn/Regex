import re

regex = r"\d\D\d\D\d\D\D\w*\D (w*\w*\D \w* \w*)\D\D(\w*)\D(\d*)"
f = open('new2_titanic.csv', 'w')

with open('Regex/titanic.csv') as file:
    while line := file.readline():
       #print(line)
        matches = re.search(regex, line)

        if matches:
            print(matches.group(1) + "," + matches.group(2) + "," + matches.group(3))
            new2_line = matches.group(1) + "," + matches.group(2) + "," + matches.group(3)
            f.write(new2_line + '\n')
f.close()