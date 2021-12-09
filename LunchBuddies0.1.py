
"""
Created on Tue Oct 19 18:52:59 2021

@author: Lunch Buddies
https://pythonawesome.com/a-bot-created-with-python-that-interacts-with-groupme/amp/
https://www.geeksforgeeks.org/simple-chat-room-using-python/amp/
https://stackoverflow.com/questions/44663389/python-creating-username-and-password-program/44663415
https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options
https://www.thepythoncode.com/article/get-geolocation-in-python

"""
import socket
from threading import Thread
import random
from datetime import datetime
import time

#imports that are not being used: 
#from threading import Thread
#from colorama import Fore, init, Back
#from geopy.geocoders import Nominatim
#from pprint import pprint
#global variables


#Functions
def Main():
    Startmenu()
    MainMenu()



def Startmenu():

    selection = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if selection == "A" or selection =="a":
        register()
    elif selection == "B" or selection =="b":
        login()
    elif selection =="Q" or selection =="q":
        logout()
    else:
        print("You must only select either A or B")
        print("Please try again")
        Startmenu()

def logout():
    Main()
##Passwords, sign up/ login
def register():
    user = input("What would you like your username to be: ")
    password = input("type a password: ")
    pass
    
def login():
    print("you are logging in")
    input("type your username: ")
    input("type your password: ")
    pass
    
#the program is initiated, so to speak, here

    
def MainMenu():
    print("")
    print("Welcome to Lunch Buddies")
    
    mainMenuChoice = input("""What would you like to do now?
                           
                          HomeScreen [1]
                           
                          Groups in your area [2]
                          
                          Friends [3]
                          
                          Group chats [4]
                          
                          Settings [5]
                           
                          : """)
    if mainMenuChoice == "1":
        HomeScreen()
        b = input("type b if you would like to return to the main menu: ")
    elif mainMenuChoice == "2":
        GroupsinYourArea()
        b = input("type b if you would like to return to the main menu: ")
    elif mainMenuChoice == "3":
        friendsMainScreen()
        b = input("type b if you would like to return to the main menu: ")
    elif mainMenuChoice == "4":
        GroupChats()
        b = input("type b if you would like to return to the main menu: ")
    elif mainMenuChoice == "5":
        Settings()
        b = input("type b if you would like to return to the main menu: ")
    
    if b == "b":
        MainMenu()
    
def HomeScreen():
    print("*")
    print("this is the home screen")
    
    
def SidebarMenu():
    print("*")
    
def Settings():
    print("*")
    print("These are settings")
    
def LocationSettings():
    print("location settings")
def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

def friendsMainScreen():
    friendschoice = input("""Would you like to add friends or find friends?
                          Add Friends [1]
                          
                          Find Friends [2] 
                          
                          Go back [b]
                          """)
    if friendschoice == "1":
        AddingFriends()
    elif friendschoice == "2":
        FindingFriends()
    elif friendschoice == "b":
        MainMenu()
        
def AddingFriends():
    print("*")
    print("This is where you can add friends")
    
def FindingFriends():
    print("*")
    print("this is where you can find new friends")
    
def GroupChats():
    print("*")
    print("These are the group chats")
    GCinput = input("""
                    Would you like to see your group chats or find new ones?
                    
                    My group chats [1]
                    
                    Find new ones [2]
                    
                    Join GC now? [3]
                    
                    back to main menu [b]
                    
                    """)
    if GCinput == "1":
        GroupchatsOld()
    elif GCinput == "2":
        GroupchatsNew()
    elif GCinput == "3":
        print("you will iniate a server")
        GroupChatServerStart()
        print("You have created a server...")
        print("-----------------------------")
        
        print("You can now talk in that server: ")
    elif GCinput == "b":
        MainMenu()
def GroupchatsOld():
    print("These are your group chats")
    oldinput = input(""""What now?
                     
                     back to main menu [b]
                     
                     """"")
    if oldinput == "b":
        MainMenu()
def GroupchatsNew():
    print("these are group chats in your area that you can join")
    newinput = input(""""What now?
                     
                     back to main menu [b]
                     
                     """"")
    if newinput == "b":
        MainMenu()
def GroupsinYourArea():
    print("These are the groups in your area: ")
    

def GroupChatServerStart():
            
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5002 # port we want to use
    separator_token = "<SEP>" # we will use this to separate the client name & message

    # initialize list/set of all connected client's sockets
    client_sockets = set()
    # create a TCP socket
    s = socket.socket()
    # make the port as reusable port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind the socket to the address we specified
    s.bind((SERVER_HOST, SERVER_PORT))
    # listen for upcoming connections
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    
    def listen_for_client(cs):
        """
        This function keep listening for a message from `cs` socket
        Whenever a message is received, broadcast it to all other connected clients
        """
        while True:
            try:
                # keep listening for a message from `cs` socket
                msg = cs.recv(1024).decode()
            except Exception as e:
                # client no longer connected
                # remove it from the set
                print(f"[!] Error: {e}")
                client_sockets.remove(cs)
            else:
                # if we received a message, replace the <SEP> 
                # token with ": " for nice printing
                msg = msg.replace(separator_token, ": ")
                # iterate over all connected sockets
            for client_socket in client_sockets:
                # and send the message
                client_socket.send(msg.encode())
    while True:
        # we keep listening for new connections all the time
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")
        # add the new connected client to connected sockets
        client_sockets.add(client_socket)
        # start a new thread that listens for each client's messages
        t = Thread(target=listen_for_client, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()
        # close client sockets
    # close client sockets
    for cs in client_sockets:
        cs.close()
    # close server socket
    s.close()
#use: GroupChatServerStart() to initiate a server as host and from another console use the #function: ClientJoinGCCode()
## from How to Make a Chat Application in Python - Python Code (thepythoncode.com) ##



def ClientJoinGCCode():

    # init colors
    init()

    # set the available colors
    colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
        Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
        Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
    ]

    # choose a random color for the client
    client_color = random.choice(colors)

    # server's IP address
    # if the server is not on this machine, 
    # put the private (network) IP address (e.g 192.168.1.2)
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 5002 # server's port
    separator_token = "<SEP>" # we will use this to separate the client name & message

    # initialize TCP socket
    s = socket.socket()
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    # connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    # prompt the client for a name
    name = input("Enter your nickname: ")

    def listen_for_messages():
        while True:
            message = s.recv(1024).decode()
            print("\n" + message)

    # make a thread that listens for messages to this client & print them
    t = Thread(target=listen_for_messages)
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

    while True:
        # input message we want to send to the server
        to_send =  input("Say Something: ")
        # a way to exit the program
        if to_send.lower() == 'q':
            break
        # add the datetime, name & the color of the sender
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
        # finally, send the message
        s.send(to_send.encode())

    # close the socket
    s.close()
    
    print("*")  



#MainLineCode Start
Main()








"""#####pseudoCode Start
name2 = "Joe"
state2 = "California"
city2 = "Orange"
age2 = 21
interests2 = "books, tv"

location2 = state2 + ", " + city2
person2Characterized = [name2, location2, age2, interests2]
print('This is a potential match!')
print(person2Characterized)

name1 = input("what is your name? ")
state1 = input("What state you are in, not emotionally: ")
city1 = input("Please name what city you live in: ")
age1 = input("How young are you? XD: ")
interests1 = input(""Name anything you are interested in: Do this in a comma seperated list
                   For Example: dodgeball, videogames, books:
                        ")

location1 = state1 + ", " + city1
person1Characterized = [location1, age1, interests1]
print("This is you!")
print(">>>")
print(person1Characterized)
print("   ")
print("   ")
print("   ")

for i in interests1:
    if i in interests2:
        print("You've got a match!")
        
        print("This is your match: ")
        print(person2Characterized)
        answer1 = input("Would you like to match with" + name2 + " [y] or [n]: ")
        if answer1 == "y":
            print("congrats you will now be put into a group chat with this person")
        if answer1 == "n":
            print("Okay, no match for you then")
            
    else:
        print("sorry nobody matches your interests")
    break

#####pseudoCode end

"""

