# HomoglyphSteganography

This short program is mainly inspired by this website http://holloway.co.nz/steg/ <br/>
Some messages can be hidden in tweets:<br/>
<b>Tweet</b>: "This is a sample message posted on Twitter"<br/>
<b>Hidden message</b>: "Emma Stone"

<code>$ python3 stegano.py -e 'This is a sample message posted on Twitter','Emma Stone'</code>

It gives us the following message (without quotes): 'Thіｓ ｉs ａ sａmple meｓｓaｇe pоｓｔed on Twitter'.
To get the hidden message:

<code></code><code>$ python3 stegano.py -d 'Thіｓ ｉs ａ sａmple meｓｓaｇe pоｓｔed on Twitter'</code>

It gives us the name of the best actress in the world<br/>
Warning : it doesn't work with all characters. Your tweet should only contain "<i> abcdefghijklmnopqrstuvwxyz123456789'0.:/\\%-_?&;</i>" (all capital letters will be changed)
