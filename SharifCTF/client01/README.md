# client01 challenge writeup

**Category:** Forensics - 75 points

**Description:**

> [Linked archive](./client01.tar.gz)

> Attached file is the homepage of the client01. He knows the flag.


## Solution write-up

Let's unpack the archive to see what we are given.

```
$ tar zxf client01.tar.gz
$ cd client01/
$ ll
total 112
drwxr-xr-x 18 syngard syngard 4096 Jan 24 06:13 ./
drwxr-xr-x  3 syngard syngard 4096 Feb  4 17:52 ../
-rw-r--r--  1 syngard syngard  220 Jan 21 08:20 .bash_logout
-rw-r--r--  1 syngard syngard 3526 Jan 21 08:20 .bashrc
drwx------  6 syngard syngard 4096 Feb  4 17:52 .cache/
drwxr-xr-x  3 syngard syngard 4096 Feb  4 17:52 .cinnamon/
drwx------  9 syngard syngard 4096 Feb  4 17:52 .config/
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Desktop/
-rw-r--r--  1 syngard syngard   55 Jan 21 08:33 .dmrc
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Documents/
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Downloads/
drwx------  2 syngard syngard 4096 Jan 21 08:33 .gconf/
drwx------  3 syngard syngard 4096 Jan 21 08:33 .gnupg/
-rw-------  1 syngard syngard  632 Jan 24 06:09 .ICEauthority
drwx------  3 syngard syngard 4096 Jan 21 08:33 .local/
drwx------  4 syngard syngard 4096 Feb  4 17:52 .mozilla/
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Music/
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Pictures/
-rw-r--r--  1 syngard syngard  675 Jan 21 08:20 .profile
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Public/
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Templates/
drwx------  4 syngard syngard 4096 Jan 21 08:35 .thunderbird/
drwxr-xr-x  2 syngard syngard 4096 Jan 21 08:33 Videos/
-rw-------  1 syngard syngard   51 Jan 24 06:09 .Xauthority
-rw-------  1 syngard syngard 7072 Jan 24 06:13 .xsession-errors
-rw-------  1 syngard syngard 7046 Jan 21 08:44 .xsession-errors.old
```

There's quite a lot of stuff here. I started by checking the standart folders to see if they contained anything interesting but they were all empty.

```
$ ls -R
.:
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos

./Desktop:

./Documents:

./Downloads:

./Music:

./Pictures:

./Public:

./Templates:

./Videos:
```

Okay so we have to look inside of the other folders. The first one that caught my eye was `.mozilla`. After a bit a looking around, i found a [tool](http://www.dumpzilla.org/) that allowed easy data recovery from a `.mozilla` file. With a bit of help from the manual, I looked at the users downloads, his or her history, bookmarks and registered passwords. 

``` 
$ python dumpzilla.py .mozilla/firefox/c3a958fk.default/ --Downloads --History --Bookmarks --Passwords

Execution time: 2018-02-04 18:16:14.285690
Mozilla Profile: .mozilla/firefox/c3a958fk.default/

[ERROR]: Downloads database not found !


====================================================================================================
History Downloads    [SHA256 hash: 20fc6aa59fab92d8388d9f6e4065a238ba8a9e0157ad480c885c34efe60a6f62]
====================================================================================================




====================================================================================================
Directories          [SHA256 hash: 35df04f8cb094e6d43829f95dbd13b479aae7c8e534752f75c24c1020b3b2b41]
====================================================================================================




====================================================================================================
History              [SHA256 hash: 20fc6aa59fab92d8388d9f6e4065a238ba8a9e0157ad480c885c34efe60a6f62]
====================================================================================================


Last visit: 2018-01-24 06:11:05
Title: Welcome to Firefox
URL: https://www.mozilla.org/en-US/firefox/52.5.2/firstrun/
Frequency: 1


Last visit: 2018-01-24 06:12:17
Title: filehosting.org | Download | file
URL: http://www.filehosting.org/file/details/720884/Ncemd1SxbOVaOrbW/file
Frequency: 1




====================================================================================================
Bookmarks            [SHA256 hash: 20fc6aa59fab92d8388d9f6e4065a238ba8a9e0157ad480c885c34efe60a6f62]
====================================================================================================


Title: Getting Started
URL: https://www.mozilla.org/en-US/firefox/central/
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:53


Title: Help and Tutorials
URL: https://www.mozilla.org/en-US/firefox/help/
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:53


Title: Customize Firefox
URL: https://www.mozilla.org/en-US/firefox/customize/
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:53


Title: Get Involved
URL: https://www.mozilla.org/en-US/contribute/
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:53


Title: About Us
URL: https://www.mozilla.org/en-US/about/
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:53


Title: Most Visited
URL: place:sort=8&maxResults=10
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:53


Title: Recent Tags
URL: place:type=6&sort=14&maxResults=10
Date add: 2018-01-24 06:10:53
Last modified: 2018-01-24 06:10:54


Title: History
URL: place:type=3&sort=4
Date add: 2018-01-24 06:11:07
Last modified: 2018-01-24 06:11:07


Title: Downloads
URL: place:transition=7&sort=4
Date add: 2018-01-24 06:11:07
Last modified: 2018-01-24 06:11:07


Title: Tags
URL: place:type=6&sort=1
Date add: 2018-01-24 06:11:07
Last modified: 2018-01-24 06:11:07


Title: None
URL: place:folder=TOOLBAR
Date add: 2018-01-24 06:11:07
Last modified: 2018-01-24 06:11:07


Title: None
URL: place:folder=BOOKMARKS_MENU
Date add: 2018-01-24 06:11:07
Last modified: 2018-01-24 06:11:07


Title: None
URL: place:folder=UNFILED_BOOKMARKS
Date add: 2018-01-24 06:11:07
Last modified: 2018-01-24 06:11:07


[ERROR]: Signons database not found !


================================================================================================================
Total information
================================================================================================================


Total Downloads: 0
Total History downloads: 0
Total urls in History: 2
Total urls in Bookmarks: 13
Total passwords: 0
Total passwords decode: 0
```

Nothing interesting in the Download section, nor in the Bookmarks or Passwords. However there is actually something for us in the user's history. We see that she visited a certain webpage used for sharing documents.

```
Last visit: 2018-01-24 06:12:17
Title: filehosting.org | Download | file
URL: http://www.filehosting.org/file/details/720884/Ncemd1SxbOVaOrbW/file
Frequency: 1
```

I then went to this page and downloaded the file. However the challenge wasn't over yet.

```
$ file file
file: data
$ hd file | head
00000000  89 4e 47 0d 0a 1a 0a 00  00 00 0d 49 48 44 52 00  |.NG........IHDR.|
00000010  00 03 e8 00 00 00 c8 04  03 00 00 00 89 c9 d6 7c  |...............||
00000020  00 00 00 1b 50 4c 54 45  00 00 00 ff ff ff 5f 5f  |....PLTE......__|
00000030  5f 9f 9f 9f bf bf bf df  df df 7f 7f 7f 3f 3f 3f  |_............???|
00000040  1f 1f 1f ad a0 d6 e1 00  00 00 09 70 48 59 73 00  |...........pHYs.|
00000050  00 0e c4 00 00 0e c4 01  95 2b 0e 1b 00 00 0e fc  |.........+......|
00000060  49 44 41 54 78 9c ed 9c  cf 73 1b 37 12 85 87 3f  |IDATx....s.7...?|
00000070  44 ce 51 23 91 96 8f 62  c9 49 e5 28 7a 57 e5 ab  |D.Q#...b.I.(zW..|
00000080  b8 29 af 73 d4 d8 b1 e3  a3 55 bb a9 f8 28 96 e3  |.).s.....U...(..|
00000090  2a 1f 49 25 f4 fe db 3b  e8 6e 00 0f 98 19 89 ca  |*.I%...;.n......|
```

What could this file be ? I thought at first that it might be a trap, a false track. But given that this was only a 75 points challenge that would be wierd. My guess was that this was en encrypted image

I then looked at the main image formats headers to see if one was more or less similar to the one I had. And I found exactly [what I was looking for](https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header).

The first byte corresponds but we have to insert a second byte to form a valid PNG header. So that's exactly what I did

```python
with open('file','rb') as f1:
    with open('decoded_file.png','wb') as f2:
        b = f1.read(1)
        f2.write(b)
        f2.write('\x50')
        while True:
            b=f1.read(1)
            if b:
                f2.write(b)
            else: break
```

Once ze run this scrip we get an image that we can open

[](./decoded_file.png)

Even if it is just the upper half, we can still easily read the flag.
