import optparse


opts = optparse.OptionParser()

opts.add_option("-f", "--file", dest='fname', help="This is the file name that you would like to read")
opts.add_option("-i", "--interface", dest='interface', help="This is the interface that you would like to search")

(options, arguments) = opts.parse_args()

with open(str(options.fname), "r") as f:
    lines = f.readlines()
    index = ""
    for line in lines:
        if options.interface in line:
            index = list(line)[21]
            break

    for line in lines:
        if list(line)[21] is index:
            print(line.strip())