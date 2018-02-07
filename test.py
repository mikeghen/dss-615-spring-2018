infile = open("Dev.txt", 'r')
dev = [line.rstrip() for line in infile]
infile.close()
dev[0], dev[-1] = dev[-1], dev[0]
word = ("").join(dev) print(word)
