from studentCode import submitDict

data = submitDict()
newdict = {}

for name in data:
    if name == 'MCCONNELL MICHAEL S':
        record = data[name]
        print len(record)

        