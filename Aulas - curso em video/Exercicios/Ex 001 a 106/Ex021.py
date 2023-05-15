# 21 - Faça um programa que abra e reproduza o audio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load("Bachelors Of Science - Have You Ever Tried.mp3")
pygame.mixer.music.play()
pygame.event.wait()


