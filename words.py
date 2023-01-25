import optparse


opts = optparse.OptionParser()

opts.add_option("-f", "--file", dest='fname', help="This is the file name that you would like to read")
opts.add_option("-w", "--word", dest='word', help="This is the word that you would like to search")

(options, arguments) = opts.parse_args()
print(options.fname)
print(options.word)

count = 0
with open(str(options.fname), "r") as f:
    lines = f.readlines()
    for line in lines:
        if options.word in line:
            count += 1

print(f"the word {options.word} is {count} times on {options.fname}")