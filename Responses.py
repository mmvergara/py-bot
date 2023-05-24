import discord
import random


def get_response(message:str)->str:
    p_message = message.lower()

    if p_message == 'hello':
        return "Hey There!"
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    return "No response"