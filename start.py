import read_growth as rd
import API_request as ap

# Input to select a feature of the app
feature_select = input('''Welcome to Grapher! how i can help you?
1. Population growth per country
2. API load
Introduce an option: ''')
# Features list to request
option_dict = {
    "1": "Population growth per country",
    "2": "API load",
}

if feature_select in option_dict:
  # Get the corresponding option
  feature_pick = option_dict[feature_select]
else:
   feature_pick = 0
   
print("--------------------------------------------------")

# Validating feature_pick
if feature_pick != 0:
    print(feature_pick, " is selected")
else:
    print("Wrong selection, try again")

print("--------------------------------------------------")

# Printing option
if feature_pick == "Population growth per country":
    rd.rdg_init()
elif feature_pick == "API load":
    ap.get_categories()

