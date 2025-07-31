import os
import sys
import time
import threading
from kivy.clock import Clock

class HotReloader:
    def __init__(self, app, watch_paths=None, interval=1):
        self.app = app
        self.watch_paths = watch_paths or [os.path.join(os.getcwd(), 'kv')]
        self.interval = interval
        self._mtimes = {}
        self._running = False
        self._thread = None

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._watch, daemon=True)
            self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()

    def _watch(self):
        while self._running:
            changed = False
            for path in self.watch_paths:
                for root, _, files in os.walk(path):
                    for fname in files:
                        if fname.endswith('.kv'):
                            fpath = os.path.join(root, fname)
                            mtime = os.path.getmtime(fpath)
                            if fpath not in self._mtimes:
                                self._mtimes[fpath] = mtime
                            elif self._mtimes[fpath] != mtime:
                                self._mtimes[fpath] = mtime
                                changed = True
            if changed:
                Clock.schedule_once(lambda dt: self.reload())
            time.sleep(self.interval)

    def reload(self):
        print('[HotReload] Arquivo KV alterado. Recarregando interface...')
        self.app.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)
