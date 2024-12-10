# Pygame_ComposableUI
A module for making a composable UI using Pygame

I was making my own [Smart mirror](http://example.com) and needed to be able to easily create different
parts of the screen without hard-coding them. So I created a submodule that did everything I needed it to do in a way
that utilizes a "stack," where you just push each individually created UI element onto a stack, then render the stack 
all in one go. It all had to work on `pygame` because I was using a Raspberry pi to run the whole thing.

I want to make this public so that it can be improved by others who find they also have projects where they want to be
able to compose a UI or something on the fly using Pygame!