### Easy Instagram Downloader for gallery-dl

import os

os.system('clear')

print("Easy Instagram Downloader for gallery-dl")
print("Make sure you run this program in the directory where you'd like all content saved (e.g. \"Instagram Archives\" in your Downloads folder)\n\n")

# while True:
#     browser_cookies = input("Will you be importing firefox browser cookies? (Y/N) ")
#     if browser_cookies == 'y' or browser_cookies == 'Y':
#         browser = " --cookies-from-browser firefox "
#         break
#     elif browser_cookies == 'n' or browser_cookies == 'N':
#         browser = " "
#         break
#     else:
#         print("ERROR! Invalid input.")

### BEGIN RAMBLE ###
## I've decided that instead of sticking with the above, it makes it much more simple to just default to this.
## If you'd like to revert to the previous method, comment out the line of code below and uncomment the while loop above.
browser = " --cookies-from-browser firefox "
## Instead of Firefox, you can replace with your browser of choice.
### END RAMBLE ###

print("")
user = input("Enter the Instagram username: ")
os.system('clear')
print("Target selected: @" + user + "\n\n")
print("What would you like to download? \nAvailable: posts,reels,tagged,stories,highlights")
print("Separate multiple options with a comma without spaces.")
media_selection = "all"
print("Or, type \"all\" to download everything.")
media_selection = input("(default is \"all\"): ")
if media_selection == "all" or media_selection == "":
    media_selection = "posts,reels,tagged,stories,highlights"
media_grab = media_selection.split(',')

o = "-o include="
save_dir = "-D ./" + user + "/"
url = "https://www.instagram.com/" + user

os.system('clear')
for media in media_grab:
    print("Now gathering " + media + " from @" + user)

    command = "gallery-dl" + browser + o + media + " " + save_dir + media + " " + url

    # Run the command in the terminal
    os.system(command)

print("Job complete.\n")
