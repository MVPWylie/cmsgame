


def start():
    answer = input("Care for a game? (yes/no) [Input in this game is sensitive. No capitals.] ")

    if answer == "yes":

        answer = input("You wake up in a Covington Middle School bathroom. Would you like to leave or stay? (leave/stay) ")
        if answer == "leave":
            answer = input("Would you like to go to the gym or the cafeteria? (gym/cafeteria) ")
            if answer == "gym":
                print("You enter the gym. You see some basketball players warming up. One of them is Maya. She is cool. ")
                answer = input('You can talk to her or watch them warm up. (talk/watch) ')
                if answer == 'watch':
                    print('Maya says "Whatcha lookin at creep? Mind your own business!" She throws a basketball at your head. ')
                    begin = input("You die. Press Enter to restart. ")
                    begin = start()
                elif answer == "talk":
                    print("You say hi to Maya. She says that she needs your help. You ask with what and she tells you how ")
                    answer = input("she needs a hashbrown or two to get her energy up. (help/ignore) ")
                    if answer == "ignore":
                        print(""""Oh so you don't wanna help? That's fine. Bye." You walk out of the gym and coach Turner """)
                        begin = input("smacks you and you die. Press Enter to restart. ")
                        begin = start()
                    elif answer == "help":
                        print(""""Thank you so much. You wont regret this." Said Maya. """)
                        answer = input("Do you want to take a bike or a car (bike/car) ")
                        if answer == "bike":
                            answer = input("You get in the bike and can go to (Burger King/McDonalds/Chick-fil-A/Jack in the Box) .")
                            if answer == "Burger King":
                                print("You go to Burger King and get 3 hashbrowns. When you get back to the school Maya says ")
                                begin = input('"What is this garbage? You are gonna die for this!" You died. Press Enter to restart. ')
                                begin = start()

                            elif answer == "McDonalds":
                                print('"OH MY GOD! Thank you! I needed this." Maya leans over and kisses you on the cheek. ')
                                begin = input("(Ending 1) Press Enter to restart.")
                                begin = start()

                            elif answer == "Chick-fil-A":
                                print("You go to Chick-fil-A and get 3 hashbrowns. When you get back to the school Maya says ")
                                begin = input('"What is this garbage? You are gonna die for this!" You died. Press Enter to restart. ')
                                begin = start()

                            elif answer == "Jack in the Box":
                                print("You go to Chick-fil-A and get 3 hashbrowns. When you get back to the school Maya says ")
                                begin = input('"What is this garbage? You are gonna die for this!" You died. Press Enter to restart. ')
                                begin = start()

                            else:
                                begin = input("Invalid Response. Press Enter to restart. ")
                                begin = start()

                        elif answer == "car":
                            begin = input("You go hop into the car but on the ride it explodes. Press Enter to restart. ")
                            begin = start()
                        else:
                            begin = input("Invalid response. Press Enter to restart. ")
                            begin = start()
                else:
                    begin = input("Invalid response. Press Enter to restart. ")
                    begin = start()
            elif answer == "cafeteria":
                print("You walk into the cafeteria. You see an ominous figure sitting at a lunch table eating ")
                answer = input("nicely made pankcakes. You may talk or go get in the lunch line. (talk/line) ")
                if answer == "talk":
                    print("You say hello to the figure. They dont say anything back. After a few seconds they take off a ")
                    print("hat or two and you find out that it is a short little girl named Taylor. She asks who you are ")
                    name = input("and you say: ")
                    print("Well there " + name + ", you should go down to the band hall. If not then maybe Ms. Ludwig's room. ")
                    answer = input("(ludwigs/band) " )
                    if answer == "ludwigs":
                        print("You go to Ms. Ludwig's room and find Cleo. She says that if you are looking for money ")
                        print("you can find it in the teacher's purse. If you want to speak with Joel he is in science.")
                        answer = input("(money/joel) " )
                        if answer == "money":
                            print('Ms. Ludwig walks in while you are stealing her money. She says "YOU SON OF A B-"(You died) ')
                            begin = input("Press Enter to restart. ")
                            begin = start()
                        elif answer == "joel":
                            print("You walk down to science class. You see Joel. He says nothing and hands you a map.")
                            answer = input("You wonder where Ms. Rothermell is. It probobly doesn't matter. (rothermell/map) ")
                            if answer == "map":
                                print("You follow the map and realize it goes outside. Out there you see a gravestone with a ")
                                print('trumpet on it. You read the stone and see "Here lies Javag". You think it is strange but ')
                                print('but then you hear a voice behind you say "Oh I just miss her so much. Why did she have to go?"')
                                print('You turn around and realize that it is a girl named Bree. You see her kissing the ')
                                print('grave and sobbing uncontrollably. You can say you are sorry for her loss or you can')
                                answer = input('leave and say nothing. (sorry/nothing) ')
                                if answer == "sorry":
                                    print('"Thank you so much I really appreciate it. You are a true friend." She says with a tear ')
                                    print("in her eye. She invites you to an official funeral where everyone is going to be at. ")
                                    begin = input("(Ending 2)Press Enter to restart. ")
                                    begin = start()

                                elif answer == "nothing":
                                    print("You say nothing. A few minutes after you leave there is a blinding light in front ")
                                    print('of you. The light dims and you see the one and only Javag appear. She says "Be nicer ')
                                    print('to Bree! My death has been hard enough on her. I am going to destroy you and everyone ')
                                    print('you ever loved.". You then just see darkness. You wait and wait, but nothing happens.')
                                    begin = input("Press Enter to restart. ")
                                    begin = start()


                                else:
                                    begin = input("Press Enter to restart. ")
                                    begin = start()

                            elif answer == "rothermell":
                                print("You look around for Ms. Rothermell but you don't see her. You look under her desk ")
                                print("and see her hiding. She says not to tell anyone and since you are a kind person you don't. ")
                                print('You walk outside the room with the map but you are greated my two tall men in all black')
                                print('suits. They say "You have seen too much. You will be eliminated.". They inject you with ')
                                print('a syringe as you are losing consiousness you hear them say "Target neutralized." (Ending 3) ')
                                begin = input('Press Enter to restart.')
                                begin = start()

                            else:
                                begin = input("Invalid response. Press Enter to restart. ")
                                begin = start()

                        else:
                            begin = input("Invalid response. Press Enter to restart. ")
                            begin = start()
                    elif answer == "band":
                        print("You walk into the band hall and see Pya, Harrison, Georgia, and Dash. You ask them if they" )
                        print('know where Maya and Bree are. "Maya is training for basketball and I think Bree is at a ')
                        print('funeral or something." said Pya. Mason walks into the room and plays a loud THWAMP out of ')
                        print('trumpet. He is wearing a fine trench coat as he asks you if you have seen the inside of the ')
                        answer = input('percussion closet. You say (yes/no)')
                        if answer == "yes":
                            print("You go into the percussion closet and start smooching Mason. It is pretty easy since ")
                            begin = input("he is so hot.(Ending 4) Press Enter to restart. ")
                            begin = start()

                        elif answer == "no":
                            print("Mason walks into the percussion closet. While he is in there Harrison pins you against ")
                            print("a wall and starts kissing you. He isn't hot at all but you are so caught up in the moment")
                            input("that it doesn't matter.(Ending 5) Press Enter to restart. ")

                    else:
                        begin = input("Invalid response. Press Enter to restart. ")
                        begin = start()

                elif answer == "line":
                    print("There is no one in the line so you were first to get the pancakes made fresh by Kai. You can ")
                    answer = input("take one or two pancakes. (1/2) ")
                    begin = input("Uh oh, he poisoned the pancakes. Press Enter to restart. ")
                    begin = start()
                else:
                    begin = input("Uh oh, he poisoned the pancakes. Press Enter to restart. ")
                    begin = start()
            else:
                begin = input("Invalid response. Press Enter to restart.")
                begin = start()

        elif answer == "stay":
            print("You stay in the bathroom but you get bored quickly. At some point you open a stall and there is a large ")
            begin = input("hole in the wall. There is also a toilet. (flush/hole) ")
            begin = start()
            if answer == "flush":
                print("You go over to the toilet and flush it a few times. You wait a few seconds and then the toilet ")
                print("stall lowers like an elevator. You are now in a basement and see an old tv and Jonah sitting in front ")
                print("""of it. The tv is playing an episode of Violin101, Jonah's favorite. He says "I have been watching this """)
                print("""for 7 months. Can you help me out?". You cannot. You are trapped. I hope you like the show too. """)
                begin = input("""(Ending 6) Press Enter to restart. """)
                begin = start()

            elif answer == "hole":
                print("You crouch into the hole and after crawling through a long tunnel you find a pile of gold coins. You ")
                print("then hear an incredible roar. Then there is some kind of bird shaped animal that soares through the sky. ")
                print("The small beast lands and you see that is a small dragon looking animal. It lunges at you and severely ")
                print("wounds you. A hero named Jonah jumps out of absolutely no where. He slays the beast. This kind man ")
                print("invites you into his house and cooks the animal. When trying to leave you realise that the tunnel collapsed. ")
                begin = input("Now the only question is who roared, Jonah or the dragon?(Ending 7) Press Enter to restart. ")
                begin = start()

            else:
                begin = input("Invalid Response. Press Enter to restart.")


        else:
            begin = input("Invalid response. Press Enter to restart.")
            begin = start()

    else:
        input("Maybe next time. Press Enter to quit. ")

start()
