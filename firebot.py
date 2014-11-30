import subprocess
import sys
from wikipedia import wikipedia
from jabberbot import *

class Fire_bot(JabberBot):
    @botcmd
    def whois(self, mess, args):
        """Displays whois information of a domain or ip"""
        return subprocess.check_output(['whois', '-H', args]).strip()
        
    @botcmd
    def youtube(self, mess, args):
        """Generates download link for youtube video"""
        return subprocess.check_output(['youtube-dl', '-g', args]).strip()
        
    @botcmd
    def free(self, mess, args):
        """Displays system memory information"""
        return subprocess.check_output(['free', '-m']).strip()
        
    @botcmd
    def wiki(self, mess, args):
        """Fetch 2 sentences of a wikipedia article"""
        return wikipedia.summary(args, sentences=2)
        
    @botcmd
    def file(self, mess, args):
        """Displays contents of a file"""
        return subprocess.check_output(['cat', '/home/1337/cute-cat.txt']).strip()
        

username = 'bot@192.168.1.2'
password = 'bot'
fire_bot = Fire_bot(username, password)
fire_bot.serve_forever()
