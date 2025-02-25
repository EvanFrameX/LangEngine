import os
import tkinter as tk
import pygame
import sys
import datetime as timer
import webbrowser as link
import bs4, requests 
import pyautogui as PAG

root = tk.Tk()
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

def stamp(arg):
        print(arg)
def add(first, second):
        return first + second
def sub(first, second):
        return first - second
def mul(first, second):
        return first * second
def dev(first, second):
        return first / second

def create_directory(directory_name):
    """Create a new directory if it doesn't exist."""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{directory_name}': {e}")

def list_files(directory_name):
    """List all files in a given directory."""
    try:
        with os.scandir(directory_name) as entries:
            print(f"Files in '{directory_name}':")
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except Exception as e:
        print(f"Error listing files in '{directory_name}': {e}")

def delete_file(file_name):
    """Delete a file if it exists."""
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error deleting file '{file_name}': {e}")


def get_current_working_directory():
    """Return the current working directory."""
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")
    return cwd

def create_window(name, width, length):
        root.title(f'{name}')
        root.geometry(f'{width}+{length}')

def run_window():
     root.mainloop()

def label_create(text, font, width, padding):
        label = tk.Label(root, text=f'{text}', font=(f'{font}', width))
        label.pack(pady=int(padding))

def button_create(text, commando, padding):
        button = tk.Button(root, text=f'{text}', command=commando)
        button.pack(pady=int(padding))

def action(element, key, action):
        element.bind(f'<{key}>', action)

def screen(title, width, height):
        pygame.display.set_mode((width, height))
        pygame.display.set_caption(f'{title}')
        
def draw(shape, color, transform, rad, first, second, array_points):
        if str(shape) == "rectangle":
                pygame.draw.rect(screen, color, transform)
        elif str(shape) == "circle":
                pygame.draw.circle(screen, color, pos, rad)
        elif str(shape) == "line":
                pygame.draw.line(screen, color, first, second, transform)
        elif str(shape) == "polygon":
                pygame.draw.polygon(screen, color, array_point)

def img_load(path):
        pygame.image.load(path)

def set_to_screen(img, x, y):
        screen.blit(igm, (x, y))

def check_press():
        pygame.key.get_pressed()

def snd_load(path):
        pygame.mixer.Sound(path)
        
def load_and_play(path):
        sound = pygame.mixer.Sound(path)
        sound.play()

def field(FPS):
        clock.tick(FPS)
        
def quit():
        pygame.quit()
        sys.exit()

def talk(text, lang):
        voice = engine.getProperty("voices")
        engine.setProperty("voice", lang.id)
        engine.say(text)
        engine.runAndWait()

def hear(audio, text, lang, debug):
        r = Recognizer()
        with Microphone() as source:
                audio = r.listen(source)
                text = r.recognize_google(audio, language=f'{lang}')
                if debug:
                        print(str(text))

def check_inside(element, inpt):
        return element in inpt

def create_file(name, extention, write, letter):
        with open(f'{name}{extention}', f'{letter}') as file:
                if int(write) == 0:
                        print('')
                else:
                        file.write(write)

def link(directory):
        link.open(str(directory))

def word_start(arg1, arg2):
        return arg1.startsqith(arg2)

def scrape(var, arg):
        var=bs4.BeautifulSoup(arg, 'html.parser')

def move_mouse(x, y, time):
        PAG.moveTo(x, y, time)

def mouse_hold():
        return PAG.mouseDown()
def mouse_release():
        return PAG.mouseUp()

def pick_img(every, deflist, path):
        if every:
                if deflist:
                        return list(PAG.locateAllCenterOnScreen(path))
                else:
                        return PAG.locateAllCenterOnScreen(path)
        else:
                return PAG.locateCenterOnScreen(path)

def key_do_press(keys):
        PAG.hotkey(keys)

def centry(path):
        PAG.center(path)

