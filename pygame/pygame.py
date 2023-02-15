# pygame [script_name]
# written on 13-feb-203 
# author : Sanjeev Stephan Murmu
import os 

figlet_path = "D:\\myscripts\\poweruser\\figlet.py"

list_of_games = {"Learn Alphabet position":"D:\\myscripts\\script.py\\pygame\\learn_alphabet_positions\\python-game-alphabet-position.py",
                "Muliplicaiton [Calculator]":"D:\\myscripts\\script.py\\pygame\maths\\101_input_multiply.py",
                "Random Muliplicaiton Game":"D:\\myscripts\\script.py\\pygame\maths\\102_random_multiply.py",
                "Square Game": "D:\\myscripts\\script.py\\pygame\maths\\100_square.py"
                }

# Get the length of the dictionary
length = len(list_of_games)

# Get the values of the dictionary
paths = list_of_games.values()

# Convert the values into a list
paths_list = list(paths)

class pygame:
    def launch():
        os.system('cls')  # Clears the Screen first
 
    def displayMsg(path_num=0, msg="pygame"):
        os.system("python {} --message {}".format(figlet_path,msg)) # display the pygame-welcome test 

    def excuteScript(path_num):
        #path_num=path_num+1
        os.system("python {}".format(paths_list[path_num])) # ask the os to execute our python script | formatting | passing the url of the script.py

    def format_list(list):
        #for i, item in enumerate(list):
        #for name, path in list_of_games.items():
        # Loop through the key-value pairs along with a counter
        for i, (name, path) in enumerate(list_of_games.items()):
            game_no = i
            print("[ {} ] {}".format(game_no,name))         # nicely formate the list using for loop
            #print("[{}] -> {}".format("Location",path))
    
    def user_input():
        choice = int(input("[{}]Select any option (0-{}) :".format("INPUT",str(length-1)))) # Choose any option from 1-3

        if choice == 0:
            print("Guess Alphabet's Position")
            pygame.excuteScript(choice)   # execute the script [python-game-alphabet-position.py]
        elif choice == 1:
            print("Multiplication Exercise")
            pygame.excuteScript(choice)   # execute the script [101_input_multiply.py]    
        elif choice == 2:
            print('Square Exercise')
            pygame.excuteScript(choice)   # execute the script [102_random_multiply.py]    
        elif choice == 3:
            print('Square Exercise')
            pygame.excuteScript(choice)   # execute the script [100_square.py]
        else :
            print("Invalid Options")

if __name__ ==  "__main__":
    pygame.launch()                   # Launch the PyGame
    pygame.displayMsg()               # Display Welcome - figlet text
    pygame.format_list(list_of_games) # formate the list -> [1] list-item | [2] list-item
    pygame.user_input()               # ask the user for input