example = {}
example.setdefault('a', []).append('apple')
example.setdefault('b', []).append('boots')
example.setdefault('c', []).append('cat')
example.setdefault('a', []).append('ant')
example.setdefault('a', []).append('apple')

print(example)
student={}
student.setdefault("name",[]).append("Ram")
student.setdefault("name",[]).append("Ramukaka")
student.setdefault("name",[]).append("Ramesh")
student.setdefault("name",[]).append("Ramila")

student.setdefault("course",[]).append("Python")
student.setdefault("course",[]).append("C++")
student.setdefault("course",[]).append("DBMS")
student.setdefault("course",[]).append("JAva")

print(student)
print("all students: ",student["name"])
print("all courses:",student["course"])

print(student["Ram"])
