timetable = {
    "Monday": ["Python", "Maths", "Lab"],
    "Tuesday": ["Databases", "English"],
    "Wednesday": ["Python", "Project"]
}

for day, subjects in timetable.items():
    print(f"{day:<12}{', '.join(subjects)}")

timetable["Thursday"] = ["Revision"]
timetable["Monday"].append("Sports")

print(f"\nMonday now has {len(timetable['Monday'])} periods.")

all_subjects = set()

for subjects in timetable.values():
    all_subjects.update(subjects)

print("Unique subjects:", sorted(all_subjects))