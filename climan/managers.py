# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------
import shutil
import sys

import click

from climan.configs import ConfigsBuilder


class ClickManager:

    def __init__(self, metadata: dict):
        self.config = ConfigsBuilder.build_config(metadata)

    def show_head(self):
        msg = self.smart_echo(text='', char='*')
        msg += self.smart_echo(f'{self.config.title}', '*')
        msg += self.smart_echo(f'{self.config.description}', ' ')
        return msg

    def show_footer(self):
        msg = self.smart_echo(f'{self.config.donate}', '-')
        msg = self.smart_echo(f'{self.config.url}', '-')
        msg += self.smart_echo(f'{self.config.copyright}', '*')
        return msg

    @staticmethod
    def echo(msg: str, print_flag=True) -> str:
        if print_flag:
            click.echo(str(msg))
        return msg

    def smart_echo(self, text='', char='-', print_flag=True):
        columns = self.term_width()
        symbol = ' ' if not char else char
        msg = f' {text} '.center(columns, symbol[:1]) \
            if text else f''.center(columns, symbol[:1])

        if print_flag:
            self.echo(msg)

        return msg

    @staticmethod
    def open_url(url):
        click.launch(url)

    def show_status(self, status, console=True):
        msg = 'Successfully!' if status else 'Error!'

        if console:
            self.echo(msg)

        return msg

    @staticmethod
    def get_action(title: str) -> bool:
        while 1:
            click.echo(f'{title} [y/n/e]?: ')
            char = click.getchar()

            if char.lower() in ('y', 'н'):
                return True
            elif char.lower() in ('n', 'т'):
                return False
            elif char.lower() in ('e', 'у'):
                sys.exit(0)

    @staticmethod
    def term_width():
        return shutil.get_terminal_size()[0]

    @staticmethod
    def input(title):
        return input(title)

    @staticmethod
    def print_via_pager(msg):
        try:
            click.echo_via_pager(msg)
        except (PermissionError, OSError):
            pass
