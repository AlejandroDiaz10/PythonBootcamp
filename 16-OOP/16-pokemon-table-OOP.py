# python3 -m venv env
# source env/bin/activate 
# pip install prettytable 

# Import the PrettyTable class
from prettytable import PrettyTable

# Create an object called table from the PrettyTable class
table = PrettyTable()

# Use its atributes and methods to add columns and rows
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Bulbasaur", "Grass"])

# Align the columns to the left (using the align attribute)
table.align = "l"

# Print the table
print(table)