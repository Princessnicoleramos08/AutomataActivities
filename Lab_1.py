#NUMBER1
def automaton(string):
    state = '1'
    transitions = {
        '1': {'1': '2'},          
        '2': {'0': '3'},         
        '3': {'0': 'X'},            
        'X': {'0': '4', '1': '5'}, 
        '4': {'0': '4', '1': '5'},  
        '5': {'0': '4', '1': '5'}   
    }

    accepting_states = {'4'}  

    for char in string:
        if char in transitions.get(state, {}):
            state = transitions[state][char]
        else:
            return False
    return state in accepting_states


print(" Automaton Tester")
print("Type a string using '1' and '0' to test it.\n")

while True:
    user_input = input("Enter a binary string: ")
    result = " Accepted" if automaton(user_input) else " Rejected"
    print(f"'{user_input}' → {result}\n")


#IT ONLY ACCEPT
#"1000" 
# "100110"
# "100000" 

#ONLY REJECT
# "110" 
# "100" 
# "1001"




#NUMBER 2
# ACCEPTED_STRINGS = {"aa", "ab", "abab"}


# def check_dfa(string: str) -> str:
#     """
#     Checks if the given string is accepted by the DFA.
#     Only accepts: "aa", "ab", "abab".
#     """
#     return "ACCEPTED " if string in ACCEPTED_STRINGS else "REJECTED "

# def main():
#     print("DFA Checker")
#     print("This DFA accepts only: 'aa', 'ab', 'abab'")
#     print("-" * 40)

#     while True:
#         user_input = input("Enter a string of a's and b's: ").lower()
#         print(check_dfa(user_input))
#         print("-" * 40)

# if __name__ == "__main__":
#     main()

