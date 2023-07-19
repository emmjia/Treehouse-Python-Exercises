import datetime

# Step 1
# Ask the user for their name and the year they were born.

print("Hello, what is your name and what year were you born?")
name = input("Name? ")

year = input("Birth Year? ")

while not year.isdigit():
    try:
        int(year)
    except ValueError:
        print("An integer needs to be provided. Please provide a numerical value to the question")    
    year = input("birth year? ")
    
print(f"Please to meet you {name} from the year {year}.")   
year = int(year)
 
# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.

print(f"So {name}...")

year_25 = year + 25

year_50 = year + 50 

year_75 = year + 75

year_100 = year + 100

# Step 3
# If they're already past any of these ages, skip them.

year_list = [year_25,year_50,year_75,year_100]
age_list = [25,50,75,100]
current_year = datetime.datetime.now().year

for age_year, age in zip(year_list, age_list):
    if age_year > current_year:
        print(f"At the year {age_year} you will be {age}")
    else:
        pass