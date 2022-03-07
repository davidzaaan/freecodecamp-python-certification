import re

# Project 1
''' Arithmetic operator solution freeCodeCamp '''

def my_func(numbers, *display):
    terms = {}
    if len(numbers) > 5:
        return 'Error: Too many problems.'

    ##### Numbers parsing #####
    for op in numbers:
        # Addition terms parsing...
        if '+' in op:
            sum_terms = re.split("[+]|[-]", op) # Splitting the two operands by their operator
            if len(sum_terms[0].strip()) > 4 or len(sum_terms[1].strip()) > 4:
                return ("Error: Numbers cannot be more than four digits.")
            try:
                # Optimize this with sum and map
                terms[op] = int(sum_terms[0]) + int(sum_terms[1])
            except:
                return ('Error: Numbers must only contain digits.')
        # Substraction terms parsing...
        elif '-' in op:
            subs_terms = re.split("[+]|[-]", op) # Splitting the two operands by their operator
            if len(subs_terms[0].strip()) > 4 or len(subs_terms[1].strip()) > 4:
                return ("Error: Numbers cannot be more than four digits.")
            try:
                # Optimize this with sum and map
                terms[op] = int(subs_terms[0]) - int(subs_terms[1])
            except:
                return ('Error: Numbers must only contain digits.')
        else:
            return("Error: Operator must be '+' or '-'.")
    ##### End of number parsing #####

    ##### Numbers formatting for display #####
    my_str = ""

    # First operands line
    for term in numbers:
        string = term.split(" ")
        res = max(string, key = len)
        my_str += f"{' ' * ( (len(res) + 2) - len(string[0]) )}{string[0]}{' ' * 4}"
        

    my_str = my_str.rstrip() # Cleaning extra spaces or new lines
    my_str += '\n'

    # Second operands line
    for term in numbers:
        string = term.split(" ")
        res = max(string, key = len)
        my_str += f"{string[1]}{' ' * ( (len(res) + 2 - len(string[1])) - len(string[2]) )}{string[2]}{' ' * 4}"


    my_str = my_str.rstrip() # Cleaning extra spaces or new lines
    my_str += '\n'

    # Hyphen bottom division for the result's displaying
    for term in numbers:
        string = term.split(" ")
        res = max(string, key = len)
        my_str += f"{'-' * (len(res) + 2)}{' ' * 4}"
        
    # Display the respective results
    if True in display:
        my_str = my_str.rstrip() # Cleaning extra spaces or new lines
        my_str += '\n'
        for term in numbers:
            string = term.split(" ")
            res = max(string, key = len)
            my_str += f"{' ' * ( (len(res) + 2) - len(str(terms[term])) )}{str(terms[term])}{' ' * 4}"
            
    ##### End of numbers formatting for display #####
    my_str = my_str.rstrip() # Cleaning extra spaces or new lines
    return my_str



print(my_func(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))















# def parse_numbers(numarray):
#     terms = {}
#     for op in numarray:
#         if '+' in op:
#             print('addition')
#             sum_terms = re.split("[+]|[-]", op)
#             try:
#                 if len(sum_terms[0].strip()) > 4 or len(sum_terms[1].strip()) > 4:
#                     return
#                 terms[op] = int(sum_terms[0]) + int(sum_terms[1])
#             except:
#                 print('Error: Numbers must only contain digits.')
#         elif '-' in op:
#             print('substraction')
#             subs_terms = re.split("[+]|[-]", op)
#             try:
#                 if len(subs_terms[0].strip()) > 4 or len(subs_terms[1].strip()) > 4:
#                     return
#                 terms[op] = int(subs_terms[0]) - int(subs_terms[1])
#             except:
#                 print('Error: Numbers must only contain digits.')
#         else:
#             print("Error: Operator must be '+' or '-'.")

#     return terms
    
# def printer(numarray, terms):
#     result = '13'
#     arr = ["32 + 8", "1232 - 301", "9999 + 9999", "523 - 49"]
#     for term in arr:
#         string = term.split(" ")
#         res = max(string, key = len)
#         print(f"{'#' * ((len(res) + 2) - len(string[0]))}{string[0]}", end=" " * 4)

#     print()
#     for term in arr:
#         string = term.split(" ")
#         res = max(string, key = len)
#         print(f"{string[1]}{'#' * ((len(res) + 2 - len(string[1])) - len(string[2]))}{string[2]}", end=" " * 4)

#     print()
#     for term in arr:
#         string = term.split(" ")
#         res = max(string, key = len)
#         print("-" * (len(res) + 2), end=" " * 4)

#     print()
#     if True:
#         for term in arr:
#             string = term.split(" ")
#             res = max(string, key = len)
#             print(f"{'#' * ((len(res) + 2) - len(terms[term]))}{terms[term]}", end=" " * 4)

            

