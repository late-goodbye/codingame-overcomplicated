# Intro
Finally, we have received the first messages from aliens! Unfortunately, we cannot understand them because they have a very unique way of speaking.

Here is how aliens encode their messages:
- At each step of the encoding, they remove a bigger part from the beginning of the original message, starting from 1 character only. First, they take the first character, then 2 characters, then 3, etc...
- Starting from an empty result string, they add each part taken from the original message alternatively at the end and at the beginning of the result string. They add the first part at the end, the second part at the beginning, the third part at the end, etc...

## Example
abcdefgh becomes ghibcadef

1) Take "a" from **abcdefghi**, add it at the end of an empty string -> **a**
2) Take "bc" from **bcdefghi**, add it at the beginning of **a** -> **bca**
3) Take "def" from **defghi**, add it at the end of **bad** -> **bcadef**
4) Take the remaining characters "ghi" and add it at the beginning of **bcadef** -> **ghibcadef**

Your job here is to _decode_ or _encode_ the messages to discuss with aliens.

## Input
Line 1: An integer N indicating the number of times the message was transformed. If N is positive you have to decode i.e. retrieve the original message. If N is negative you have to encode i.e. transform the message.

Line 2: A string message to be decoded or encoded.

## Output
One line: The original message (if N is positive) or the transformed message (if N is negative).

## Constraints
-10 ≤ N ≤ 10

0 < message length < 1024

_Note: I think it isn't important if I will use Python programming language._