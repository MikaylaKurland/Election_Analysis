#counties = ["Arapahoe","Denver","Jefferson"]
#my_list=list()
#counties.append("El Paso")
#print(counties)
#my_tuple=tuple()
#counties_dict["Arapahoe"]=422829
#counties_dict["Denver"] = 463353
#counties_dict["Jefferson"] = 432438
#print(counties_dict)
#print(len(counties_dict))
#print(counties_dict.values())
#print(counties_dict.get("Denver"))
#voting_data=[]
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)
#__________________________________________________________________________
#Skill Drill #1
counties_dict={}
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
#__________________________________________________________________________
#Skill Drill #2
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    #print(county_dict)
    for value in county_dict.values():
        #print(value)
        print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")
#__________________________________________________________________________
      