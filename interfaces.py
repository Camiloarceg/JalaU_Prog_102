import optparse


opts = optparse.OptionParser()

opts.add_option(
    "-f",
    "--file",
    dest="fname",
    help="This is the file name that you would like to read",
)
opts.add_option(
    "-i",
    "--interface",
    dest="interface",
    help="This is the interface that you would like to search",
)

(options, arguments) = opts.parse_args()

with open(str(options.fname), "r") as f:
    lines = f.readlines()
    index = ""
    # locate the interface an extrac index
    for line in lines:
        if options.interface in line:
            index = list(line)[21]
            break
    # count 11 points and then validate if next char is index
    for line in lines:
        point_count = 0
        for char in line:
            if point_count == 11:
                if char is index:
                    print(line.strip())
            if char is ".":
                point_count += 1
