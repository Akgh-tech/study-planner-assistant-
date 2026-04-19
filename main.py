subjects = input("Enter subjects (comma separated): ")
time = int(input("Enter total study time (in hours): "))

subject_list = subjects.split(",")

if time <= 2:
    print("Focus on:", subject_list[0])
else:
    per_subject = time / len(subject_list)
    for sub in subject_list:
        print(f"Study {sub.strip()} for {round(per_subject,1)} hours")

print("Take a 5-10 min break every hour.")
print("Revise important topics at the end.")
