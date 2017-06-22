from details import spy, friends,ChatMessage,Spy

from steganography.steganography import Steganography

from datetime import datetime

status_message = ['on work','updating....','on mood to learn']

print 'Hello let\s get started'

existing = raw_input(" Do You Want continue as " + spy.salutation + " " + spy.name + "  (Y/N)?  ").upper()

def add_status(current_status_message) :
    updated_status_message = None

    if current_status_message != None :
        print 'your current status message is %s \n' % (current_status_message)
    else :
        print 'you don\'t have any status message..\n'

        default = raw_input("do you want to select from the older status message(y/n)? Or want to write new?(n)")

        if default.upper() == "N" :
            new_status_message = raw_input("what stauts do you want to set?")

            if len(new_status_message) > 0:
                status_message.append(new_status_message)
                updated_status_message = new_status_message
                if updated_status_message.isspace():
                    print 'you don\'t have any status..'
                else:
                    updated_status_message = updated_status_message.strip()
                    print updated_status_message

        elif default.upper() == 'Y' :
            item_position = 1


            for message in status_message :
                print '%d.  %s' % (item_position, message)
                item_position = item_position + 1
            message_selection = int(raw_input("\n choose from the above message"))


            if len(status_message) >= message_selection :
                updated_status_message = status_message[message_selection - 1]
            else:
                print 'the option you choose not available'
            if updated_status_message:
                print 'Your updated status message is: %s' % (updated_status_message)

            else:
                updated_status_message.startswith(" ")
                print 'You current don\'t have a status update'




    return updated_status_message

def add_friend() :
    present_friend = spy('','',0,0.0)
    present_friend.name = raw_input("please add your friend's name")
    present_friend.salutation = raw_input("are they mr. or miss.?")

    present_friend.name = present_friend.salutation + " " + present_friend.name

    present_friend.age = raw_input("age?")
    present_friend.age = int(present_friend.age)

    present_friend.rating = raw_input("rating?")
    present_friend.rating = float(present_friend.rating)

    if len(present_friend.name) > 0 and present_friend.age >= 20 and present_friend.rating >= 2.0:
        friends.append(present_friend)
        print 'Friend Added!'
    else:
        print 'sorry! unable to add..invalid entry!'

    return len(friends)

def select_friend():
    item_number = 0

    for friend in friends:
        print '%d  %s with age %d with rating %.2f is online' % (item_number + 1, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of image?")
    output_path = "output.jpg "
    text = raw_input("what do you want to say? ")
    Steganography.encode(original_image , output_path, text)


    new_chat = ChatMessage(text,True)



    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"

def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)


    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

def read_chat_history():

    read_for = select_friend()

    print '\n5'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def start_chat(spy) :
    current_status_message = None
    spy.name = spy.salutation + " " + spy.name

    if spy.age >=20 and spy.age <=50 :

        print "Authentication Complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of spy:" + str(
            spy.rating) \
              + " Proud to Have You onboard.."

        show_menu = True
        while show_menu :
            menu_choices = "What do you want to do?\n 1. Add a Status\n 2. Add a Friend\n 3. Send a Secret Message\n 4. Read a Secret Message\n" \
                           " 5. Read chat history\n 6. show status \n 7. show friends list\n 8. exit apllication\n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0 :
                menu_choice = int(menu_choice)

                if menu_choice == 1 :
                    print 'you choose to Status Update'
                    current_status_message = add_status(current_status_message)

                elif menu_choice == 2 :
                    print 'you can add a friend now!'
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3 :
                    print 'you can send a secret message here!'
                    send_message()
                elif menu_choice == 4 :
                    print 'you can read a secret message here!'
                    read_message()
                elif menu_choice == 5 :
                    print 'Your chat history'
                    read_chat_history()
                elif menu_choice == 6:
                    print 'your staus message here!\n'
                    if current_status_message.startswith("  "):
                        print 'you don\'t have status.. '
                    elif current_status_message.isspace():
                        print'you don\'t have any status..'
                    else:
                        current_status_message = add_status(current_status_message)
                elif menu_choice == 7 :
                    print 'your friends are..\n'
                    for i in friends:
                       print i.name

                elif menu_choice == 8 :
                    exit()
                else :
                    show_menu = False
    else:
        print 'sorry You are not eligible to be a spy'




if existing == "Y":
     start_chat(spy)

else:

    spy = Spy('','',0,0.0)

    spy.name = raw_input("welcome to spy chat,tou need to tell your name first:")
    if len (spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = int(raw_input("What is your Age?"))
        spy.age = int(spy.age)

        spy.rating = float(raw_input("what is your rating:"))
        if spy.rating >= 4.5:
            print "wow! Great Ace."
        elif spy.rating >= 4.0 and spy.rating < 4.5 :
            print "you are good."
        elif spy.rating >= 3.0 and spy.rating < 4.0 :
            print "you can do better."
        else:
            print 'We can always need to help in Office..'

        spy_rating = float(spy.rating)

        spy_is_online = True

        start_chat(spy)
    else :
        print "A Spy needs a valid Name!"





