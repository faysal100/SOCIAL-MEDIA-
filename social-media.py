from colorama import Fore
print(Fore.GREEN + 'WELCOME TO HOODMASTER SERVER')
print('WITH THIS TOOL YOU CAN INCREASE SOCIAL MEDIA TRAFFIC:FACEBOOK,INSTAGRAM,TIKTOK,YOUTUBE likes,followers and views have fun')



import sys
import time
def loading():
 print("LOADING", end ="")
 loading = True  # a simple var to keep the loading status
 loading_speed = 4  # number of characters to print out per second
 loading_string = "." * 6  # characters to print out one by one (6 dots in this example)
 while loading:
     for index, char in enumerate(loading_string):
        # you can check your loading status here
         # if the loading is done set `loading` to false and break
         sys.stdout.write(char)  # write the next char to STDOUT
         sys.stdout.flush()  # flush the output
         time.sleep(1.0 / loading_speed)  # wait to match our speed
     index += 1  # lists are zero indexed, we need to increase by one for the accurate count
     # backtrack the written characters, overwrite them with space, backtrack again:
     sys.stdout.write("\b" * index + " " * index + "\b" * index)
     sys.stdout.flush()
     break

def space():
 print('')
 print('')
 print('')
 print('')
 print('')
 print('')

space()
print(Fore.BLUE + '1.FACEBOOK 2.INSTAGRAM 3.TIKTOK')
print('')
print(Fore.YELLOW + '4.YOUTUBE 5.TWITTER 6.SPOTIFY')
print('')
print(Fore.GREEN + '7.TELEGRAM 8.LINKEDIN 9.SNAPCHAT')
print('')
print(Fore.BLUE + '10.TWITCH 11.DISCORD 12.GOOGLE')
print('')
print('')
print('')
print('')

choice = input('which platform do you want to increase traffic?please type a full name:')

if choice=='youtube':
 print('you chose youtube')
 option = input('views,subs or likes?: ')
 if option=='views' or 'likes':
  option2 = input('How many?: ')
  input('video link?: ')
  loading()
  space()
  print(Fore.GREEN + 'link found!')
  space()
  loading()
  space()
  print(Fore.YELLOW + 'LOADING LIKES..')
  print(Fore.BLUE + '')
  loading()
  space()
  print(Fore.RED + 'SERVER CONNECTED!!')
  space()
  loading()
  space()
  print(Fore.GREEN + 'You have added', '' , option2, option)
  space()
  print(Fore.MAGENTA + 'THANK YOU FOR USING MY PROGRAM THE PROCESS WILL TAKE LESS THAN AN HOUR..')
  print('')
 else:
  input('channel link?:')
  loading()
elif choice=='instagram':
 print(Fore.RED + 'you chose instagram')
 option1 = input('likes or subs?:')
 if option1=='likes':
  input('post link?: ')
 else:
  input('channel link?: ')
elif choice=='facebook':
 print('wise, you chose facebook')
elif choice=='twitter':
 print(Fore.BLUE + 'nice twitter is a good choise')
elif choice=='tiktok':
 print(Fore.GREEN + 'PERFECT!! YOU CHOSE TWITTER')
elif choice=='twitch':
 print(Fore.RED + 'you chose twitch')
elif choice=='telegram':
 print(Fore.YELLOW + 'you chose telegram!!')
elif choice=='spotify':
 print('spotify it is!!')
elif choice=='snapchat':
 print('Your choice is snapchat!!')
elif choice=='discord':
 print('Thank you discord it is!!')
elif choice=='google':
 print('you chose google')
else:
 print(Fore.RED + 'INCORRECT OPTION')
 print('kindly choose from the options 1-12 in words and small letters')
 print('START THE PROGRAM AGAIN')
