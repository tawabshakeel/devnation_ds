def remove_duplication(initial_list): # Function made
    final_list = list(dict.fromkeys(initial_list)) # We can use dict.fromKeys function it converts list into dictionary.
    return final_list # returned the final list