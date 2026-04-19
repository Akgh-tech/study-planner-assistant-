print("🤖 Smart Study Planner Assistant")
print("----------------------------------")

subjects = input("Enter subjects (comma separated): ")
time = float(input("Enter total study time (in hours): "))

subject_list = subjects.split(",")

print("\n🤖 Analyzing your input...")

# Smart decision logic
if time <= 1:
    print("⚠️ Very limited time. Focus on one important subject.")
    print(f"👉 Study {subject_list[0].strip()} only.")
elif time <= 3:
    print("📖 Moderate time. Cover 1-2 subjects with revision.")
    for sub in subject_list[:2]:
        print(f"👉 Study {sub.strip()}")
else:
    print("🚀 Good time! Creating a balanced plan...")
    per_subject = time / len(subject_list)
    for sub in subject_list:
        print(f"👉 Study {sub.strip()} for {round(per_subject,1)} hours")

# Extra touches
print("\n⏰ Take a 5-10 min break every hour.")
print("🔁 Revise key topics at the end.")
print("✨ Stay consistent. You got this!")
