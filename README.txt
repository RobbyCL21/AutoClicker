Welcome to the Autoclicker program

Step 1: The IMPORTS

# TIME

We will need the sleep function to because python can not just run a click over and over again , it needs a moment
to pause and take a break so we import time for the sleep

# THREADING

We need to run 2 functions at the same time so we need to use threading so we can have those 2 codes run together:
1. To click when u press your button 
2. To check if you press the button or not because else we will not be able to stop it again 

# PYNPUT 

With this code we can then talk to the mouse and the keyboard to check what key and which mouse click ( left or right )

Step 2: TOGGLE KEY DEFINITION AND CLICKING BASICS

1. TOGGLE_KEY, this as it says is the key that is going to toggle your clicking. This can be any char just put ur preference

2. Clicking, has to be false from the start cuz if u put it on true , and run the code your clicker will start clicking from the start
This can cause problems so false!

3. Mouse, we gonna define mouse as controller to make sure we can call the mouse to be clicked 

Step 3: Clicking function

This function is going to check if the clicking = True , when it is not it will stay in sleep mode ( this is for the threading ).
If its true it clicks 1 time and then sleeps for 0.001 second and clicks again and so on and on 

Step 4: the toggling EVENT

This code will say 'if you press the toggle key change the clicking" so when u first click it , it will go from False to True
Clicking it again will go from True to False , shutting down ur auto clicker

In this code it says Clicking is false , so when toggle key is pressed clicking = not clicking will basically say 
clicking is not false ( since we said clicking = false ) 

Step 5: threading

The threading will make sure both codes run at the same time , so clicking will be checked for being false or true
and the clicking will be done if it is indeed true
While its clicking it still has to check if the toggle is being activated as we said before so thats why we run both at the
same exact moment

Step 6: Run the code!

Now u can run the code , put ur mouse on a location for clicking ( like a cookie for cookieclicker )
And then press your key to toggle it 

ADDITIONAL:

You can add a Toggle key for stopping the code ( if u have some coding experience ) and then u can say that if the toggle is being pressed 
that the code stops running and then u can press your toggle key of the clicker safe and well without having to worry that
your code might still be running!!