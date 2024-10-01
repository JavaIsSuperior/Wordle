import nav

file_name = input("Enter a dictionary file name (empty to use default): ")
file_name = "default_dictionary.txt" if file_name == "" else file_name

nav.run_game(file_name)
