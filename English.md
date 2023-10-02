The main function of this tool is to detect batch urls or interfaces, and support the browser to automatically open specified urls to avoid manually reopening URLs



Why use IDT?

When you collect a lot of interfaces, accessing one would be a waste of time. However, simply knowing the status code and output URL is not enough, and you still need to manually open the browser to check for unauthorized vulnerabilities. IDT supports automatic browser opening of URLs, avoiding repetitive manual testing operations. You only need to use your eyes to observe whether the webpage has suspicious critical or unauthorized vulnerabilities



advantage

Support filtering URL status codes

Support for automated browser opening URLs

Support for proxy mode

option

Usage: IDT. py [- h] [- u FILE] [- o OUTPUT] [- sc STATUSCODE] [- b] [- oss] [- d] [-- proxy PROXY]



Open URLs and check for OSS keys



Optional arguments:

-h. -- help show this help message and exit

-U FILE, -- file FILE Enumerate files for urls

-O OUTPUT, -- output OUTPUT

Specify the output file

-Sc STATUS_ CODE, -- status_ Code Status_ CODE

Filter status code

-b. -- browser Open urls in a web browser

-Oss, -- detect_ Oss Detect oss keys

-d. -- default_ Status_ Code

Default output status code for the current URL

--Proxy PROXY use proxies



Usage example:

-The u option specifies the URL file for batch processing



Python IDT.py - u url.txt

The default output is the URL of the return value status code of 200



image



Using the - b parameter, the output URL interface will be opened using the browser for access



Python3 IDT.py - u url.txt - b

image



Use the - d parameter to specify the default status code for outputting all urls



Python IDT.py - u url.txt - d

image



Use the - sc parameter to filter status codes and output the specified URL



Python IDT.py - u url.txt - sc 301

image



Add the - o parameter and save as a file



Python IDT.py - u url.txt - o a.txt

Add - Proxy parameter supports proxy mode



Python IDT.py - u url.txt -- proxy 127.0.0.1:10809
