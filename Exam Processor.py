

# Component in option 1 
# Component in option 2
registered_studentnames= []
registered_studentids = []
# Component in option 2
registered_subjects = []
# Component in option 3
student_name_and_id = {}
# Component in option 4
student1_subject_grades = {}
student1_gradescore_letters = []
# Component in option 5
# student2_subject_grades = {}
# student2_gradescore_letters = []
# # Component in option 6
# student3_subject_grades = {}
# student3_gradescore_letters = []
# # Component in option 7
# student4_subject_grades = {}
# student4_gradescore_letters = []
# # Component in option 8
# student5_subject_grades = {}
# student5_gradescore_letters = []
# # Component in option 9
# student6_subject_grades = {}
# student6_gradescore_letters = []
# # Component in option 10
# student7_subject_grades = {}
# student7_gradescore_letters = []
# # Component in option 11
# student8_subject_grades = {}
# student8_gradescore_letters = []
# # Component in option 12
# student9_subject_grades = {}
# student9_gradescore_letters = []
# # Component in option 13
# student10_subject_grades = {}
# student10_gradescore_letters = []

def exam_processing_system():
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("1: Register student names and ID")
    print("2: Register the subjects studied in the Semester")
    print("3: Print registered student names and ID")
    print("4: Register the grades for student 1")
    # print("5: Register the grades for student 2")
    # print("6: Register the grades for student 3")
    # print("7: Register the grades for student 4")
    # print("8: Register the grades for student 5")
    # print("9: Register the grades for student 6")
    # print("10: Register the grades for student 7")
    # print("11: Register the grades for student 8")
    # print("12: Register the grades for student 9")
    # print("13: Register the grades for student 10")
    print("14: Print the full report for all students")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    option = input("Please select an option from the ones listed above: ")

    if option=="1":
        i = 0
        while i<1: 
            student_name = input("Enter the name of student you want to register: ")
            student_id = input("Enter the ID of the student you want to register: ")
            registered_studentnames.append(student_name)
            registered_studentids.append(student_id)
            student_name_and_id[student_name] = student_id
            i += 1

        print(student_name_and_id)
        exam_processing_system()
    elif option=="2":
        j=0
        while j<5:
            subject_name = input("Enter the name of subject you want to register: ")
            registered_subjects.append(subject_name)
            j += 1
        print(registered_subjects)
        exam_processing_system()
    elif option=="3":
        if student_name_and_id == {}:
            print("There are no students to print. Register students and id for printing")
            exam_processing_system()
        else:
            print(student_name_and_id)
            exam_processing_system()
    elif option=="4":
        if registered_subjects == []:
            print("There are no subjects to register grades for. Register subjects first")
            exam_processing_system()
        else:
            for subject in registered_subjects:
                print("Subject: ", subject)
                grade = int(input("Enter grade for this subject"))
                student1_subject_grades[subject] = grade
                if grade >= 90 and grade <= 100:
                    student1_gradescore_letters.append("A")
                elif grade >= 87 and grade <= 89:
                    student1_gradescore_letters.append("A-")
                elif grade >= 84 and grade <= 86:
                    student1_gradescore_letters.append("B+")
                elif grade >= 80 and grade<= 83:
                    student1_gradescore_letters.append("B")
                elif grade >= 77 and grade <= 79:
                    student1_gradescore_letters.append("B-")
                elif grade >= 74 and grade <= 76:
                    student1_gradescore_letters.append("C+")
                elif grade >= 70 and grade <= 73:
                    student1_gradescore_letters.append("C")
                elif grade >= 67 and grade<= 69:
                    student1_gradescore_letters.append("C-")
                elif grade>= 64 and grade<= 66:
                    student1_gradescore_letters.append("D+")
                elif grade >= 62 and grade <= 63:
                    student1_gradescore_letters.append("D")
                elif grade >= 60 and grade <= 61:
                    student1_gradescore_letters.append("D-")
                elif grade<= 59:
                    student1_gradescore_letters.append("F")
                else:
                    student1_gradescore_letters.append("Invalid score")
        print(student1_subject_grades)
        print(student1_gradescore_letters)
        exam_processing_system()
    # elif option=="5":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student2_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student2_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student2_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student2_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student2_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student2_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student2_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student2_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student2_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student2_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student2_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student2_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student2_gradescore_letters.append("F")
    #             else:
    #                 student2_gradescore_letters.append("Invalid score")
    #     print(student2_subject_grades)
    #     print(student2_gradescore_letters)
    #     exam_processing_system()
    # elif option=="6":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student3_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student3_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student3_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student3_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student3_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student3_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student3_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student3_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student3_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student3_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student3_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student3_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student3_gradescore_letters.append("F")
    #             else:
    #                 student3_gradescore_letters.append("Invalid score")
    #     print(student3_subject_grades)
    #     print(student3_gradescore_letters)
    #     exam_processing_system()
    # elif option=="7":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student4_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student4_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student4_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student4_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student4_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student4_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student4_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student4_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student4_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student4_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student4_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student4_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student4_gradescore_letters.append("F")
    #             else:
    #                 student4_gradescore_letters.append("Invalid score")
    #     print(student4_subject_grades)
    #     print(student4_gradescore_letters)
    #     exam_processing_system()
    # elif option=="8":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student5_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student5_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student5_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student5_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student5_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student5_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student5_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student5_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student5_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student5_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student5_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student5_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student5_gradescore_letters.append("F")
    #             else:
    #                 student5_gradescore_letters.append("Invalid score")
    #     print(student5_subject_grades)
    #     print(student5_gradescore_letters)
    #     exam_processing_system()
    # elif option=="9":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student6_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student6_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student6_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student6_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student6_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student6_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student6_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student6_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student6_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student6_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student6_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student6_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student6_gradescore_letters.append("F")
    #             else:
    #                 student6_gradescore_letters.append("Invalid score")
    #     print(student6_subject_grades)
    #     print(student6_gradescore_letters)
    #     exam_processing_system()
    # elif option=="10":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student7_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student7_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student7_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student7_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student7_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student7_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student7_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student7_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student7_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student7_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student7_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student7_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student7_gradescore_letters.append("F")
    #             else:
    #                 student7_gradescore_letters.append("Invalid score")
    #     print(student7_subject_grades)
    #     print(student7_gradescore_letters)
    #     exam_processing_system()
    # elif option=="11":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student8_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student8_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student8_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student8_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student8_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student8_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student8_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student8_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student8_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student8_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student8_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student8_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student8_gradescore_letters.append("F")
    #             else:
    #                 student8_gradescore_letters.append("Invalid score")
    #     print(student8_subject_grades)
    #     print(student8_gradescore_letters)
    #     exam_processing_system()
    # elif option=="12":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student9_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student9_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student9_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student9_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student9_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student9_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student9_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student9_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student9_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student9_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student9_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student9_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student9_gradescore_letters.append("F")
    #             else:
    #                 student9_gradescore_letters.append("Invalid score")
    #     print(student9_subject_grades)
    #     print(student9_gradescore_letters)
    #     exam_processing_system()
    # elif option=="13":
    #     if registered_subjects == []:
    #         print("There are no subjects to register grades for. Register subjects first")
    #         exam_processing_system()
    #     else:
    #         for subject in registered_subjects:
    #             print("Subject: ", subject)
    #             grade = int(input("Enter grade for this subject"))
    #             student10_subject_grades[subject] = grade
    #             if grade >= 90 and grade <= 100:
    #                 student10_gradescore_letters.append("A")
    #             elif grade >= 87 and grade <= 89:
    #                 student10_gradescore_letters.append("A-")
    #             elif grade >= 84 and grade <= 86:
    #                 student10_gradescore_letters.append("B+")
    #             elif grade >= 80 and grade<= 83:
    #                 student10_gradescore_letters.append("B")
    #             elif grade >= 77 and grade <= 79:
    #                 student10_gradescore_letters.append("B-")
    #             elif grade >= 74 and grade <= 76:
    #                 student10_gradescore_letters.append("C+")
    #             elif grade >= 70 and grade <= 73:
    #                 student10_gradescore_letters.append("C")
    #             elif grade >= 67 and grade<= 69:
    #                 student10_gradescore_letters.append("C-")
    #             elif grade>= 64 and grade<= 66:
    #                 student10_gradescore_letters.append("D+")
    #             elif grade >= 62 and grade <= 63:
    #                 student10_gradescore_letters.append("D")
    #             elif grade >= 60 and grade <= 61:
    #                 student10_gradescore_letters.append("D-")
    #             elif grade<= 59:
    #                 student10_gradescore_letters.append("F")
    #             else:
    #                 student10_gradescore_letters.append("Invalid score")
    #     print(student10_subject_grades)
    #     print(student10_gradescore_letters)
    #     exam_processing_system()
    elif option=="14":
        if student1_subject_grades == {}: # or student2_subject_grades =={} or student3_subject_grades == {} or student4_subject_grades =={} or student5_subject_grades =={} or student6_subject_grades =={} or student7_subject_grades =={} or student8_subject_grades =={} or student9_subject_grades =={} or student10_subject_grades =={}:
            print("There are no grades to display. Register grades first")
            exam_processing_system()
        elif student_name_and_id == {}:
            print("There are no students to display grades for. Register students first")
            exam_processing_system()
        else:
            first_student_name = list(student_name_and_id.keys())[0]
            first_student_id = list(student_name_and_id.values())[0]

            first1_subject_name = list(student1_subject_grades.keys())[0]
            first1_subject_score = list(student1_subject_grades.values())[0]

            second1_subject_name = list(student1_subject_grades.keys())[1]
            second1_subject_score = list(student1_subject_grades.values())[1]

            third1_subject_name = list(student1_subject_grades.keys())[2]
            third1_subject_score = list(student1_subject_grades.values())[2]

            fourth1_subject_name = list(student1_subject_grades.keys())[3]
            fourth1_subject_score = list(student1_subject_grades.values())[3]

            fifth1_subject_name = list(student1_subject_grades.keys())[4]
            fifth1_subject_score = list(student1_subject_grades.values())[4]
            
            mean1 = (first1_subject_score + second1_subject_score + third1_subject_score + fourth1_subject_score + fifth1_subject_score)/5
            #-------------------------------------------------------------------------------------
            # second_student_name = list(student_name_and_id.keys())[1]
            # second_student_id = list(student_name_and_id.values())[1]

            # first2_subject_name = list(student2_subject_grades.keys())[0]
            # first2_subject_score = list(student2_subject_grades.values())[0]

            # second2_subject_name = list(student2_subject_grades.keys())[1]
            # second2_subject_score = list(student2_subject_grades.values())[1]

            # third2_subject_name = list(student2_subject_grades.keys())[2]
            # third2_subject_score = list(student2_subject_grades.values())[2]

            # fourth2_subject_name = list(student2_subject_grades.keys())[3]
            # fourth2_subject_score = list(student2_subject_grades.values())[3]

            # fifth2_subject_name = list(student2_subject_grades.keys())[4]
            # fifth2_subject_score = list(student2_subject_grades.values())[4]
            
            # mean2 = (first2_subject_score + second2_subject_score + third2_subject_score + fourth2_subject_score + fifth2_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # third_student_name = list(student_name_and_id.keys())[2]
            # third_student_id = list(student_name_and_id.values())[2]

            # first3_subject_name = list(student3_subject_grades.keys())[0]
            # first3_subject_score = list(student3_subject_grades.values())[0]

            # second3_subject_name = list(student3_subject_grades.keys())[1]
            # second3_subject_score = list(student3_subject_grades.values())[1]

            # third3_subject_name = list(student3_subject_grades.keys())[2]
            # third3_subject_score = list(student3_subject_grades.values())[2]

            # fourth3_subject_name = list(student3_subject_grades.keys())[3]
            # fourth3_subject_score = list(student3_subject_grades.values())[3]

            # fifth3_subject_name = list(student3_subject_grades.keys())[4]
            # fifth3_subject_score = list(student3_subject_grades.values())[4]
            
            # mean3 = (first3_subject_score + second3_subject_score + third3_subject_score + fourth3_subject_score + fifth3_subject_score)/5

            # #-------------------------------------------------------------------------------------
            # fourth_student_name = list(student_name_and_id.keys())[3]
            # fourth_student_id = list(student_name_and_id.values())[3]

            # first4_subject_name = list(student4_subject_grades.keys())[0]
            # first4_subject_score = list(student4_subject_grades.values())[0]

            # second4_subject_name = list(student4_subject_grades.keys())[1]
            # second4_subject_score = list(student4_subject_grades.values())[1]

            # third4_subject_name = list(student4_subject_grades.keys())[2]
            # third4_subject_score = list(student4_subject_grades.values())[2]

            # fourth4_subject_name = list(student4_subject_grades.keys())[3]
            # fourth4_subject_score = list(student4_subject_grades.values())[3]

            # fifth4_subject_name = list(student4_subject_grades.keys())[4]
            # fifth4_subject_score = list(student4_subject_grades.values())[4]
            
            # mean4 = (first4_subject_score + second4_subject_score + third4_subject_score + fourth4_subject_score + fifth4_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # fifth_student_name = list(student_name_and_id.keys())[4]
            # fifth_student_id = list(student_name_and_id.values())[4]

            # first5_subject_name = list(student5_subject_grades.keys())[0]
            # first5_subject_score = list(student5_subject_grades.values())[0]

            # second5_subject_name = list(student5_subject_grades.keys())[1]
            # second5_subject_score = list(student5_subject_grades.values())[1]

            # third5_subject_name = list(student5_subject_grades.keys())[2]
            # third5_subject_score = list(student5_subject_grades.values())[2]

            # fourth5_subject_name = list(student5_subject_grades.keys())[3]
            # fourth5_subject_score = list(student5_subject_grades.values())[3]

            # fifth5_subject_name = list(student5_subject_grades.keys())[4]
            # fifth5_subject_score = list(student5_subject_grades.values())[4]
            
            # mean5 = (first5_subject_score + second5_subject_score + third5_subject_score + fourth5_subject_score + fifth5_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # sixth_student_name = list(student_name_and_id.keys())[5]
            # sixth_student_id = list(student_name_and_id.values())[5]

            # first6_subject_name = list(student6_subject_grades.keys())[0]
            # first6_subject_score = list(student6_subject_grades.values())[0]

            # second6_subject_name = list(student6_subject_grades.keys())[1]
            # second6_subject_score = list(student6_subject_grades.values())[1]

            # third6_subject_name = list(student6_subject_grades.keys())[2]
            # third6_subject_score = list(student6_subject_grades.values())[2]

            # fourth6_subject_name = list(student6_subject_grades.keys())[3]
            # fourth6_subject_score = list(student6_subject_grades.values())[3]

            # fifth6_subject_name = list(student6_subject_grades.keys())[4]
            # fifth6_subject_score = list(student6_subject_grades.values())[4]
            
            # mean6 = (first6_subject_score + second6_subject_score + third6_subject_score + fourth6_subject_score + fifth6_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # seventh_student_name = list(student_name_and_id.keys())[6]
            # seventh_student_id = list(student_name_and_id.values())[6]

            # first7_subject_name = list(student7_subject_grades.keys())[0]
            # first7_subject_score = list(student7_subject_grades.values())[0]

            # second7_subject_name = list(student7_subject_grades.keys())[1]
            # second7_subject_score = list(student7_subject_grades.values())[1]

            # third7_subject_name = list(student7_subject_grades.keys())[2]
            # third7_subject_score = list(student7_subject_grades.values())[2]

            # fourth7_subject_name = list(student7_subject_grades.keys())[3]
            # fourth7_subject_score = list(student7_subject_grades.values())[3]

            # fifth7_subject_name = list(student7_subject_grades.keys())[4]
            # fifth7_subject_score = list(student7_subject_grades.values())[4]
            
            # mean7 = (first7_subject_score + second7_subject_score + third7_subject_score + fourth7_subject_score + fifth7_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # eighth_student_name = list(student_name_and_id.keys())[7]
            # eighth_student_id = list(student_name_and_id.values())[7]

            # first8_subject_name = list(student8_subject_grades.keys())[0]
            # first8_subject_score = list(student8_subject_grades.values())[0]

            # second8_subject_name = list(student8_subject_grades.keys())[1]
            # second8_subject_score = list(student8_subject_grades.values())[1]

            # third8_subject_name = list(student8_subject_grades.keys())[2]
            # third8_subject_score = list(student8_subject_grades.values())[2]

            # fourth8_subject_name = list(student8_subject_grades.keys())[3]
            # fourth8_subject_score = list(student8_subject_grades.values())[3]

            # fifth8_subject_name = list(student8_subject_grades.keys())[4]
            # fifth8_subject_score = list(student8_subject_grades.values())[4]
            
            # mean8 = (first8_subject_score + second8_subject_score + third8_subject_score + fourth8_subject_score + fifth8_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # ninth_student_name = list(student_name_and_id.keys())[8]
            # ninth_student_id = list(student_name_and_id.values())[8]

            # first9_subject_name = list(student9_subject_grades.keys())[0]
            # first9_subject_score = list(student9_subject_grades.values())[0]

            # second9_subject_name = list(student9_subject_grades.keys())[1]
            # second9_subject_score = list(student9_subject_grades.values())[1]

            # third9_subject_name = list(student9_subject_grades.keys())[2]
            # third9_subject_score = list(student9_subject_grades.values())[2]

            # fourth9_subject_name = list(student9_subject_grades.keys())[3]
            # fourth9_subject_score = list(student9_subject_grades.values())[3]

            # fifth9_subject_name = list(student9_subject_grades.keys())[4]
            # fifth9_subject_score = list(student9_subject_grades.values())[4]
            
            # mean9 = (first9_subject_score + second9_subject_score + third9_subject_score + fourth9_subject_score + fifth9_subject_score)/5
            # #-------------------------------------------------------------------------------------
            # tenth_student_name = list(student_name_and_id.keys())[9]
            # tenth_student_id = list(student_name_and_id.values())[9]

            # first10_subject_name = list(student10_subject_grades.keys())[0]
            # first10_subject_score = list(student10_subject_grades.values())[0]

            # second10_subject_name = list(student10_subject_grades.keys())[1]
            # second10_subject_score = list(student10_subject_grades.values())[1]

            # third10_subject_name = list(student10_subject_grades.keys())[2]
            # third10_subject_score = list(student10_subject_grades.values())[2]

            # fourth10_subject_name = list(student10_subject_grades.keys())[3]
            # fourth10_subject_score = list(student10_subject_grades.values())[3]

            # fifth10_subject_name = list(student10_subject_grades.keys())[4]
            # fifth10_subject_score = list(student10_subject_grades.values())[4]
            
            # mean10 = (first10_subject_score + second10_subject_score + third10_subject_score + fourth10_subject_score + fifth10_subject_score)/5
            #-------------------------------------------------------------------------------------
            #-------------------------------------------------------------------------------------
            #-------------------------------------------------------------------------------------

            def mean_letter_grader(x):
                if x >= 90 and x <= 100:
                    return("A")
                elif x >= 87 and x < 90:
                    return("A-")
                elif x >= 84 and x < 87:
                    return("B+")
                elif x >= 80 and x < 84:
                    return("B")
                elif x >= 77 and x < 80:
                    return("B-")
                elif x >= 74 and x < 77:
                    return("C+")
                elif x >= 70 and x < 74:
                    return("C")
                elif x >= 67 and x < 70:
                    return("C-")
                elif x>= 64 and x < 67:
                    return("D+")
                elif x >= 62 and x < 64:
                    return("D")
                elif x >= 60 and x < 62:
                    return("D-")
                elif x < 60:
                    return("F")
                else:
                    return("Invalid score")

            # ----------------------------------------------------------------------------------------------------------------
            
            def comment_grader(y):
                if y == "A":
                    return("Exceptional performance!")
                elif y == "A-":
                    return("Excellent work!")
                elif y == "B+":
                    return("Very Good Job!")
                elif y == "B":
                    return("Good work!")
                elif y == "B-":
                    return("Fairly Good Effort!")
                elif y == "C+":
                    return("Satisfactory perfomance!")
                elif y == "C":
                    return("Average work!")
                elif y =="C-":
                    return("Below Average!")
                elif y == "D+":
                    return("Needs improvement!")
                elif y == "D":
                    return("Poor performance!")
                elif y == "D-":
                    return("Very weak understanding!")
                elif y == "F":
                    return("Failing!")
                else:
                    return("Invalid grade")

            # ----------------------------------------------------------------------------------------------------------------

            print("------------------------ALL STUDENT REPORTS------------------------")
            print("--------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------")
            print("NAME:", first_student_name, "      ", "ID:", first_student_id)
            print("SUBJECT           SCORE            GRADE")
            print(first1_subject_name, "           ", first1_subject_score, "           ", student1_gradescore_letters[0])
            print(second1_subject_name, "           ", second1_subject_score, "           ", student1_gradescore_letters[1])
            print(third1_subject_name, "           ", third1_subject_score, "           ", student1_gradescore_letters[2])
            print(fourth1_subject_name, "           ", fourth1_subject_score, "           ", student1_gradescore_letters[3])
            print(fifth1_subject_name, "           ", fifth1_subject_score, "           ", student1_gradescore_letters[4])
            print("MEAN:", "           ", mean1, "           ", mean_letter_grader(mean1))
            print("COMMENT:", " ", comment_grader(mean_letter_grader(mean1)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", second_student_name, "      ", "ID:", second_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first2_subject_name, "           ", first2_subject_score, "           ", student2_gradescore_letters[0])
            # print(second2_subject_name, "           ", second2_subject_score, "           ", student2_gradescore_letters[1])
            # print(third2_subject_name, "           ", third2_subject_score, "           ", student2_gradescore_letters[2])
            # print(fourth2_subject_name, "           ", fourth2_subject_score, "           ", student2_gradescore_letters[3])
            # print(fifth2_subject_name, "           ", fifth2_subject_score, "           ", student2_gradescore_letters[4])
            # print("MEAN:", "           ", mean2, "           ", mean_letter_grader(mean2))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean2)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", third_student_name, "      ", "ID:", third_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first3_subject_name, "           ", first3_subject_score, "           ", student3_gradescore_letters[0])
            # print(second3_subject_name, "           ", second3_subject_score, "           ", student3_gradescore_letters[1])
            # print(third3_subject_name, "           ", third3_subject_score, "           ", student3_gradescore_letters[2])
            # print(fourth3_subject_name, "           ", fourth3_subject_score, "           ", student3_gradescore_letters[3])
            # print(fifth3_subject_name, "           ", fifth3_subject_score, "           ", student3_gradescore_letters[4])
            # print("MEAN:", "           ", mean3, "           ", mean_letter_grader(mean3))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean3)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", fourth_student_name, "      ", "ID:", fourth_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first4_subject_name, "           ", first4_subject_score, "           ", student4_gradescore_letters[0])
            # print(second4_subject_name, "           ", second4_subject_score, "           ", student4_gradescore_letters[1])
            # print(third4_subject_name, "           ", third4_subject_score, "           ", student4_gradescore_letters[2])
            # print(fourth4_subject_name, "           ", fourth4_subject_score, "           ", student4_gradescore_letters[3])
            # print(fifth4_subject_name, "           ", fifth4_subject_score, "           ", student4_gradescore_letters[4])
            # print("MEAN:", "           ", mean4, "           ", mean_letter_grader(mean4))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean4)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", fifth_student_name, "      ", "ID:", fifth_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first5_subject_name, "           ", first5_subject_score, "           ", student5_gradescore_letters[0])
            # print(second5_subject_name, "           ", second5_subject_score, "           ", student5_gradescore_letters[1])
            # print(third5_subject_name, "           ", third5_subject_score, "           ", student5_gradescore_letters[2])
            # print(fourth5_subject_name, "           ", fourth5_subject_score, "           ", student5_gradescore_letters[3])
            # print(fifth5_subject_name, "           ", fifth5_subject_score, "           ", student5_gradescore_letters[4])
            # print("MEAN:", "           ", mean5, "           ", mean_letter_grader(mean5))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean5)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", sixth_student_name, "      ", "ID:", sixth_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first6_subject_name, "           ", first6_subject_score, "           ", student6_gradescore_letters[0])
            # print(second6_subject_name, "           ", second6_subject_score, "           ", student6_gradescore_letters[1])
            # print(third6_subject_name, "           ", third6_subject_score, "           ", student6_gradescore_letters[2])
            # print(fourth6_subject_name, "           ", fourth6_subject_score, "           ", student6_gradescore_letters[3])
            # print(fifth6_subject_name, "           ", fifth6_subject_score, "           ", student6_gradescore_letters[4])
            # print("MEAN:", "           ", mean6, "           ", mean_letter_grader(mean6))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean6)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", seventh_student_name, "      ", "ID:", seventh_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first7_subject_name, "           ", first7_subject_score, "           ", student7_gradescore_letters[0])
            # print(second7_subject_name, "           ", second7_subject_score, "           ", student7_gradescore_letters[1])
            # print(third7_subject_name, "           ", third7_subject_score, "           ", student7_gradescore_letters[2])
            # print(fourth7_subject_name, "           ", fourth7_subject_score, "           ", student7_gradescore_letters[3])
            # print(fifth7_subject_name, "           ", fifth7_subject_score, "           ", student7_gradescore_letters[4])
            # print("MEAN:", "           ", mean7, "           ", mean_letter_grader(mean7))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean7)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", eighth_student_name, "      ", "ID:", eighth_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first8_subject_name, "           ", first8_subject_score, "           ", student8_gradescore_letters[0])
            # print(second8_subject_name, "           ", second8_subject_score, "           ", student8_gradescore_letters[1])
            # print(third8_subject_name, "           ", third8_subject_score, "           ", student8_gradescore_letters[2])
            # print(fourth8_subject_name, "           ", fourth8_subject_score, "           ", student8_gradescore_letters[3])
            # print(fifth8_subject_name, "           ", fifth8_subject_score, "           ", student8_gradescore_letters[4])
            # print("MEAN:", "           ", mean8, "           ", mean_letter_grader(mean8))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean8)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", ninth_student_name, "      ", "ID:", ninth_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first9_subject_name, "           ", first9_subject_score, "           ", student9_gradescore_letters[0])
            # print(second9_subject_name, "           ", second9_subject_score, "           ", student9_gradescore_letters[1])
            # print(third9_subject_name, "           ", third9_subject_score, "           ", student9_gradescore_letters[2])
            # print(fourth9_subject_name, "           ", fourth9_subject_score, "           ", student9_gradescore_letters[3])
            # print(fifth9_subject_name, "           ", fifth9_subject_score, "           ", student9_gradescore_letters[4])
            # print("MEAN:", "           ", mean9, "           ", mean_letter_grader(mean9))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean9)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            # print("NAME:", tenth_student_name, "      ", "ID:", tenth_student_id)
            # print("SUBJECT           SCORE            GRADE")
            # print(first10_subject_name, "           ", first10_subject_score, "           ", student10_gradescore_letters[0])
            # print(second10_subject_name, "           ", second10_subject_score, "           ", student10_gradescore_letters[1])
            # print(third10_subject_name, "           ", third10_subject_score, "           ", student10_gradescore_letters[2])
            # print(fourth10_subject_name, "           ", fourth10_subject_score, "           ", student10_gradescore_letters[3])
            # print(fifth10_subject_name, "           ", fifth10_subject_score, "           ", student10_gradescore_letters[4])
            # print("MEAN:", "           ", mean10, "           ", mean_letter_grader(mean10))
            # print("COMMENT:", " ", comment_grader(mean_letter_grader(mean10)))

            # print("--------------------------------------------------------------------------------------------------")
            # print("--------------------------------------------------------------------------------------------------")
            
        exam_processing_system()

    else:
        print("Invalid input. Please enter a valid option.")
        exam_processing_system()


        

exam_processing_system()