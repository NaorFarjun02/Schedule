class_a={
    "08:00":"",
    "10:00":"",
    "12:00":""
}
class_b={
    "08:00":"",
    "10:00":"",
    "12:00":""
}

class_c={
    "08:00":"",
    "10:00":"",
    "12:00":""
}


classes_list={
    "math":{
        "not_available":[]
        },
    "physics":{
         "not_available":[]
        },
    "sport":{
         "not_available":[]
        }
}

def check_classes(class_z):
    lessons=[]
    for les in class_z.keys():
        if class_z[les] != "":
            lessons.append(class_z[les])
    return lessons

def add_lessons(class_z):
    class_lessons=check_classes(class_z)
    for les in classes_list.keys():
        if les in class_lessons:
            continue
        for i in class_z.keys():
            if les in class_lessons:
                break
            if i in classes_list[les]["not_available"]:
                continue
            if class_z[i] == "":
                class_z[i]=les
                classes_list[les]["not_available"].append(i)
                class_lessons.append(les)

    return class_z

print(str(classes_list))
print("class_a: " + str(add_lessons(class_a)))
print("class_b: " + str(add_lessons(class_b)))
print("class_b: " + str(add_lessons(class_b)))
print("class_c: " + str(add_lessons(class_c)))
print(str(classes_list))

