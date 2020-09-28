# minqlx - A Quake Live server administrator bot.
# Copyright (C) 2015 Mino <mino@minomino.org>

# This file is part of minqlx.

# minqlx is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# minqlx is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with minqlx. If not, see <http://www.gnu.org/licenses/>.

import minqlx
import random
import time
import re

from minqlx.database import Redis

_curb = re.compile(r"curb", flags=re.IGNORECASE)
_nooption = re.compile(r"^no option$", flags=re.IGNORECASE)
_dontyousee = re.compile(r"^dont you see$", flags=re.IGNORECASE)
_fuckit = re.compile(r"fuck it", flags=re.IGNORECASE)
_horrible = re.compile(r"horrible", flags=re.IGNORECASE)
_never = re.compile(r"never", flags=re.IGNORECASE)
_startover = re.compile(r"start over", flags=re.IGNORECASE)
_toolate = re.compile(r"too late", flags=re.IGNORECASE)


class foo(minqlx.Plugin):
    database = Redis

    def __init__(self):
        super().__init__()
        self.add_hook("chat", self.handle_chat)
        self.add_command("cookies", self.cmd_cookies)
        self.last_sound = None

        self.set_cvar_once("qlx_funSoundDelay", "3")

    def handle_chat(self, player, msg, channel):
        if channel != "chat":
            return

        msg = self.clean_text(msg)
        if _curb.match(msg):
            self.play_sound("sound/rc/curb.ogg")
        elif _nooption.match(msg):
            self.play_sound("sound/rc/no_option.ogg")
        elif _dontyousee.match(msg):
            self.play_sound("sound/rc/dontyousee.ogg")
        elif _fuckit.match(msg):
            self.play_sound("sound/rc/fuckit.ogg")
        elif _horrible.match(msg):
            self.play_sound("sound/rc/horrible.ogg")
        elif _never.match(msg):
            self.play_sound("sound/rc/never.ogg")
        elif _startover.match(msg):
            self.play_sound("sound/rc/start_over.ogg")
        elif _toolate.match(msg):
            self.play_sound("sound/rc/toolate.ogg")


    def play_sound(self, path):
        if not self.last_sound:
            pass
        elif time.time() - self.last_sound < self.get_cvar("qlx_funSoundDelay", int):
            return

        self.last_sound = time.time()
        for p in self.players():
            if self.db.get_flag(p, "essentials:sounds_enabled", default=True):
                super().play_sound(path, p)

    def cmd_cookies(self, player, msg, channel):
        x = random.randint(0, 100)
        if not x:
            channel.reply("^6♥ ^7Here you go, {}. I baked these just for you! ^6♥".format(player))
        elif x == 1:
            channel.reply("What, you thought ^6you^7 would get cookies from me, {}? Hah, think again.".format(player))
        elif x < 50:
            channel.reply("For me? Thank you, {}!".format(player))
        else:
            channel.reply("I'm out of cookies right now, {}. Sorry!".format(player))
