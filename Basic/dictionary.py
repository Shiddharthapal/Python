student={
    "name":"shiddhartha",
    "cgpa":3.77,
    "score":{
        "math":76,
        "eng":45,
        "ban":54,
    }
}

print(student["name"])
print(student["cgpa"])
print(student["score"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))
print(student.get("score"))
print(student["score"]["ban"])


newData={
    "id":"221-35-1069"
}
student.update(newData)
print(student.items())