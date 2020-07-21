import webbrowser
from googlesearch import *
import random
import time
import pyttsx3
import requests
from pprint import pprint
import smtplib
from selenium import webdriver
import speech_recognition as sr
import mysql.connector as mycon

mydb=mycon.connect(host="localhost", passwd="", database="JUNE", user="root")
mycursor= mydb.cursor()
mainl = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

memory = []
Schedule = []
greetings = ['hallo','high','hay','hello','hola','hey','yo','yolo','hi','hie','namaste','bonjour','hello JUNE','hola JUNE','hey JUNE','yo JUNE','yolo JUNE','hi JUNE','hie JUNE','namaste JUNE','bonjour JUNE']
greetings_responses = ['hello','hola','hey','yo','yolo','hi','hie','namaste','bonjour']
initial_questions = ['how are you','how r u','how are you doing','howdy','how have you been','how you been','hows life','how is life','how are you JUNE','how you doing','how are you doing JUNE','howdy JUNE','how have you been JUNE','hows life JUNE','how is life JUNE']
initial_responses = ['i am fine','i am doing well','never been better','couldnt be better']
call_questions = ['do i have recent missed calls','recent missed calls','anything pending','do i have recent missed calls JUNE','recent missed calls JUNE','anything pending JUNE']
call_responses = ['you have two missed calls','you are all clear','nope nothing pending','you have one missded call','you dont have any missed calls']
message_questions = ['do I have recent messages','recent unread messages','do i have recent messages JUNE','recent unread messages JUNE','unread messages','unread messages JUNE']
message_responses = ['you are all clear','nope no messages','you have 1 unread message','you have two unread messages']
mail_questions = ['do I have pending mails','unread mails','do i have pending mails JUNE','unread mails JUNE']
mail_responses = ['you are all clear','nope no mails','you have 1 unread mail','you have two unread mails']
call_action_questions = ['JUNE call','call','JUNE can you call','call back','JUNE give a call back','can you call back']
call_action_responses = ['connecting call please wait','i am sorry call failed','sorry you do not have any network','call connected']
message_action_questions = ['JUNE can you message','can you message','message']
message_action_responses = ['sending message','i am sorry message could not be sent','you dont have balance','i am sorry you dont have network']
mail_action_questions = ['JUNE can u respond to the mail','reply to the mail','send a mail','JUNE send a mail','mail','email']
beauty_questions = ['how do I look','look','how do i lock','how am i looking','do i look fine','how does this look','looking good','how do i look JUNE','how am i looking JUNE','do i look fine JUNE','how does this look JUNE','looking good JUNE','JUNE how do i look','JUNE how am i looking','JUNE do i look fine','JUNE how does this look','JUNE looking good']
beauty_responses = ['on a scale of 1 - 10 i would give you a 50','the whole world would agree with me that you look simply cute','B-E-A-U-T-I-F-U-L','you would make the opposite sex go crazy','you are on fire','well if i had to guess i would say you look marvelous','i would say you look fairly attractive','a correlation of the available spatio-temporal,sematic,and conversational evidence supports the provisional conclusion that you are totally hot. plus or minus one standard cuteness deviation']
math_questions = ['JUNE add','JUNE multiply','JUNE subtract','JUNE divide','divide','multiply','add','subtract']
action_questions = ['open WhatsApp','open music','open videos','open application','JUNE open whatsapp','JUNE open music','JUNE open videos','JUNE open application']
action_responses = ['openeing please wait','i am sorry could not process your request','processing request','please wait','opening']
comebacks_questions = ['Siri','cortana','okay Google','hey galaxy','hey siri','hey cortana','hey google','galaxy','do you know siri','do you know cortana','do you know okay google','do you know hey galaxy']
comebacks_responses = ['i am sorry who','very funny, not Ha-Ha funny but funny']
inquiry = ['what all can you do','what can you do','what is your use','what can u do','how can you help me','who are you']
inquiry_responses = ['Hi, I am JUNE, Maniyas personal virtual assistant. i am here to help you make your work easier. I can send mails on your behalf. i solve mathematical operations. i can show you latest movies,latest music, nearby places for food and entertainment. news and weather of the day, google search for you']
memory_respond = ['show me our chats','our chat history','show me the chat library','our chats','history']
weather_questions = ['how is the weather today','whether','weather','JUNE show me the weather','JUNE what is todays weather','what is todays weather','todays weather','show me weather','how is it outside today','good day to go out JUNE']
weather_responses = ['I am on it']
movies_questions = ['which are the latest movies','book movie tickets',"movies",'i want to watch a movie','latest movies','watch a movie','i want to book movie tickets']
movies_responses = ['all you had to do is ask']
music_questions = ['latest music','what are the trending music','what are the latest music','any new albums','latest albums','latest songs','waht are the latest songs']
music_responses = ['searching music you can sway on']
news_questions = ['todays headlines','what are todays headlines','headlines','news','news of the day','news','JUNE what is the news of today']
news_responses = ['There you go']
maps_questions = ['what is my current location','location','current location','nearby places','maps','my location','where am i','where am i JUNE']
maps_responses = ['i am on it']
schedule_questions = ['remind me to','make my schedule','schedule','prepare my schedule','some important things to do','to do list','make my to do list','note down reminders']
schedule_responses = ['right away']
schedule_display = ['i want to see my schedule','show me my schedule','display my schedule','show me my reminders','my reminders','my to do list','show me my to do list']
schedule_display_responses = ['showing your schedule','showing your to do list','showing your reminders']
food_questions = ['near by restaurants','food restaurants','places to eat','i want to go out for food','food joints','i want to have food outside','nearby restaurants']
food_responses = ['Searching for near by restaurants']
entertainment_questions = ['I am getting bored','i am getting bored','i am so bored','i want to go out today','near by entertainment places','i wan to do something entertaining']
entertainment_responses = ['i understand, here is something for you']
nickname_demand = ['give me a nickname','from now on you will call me','my nickname','nickname']
compliments = ['you are awesome JUNE','you rock','you are the best','i love you JUNE','no body can beat you','you are awesome','JUNE you are awesome','you are the best JUNE','JUNE you are the best']
compliments_responses = ['its kind of you to say','well i am pleased you love me','all thanks to my maker']
depart = ['goodbye','bye bye','c u latter','c u later','bye','thanks JUNE','thanks','see you later','thanks bye','merci','danke','shukriya','dhanyavad']
jokes_questions = ['JUNE tell me a joke','tell me a joke','i am bored tell me a joke','jokes','jokes']
jokes_responses = ['what do you call a bommerang that doesnt return. A stick','what did one ocean say to the other. nothing they just waved','i wanted to buy a new boomerang. also tell me how to throw away the old one.']
google_questions = ['JUNE search','JUNE search on google','do a Google search for me','google search','search for','search on google','JUNE google search']
Walkman_questions = ['play my music','play me music','play me a music','JUNE my music','play music','my music','music']
print(time.strftime("%Y-%m-%d %H:%M"))
print("")
print( "")
U_INPUT_AUDIO = input('Would you like to use microphone or type input. Enter the option of mic for audio aided JUNE >>>:-  ')
if U_INPUT_AUDIO in ['audio','AUDIO',"mic",'MIC','MICROPHONE','Mic','Microphone','microphone','Audio']:
    while True:
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source)   

        try:
            user_input=r.recognize_google(audio)
        except sr.UnknownValueError:
            
            user_input = ""

        except sr.RequestError as e:
            
            user_input = ""
            print(">>>ME :",user_input)
        
        if user_input in greetings:
            random_response = random.choice(greetings_responses)
            time.sleep(0.5)
            print(random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))
        elif user_input in initial_questions:
            random_response = random.choice(initial_responses)
            time.sleep(0.5)
            print(random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in call_questions:
            random_response = random.choice(call_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in message_questions:
            random_response = random.choice(message_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in mail_action_questions:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            engine.say("enter your email ID")
            engine.runAndWait()
            Email = input("enter your email ID >>> : ")
            engine.say("enter your password")
            engine.runAndWait()
            Pass = input("enter your password >>> : ")
            server.login(Email, Pass)
            engine.say("enter receivers Email ID")
            engine.runAndWait()
            Rec_Email = input("enter receivers Email ID >>> : ")
            engine.say("Enter the message you want to send")
            engine.runAndWait()
            msg = input("Enter the message you want to send >>> : ")
            server.sendmail(Email, Rec_Email, msg)
            server.quit()
            print("mail sent")
            engine.say("mail sent")
            engine.runAndWait()
        elif user_input in call_action_questions:
            random_response = random.choice(call_action_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in message_action_questions:
            random_response = random.choice(message_action_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in mail_questions:
            random_response = random.choice(mail_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in beauty_questions:
            random_response = random.choice(beauty_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in action_questions:
            random_response = random.choice(action_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in math_questions:
            operand1 = int(input('please enter the numbers:- '))
            operand2 = int(input('please enter the numbers:- '))

            if user_input == 'add' or user_input == 'JUNE add':
                Sum = operand1 + operand2
                print (Sum)
                engine.say(Sum)
                engine.runAndWait()
            elif user_input == 'multiply' or user_input == 'JUNE multiply':
                Mul = operand1 * operand2
                print (Mul)
                engine.say(Mul)
                engine.runAndWait()
            elif user_input == 'divide' or user_input == 'JUNE divide':
                div = operand1 / operand2
                print (div)
                engine.say(div)
                engine.runAndWait()
            elif user_input == 'subtract' or user_input == 'JUNE subtract':
                sub = operand1 - operand2
                print (sub)
                engine.say(sub)
                engine.runAndWait()
            else:
                print ('sorry i didnt quite understand')
                engine.say('sorry i didnt quite understand')
                engine.runAndWait()
                print ('this may not be in my library')
                engine.say('this may not be in my library')
                engine.runAndWait()
        elif user_input in inquiry:
            random_response = random.choice(inquiry_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in comebacks_questions:
            random_response = random.choice(comebacks_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in memory_respond:
            print (memory)

        elif user_input in depart:
            time.sleep(0.5)
            print ('it was nice chatting with you, we shall catch up later')
            engine.say('it was nice chatting with you, we shall catch up later')
            engine.runAndWait()
            mycursor.execute("select * from JUNE.PY_LICENSE")
            for a in mycursor:
                print(a)
            mycursor.execute("""select 'JUNE is subject to copyrights under #89-3b Software Ownership, Protection against Plagerism Guidelines PVT. LTD.'""")
            for b in mycursor:
                print(b)
            break
        elif user_input in weather_questions:
            random_response = random.choice(weather_responses)
            print( random_response)
            engine.say(random_response)
            engine.runAndWait()
            def weather_data(query):
                res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
                return res.json();
            def print_weather(result,city):
                t="{}'s temperature: {}°C ".format(city,result['main']['temp'])
                s="Wind speed: {} m/s".format(result['wind']['speed'])
                q="Description: {}".format(result['weather'][0]['description'])
                p="Weather: {}".format(result['weather'][0]['main'])
                l=t+"\n"+s+"\n"+q+"\n"+p
                print(l)
    
            def main():
                city=input('Enter the city:')
                print()
                try:
                        query='q='+city;
                        w_data=weather_data(query)
                        print_weather(w_data, city)
                        print()
                except:
                        print('City name not found...')
                        return "city not found"

            if __name__=='__main__':
                main()
                
        
            memory.append((user_input, random_response))
        elif user_input in movies_questions:
            random_response = random.choice(movies_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            webbrowser.open('http://in.bookmyshow.com/')
            memory.append((user_input, random_response))
        elif user_input in music_questions:
            random_response = random.choice(music_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('http://www.bing.com/search?q=latest+music&src=IE-SearchBox&FORM=IENTTR&conversationid=')
            memory.append((user_input, random_response))
        elif user_input in news_questions:
            random_response = random.choice(news_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            webbrowser.open("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
            memory.append((user_input, random_response))
        elif user_input in maps_questions:
            random_response = random.choice(maps_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('https://www.google.co.in/maps/place/')
            memory.append((user_input, random_response))
        elif user_input in schedule_questions:
            random_response = random.choice(schedule_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            engine.say('What would you like to add')
            engine.runAndWait()
            SDH = input('What would you like to add : ')
            engine.say('for when would you like me to add it')
            engine.runAndWait()
            SDT = input('When : ')
            Schedule.append((SDH, SDT))

            memory.append((user_input, random_response, SDH, SDT))
        elif user_input in schedule_display:
            random_response = random.choice(schedule_display_responses)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            print( Schedule)
            memory.append((user_input, random_response))
        elif user_input in food_questions:
            random_response = random.choice(food_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('https://www.google.co.in/maps/search/nearby+restaurants/@28.4443557,77.0852257,15z/data=!3m1!4b1')
            memory.append((user_input, random_response))
        elif user_input in entertainment_questions:
            random_response = random.choice(entertainment_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('https://www.google.co.in/maps/search/entertainment+places/@28.4563798,76.9914966,12z/data=!3m1!4b1')
            memory.append((user_input, random_response))
        elif user_input in nickname_demand:
            print ("Okay fancy person you can have your self a nickname")
            engine.say("Okay fancy person you can have your self a nickname")
            engine.runAndWait()
            engine.say('What would you like your nickname to be')
            engine.runAndWait()
            nick = input('What would you like your nickname to be : ')
            print ("Okay from now on i call you", nick)
            engine.say("Okay from now on i call you")
            engine.say(nick)
            engine.runAndWait()
            print ("what would you like to do", nick)
            engine.say("what would you like to do")
            engine.say(nick)
            engine.runAndWait()
        elif user_input in compliments:
            random_response = random.choice(compliments_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            memory.append((user_input, random_response))
        elif user_input in jokes_questions:
            random_response = random.choice(jokes_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))
        elif user_input in Walkman_questions:
            print ("Bringing Your Muisc right up")
            engine.say("Bringing Your Muisc right up")
            engine.runAndWait()
            time.sleep(3)
            webbrowser.open("https://www.youtube.com/watch?v=A8q4O1mwnEc&list=RDA8q4O1mwnEc&start_radio=1&t=0")
            time.sleep(10)
        elif user_input in google_questions:
            engine.say("What would you like to search")
            engine.runAndWait()
            with sr.Microphone() as source:                                                                       
                    print("Speak:")                                                                                   
                    audio = r.listen(source)   

            try:
                    query=r.recognize_google(audio)
            except sr.UnknownValueError:
                    print("Could not understand audio")
                    

            except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    
                    
           
           
            chrome_path = r'"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            memory.append((user_input))
        elif user_input == "":
            
            print (':')
        else:
            print ('i am sorry i did not understand what you mean')
            engine.say('i am sorry i did not understand what you mean')
            engine.runAndWait()
            print ("Let me do a quick google search")
            engine.say("let me do a quick google search")
            engine.runAndWait()
            query = user_input
            #base_url = "https://www.google.co.in/?gfe_rd=cr&ei=PZHCV9aZE6fv8wflioH4Cg&safe=active&gws_rd=ssl&safe=active#safe=active&q="
            #final_url = base_url + parse(query)
            chrome_path = r'"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            #webbrowser.open(final_url, new=1, autoraise=True)
            memory.append(query)
else:
    while True:
        user_input = input('>>>ME: ')
        if user_input in greetings:
            random_response = random.choice(greetings_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))
        elif user_input in initial_questions:
            random_response = random.choice(initial_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in call_questions:
            random_response = random.choice(call_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in message_questions:
            random_response = random.choice(message_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in mail_action_questions:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            engine.say("enter your email ID")
            engine.runAndWait()
            Email = input("enter your email ID >>> : ")
            engine.say("enter your password")
            engine.runAndWait()
            Pass = input("enter your password >>> : ")
            server.login(Email, Pass)
            engine.say("enter receivers Email ID")
            engine.runAndWait()
            Rec_Email = input("enter receivers Email ID >>> : ")
            engine.say("Enter the message you want to send")
            engine.runAndWait()
            msg = input("Enter the message you want to send >>> : ")
            server.sendmail(Email, Rec_Email, msg)
            server.quit()
            print ("mail sent")
            engine.say("mail sent")
            engine.runAndWait()
        elif user_input in call_action_questions:
            random_response = random.choice(call_action_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in message_action_questions:
            random_response = random.choice(message_action_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in mail_questions:
            random_response = random.choice(mail_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in beauty_questions:
            random_response = random.choice(beauty_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in action_questions:
            random_response = random.choice(action_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in math_questions:
            operand1 = int(input('please enter the numbers:- '))
            operand2 = int(input('please enter the numbers:- '))

            if user_input == 'add' or user_input == 'JUNE add':
                Sum = operand1 + operand2
                print (Sum)
                engine.say(Sum)
                engine.runAndWait()
            elif user_input == 'multiply' or user_input == 'JUNE multiply':
                Mul = operand1 * operand2
                print (Mul)
                engine.say(Mul)
                engine.runAndWait()
            elif user_input == 'divide' or user_input == 'JUNE divide':
                div = operand1 / operand2
                print (div)
                engine.say(div)
                engine.runAndWait()
            elif user_input == 'subtract' or user_input == 'JUNE subtract':
                sub = operand1 - operand2
                print (sub)
                engine.say(sub)
                engine.runAndWait()
            else:
                print ('sorry i didnt quite understand')
                engine.say('sorry i didnt quite understand')
                engine.runAndWait()
                print ('this may not be in my library')
                engine.say('this may not be in my library')
                engine.runAndWait()
        elif user_input in inquiry:
            random_response = random.choice(inquiry_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in comebacks_questions:
            random_response = random.choice(comebacks_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))

        elif user_input in memory_respond:
            print (memory)

        elif user_input in depart:
            time.sleep(0.5)
            print ('it was nice chatting with you, we shall catch up later')
            engine.say('it was nice chatting with you, we shall catch up later')
            engine.runAndWait()
            mycursor.execute("select * from JUNE.PY_LICENSE")
            for a in mycursor:
                print(a)
            mycursor.execute("""select 'JUNE is subject to copyrights under #89-3b Software Ownership, Protection against Plagerism Guidelines PVT. LTD.'""")
            for b in mycursor:
                print(b)
            break
        elif user_input in weather_questions:
            random_response = random.choice(weather_responses)
            print( random_response)
            engine.say(random_response)
            engine.runAndWait()
            def weather_data(query):
                res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
                return res.json();
            def print_weather(result,city):
                t="{}'s temperature: {}°C ".format(city,result['main']['temp'])
                s="Wind speed: {} m/s".format(result['wind']['speed'])
                q="Description: {}".format(result['weather'][0]['description'])
                p="Weather: {}".format(result['weather'][0]['main'])
                l=t+"\n"+s+"\n"+q+"\n"+p
                print(l)
    
            def main():
                city=input('Enter the city:')
                print()
                try:
                        query='q='+city;
                        w_data=weather_data(query)
                        print_weather(w_data, city)
                        print()
                except:
                        print('City name not found...')
                        return "city not found"

            if __name__=='__main__':
                main()
                
            memory.append((user_input, random_response))
        elif user_input in movies_questions:
            random_response = random.choice(movies_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('http://in.bookmyshow.com/')
            memory.append((user_input, random_response))
        elif user_input in music_questions:
            random_response = random.choice(music_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('http://www.bing.com/search?q=latest+music&src=IE-SearchBox&FORM=IENTTR&conversationid=')
            memory.append((user_input, random_response))
        elif user_input in news_questions:
           random_response = random.choice(news_responses)
           time.sleep(0.5)
           print (random_response)
           engine.runAndWait()
           webbrowser.open("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
           memory.append((user_input, random_response))
        elif user_input in maps_questions:
            random_response = random.choice(maps_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('https://www.google.co.in/maps/place/')
            memory.append((user_input, random_response))
        elif user_input in schedule_questions:
            random_response = random.choice(schedule_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            engine.say('What would you like to add')
            engine.runAndWait()
            SDH = input('What would you like to add : ')
            engine.say('for when would you like me to add it')
            engine.runAndWait()
            SDT = input('When : ')
            Schedule.append((SDH, SDT))

            memory.append((user_input, random_response, SDH, SDT))
        elif user_input in schedule_display:
            random_response = random.choice(schedule_display_responses)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            print (Schedule)
            memory.append((user_input, random_response))
        elif user_input in food_questions:
            random_response = random.choice(food_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('https://www.google.co.in/maps/search/nearby+restaurants/@28.4443557,77.0852257,15z/data=!3m1!4b1')
            memory.append((user_input, random_response))
        elif user_input in entertainment_questions:
            random_response = random.choice(entertainment_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            webbrowser.open('https://www.google.co.in/maps/search/entertainment+places/@28.4563798,76.9914966,12z/data=!3m1!4b1')
            memory.append((user_input, random_response))
        elif user_input in nickname_demand:
            print ("Okay fancy person you can have your self a nickname")
            engine.say("Okay fancy person you can have your self a nickname")
            engine.runAndWait()
            engine.say('What would you like your nickname to be')
            engine.runAndWait()
            nick = input('What would you like your nickname to be : ')
            print ("Okay from now on i call you", nick)
            engine.say("Okay from now on i call you")
            engine.say(nick)
            engine.runAndWait()
            print ("what would you like to do", nick)
            engine.say("what would you like to do")
            engine.say(nick)
            engine.runAndWait()
        elif user_input in compliments:
            random_response = random.choice(compliments_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()

            memory.append((user_input, random_response))
        elif user_input in jokes_questions:
            random_response = random.choice(jokes_responses)
            time.sleep(0.5)
            print (random_response)
            engine.say(random_response)
            engine.runAndWait()
            memory.append((user_input, random_response))
        elif user_input in Walkman_questions:
            print ("Bringing Your Music right up")
            engine.say("Bringing Your Muisc right up")
            engine.runAndWait()
            time.sleep(3)
            webbrowser.open("https://www.youtube.com/watch?v=A8q4O1mwnEc&list=RDA8q4O1mwnEc&start_radio=1&t=0")
            time.sleep(10)
        elif user_input in google_questions:
            engine.say("What would you like to search")
            engine.runAndWait()
            query=input("search==>")
                    
                    
           
           
            chrome_path = r'"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            memory.append((user_input))
        else:
            print ('i am sorry i did not understand what you mean')
            engine.say('i am sorry i did not understand what you mean')
            engine.runAndWait()
            print ("Let me do a quick google search")
            engine.say("let me do a quick google search")
            engine.runAndWait()
            query = user_input
            #base_url = "https://www.google.co.in/?gfe_rd=cr&ei=PZHCV9aZE6fv8wflioH4Cg&safe=active&gws_rd=ssl&safe=active#safe=active&q="
            #final_url = base_url + parse(query)
            chrome_path = r'"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            #webbrowser.open(final_url, new=1, autoraise=True)
            memory.append(query)
