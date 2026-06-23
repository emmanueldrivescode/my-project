import json

json_string = '{"name": "Emmanuel", "age": 21, "is_student": true}'

student = {
    "name": "Emmanuel Dairo",
    "age": 21,
    "level": 200,
    "department": "Computer Science",
    "is_active": True,
    
    "cgpa": 4.25,
    
    "skills": ["Python", "HTML", "CSS", "Git", "JavaScript"],
    
    "courses": {
        "first_semester": ["CSC201", "MTH201", "GST201"],
        "second_semester": ["CSC202", "MTH202", "GST202"]
    },
    
    "projects": [
        {
            "title": "Student Registration System",
            "language": "C#",
            "status": "completed"
        },
        {
            "title": "Portfolio Website",
            "language": "HTML/CSS/JS",
            "status": "in progress"
        }
    ],
    
    "address": {
        "city": "Port Harcourt",
        "state": "Rivers",
        "country": "Nigeria"
    }
}

text = json.loads(json_string)
print(text)

with open("user.json", "r") as file:
    data = json.load(file)
    print(data["projects"][1])

text2 = json.dumps(
        student, 
        sort_keys=True, 
        separators=(". ", " = "), 
        indent=2
    )
print(text2)