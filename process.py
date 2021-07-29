import csv
import sys
def cuboid(u_rack, x_min, x_max, y_min, y_max, z_min, z_max, vert, text, face):
    print("o {}".format(u_rack))
    print("v {} {} {}".format(x_min, z_min, y_min * -1))
    print("v {} {} {}".format(x_min, z_max, y_min * -1))
    print("v {} {} {}".format(x_min, z_min, y_max * -1))
    print("v {} {} {}".format(x_min, z_max, y_max * -1))
    print("v {} {} {}".format(x_max, z_min, y_min * -1))
    print("v {} {} {}".format(x_max, z_max, y_min * -1))
    print("v {} {} {}".format(x_max, z_min, y_max * -1))
    print("v {} {} {}".format(x_max, z_max, y_max * -1))
    print("vt 0.375000 0.000000")
    print("vt 0.625000 0.000000")
    print("vt 0.625000 0.250000")
    print("vt 0.375000 0.250000")
    print("vt 0.625000 0.500000")
    print("vt 0.375000 0.500000")
    print("vt 0.625000 0.750000")
    print("vt 0.375000 0.750000")
    print("vt 0.625000 1.000000")
    print("vt 0.375000 1.000000")
    print("vt 0.225000 0.500000")
    print("vt 0.225000 0.750000")
    print("vt 0.875000 0.500000")
    print("vt 0.875000 0.750000")
    print("vn -1.0000 0.0000 0.0000")
    print("vn 0.0000 0.0000 -1.0000")
    print("vn 1.0000 0.0000 0.0000")
    print("vn 0.0000 0.0000 1.0000")
    print("vn 0.0000 -1.0000 0.0000")
    print("vn 0.0000 1.0000 0.0000")
    print("usemtl None")
    print("s off")
    #f 1/1/1 2/2/1 4/3/1 3/4/1
    print("f ", end="")
    print("{}/{}/{} ".format((vert + 1), (text + 1), (face + 1)), end="")
    print("{}/{}/{} ".format((vert + 2), (text + 2), (face + 1)), end="")
    print("{}/{}/{} ".format((vert + 4), (text + 3), (face + 1)), end="")
    print("{}/{}/{}".format((vert + 3), (text + 4), (face + 1)))
    #f 3/4/2 4/3/2 8/5/2 7/6/2
    print("f ", end="")
    print("{}/{}/{} ".format((vert + 3), (text + 4), (face + 2)), end="")
    print("{}/{}/{} ".format((vert + 4), (text + 3), (face + 2)), end="")
    print("{}/{}/{} ".format((vert + 8), (text + 5), (face + 2)), end="")
    print("{}/{}/{}".format((vert + 7), (text + 6), (face + 2)))
    #f 7/6/3 8/5/3 6/7/3 5/8/3
    print("f ", end="")
    print("{}/{}/{} ".format((vert + 7), (text + 6), (face + 3)), end="")
    print("{}/{}/{} ".format((vert + 8), (text + 5), (face + 3)), end="")
    print("{}/{}/{} ".format((vert + 6), (text + 7), (face + 3)), end="")
    print("{}/{}/{}".format((vert + 5), (text + 8), (face + 3)))
    #f 5/8/4 6/7/4 2/9/4 1/10/4
    print("f ", end="")
    print("{}/{}/{} ".format((vert + 5), (text + 8), (face + 4)), end="")
    print("{}/{}/{} ".format((vert + 6), (text + 7), (face + 4)), end="")
    print("{}/{}/{} ".format((vert + 2), (text + 9), (face + 4)), end="")
    print("{}/{}/{}".format((vert + 1), (text + 10), (face + 4)))
    #f 3/11/5 7/6/5 5/8/5 1/12/5
    print("f ", end="")
    print("{}/{}/{} ".format((vert + 3), (text + 11), (face + 5)), end="")
    print("{}/{}/{} ".format((vert + 7), (text + 6), (face + 5)), end="")
    print("{}/{}/{} ".format((vert + 5), (text + 8), (face + 5)), end="")
    print("{}/{}/{}".format((vert + 1), (text + 12), (face + 5)))
    #f 8/5/6 4/13/6 2/14/6 6/7/6
    print("f ", end="")
    print("{}/{}/{} ".format((vert + 8), (text + 5), (face + 6)), end="")
    print("{}/{}/{} ".format((vert + 4), (text + 13), (face + 6)), end="")
    print("{}/{}/{} ".format((vert + 2), (text + 14), (face + 6)), end="")
    print("{}/{}/{}".format((vert + 6), (text + 7), (face + 6)))
    print("")

if (len(sys.argv) < 2):
    print("this script needs to be given the name of the file to process")
    exit()


# import csv
try:
    with open(sys.argv[1], newline='') as csv_input:
        reader = csv.reader(csv_input)
        test_data = list(reader)
except:
    print("unable to import rack.csv")
    exit()

# find the highest value
block_count = 0
x_min = 0
x_max = 0
y_min = 0
y_max = 0
z_min = 0
z_max = 0
vert = 0
text = 0
face = 0
for line in test_data:
    if (len(line) == 9):
        x_min = 0
        for number in line:
            x_max = x_min + 9.8
            y_max = y_min + 0.8
            z_min = 0
            z_max = float(number) * 0.1
            cuboid(block_count, x_min, x_max, y_min, y_max, z_min, z_max, vert, text, face)
            vert = vert + 8
            text = text + 14
            face = face + 6
            x_min = x_min + 10
        y_min = y_min + 1
        block_count = block_count + 1
