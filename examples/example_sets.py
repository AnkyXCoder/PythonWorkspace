# You are working for the school Principal. We have a database of school students:
all_students = {'Bobby','Tammy','Jammy','Sally','Danny'}
print('list of students: ', all_students)
#during class, the teachers take attendance and compile it into a list. 
present_students = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!

print('absent students are: ', all_students.difference(present_students))