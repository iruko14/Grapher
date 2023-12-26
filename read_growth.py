import pandas as pd
import matplotlib.pyplot as plt

def rdg_init():
    print("WIP")

    print("--------------------------------------------------")

    # Import the csv file
    df = pd.read_csv("growth_of_populations.csv")

    # Show the un input menu
    value_input = input(''' Which measure do you want to select?
1. Ø Growth/year
2. Growth 2013-2022
Select an option: ''')

    # Validating the user option
    if value_input == "1":
        value_input = "Ø Growth/year"
    elif value_input == "2":
        value_input = "Growth 2013-2022"
    else:
        value_input = 0

    print("--------------------------------------------------")

    # Printing the selected option
    if value_input != 0:
        print(value_input, "is selected")
    else:
        print("Wrong selection, try again")

    # Converting value_input in a measure index
    measure = df[value_input]

    print("--------------------------------------------------")

    while value_input != 0:
        
        # Creating a countries list
        countries = []

        # Loop to country select
        while True:
            country = input("Select a country: ")

            # Validating the country select
            if country in df["Country/Region"].tolist():
                countries.append(country)
            else:
                print("Wrong selection, try again")

            print("--------------------------------------------------")

            # Ask to user to adding more countries
            continue_select = input("Do you want to add more countries? (yes/no): ")
            continue_select = continue_select.lower()

            if continue_select == "yes":
                continue
            elif continue_select == "no":
                break
            else:
                print("Wrong selection, try again")

        print("--------------------------------------------------")

        #Showing selected countries
        print('Selected countries:', countries)
        

        # Converting the countries list to index
        index = pd.Index([])
        def get_indices(countries, df):
            """
            Obtains the indexes by the selected countries

            Args:
                countries: Selected countries list
                df: CSV Dataframe

            Returns:
                Index list of the selected countries
            """

            index = []
            for country in countries:
                index.append(df["Country/Region"].tolist().index(country))

            return index
        

        index = get_indices(countries, df)

        # Getting direct index values by countries
        countries_index = df["Country/Region"]

        measure_value = measure[index]

        # Deleting the "%" character by the measure to sort y axis
        def delete_perc (measure_value):
            return float(measure_value[:-1])
        
        measure_value = [delete_perc(measure_value) for measure_value in measure_value]

        print("--------------------------------------------------")

        print('measure values:', measure_value)

        print("--------------------------------------------------")

        # Creating the bar chart
        plt.bar(countries_index[index], measure_value, color='red', alpha=0.5)
        plt.title("GDP Growth")
        plt.xlabel("Country")
        plt.ylabel(measure.name)
        plt.axhline(0, color='red')
        plt.show()

        break