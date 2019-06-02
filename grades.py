'''
By Gargi Sharma
Asg1 - Comp 6411
'''
import compute
class Grades:
    def componentAverage(self):
        print(100 * '-')
        print("Check Marks by individual Component")
        print("A1>A1 Average")
        print("A2>A2 Average")
        print("PR>PR Average")
        print("T1>T1 Average")
        print("T2>T2 Average")
        print(100 * '-')
        data = input("Pick one option from A1,A2,PR,T1,T2:")
        if data == "a1" or data == "A1":
            compute.asg1_avg()
        elif data == "a2" or data == "A2":
            compute.asg2_avg()
        elif data == "PR" or data == "pr" or data == "Pr" or data == "pR":
            compute.project_avg()
        elif data == "T1" or data == "t1":
            compute.test1_avg()
        elif data == "T2" or data == "t2":
            compute.test2_avg()
        else:
            print("Please enter valid number")

    def individualComp(self):
        print(100 * '-')
        print("Check Marks by individual Component")
        print("A1> Display A1 Marks")
        print("A2> Display A2 Marks")
        print("PR> Display Project Marks")
        print("T1> Display T1 Marks")
        print("T2> Display T2 Marks")
        print(100 * '-')
        data = input("Pick one answer from A1,A2,PR,T1,T2:")
        if data == "a1" or data == "A1":
            compute.asg1()
        elif data == "a2" or data == "A2":
            compute.asg2()
        elif data == "PR" or data == "pr" or data == "Pr" or data == "pR":
            compute.project()
        elif data == "T1" or data == "t1":
            compute.test1()
        elif data == "T2" or data == "t2":
            compute.test2()
        else:
            print("Please enter valid number")

    def defaultMenu(self):
        while True:
            print(100 * '-')
            print("M A I N - M E N U")
            print(100 * '-')
            print("1> Display individual component")
            print("2> Display component average")
            print("3> Display Standard Report")
            print("4> Sort by alternate column")
            print("5> Change Pass/Fail point ")
            print("6> Exit")
            print(100 * '-')
            userinput = input('Enter any one choice from the above list [1-6] : ')
            selectedChoice = userinput
            if selectedChoice == "1":
                self.individualComp()
            elif selectedChoice == "2":
                self.componentAverage()
            elif selectedChoice == "3":
                compute.standardReport()
            elif selectedChoice == "4":
                compute.sortingReportmenu()
            elif selectedChoice == "5":
                compute.changePassFail()
            elif selectedChoice == "6":
                compute.exitFile()
                exit()
            else:
                compute.invalidFunction();

#--------------------------------------Default Function-------------------------------------------------------------#
startFunction = Grades()
startFunction.defaultMenu()




