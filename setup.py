from setuptools import setup, find_packages

setup(
    name="LangEngine",  # Replace with your package name
    version="0.1",     # Package version
    packages=find_packages(pygame, pyautogui, requests, bs4, os, tkinter, sys, datetime, webbrowser),  # Automatically find and include your package modules
    description="The current engine 'VenomCore' (Work In Progress) currently is capable of",
    author="EvanFrameX",
    author_email="piescandale@gmail.com",
    install_requires=[pygame, pyautogui, requests, bs4, os, tkinter, sys, datetime, webbrowser],  # List any package dependencies
)
