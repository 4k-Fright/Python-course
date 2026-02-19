# Exercise 1: Software Licensing Tracker

# Dictionary with (user_email, software_name) as key and expiration date as value
licenses = {
    ("user1@gmail.com", "Photoshop"): "2026-01-10",
    ("user2@gmail.com", "PyCharm"): "2025-12-01",
    ("user3@gmail.com", "VSCode"): "2027-03-15"
}

# Update one expiry date
licenses[("user2@gmail.com", "PyCharm")] = "2026-12-01"

print("Updated licenses:", licenses)



# Exercise 2: Stock Portfolio

# Use (investor_name, stock_symbol) as key and number of shares  as value
stock = {
    ("Sammie", "META"): 50,
    ("Jeremy", "NETFLIX"): 30,
    ("Rheamy", "SPOTIFY"): 20,
    ("Eirene", "AMAZON"): 15
}

# Increase shares of one stock
stock[("Sammie", "META")] += 25
print("Updated stock:", stock)

# Calculate total number of shares held by Sammie
total_shares = 0
for (invest, stock), shares in stock.items():
    if invest == "Sammie":
        total_shares += shares

print("Total shares held by Sammie:", total_shares)



# Exercise 3
# Health (Patient Check-in Records)

# Store check-in times using (patient_id, date) as key and time as value
checkins = {
    ("Patient1", "2026-02-15"): "09:00 AM",
    ("Patient2", "2026-02-15"): "09:30 AM",
    ("Patient3", "2026-02-15"): "10:15 AM",
    ("Patient4", "2026-02-15"): "11:00 AM",
    ("Patient5", "2026-02-15"): "11:45 AM"
}
print("Checkings:", checkins)



# Exercise 4: Student Scores

# Dictionary with (student_name, subject) as key and score as value
scores = {
    ("Sammie", "Math"): 89,
    ("Rachel", "Chemistry"): 72,
    ("Ozuor", "Math"): 88,
    ("Virtue", "English"): 92,
    ("Xavier", "French"): 81
}
print("Scores:", scores)

# Get Sammie's Math score
sammie_math = scores.get(("Sammie", "Math"))
print("Sammie's Math score:", sammie_math)

# Calculate average score
total = sum(scores.values())
count = len(scores)

average = total / count
print("Average score:", average)



# Exercise 5: Machine Maintenance Records

# Use (machine_id, date) as key and status as value
maintenance = {
    ("Machine1", "2026-02-11"): "Pending",
    ("Machine2", "2026-02-23"): "Pending",
    ("Machine3", "2026-02-19"): "Renewed",
    ("Machine4", "2026-02-29"): "Pending",
    ("Machine5", "2026-02-31"): "Confirmed",
    ("Machine6", "2026-02-10"): "Serviced",
    ("Machine7", "2026-02-24"): "Pending"
}

# Change status of one machine
maintenance[("Machine5", "2026-02-31")] = "Later things"
print("Status change:", maintenance)

# Count how many machines are pending service
pending_count = 0
for status in maintenance.values():
    if status == "Pending":
        pending_count += 1

print("Pending machines:", pending_count)