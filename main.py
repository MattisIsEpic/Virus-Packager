MainFile = input('What is the files name: ')
print('1: Create autorun file')
Op = int(input('What operation to do: '))
if Op == 1:
    writeFile = open('Build/autorun.inf', 'w')
    writeFile.write('[autorun]\n')
    writeFile.write(f'open={MainFile}')