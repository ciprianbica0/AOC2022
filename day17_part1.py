import time

f = open("day17_input.txt", "r")
t1 = time.time()

# SETUP
jet_streams = f.read()
print(jet_streams)

t2 = time.time()
print("Duration", t2-t1, "~=", "%0.2f" % ((t2-t1)/60), "minutes")
