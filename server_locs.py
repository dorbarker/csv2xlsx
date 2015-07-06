import subprocess, time

def run_test():

   proc = subprocess.Popen(["speedtest"], stderr = subprocess.PIPE, stdout = subprocess.PIPE)

   out, err = proc.communicate()

   return out

def parse_loc(test_out):

    l = test_out.split("\n")[4]
    first = l.split("(")[1]
    second = first.split(")")[0]
    third = second.split(", ")

    return third

def writer(parsed):

    with open("server_locs.csv", "a") as f:
        f.write("{},{}\n".format(parsed[0], parsed[1]))


while True:

    testout = run_test()
    parsed = parse_loc(testout)
    writer(parsed)
    
    print("Contacted server at {}".format(', '.join(parsed)))

    time.sleep(10 * 60)


