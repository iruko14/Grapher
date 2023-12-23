import read_growth as rd
import API_request as ap

# Input to select a feature of the app
feature_select = input('''Welcome to Grapher! how i can help you?
1. Population growth per country
2. API load: 
''')
# Features list to request
option_dict = {
    "1": "Population growth per country",
    "2": "API load",
}

if feature_select in option_dict:
  # Get the corresponding option
  feature_pick = option_dict[feature_select]

print("--------------------------------------------------")

print(feature_pick, " is selected")

print("--------------------------------------------------")


if feature_pick == "Population growth per country":
    rd.rdg_init()
elif feature_pick == "API load":
    ap.API_init()
else:
   print("wrong_selection, try again")
