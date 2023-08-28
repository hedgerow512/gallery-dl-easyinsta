# gallery-dl-easyinsta
A simple UI python script to easily download Instagram content with gallery-dl

Hello
---
I made a simple UI in Python to download content from Instagram profiles in their entirety, assuming you have gallery-dl and python3 properly installed.

NOTE for Windows Users
---
If you run this program on Windows, you should replace `os.system('clear')` with `os.system('cls')` in the source code. Mac and Linux users need not to change anything.

Usage & Mechanics
---
Download **eid.py** and run it in a terminal with `python3 /path/to/location/eid.py`

The program will only ask you two questions: The Instagram user which to download from and what to download (posts, reels, tagged media, stories, highlights). After that, it will create a directory in the folder it's running from and will automatically download to it, organizing posts, reels, etc into their own subfolders.

So, for example, you want to download only posts, reels, and stories from Mark Zuckerberg's profile @zuck. You will input `zuck` when prompted for the user, and input `posts,reels,stories` when prompted for media selection. The program will create a new folder at `./zuck`, with the associated downloaded files being stored in `./zuck/posts/`, `./zuck/reels/`, and `./zuck/stories/`. I'd suggest running this in a directory dedicated to your Instagram saves every time you run this program for ease of file management, such as in `~/Desktop/InstagramSaves/`.

The program will automatically import cookies from Firefox (though, you can change to a different browser in the source code if you desire). This is so you have access to all the media, assuming you're logged into Instagram in the browser.

Selling Point
---
My programming skills aren't that great, but it's good enough to get the job done easily. After using gallery-dl for a few days for multiple jobs, scrolling back and forth in the terminal to edit the commands for a specific user, manually needing to organize the downloaded content myself, I find the method I created to be much easier and faster to work with.
