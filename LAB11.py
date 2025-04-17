# set1 = set("abcdefg")
# set2 = set("adegjke")
# set3 = set("aaaaaaaaaaa")

# print(set1)




# set1 = set("abcdklmij")
# set2 = set("efghdijnop")
# set3 = set("qrstklmijnop")

# print(set1.intersection(set2.intersection(set3)))
# print(set3.intersection(set2))
# # print(set1.difference(set2.difference(set3)))
# print(set1.intersection(set2).difference(set3))
# print(set1.intersection(set3.difference(set2 and set2.intersection(set3.difference(set1)))))




def findCSMath():
    infile = open("cs.txt", "r")
    cs_majors = set(line.strip() for line in infile.readlines())
    infile.close()

    Oinfile = open("math.txt", "r")
    math_majors = set(line.strip() for line in Oinfile.readlines())
    Oinfile.close()

    cs_majors.discard("first_name,last_name")
    math_majors.discard("first_name,last_name")


    # print(cs_majors)
    # print(math_majors)
    # print(cs_majors.intersection(math_majors))
    # print(cs_majors.union(math_majors))

findCSMath()


def findStudentYearSets():
    infile = open("studentYear.txt", "r")
    freshman = set()
    sophomores = set()
    juniors = set()
    seniors = set()

    for line in infile.readlines():
        student, year = line.strip().split(",")
        year = int(year)
        if year == 1:
            freshman.add(student)
        elif year == 2:
            sophomores.add(student)
        elif year == 3:
            juniors.add(student)
        elif year == 4:
            seniors.add(student)

    infile.close()
    return freshman, sophomores, juniors, seniors


def findSophomoreCSMajors():
    cs_majors = findCSMath()
    _, sophomores, _, _ = findStudentYearSets()
    sophomore_cs_majors = cs_majors.intersection(sophomores)

    print("Sophomore CS Majors:", sophomore_cs_majors)

findSophomoreCSMajors()