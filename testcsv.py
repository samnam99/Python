f = open('./testfileforcsv2.txt')
for lines in iter(f):
    #print (lines)
   
    lines = lines.strip()  # the while loop will leave a trailing space, 
                  # so the trailing whitespace must be dealt with
                  # before or after the while loop
    while '  ' in lines:
        lines = lines.replace('  ', ' ')

    lines=lines.replace(' ', ',')
    lines=lines.replace(',,', ',')

    print (lines)

f.close()

