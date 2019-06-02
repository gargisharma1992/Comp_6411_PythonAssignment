'''
By Gargi Sharma
Asg1 - Comp 6411
'''
#-------------------------------------Individual menu  STARTS here-------------------------------------------------------#
def get_ind_result(line):
  key, sep, value = line.strip().partition("|")
  return int(key), value

def asg1():
    with open("a1.txt") as fd:
        first_line = fd.readline()
        print("A1 Grades ( "+first_line.rstrip(),")")
        dict1 = dict(get_ind_result(line) for line in fd)
    with open("class.txt") as fd:
        dict2 = dict(get_ind_result(line) for line in fd)
        dict3={}
        for key in dict1.keys():
         if key in dict2.keys():
            dict3[key] = []
            dict3[key].append(dict1[key])
            dict3[key].append(dict2[key])
         #print(dict3)
        for kv in dict3.items():
            #print(kv)
            names = kv[1];
            a = names[1].split("|")
            a.reverse()
            result = ",".join(a)
            space = 14 - len(result)
            dummy = ""
            if (space > 0):
                for x in range(0, space):
                    dummy = dummy + " "
                result = result + dummy
            print(kv[0], '\t', result, '\t', names[0])

def asg2():
    with open("a2.txt") as fd:
        first_line = fd.readline()
        print("A2 Grades ( " + first_line.rstrip(), ")")
        dict1 = dict(get_ind_result(line) for line in fd)
    with open("class.txt") as fd:
        dict2 = dict(get_ind_result(line) for line in fd)
        dict3={}
        for key in dict1.keys():
         if key in dict2.keys():
            dict3[key] = []
            dict3[key].append(dict1[key])
            dict3[key].append(dict2[key])
        for kv in dict3.items():
            names = kv[1];
            a = names[1].split("|")
            a.reverse()
            result = ",".join(a)
            space = 14 - len(result)
            dummy = ""
            if (space > 0):
                for x in range(0, space):
                    dummy = dummy + " "
                result = result + dummy
            print(kv[0], '\t', result, '\t', names[0])


def project():
    with open("project.txt") as fd:
        first_line = fd.readline()
        print("PR Grades ( " + first_line.rstrip(), ")")
        dict1 = dict(get_ind_result(line) for line in fd)
    with open("class.txt") as fd:
        dict2 = dict(get_ind_result(line) for line in fd)
        dict3={}
        for key in dict1.keys():
         if key in dict2.keys():
            dict3[key] = []
            dict3[key].append(dict1[key])
            dict3[key].append(dict2[key])
        for kv in dict3.items():
            names = kv[1];
            a = names[1].split("|")
            a.reverse()
            result = ",".join(a)
            space = 14 - len(result)
            dummy = ""
            if (space > 0):
                for x in range(0, space):
                    dummy = dummy + " "
                result = result + dummy
            print(kv[0], '\t', result, '\t', names[0])

def test1():
    with open("test1.txt") as fd:
        first_line = fd.readline()
        print("T1 Grades ( " + first_line.rstrip(), ")")
        dict1 = dict(get_ind_result(line) for line in fd)
    with open("class.txt") as fd:
        dict2 = dict(get_ind_result(line) for line in fd)
        dict3={}
        for key in dict1.keys():
         if key in dict2.keys():
            dict3[key] = []
            dict3[key].append(dict1[key])
            dict3[key].append(dict2[key])
        for kv in dict3.items():
            names = kv[1];
            a = names[1].split("|")
            a.reverse()
            result = ",".join(a)
            space = 14 - len(result)
            dummy = ""
            if (space > 0):
                for x in range(0, space):
                    dummy = dummy + " "
                result = result + dummy
            print(kv[0], '\t', result, '\t', names[0])

def test2():
    with open("test2.txt") as fd:
        first_line = fd.readline()
        print("T2 Grades ( " + first_line.rstrip(), ")")
        dict1 = dict(get_ind_result(line) for line in fd)
    with open("class.txt") as fd:
        dict2 = dict(get_ind_result(line) for line in fd)
        dict3={}
        for key in dict1.keys():
         if key in dict2.keys():
            dict3[key] = []
            dict3[key].append(dict1[key])
            dict3[key].append(dict2[key])
        for kv in dict3.items():
            names = kv[1];
            a = names[1].split("|")
            a.reverse()
            result = ",".join(a)
            space = 14 - len(result)
            dummy = ""
            if (space > 0):
                for x in range(0, space):
                    dummy = dummy + " "
                result = result + dummy
            print(kv[0], '\t', result, '\t', names[0])

#-------------------------------------Individual menu  ends here-------------------------------------------------------#

#-------------------------------------Component-2  average starts here-------------------------------------------------#
def get_pair(line):
    key, sep, value = line.strip().partition("|")
    if value == '' or value == "":
        value = 0
    #return int(key), value
    return int(key), int(value)

def asg1_avg():
  with open("a1.txt") as fd:
    max_marks = fd.readline()
    dict1 = dict(get_pair(line) for line in fd)
    sumOfValues = sum(dict1.values())
    total_records = len(dict1)
    average1 = sumOfValues / total_records
    average = round(average1,2)
    print("A1 average:", +average, "/" + max_marks)

def asg2_avg():
  with open("a2.txt") as fd:
    max_marks = fd.readline()
    dict1 = dict(get_pair(line) for line in fd)
    sumOfValues = sum(dict1.values())
    total_records = len(dict1)
    average1 = sumOfValues / total_records
    average = round(average1, 2)
    print("A2 average:", +average, "/" + max_marks)

def project_avg():
  with open("project.txt") as fd:
    max_marks = fd.readline()
    dict1 = dict(get_pair(line) for line in fd)
    sumOfValues = sum(dict1.values())
    total_records = len(dict1)
    average1 = sumOfValues / total_records
    average = round(average1, 2)
    print("PR average:", +average, "/" + max_marks)

def test1_avg():
  with open("test1.txt") as fd:
    max_marks = fd.readline()
    dict1 = dict(get_pair(line) for line in fd)
    sumOfValues = sum(dict1.values())
    total_records = len(dict1)
    average1 = sumOfValues / total_records
    average = round(average1, 2)
    print("T1 average:", +average, "/" + max_marks)

def test2_avg():
  with open("test2.txt") as fd:
    max_marks = fd.readline()
    dict1 = dict(get_pair(line) for line in fd)
    sumOfValues = sum(dict1.values())
    total_records = len(dict1)
    average1 = sumOfValues / total_records
    average = round(average1, 2)
    print("T2 average:", +average, "/" + max_marks)

#-------------------------------------Component-2  average ends here---------------------------------------------------#

#-------------------------------------Component-3 Standard report starts here------------------------------------------#
def get_pair_standardreport(line):
  key, sep, value = line.strip().partition("|")
  if value=='' or value=="":
      value=0
  return int(key), value

a1_max_marks = 0
a2_max_marks = 0
pr_max_marks = 0
t1_max_marks = 0
t2_max_marks = 0
def standardReport():
    print("ID", '\t', "LN", '\t\t', "FN", '\t\t', "A1", '\t\t', "A2", '\t\t', "PR", '\t\t', "T1", '\t\t', "T2",
          '\t\t',"GR", '\t\t', "FL")
    with open("a1.txt") as fd:
        a1_max = fd.readline()
        dict1 = dict(get_pair_standardreport(line) for line in fd)

        with open("a2.txt") as fd:
            a2_max = fd.readline()
            dict2 = dict(get_pair_standardreport(line) for line in fd)
        with open("project.txt") as fd:
            pr_max = fd.readline()
            dict3 = dict(get_pair_standardreport(line) for line in fd)
            # print(prReport)
        with open("test1.txt") as fd:
            t1_max = fd.readline()
            dict4 = dict(get_pair_standardreport(line) for line in fd)
        with open("test2.txt") as fd:
            t2_max = fd.readline()
            dict5 = dict(get_pair_standardreport(line) for line in fd)
        with open("class.txt") as fd:

            dict6 = dict(get_pair_standardreport(line) for line in fd)
            dict7 = {}
            for key in dict1.keys():
                if key in dict2.keys():
                    dict7[key] = []
                    dict7[key].append(dict1[key])
                    dict7[key].append(dict2[key])
                    dict7[key].append(dict3[key])
                    dict7[key].append(dict4[key])
                    dict7[key].append(dict5[key])
                    dict7[key].append(dict6[key])
            # for kv in dict7.items():
            for kv in sorted(dict7.items(), key=lambda x: x[0]):
                student_id = kv[0];
                names = kv[1];
                seperate_name = names[5];
                a = seperate_name.split("|")
                a.reverse()
                result = " ".join(a)
                asg1marks = names[0]
                asg2marks = names[1]
                prmarks = names[2]
                t1marks = names[3]
                t2marks = names[4]
                # print(asg1marks)
                firstname, lastname = result.split()

                a1_points = int(asg1marks) / int(a1_max)
                final_a1_points = a1_points * 7.5
                # print(final_a1_points)

                a2_points = int(asg2marks) / int(a2_max)
                final_a2_points = a2_points * 7.5
                # print(final_a2_points)

                pr_points = int(prmarks) / int(pr_max)
                final_pr_points = pr_points * 25

                t1_points = int(t1marks) / int(t1_max)
                final_t1_points = t1_points * 30

                t2_points = int(t2marks) / int(t2_max)
                final_t2_points = t2_points * 30

                finalGradePoints = final_a1_points + final_a2_points + final_pr_points + final_t1_points + final_t2_points
                # print(finalGradePoints)
                FPgrade = 100 - 50
                NFP = FPgrade / 7
                Cgrade = NFP * 1
                B_grade = NFP * 2
                Bgrade = NFP * 3
                BPgrade = NFP * 4
                A_grade = NFP * 5
                Agrade = NFP * 6
                APgrade = NFP * 7
                #f_grade = math.ceil(finalGradePoints)
                f_grade = round(finalGradePoints, 2)
                if f_grade > FPgrade and f_grade <= (FPgrade + Cgrade):  # 79>50 and 79<=50+7.14
                    FL = "C"
                elif f_grade > Cgrade and f_grade <= (FPgrade + B_grade):
                    FL = "B-"
                elif f_grade > B_grade and f_grade <= (FPgrade + Bgrade):
                    FL = "B"
                elif f_grade > Bgrade and f_grade <= (FPgrade + BPgrade):
                    FL = "B+"
                elif f_grade > BPgrade and f_grade <= (FPgrade + A_grade):
                    FL = "A-"
                elif f_grade > A_grade and f_grade <= (FPgrade + Agrade):
                    FL = "A"
                elif f_grade > Agrade and f_grade <= (FPgrade + APgrade):
                    FL = "A+"
                if f_grade < FPgrade:
                    FL = "F"

                space=6-len(firstname)
                dummy=""
                if (space>0):
                    for x in range(0,space):
                        dummy=dummy+" "
                    firstname=firstname+dummy

                space = 6 - len(lastname)
                dummy = ""
                if (space > 0):
                    for x in range(0, space):
                        dummy = dummy + " "
                    lastname = lastname + dummy

                if names[0]==0:
                    a1="  "
                else:
                    if len(names[0])<2:
                        a1=names[0]+" "
                    else:
                        a1=names[0]

                if names[1]==0:
                    a2="  "
                else:
                    if len(names[1])<2:
                        a2=names[1]+" "
                    else:
                        a2=names[1]

                if names[2]==0:
                    pr="  "
                else:
                    if len(names[2])<2:
                        pr=names[2]+" "
                    else:
                        pr=names[2]

                if names[3]==0:
                    t1="  "
                else:
                    if len(names[3])<2:
                        t1=names[3]+" "
                    else:
                        t1=names[3]

                if names[4]==0:
                    t2="  "
                else:
                    if len(names[4])<2:
                        t2=names[4]+" "
                    else:
                        t2=names[4]
                print(student_id, '\t', firstname, '\t', lastname, '\t', a1, '\t\t', a2, '\t\t',
                     pr, '\t\t',t1, '\t\t', t2, '\t\t', f_grade, '\t\t', FL)


# -------------------------------------Component-3 Standard report ends here------------------------------------------#

#- ------------------------------------Component-4 Sort by alternate column starts here-------------------------------#
nlines=sum(1 for line in open("class.txt"))
#print(nlines)
list1 = [[0 for i in range(10)] for j in range(nlines)]
def sortBylastname(data):
    print("ID", '\t\t', "LN", '\t\t\t', "FN", '\t\t\t', "A1", '\t\t', "A2", '\t\t', "PR", '\t\t', "T1", '\t\t', "T2",
          '\t\t',"GR", '\t\t', "FL")
    with open("a1.txt") as fd:
        a1_max = fd.readline()
        dict1 = dict(get_pair_standardreport(line) for line in fd)

        with open("a2.txt") as fd:
            a2_max = fd.readline()
            dict2 = dict(get_pair_standardreport(line) for line in fd)
        with open("project.txt") as fd:
            pr_max = fd.readline()
            dict3 = dict(get_pair_standardreport(line) for line in fd)
            # print(prReport)
        with open("test1.txt") as fd:
            t1_max = fd.readline()
            dict4 = dict(get_pair_standardreport(line) for line in fd)
        with open("test2.txt") as fd:
            t2_max = fd.readline()
            dict5 = dict(get_pair_standardreport(line) for line in fd)
        with open("class.txt") as fd:
            dict6 = dict(get_pair_standardreport(line) for line in fd)
            dict7 = {}
            for key in dict1.keys():
                if key in dict2.keys():
                    dict7[key] = []
                    dict7[key].append(dict1[key])
                    dict7[key].append(dict2[key])
                    dict7[key].append(dict3[key])
                    dict7[key].append(dict4[key])
                    dict7[key].append(dict5[key])
                    dict7[key].append(dict6[key])
            c = 0
            #for kv in sorted(dict7.items(), key=lambda x: x[1]):
            for kv in dict7.items():
                student_id = kv[0];
                names = kv[1];
                seperate_name = names[5];
                a = seperate_name.split("|")
                a.reverse()
                result = " ".join(a)
                asg1marks = names[0]
                asg2marks = names[1]
                prmarks = names[2]
                t1marks = names[3]
                t2marks = names[4]
                # split firstname and lastname
                firstname, lastname = result.split()

                # find as1 marks
                a1_points = int(asg1marks) / int(a1_max)
                final_a1_points = a1_points * 7.5

                # find as2 marks
                a2_points = int(asg2marks) / int(a2_max)
                final_a2_points = a2_points * 7.5

                # find project marks
                pr_points = int(prmarks) / int(pr_max)
                final_pr_points = pr_points * 25

                # find t1 marks
                t1_points = int(t1marks) / int(t1_max)
                final_t1_points = t1_points * 30

                # find t2 marks
                t2_points = int(t2marks) / int(t2_max)
                final_t2_points = t2_points * 30

                # get final grade points
                finalGradePoints = final_a1_points + final_a2_points + final_pr_points + final_t1_points + final_t2_points
                # print(finalGradePoints)
                FPgrade = 100 - 50
                NFP = FPgrade / 7
                Cgrade = NFP * 1
                B_grade = NFP * 2
                Bgrade = NFP * 3
                BPgrade = NFP * 4
                A_grade = NFP * 5
                Agrade = NFP * 6
                APgrade = NFP * 7
                #f_grade = math.ceil(finalGradePoints)
                f_grade = round(finalGradePoints, 2)

                if f_grade > FPgrade and f_grade <= (FPgrade + Cgrade):  # 79>50 and 79<=50+7.14
                    FL = "C"
                elif f_grade > Cgrade and f_grade <= (FPgrade + B_grade):
                    FL = "B-"
                elif f_grade > B_grade and f_grade <= (FPgrade + Bgrade):
                    FL = "B"
                elif f_grade > Bgrade and f_grade <= (FPgrade + BPgrade):
                    FL = "B+"
                elif f_grade > BPgrade and f_grade <= (FPgrade + A_grade):
                    FL = "A-"
                elif f_grade > A_grade and f_grade <= (FPgrade + Agrade):
                    FL = "A"
                elif f_grade > Agrade and f_grade <= (FPgrade + APgrade):
                    FL = "A+"
                if f_grade < FPgrade:
                    FL = "F"
                space = 6 - len(firstname)
                dummy = ""
                if (space > 0):
                    for x in range(0, space):
                        dummy = dummy + " "
                    firstname = firstname + dummy

                space = 6 - len(lastname)
                dummy = ""
                if (space > 0):
                    for x in range(0, space):
                        dummy = dummy + " "
                    lastname = lastname + dummy

                if names[0] == 0:
                    a1 = "  "
                else:
                    if len(names[0]) < 2:
                        a1 = names[0] + " "
                    else:
                        a1 = names[0]

                if names[1] == 0:
                    a2 = "  "
                else:
                    if len(names[1]) < 2:
                        a2 = names[1] + " "
                    else:
                        a2 = names[1]

                if names[2] == 0:
                    pr = "  "
                else:
                    if len(names[2]) < 2:
                        pr = names[2] + " "
                    else:
                        pr = names[2]

                if names[3] == 0:
                    t1 = "  "
                else:
                    if len(names[3]) < 2:
                        t1 = names[3] + " "
                    else:
                        t1 = names[3]

                if names[4] == 0:
                    t2 = "  "
                else:
                    if len(names[4]) < 2:
                        t2 = names[4] + " "
                    else:
                        t2 = names[4]
                #get all the elements of final list
                list1[c][0] = student_id
                list1[c][1] = firstname
                list1[c][2] = lastname
                list1[c][3] = a1
                list1[c][4] = a2
                list1[c][5] = pr
                list1[c][6] = t1
                list1[c][7] = t2
                list1[c][8] = f_grade
                list1[c][9] = FL
                c = c + 1
    if data == "lt" or data == "LT" or data == "LN" or data == "ln" :
        list1.sort(key=lambda x: x[1])
        for lst in list1:
            print(lst[0], '\t\t', lst[1], '\t\t', lst[2], '\t\t',lst[3], '\t\t', lst[4], '\t\t',lst[5], '\t\t', lst[6], '\t\t',
                  lst[7], '\t\t',lst[8], '\t\t',lst[9])
    #elif data == "GR" or data == "gr" or data == "gR" or data == "Gr" :
    elif data == "GR" or data == "gr"  :
        list1.sort(key=lambda x: x[8], reverse=True)
        for lst in list1:
            print(lst[0], '\t\t', lst[1], '\t\t', lst[2], '\t\t', lst[3], '\t\t', lst[4], '\t\t', lst[5], '\t\t',
                  lst[6], '\t\t',lst[7], '\t\t', lst[8], '\t\t', lst[9])

#-------------------------------------Component-4 Sort by alternate column starts here------------------------------#
def sortingReportmenu():
    data = input("Sort report by selecting one option from LT or GR:")
    if data.lower() == "lt" or data.upper() == "LT" or data.lower() == "gr" or data.upper() == "GR" \
            or data.lower() == "LN" or data.lower() == "ln":
        sortBylastname(data)
    else:
        print("Please enter valid number")

#-------------------------------------Component-4 Sort by alternate column ends here-------------------------------#

#-------------------------------------Component-5 Change pass fail grade starts here-------------------------------#
gradeInput = 0
def changePassFail():
    gradeInput = input('Enter any number from [1-100] : ')
    print("ID", '\t', "LN", '\t\t', "FN", '\t\t', "A1", '\t\t', "A2", '\t\t', "PR", '\t\t', "T1", '\t\t', "T2",
          '\t\t',"GR", '\t\t', "FL")
    with open("a1.txt") as fd:
        a1_max = fd.readline()
        dict1 = dict(get_pair_standardreport(line) for line in fd)
        with open("a2.txt") as fd:
            a2_max = fd.readline()
            dict2 = dict(get_pair_standardreport(line) for line in fd)
        with open("project.txt") as fd:
            pr_max = fd.readline()
            dict3 = dict(get_pair_standardreport(line) for line in fd)
            # print(prReport)
        with open("test1.txt") as fd:
            t1_max = fd.readline()
            dict4 = dict(get_pair_standardreport(line) for line in fd)
        with open("test2.txt") as fd:
            t2_max = fd.readline()
            dict5 = dict(get_pair_standardreport(line) for line in fd)
        with open("class.txt") as fd:
            dict6 = dict(get_pair_standardreport(line) for line in fd)
            dict7 = {}
            for key in dict1.keys():
                if key in dict2.keys():
                    dict7[key] = []
                    dict7[key].append(dict1[key])
                    dict7[key].append(dict2[key])
                    dict7[key].append(dict3[key])
                    dict7[key].append(dict4[key])
                    dict7[key].append(dict5[key])
                    dict7[key].append(dict6[key])
            # for kv in dict7.items():
            for kv in sorted(dict7.items(), key=lambda x: x[0]):

                student_id = kv[0];
                names = kv[1];
                seperate_name = names[5];
                a = seperate_name.split("|")
                a.reverse()
                result = " ".join(a)
                asg1marks = names[0]
                asg2marks = names[1]
                prmarks = names[2]
                t1marks = names[3]
                t2marks = names[4]
                # print(asg1marks)
                firstname, lastname = result.split()

                a1_points = int(asg1marks) / int(a1_max)
                final_a1_points = a1_points * 7.5
                # print(final_a1_points)

                a2_points = int(asg2marks) / int(a2_max)
                final_a2_points = a2_points * 7.5

                pr_points = int(prmarks) / int(pr_max)
                final_pr_points = pr_points * 25

                t1_points = int(t1marks) / int(t1_max)
                final_t1_points = t1_points * 30

                t2_points = int(t2marks) / int(t2_max)
                final_t2_points = t2_points * 30

                finalGradePoints = final_a1_points + final_a2_points + final_pr_points + final_t1_points + final_t2_points
                FPgrade =  100 - int(gradeInput)#int(gradeInput);
                NFP = FPgrade / 7
                Cgrade = NFP * 1
                B_grade = NFP * 2
                Bgrade = NFP * 3
                BPgrade = NFP * 4
                A_grade = NFP * 5
                Agrade = NFP * 6
                APgrade = NFP * 7
                f_grade = round(finalGradePoints)
                FL="F"
                if(f_grade>=int(gradeInput.strip()) and f_grade<=(int(gradeInput.strip())+NFP)):
                   FL="C"
                if (f_grade>int(gradeInput.strip())+NFP) and f_grade<=(int(gradeInput.strip())+int(Cgrade)):
                   FL="B-"
                if (f_grade > int(gradeInput.strip()) + Cgrade and f_grade <= (int(gradeInput.strip()) + int(B_grade))):
                   FL="B"
                if (f_grade > int(gradeInput.strip()) + B_grade and f_grade <= round((int(gradeInput.strip()) + BPgrade))):
                   FL="B+"
                if (f_grade > int(gradeInput.strip()) + BPgrade and f_grade <= round((int(gradeInput.strip()) + A_grade))):
                   FL="A-"
                if (f_grade > int(gradeInput.strip()) + A_grade and f_grade <= round((int(gradeInput.strip()) + Agrade))):
                   FL="A"
                if (f_grade > int(gradeInput.strip()) + Agrade and f_grade <= round((int(gradeInput.strip()) + APgrade))):
                   FL="A+"
                if (f_grade < int(gradeInput.strip())):
                    FL="F"

                space = 6 - len(firstname)
                dummy = ""
                if (space > 0):
                    for x in range(0, space):
                        dummy = dummy + " "
                    firstname = firstname + dummy

                space = 6 - len(lastname)
                dummy = ""
                if (space > 0):
                    for x in range(0, space):
                        dummy = dummy + " "
                    lastname = lastname + dummy

                if names[0] == 0:
                    a1 = "  "
                else:
                    if len(names[0]) < 2:
                        a1 = names[0] + " "
                    else:
                        a1 = names[0]

                if names[1] == 0:
                    a2 = "  "
                else:
                    if len(names[1]) < 2:
                        a2 = names[1] + " "
                    else:
                        a2 = names[1]

                if names[2] == 0:
                    pr = "  "
                else:
                    if len(names[2]) < 2:
                        pr = names[2] + " "
                    else:
                        pr = names[2]

                if names[3] == 0:
                    t1 = "  "
                else:
                    if len(names[3]) < 2:
                        t1 = names[3] + " "
                    else:
                        t1 = names[3]

                if names[4] == 0:
                    t2 = "  "
                else:
                    if len(names[4]) < 2:
                        t2 = names[4] + " "
                    else:
                        t2 = names[4]
                print(student_id, '\t', firstname, '\t', lastname, '\t', a1, '\t\t', a2, '\t\t',
                      pr, '\t\t', t1, '\t\t', t2, '\t\t', f_grade, '\t\t', FL)
                #print(student_id, '\t', firstname, '\t\t', lastname, '\t\t', names[0], '\t\t', names[1], '\t\t',
                      #names[2], '\t\t',names[3], '\t\t', names[4], '\t\t', f_grade, '\t\t', FL)

#-------------------------------------Component-5 Change pass fail grade ends here-------------------------------#

#-------------------------------------Component-6 Exit Application-----------------------------------------------#
def exitFile():
  print("Good bye");

def invalidFunction():
  print("You have entered an Invalid number. Try again...")


