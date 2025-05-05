import json
import os
from datetime import datetime
import fpdf

file_path = "diary.txt"


def time_difference(input_time_str):

    #Calculates the time difference between now and a given time.
    #Args: input_time_str: A string representing the time in the format "YYYY-MM-DD HH:MM".
    #Returns: A string representing the time difference in hours and minutes.

    input_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M")
    now = datetime.now()
    difference = now - input_time

    total_minutes = int(difference.total_seconds() // 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    return f"{hours} hours, {minutes} minutes"

def visualize(txtfile):
    with open("diary.txt", "r", encoding="utf-8") as f:
        #ensures that this only runs of the diary is not empty
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            print("The diary is empty.")
            return

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()

    # Set title font
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Food Diary Log", ln=True, align="C")
    pdf.ln(10)  # Add a line break

    # Set content font
    pdf.set_font("Arial", size=12)

    # Iterate through the diary entries and format them nicely
    for entry in data:
        # Add a header for each meal
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=f"Meal: {entry['meal']}", ln=True)

        # Add date and time information
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(200, 10, txt=f"Date: {entry['date']} | Time: {entry['time']}", ln=True)

        # Add ingredients list
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(200, 10, txt=f"Ingredients: {entry['ingredients']}")

        pdf.ln(5)  # Add a small space between entries

    # Output the PDF to a file
    pdf.output("diary_log.pdf")


options = [
    "Enter a new log",
    "View your log",
    "Time since last meal",
    "Search a particular dish",
    "Delete my food diary."
    ]

for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")

while True:

        choice = input('What would you like to do? Choose a number between 1 and 5: ')

        if choice == '1':
            print("NEW LOG INPUT")
            while True:
                meal = input("What meal did you eat? E.g. breakfast, lunch, or dinner. ").strip().lower()
                #ensures the meal type is either breakfast lunch or dinner
                if meal == "breakfast":
                    break
                elif meal == "lunch":
                    break
                elif meal == "dinner":
                    break
                else:
                    print("Meal must be either breakfast, lunch, or dinner. Please try again.")

            # Ensures date inputted correctly
            while True:
                day = input("What is the date? Enter in YYYY-MM-DD: ")
                try:
                    date_obj = datetime.strptime(day, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please enter as YYYY-MM-DD (e.g., 2025-05-05).")

            # Ensures time inputted correctly
            while True:
                time = input("What time did you start eating? Enter in HH:MM (24-hour format): ")
                try:
                    time_obj = datetime.strptime(time, "%H:%M")
                    break
                except ValueError:
                    print("Invalid time format. Please enter as HH:MM in military time(e.g., 13:45 for 1:45 PM).")

            ingredients = input("List all the ingredients in your meal: ")

            # Store the results in a dictionary in the diary
            log_entry = {
                "date": day,
                "meal": meal,
                "time": time,
                "ingredients": ingredients
            }

            # Load existing logs if the file exists
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open("diary.txt", "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.decoder.JSONDecodeError:
                        data = []
            else:
                data = []

            # Add the new entry
            data.append(log_entry)

            # Sort the data in chronological order using an inline function, this we got from

            data.sort(key=lambda entry: datetime.strptime(f"{entry['date']} {entry['time']}", "%Y-%m-%d %H:%M"))


            # Save updated log
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

            print("✅ Meal logged successfully!")
            break

        elif choice == '2':
            # Visualize the dictionary
            visualize("diary.txt")
            break

        elif choice == "3":
            # Load the diary data from the file
            with open("diary.txt", "r", encoding="utf-8") as f:
                try:
                    diary_data = json.load(f)
                except json.decoder.JSONDecodeError:
                    print("The diary is empty.")
                    diary_data = []

            # Get the last entry’s time and date
            last_time = diary_data[-1]["time"]
            last_date = diary_data[-1]["date"]
            print("Last time:", last_time)
            print("Last date:", last_date)

            # Combine the date and time into a single string
            time = f"{last_date} {last_time}"

            # Now compute the time difference
            difference = time_difference(time)
            print(f"Time difference: {difference}")
            break

        elif choice == "4":
            try:
                with open("diary.txt", "r", encoding="utf-8") as f:
                    diary_data = json.load(f)
            except json.decoder.JSONDecodeError:
                print("The diary is empty.")

            while True:
                know_date = input("Do you remember the date of this meal? (yes/no): ").strip().lower()
                if know_date == "yes":
                    exact_date = input("Enter the date in YYYY-MM-DD: ").strip()
                    meals_on_date = [entry for entry in diary_data if entry.get("date") == exact_date]

                    if meals_on_date:
                        print(f"Meals on {exact_date}:")
                        for meal in meals_on_date:
                            print(f"- {meal['meal']} at {meal['time']} (Ingredients: {meal['ingredients']})")
                        break
                    else:
                        print(f"No meals found on {exact_date}.")
                    break

                elif know_date == "no":
                    know_year = input("Do you remember the year of the meal? (yes/no): ").strip().lower()
                    if know_year == 'yes':
                        exact_year = input("Enter it as YYYY: ").strip()
                        know_meal = input("Do you remember the meal type? (yes/no): ").strip().lower()
                        if know_meal == 'yes':
                            exact_meal = input("Enter it (e.g. breakfast/lunch/dinner): ").strip().lower()
                            meals_in_year = [
                                entry for entry in diary_data
                                if entry.get("date", "").startswith(exact_year)
                                and exact_meal in entry.get("meal", "").lower()
                            ]
                        elif know_meal == 'no':
                            print("Too many meals in 1 year. Not enough information provided to find a specific meal.")
                            break
                        else:
                            print("Answer must be either 'yes' or 'no'. Please try again.")
                            continue

                        if meals_in_year:
                            print(f"Meals in {exact_year} matching '{exact_meal}':")
                            for meal in meals_in_year:
                                print(f"- {meal['date']} - {meal['meal']} at {meal['time']}")
                        else:
                            print(f"No meals found in {exact_year} for type '{exact_meal}'.")
                        break

                    elif know_year == 'no':
                        print("Not enough information to find a meal.")
                        break
                    else:
                        print("Answer must be either 'yes' or 'no'. Please try again.")
                    break

                else:
                    print("Answer must be either 'yes' or 'no'. Please try again.")


        elif choice == "5":
            certainty = input("Are you sure you want to delete your diary? (yes/no): ").strip().lower()
            if certainty == "yes":
                with open("diary.txt", "w", encoding="utf-8") as f:
                    pass   # opening in "w" mode automatically clears the file
                print("🗑️ Diary cleared successfully.")
            else:
                print("Operation canceled. Your Diary was not cleared.")
            break

        else:
            print("choice must be either 1, 2, 3, 4 or 5. Please input again")

