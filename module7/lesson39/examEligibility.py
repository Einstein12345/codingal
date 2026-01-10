attendance = float(input("Enter attendance percentage: "))
internal_marks = int(input("Enter internal marks: "))
fee_due = input("Any fee due? (yes/no): ").lower()

if attendance >= 75 and internal_marks >= 40 and fee_due == "no":
    print("✅ You are ELIGIBLE for the exam.")
else:
    print("❌ You are NOT eligible for the exam.")

    if attendance < 75:
        print("- Attendance is below 75%")
    if internal_marks < 40:
        print("- Internal marks are below 40")
    if fee_due == "yes":
        print("- Fee is due")