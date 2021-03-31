#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import parse_yaml
import telebot
import os


class TelegramInterface():
    def __init__(self, config_path):
        self.config_path = config_path
        # Initialize TelegramBot
        yaml_object = parse_yaml(self.config_path)
        self.bot = telebot.TeleBot(yaml_object['telegram_token'])
