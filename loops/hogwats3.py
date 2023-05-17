#dict dictoonario (data structrute que te permite asociar un dato con otro) key y definicion
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
for student in students:
    print(student, students[student], sep=", ")