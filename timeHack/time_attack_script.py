# -*- coding: utf-8 -*-
import time, string
from time_password_checker import check_password

class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
    
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)
        
        
    
    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        password = ''
        max_time = 0
        for _ in range(11):
            charTimes = {}
            for charIndex in range(33, 127):
                char = chr(charIndex)
                times = []
                for _ in range(5):
                    T1 = time.perf_counter()
                    result = check_password(password + char)
                    if result == 'Correct':
                        return password + char
                    T2 = time.perf_counter()
                    times.append(T2 - T1 - max_time)
                charTimes[char] = sum(times)/len(times)
            password += max(charTimes, key=charTimes.get)
            max_time = max(charTimes.values())
        return password
    
    
# Write Up
# Please explain your solution
'''
We want to run this procedure for each character position up to the password length:

Check all possible characters and compare their average time to check the character.
The number of samples per character is arbitrary as long as it is large enough to
ignore noice in the delay. I found that 3 samples is sufficient.

We must subtract the time it takes to check the previously correct characters.
As the password string gets longer, the time to check the current character becomes a
smaller contributer to the overall checking time. This will make the comparison between
character delays more accurate.

The character with the largest average delay is an outlier. It is most likely to be
the correct character because the password checker is spending extra time to check
the next character (meaning the current character is correct).

We then append this character to the password and repeat for the next password index.
'''