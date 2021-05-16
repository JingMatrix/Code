# pylint: disable = C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401

config: ConfigAPI = config  # noqa: F821 pylint: disable = E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable = E0602,C0103

import sys, os

# Load autoconfig before the rest of python config
config.load_autoconfig(False)

config.bind(',p', 'spawn --userscript qute-pass')
config.bind('<Ctrl+p>', 'config-cycle -t content.proxy socks5://localhost:9050/ none')
config.bind('<Ctrl+r>', 'config-cycle colors.webpage.darkmode.enabled ;; restart')
config.bind('zo', 'set-cmd-text :open file:///home/jing/')

c.zoom.default = '150%'
c.aliases['mpv'] = 'spawn --userscript view_in_mpv'
c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt',
        'https://easylist.to/easylist/easyprivacy.txt',
        'https://raw.githubusercontent.com/easylist/easylistchina/master/easylistchina.txt',
        'https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt']
c.content.blocking.method = 'both'
c.content.pdfjs = True
c.downloads.remove_finished = 3000
c.fileselect.handler = 'external'
c.fileselect.single_file.command = ['alacritty','-e','nnn','-n','-p','{}']
c.fileselect.multiple_files.command = ['alacritty','-e','nnn','-n','-p','{}']
c.fileselect.folder.command = ['alacritty','-e','nnn','-n','-p','{}']

c.window.hide_decoration = True

c.fonts.default_size = '12pt'
c.fonts.web.family.standard = 'Manjari'
c.fonts.web.size.default = 17
c.input.insert_mode.auto_load = True

# c.qt.force_platform = 'wayland'
c.tabs.show = 'switching'
c.statusbar.show = 'in-mode'
c.url.start_pages = 'https://play.google.com/books/ebooks'
c.url.searchengines['DEFAULT']='https://www.google.com/search?q={}'

config.set('content.javascript.can_access_clipboard', True, 'https://github.com/*')
config.set('content.autoplay', True, 'https://jingmatrix.github.io/private/chat')
config.set('content.notifications.enabled', False)
config.set('content.headers.user_agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'http://apply.csc.edu.cn/csc/main/person/login/index.jsf')

try:
    from qutebrowser.api import message
    config.source('pyconfig/redirectors.py')

except ImportError:
    pass

