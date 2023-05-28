'''
Password Generator
password_generator.py - Soren Reber
'''
from copy import copy
import tkinter as tk
import random
from tkinter import filedialog


def main():
    # Create the Tk root object.
    root = tk.Tk()
    bg_color ='powder blue'
    special_chars = create_specials_list()
    random_chars = create_characters_list()
    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Password Generator")
    frm_main.configure(bg= bg_color)
    frm_main.master.configure(bg= bg_color)
    frm_main.master.iconbitmap('icons_images/generator_icon.ico')
    frm_main.pack(padx= 30, pady=18, fill=tk.BOTH, expand=1)
    

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main, special_chars, random_chars, bg_color)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main, special_chars, random_chars, window_color):
    button_bg_color = 'light cyan'
    button_actbg_color = 'pale green'
    special_chars_input = tk.StringVar()
    special_chars_input.set('Y')

    #Label section
    lbl_special_chars = tk.Label(frm_main, text= 'Include special Characters?', bg= window_color)
    lbl_max_chars = tk.Label(frm_main, text= 'Desired Character Length (3-32):', bg= window_color)
    lbl_input_words = tk.Label(frm_main, text= 'Enter specific words to be used:', bg= window_color)
    lbl_random_chars_result = tk.Entry(frm_main, bg= window_color, width= 33)
    lbl_random_words_result = tk.Entry(frm_main, bg= window_color, width= 33)
    lbl_error = tk.Label(frm_main, bg= window_color)
    lbl_filename = tk.Label(frm_main, bg= window_color, width= 24)

    #Input Field Section
    ent_max_chars = tk.Entry(frm_main, width= 6)
    ent_input_words = tk.Entry(frm_main, width= 16)

    #Button Section
    rad_special_chars_yes = tk.Radiobutton(frm_main, text= 'Yes', value='Y', variable= special_chars_input, bg= window_color, activebackground= window_color)
    rad_special_chars_no = tk.Radiobutton(frm_main, text= 'No', value='N', variable= special_chars_input, bg= window_color, activebackground= window_color)
    btn_reset = tk.Button(frm_main, text='Reset', width= 20, bg= button_bg_color, activebackground= 'brown1')
    btn_random_chars = tk.Button(frm_main, text= 'Use Random Characters', bg= button_bg_color, activebackground= button_actbg_color)
    btn_random_words = tk.Button(frm_main, text= 'Use Random Words', bg= button_bg_color, activebackground= button_actbg_color)
    btn_open_file = tk.Button(frm_main, text= 'Choose a text file', bg= button_bg_color, activebackground= button_actbg_color)

    #Grid Section Inputs
    lbl_max_chars.grid(row= 0, column= 0, padx= 3, pady= 3)
    ent_max_chars.grid(row= 0, column= 1, padx= 3, pady= 3)
    lbl_special_chars.grid(row= 1, column= 0, padx= 3, pady= 3)
    rad_special_chars_yes.grid(row= 1, column= 1, padx= 3, pady= 3)
    rad_special_chars_no.grid(row= 2, column= 1, padx= 3, pady= 3)
    lbl_input_words.grid(row= 3, column= 0, padx= 3, pady= 3)
    ent_input_words.grid(row= 3, column=1, padx= 3, pady= 3)

    #Grid Secton Buttons
    btn_open_file.grid(row= 4, column= 0, padx= 3, pady= 3)
    btn_random_chars.grid(row= 5, column= 0, padx= 3, pady= 3)
    btn_random_words.grid(row= 5, column= 1, padx= 3, pady= 3)

    #Grid Secton Results
    lbl_filename.grid(row= 4, column= 1, columnspan= 1, padx= 3, pady= 3)
    lbl_random_chars_result.grid(row= 6, column= 0, padx= 3, pady= 3)
    lbl_random_words_result.grid(row= 6, column= 1, padx= 3, pady= 3)
    
    #Grid Section Error and Reset
    btn_reset.grid(row= 12, column= 0, columnspan= 3, padx= 3, pady= 12)
    lbl_error.grid(row= 13,column= 0, columnspan= 8, padx= 3, pady= 18)

    def open_file_dialog():
        """
        Opens a file dialog box allowing the user to choose their own text file to randomly choose words from.
        """
        global chosen_filename
        chosen_filename = filedialog.askopenfilename(initialdir= "./text_files", title= "Select a Text File", filetypes=(('Text Files',  '*.txt'), ('All Files', '*.*')))
        slash_index = chosen_filename.rindex('/')
        extension_index = chosen_filename.rindex('.')
        filename = chosen_filename[slash_index +1: extension_index]
        lbl_filename.config(text= filename)

    def check_specials():
        """
        Gets the users input as to whether special characters are 
        allowed to be in the password.
        Returns True or False
        """
        special_chars = special_chars_input.get()
        if special_chars == 'Y':
            return True
        else:
            return False

    def check_max(): 
        """
        Checks the users input for the desired character length. Ensures that no blank amount of characters or too many
        or too few characters are use.
        Returns the maximum allowed characters
        """      
        maximum = ent_max_chars.get()   
        
        try:
            maximum = int(maximum) 
            if maximum == '':
                lbl_error.config(text= 'Please enter a number for the maximum')
                ent_max_chars.focus()
            elif maximum >= 33 or maximum < 3:
                lbl_error.config(text= 'Please enter a number equal between 3 and 32.')
                ent_max_chars.focus()                
            else:
                return maximum
        except:
            lbl_error.config(text= 'Please enter a number for the maximum')
            ent_max_chars.delete(0, tk.END)
            ent_max_chars.focus()

    def get_user_word_input():
        """
        Gets the users input for words or phrase to be used in the password.
        Returns the users inputted words with the spaces removed.
        """       
        word_input = ent_input_words.get()
        altered_input = remove_spaces(word_input)
        return altered_input

    def generate_random_chars():
        """
        Generates random password using two lists consisting of an alphanumeric and special symbol lists.
        Checks the users input to use special symbols, then either combines the two lists or removes the 
        special symbols from the already combined list depending on the users input.
        Gets the users input if they wish to include a specific word or phrase and places that in the middle
        of the generated password. Characters in the random part of the password are capitlized on a random basis.
        """        
        use_specials = check_specials()
        all_characters = add_remove_specials(random_chars, use_specials, special_chars)
        random_num = 0
        user_input = get_user_word_input()
        max_chars = check_max()  
        try:   
            while len(user_input) < max_chars:
                lbl_error.config(text="")
                random_num = random.randrange(0, 5)
                add_char_1 = random.choice(all_characters)
                add_char_2 = random.choice(all_characters)
                if random_num == 2:
                    if add_char_1 in random_chars:
                        add_char_1 = add_char_1.upper() 
                if random_num == 3:
                    if add_char_2 in random_chars:
                        add_char_2 = add_char_2.upper() 
                user_input = add_char_1 + user_input
                if len(user_input) < max_chars:
                    user_input = user_input + add_char_2
            copy(user_input)
            lbl_random_chars_result.delete(0,tk.END)
            lbl_random_chars_result.insert(0, user_input)
        except TypeError:
            print('Check_max() has not returned a maximum')

    def generate_random_words():
        """
        Generates a random password using a text file that the user chooses. 
        Checks to make sure that the generated password does not go over
        the desired character limit
        """
        user_input = get_user_word_input()
        max_chars = check_max()
        user_placement = random.choice(['front', 'back'])
        add_word_list = []
        result = ''        
        remade_word = ''
    
        try:   
            random_words = read_file(chosen_filename)
            if chosen_filename == '':
                raise NameError        
            while (len(result) + len(user_input)) < max_chars:
                remade_word = ''
                add_word_list.clear()
                add_word = random.choice(random_words)
                if len(add_word) > (max_chars - (len(result) + len(user_input))):
                    while (len(result) + len(user_input)) < max_chars:
                        result += random.choice(random_chars)
                        if (len(result) + len(user_input)) == max_chars:
                            break
                if (len(result) + len(user_input)) == max_chars:
                    break
                random_num = random.randrange(0, len(add_word))
                for i in range(len(add_word)):                        
                    if i == random_num:
                        add_word_list.append(add_word[i].upper())
                    else:
                        add_word_list.append(add_word[i])
                for letter in add_word_list:
                    remade_word += letter
                result += remade_word
            if user_placement == 'front':
                result =  user_input + result
            else:
                result = result + user_input
            copy(result)
            lbl_error.config(text="")
            lbl_random_words_result.delete(0,tk.END)
            lbl_random_words_result.insert(0, result)
            
        except TypeError:
            print('Check_max() has not returned a maximum')
        except NameError:
            print('No filename was chosen.')
            btn_open_file.focus()
            lbl_error.config(text='Please choose a text file you wish to pull words from.')
             
    def reset():
        ent_max_chars.delete(0, tk.END)
        lbl_error.config(text= '')
        ent_input_words.delete(0, tk.END)
        special_chars_input.set('Y')
        ent_max_chars.focus()
        lbl_random_chars_result.config(text='')  
        lbl_random_words_result.config(text='') 
        global chosen_filename
        chosen_filename = ''
        lbl_filename.config(text= '')
        
    #Button commands and key releases
    btn_reset.config(command= reset)
    btn_random_chars.config(command= generate_random_chars)
    btn_random_words.config(command= generate_random_words)
    btn_open_file.config(command= open_file_dialog)

def remove_spaces(words_used):
    """
    Parameter: words_used. The input from the user in the form of a string.
    Removes spaces from the users input.
    Returns the users input without spaces.
    """
    words_used = words_used.replace(' ', '')
    return words_used 

def add_remove_specials(all_chars, is_true, special_chars):
    """
    Checks the users input to use special symbols, then either combines the two lists or removes the 
    special symbols from the already combined list.
    Returns either the combined list or the list with no special characters.
    """
    if is_true == True:
        for i in range(len(special_chars)):
                if special_chars[i] not in all_chars:
                    all_chars.append(special_chars[i])
        return all_chars
    else: 
        x = 0
        list_length = len(all_chars)
        while x < list_length:
            if all_chars[x] in special_chars:
                del(all_chars[x])
                x -= 1
            x += 1
            list_length = len(all_chars)
        return all_chars

def create_specials_list():
    """
    Makes a list of all allowed special characters to be used
    in the password.
    Returns the list.
    """
    specials = ['!', '?', '@', '$', '#', '*', '&', '%', '=', '+', '-', '_']
    return specials

def create_characters_list():
    """
    Makes a list of all allowed characters to be used in the password.
    Returns the list.
    """
    random_characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for i in range(0, 10):
        random_characters.append(str(i))
    return random_characters

def read_file(filename= 'sample.txt'):
    """
    Reads a text file, appends each word to a word list. 
    Omits any spaces, too short of words (i.e. less than 4 characters), or special characters.
    Returns the list of words.
    """
    word_list= []
    word = ''
    allowed_characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    try:
        with open(filename, "rt") as txt_file:        
            for line in txt_file:
                for i in range(len(line)):
                    if line[i].lower() in allowed_characters:
                        word += line[i].lower()
                    elif len(word) > 2:
                        if word not in word_list:
                            word_list.append(word)
                            word = ''
                        else:
                            word = ''
                    else:
                        word = ''
    except FileNotFoundError:
        print('File or directory could not be found.')
    return word_list 


if __name__ == '__main__':
    main()