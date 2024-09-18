print("Please enter the following: \n")

adjective = input("adjective: ")
animal = input("animal: ")
verb_one = input("verb (present tense): ")
exclamation = input("exclamation: ").upper()
verb_two = input("verb (present tense): ")
verb_three = input("verb (present tense): ")  

ready = input("Are you ready for your story? 'Y' or 'N': \n").lower()
# added if statement
if ready == "y":
  print("\n" * 50)   
  # added ASCII art   
  print(r"""
  '.                    |       ___________________             ____________
    '.                  |      |  _______________  |           |.----------.|
 .    '.                |      | |               | |           ||     |>   ||
 |'.    '.              |      | |   ___   ___   | |           || O  /|    ||
 |. '.    '.____________|      | |  |   | |   |  | |           ||   /_(    ||
 |||.|     |            |      | |  |   | |   |  | |           || .___|__  ||
 |||||     |            |      | |  |   | |   |  | |           ||~~\____|~~||
 |||||     |            |      | |  |   | |   |  | |           || ~  ~    ~||
 |||||     |            |      | |  |   | |   |  | |           |:__________:|
 |||||     |        *   |      | |  |   | |   |  | |           '------------'
 |||||     |    *..'    |      | |  '---___---'__| |
 |  '|     |     _:_    |      | |    |_____| |__= |
 |. ()     |    (   )   |      | |   ___   ___ ()| |
 |||||     |     ) (    |      | |  |   | |   |  | |
 |||||     | ===========|      | |  |   | |   |  | |
 |||||     |   | |    | |      | |  |   | |   |  | |
 |||||     |   | |    | |      | |  |   | |   |  | |
 |||||    _|___|_|____|_|      | |  |   | |   |  | |
 |||:|--"" |___|_|____|_|      | |  '---' '---'  | |
"|  _|..--"'   '      ' |______| |               | |_________________________
 -'"'                   |______|_|_______________|_|_________________________""")

  print("\nThis is your story: \n")

  print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb_one} down the hallway. "{exclamation}" I yelled. But all I could think to do was to {verb_two} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_three} right in front of my family.\n')
if ready == 'n':
  print("That's too bad, goodbye!")

# added continuation to story
keep_going = input("Would you like to continue? 'Y' or 'N' \n")

if keep_going == "y":
  print("\nPlease enter the following: \n")   
  
  # created a check noun function that returns 'an' or 'a' depending on input
  def check_noun(noun):
    first_char = noun[0]
    vowels = "aeiouAEIOU"
    if first_char in vowels:
      return "an"
    else:
      return "a"
    
  noun = input("noun: ")
  verb_four = input("verb (present tense): ")

  print("\nWe will now continue with your story: \n")

  # story continues
  print(f"I then ran to the kitchen to grab {check_noun(noun)} {noun}. After I grabbed the {noun}, I went back to the hallway to {verb_four} the {adjective} {animal}.\n")

  print("The End.")