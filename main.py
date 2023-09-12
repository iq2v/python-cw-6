person = {
    "name":"jana",
    "age":16,
    "hobbies":["Study"]
}
print(person["name"])
print(person["age"])

#الجزء الثاني
person["age"] = 17
person["newproperty"] = "America"
print("person dictionary:",person)
print("person dictionary:", len(person))

#الجزء الثالث
person["hobbies"].append("Read")
print("person dictionary", person)

def check_hobbies(person):
    if "hobbies" in person:
        hobbies = person["hobbies"]
        if len(hobbies) > 3:
            person("wow you are amazing")
        return hobbies
    else:
        return []

person = {
    "name": "jana",
    "age" : 16,
    "hobbies":["study,read"]
}

hobbies = check_hobbies(person)
print("hobbies")


