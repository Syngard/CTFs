# Upload challenge writeup

**Category:** Web

**Description:**

> This is an useful service to unzip some files. We added a flag (flag located at XXX.XXX.XXX.XXX/flag.php) for your convenience.


## Solution write-up


By reading the source code of the page that is kindly given, or by uploading a test archive, we find that our files are uploaded in a generated directory itself located in /uploads/. 
We can also find that it will be deleted after 2 minutes but that is highly useless.

Obviously, when we try to upload a PHP script, the server won't execute it and we can only download it back. Same goes for python or bash scripts.  

If we take an in-depth look at the (un)zip man page, we can read someting interesting about symbolic links
>-y  
>­--symlinks  
> For UNIX and VMS (V8.3 and later), store symbolic links as such in the zip archive, instead of compressing and storing the file referred to by the link. This can avoid multiple copies of files being included in the archive as zip recurses the directory trees and accesses files directly and by links.


It means that we can zip our link and upload it as such. Once on the server, it will then reference the file we made it point to. Since we know where the flag is, let's create a symlink that will point to it once locate in a /uploads/upl5a46c2d953811/ type directory.


```
$ ln -s ../../flag.php zelda.link
$ zip --symlink zelda.zip zelda.link
```

Finally, we upload this archive and download back our `zelda.link` file, that actually contains the flag.php
