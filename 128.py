Grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
Students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
average = [sum(Grades[0])/len(Grades[0]), sum(Grades[1])/len(Grades[1]),
           sum(Grades[2])/len(Grades[2]), sum(Grades[3])/len(Grades[3]),
           sum(Grades[4])/len(Grades[4])]
Students_sort = sorted(Students)
dict = dict(zip(Students_sort, average))
print(dict)