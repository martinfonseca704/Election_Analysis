from cgi import print_arguments

score = int(input("What is your test score? "))

if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


#3.2.10 SKILL DRILL
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
for d in voting_data:
    county = d.get('county')
    voters = '{:,}'.format(d.get('registered_voters'))
    print(f'{county} county has {voters} registered voters.')
#3.2.10 SKILL DRILL
voting_data = [ {"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
output = [f'{x["county"]} County has {x["registered_voters"]:,} registered voters' for x in voting_data]
print(output)
##3.2.10 SKILL DRILL
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#Get Each Dictionary in a List of Dictionaries  
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for county_dict in voting_data:
    print(county_dict)

#Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

#3.2.11 Printing Formats
#The print() Function
print("Hello World")

print("Arapahoe and Denver are not in the list of counties.")
#vvvnot for running
print("Your interestpayment for the year is $" + str('interest'))

#F-strings: Formatted String Literals
#vvvnot for running
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Using F-Strings with Dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {3345} number of votes. "
    f"The total number of votes in the election was {23123}. "
    f"You received {3345 / 23123 * 100}% of the total votes.")

print(message_to_candidate)

#Format Floating-Point Decimals
#can format numbers with a thousands separator and specify a decimal precision.
#f'{value:{width}.{precision}}'

#f'{value:{width},.{precision}}'

message_to_candidate = (
    f"You received {3345:,} number of votes. "
    f"The total number of votes in the election was {23123:,}. "
    f"You received {3345 / 23123 * 100:.2f}% of the total votes.")
print(message_to_candidate)

#skill drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#skill drill
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for dic,county, registered_voters in voting_data.items():
    print( county + " county has " + str(registered_voters) + " registered voters. ")