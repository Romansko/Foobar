Braille Translation
===================

<br>Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. 
<br>But she never bothered to follow intergalactic standards for workplace accommodations, 
<br>so those minions have a hard time navigating her space station. 
<br>You figure printing out Braille signs will help them, 
<br>and - since you'll be promoting efficiency at the same time - increase your chances of a promotion. 
<br>
<br>Braille is a writing system used to read by touch instead of by sight. 
<br>Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). 
<br>You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's 
<br>command can feel the bumps on the signs and ""read"" the text with their touch. 
<br>The special printer which can print the bumps onto the signs expects the dots in the following order:
<br>1 4
<br>2 5
<br>3 6
<br>
<br>So given the plain text word ""code"", you get the Braille dots:
<br>
<br>11 10 11 10
<br>00 01 01 01
<br>00 10 00 00
<br>
<br>where 1 represents a bump and 0 represents no bump.  
<br>Put together, ""code"" becomes the output string ""100100101010100110100010"".
<br>
<br>Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing 
<br>the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, 
<br>handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) 
<br>for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

Languages
=========

<br>To provide a Python solution, edit solution.py
<br>To provide a Java solution, edit Solution.java

Test cases
==========

<br>Your code should pass the following test cases.
<br>Note that it may also be run against hidden test cases not shown here.
<br>
<br>-- Python cases --
<br>Input:
<br>solution.solution("code")
<br>Output:
<br>    100100101010100110100010
<br>
<br>Input:
<br>solution.solution("Braille")
<br>Output:
<br>    000001110000111010100000010100111000111000100010
<br>
<br>Input:
<br>solution.solution("The quick brown fox jumps over the lazy dog")
<br>Output:
<br>    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
<br>
<br>-- Java cases --
<br>Input:
<br>Solution.solution("code")
<br>Output:
<br>    100100101010100110100010
<br>
<br>Input:
<br>Solution.solution("Braille")
<br>Output:
<br>    000001110000111010100000010100111000111000100010
<br>
<br>Input:
<br>Solution.solution("The quick brown fox jumps over the lazy dog")
<br>Output:
<br>    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
<br>
<br>Use verify [file] to test your solution and see how it does. 
<br>When you are finished editing your code, use submit [file] to submit your answer. 
<br>If your solution passes the test cases, it will be removed from your home folder.
<br>