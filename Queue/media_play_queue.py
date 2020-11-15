from random import randint
from node_queue import Queue
import time


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)


class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.size > 0:
            current_track_node = self.dequeue()
            print('Now playing {}'.format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)


track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")

media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()
