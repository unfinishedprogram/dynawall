

import gi
import time
import asyncio
import threading
import os.path
import sys
from pathlib import Path

print(sys.argv)

sys.stdout.flush()

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2, Gdk
from http.server import BaseHTTPRequestHandler, HTTPServer


class WallpaperServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        home = str(Path.home())
        htmlFile = open('./content/index.html', 'r')
        pageData = htmlFile.read()

        self.wfile.write(bytes(pageData, 'utf8'))

def startWallpaperClient(url):
    window = Gtk.Window()

    window.set_type_hint(Gdk.WindowTypeHint.DESKTOP)

    window.set_can_focus(False)
    window.set_accept_focus(False)
    window.set_keep_below (True)
    
    window.connect('destroy', Gtk.main_quit)
    window.set_wmclass('dynamicwall', 'dynamicwall' + sys.argv[1])
    
    webview = WebKit2.WebView()

    webview.load_uri(url)

    window.set_name('Dynamic Wallpaper')
    window.add(webview)
    window.show_all()
    window.fullscreen()

    Gtk.main()

def serveWallpaper(hostName, serverPort):
    try:
        wallServer = HTTPServer((hostName, serverPort), WallpaperServer)
    except:
        exit()
    print('Wallpaper server started')
    try: 
        wallServer.serve_forever()
    except KeyboardInterrupt:
        pass
    wallServer.server_close()
    print('Wallpaper server closed')

hostName = 'localhost'
serverPort = 20000
url = 'http://' + hostName + ':' + str(serverPort)

wpServer = threading.Thread(target=serveWallpaper, daemon=True, args=('localhost', 20000,))
wpClient = threading.Thread(target=startWallpaperClient, daemon=True, args=(url,))

wpServer.start()
startWallpaperClient(url)
