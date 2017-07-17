import random

from models import session, Song, Artist

def get_random_song(artist=None):
    query = session.query(Song)

    # Apply filters
    if artist is not None:
        query = query.filter(Song.artist.has(name=artist))

    # Get results
    songs = query.all()

    if len(songs) == 0:
        return None

    # Pick a random song
    song = songs[random.randint(0, len(songs) - 1)]
    return song
