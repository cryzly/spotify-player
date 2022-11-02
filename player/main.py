from pprint import pprint
from time import sleep
import logging as log

from spotipy.oauth2 import SpotifyOAuth
import spotipy

log.basicConfig(level=log.INFO, format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')

if __name__ == "__main__":

    # OAuth with User
    scopes = "user-read-playback-state,user-modify-playback-state"
    client_credentials_manager = SpotifyOAuth(
        client_id='',
        client_secret='',
        scope=scopes,
        redirect_uri='http://localhost:8080')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    log.info('Successfully exchanged Token from Spotify')

    # Shows playing devices
    devices = sp.devices()
    log.debug(f'Retrieved devices: {devices}')

    searched_device_name = ''
    device_id = ''
    for device in devices['devices']:
        device_name = device['name']
        log.debug(f'Checking device_name from Spotify against searched one: {device_name} == {searched_device_name}')
        if device_name == searched_device_name:
            device_id = device['id']

    log.info(f'device_id for {searched_device_name} is {device_id}')

    # Change track
    sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'], device_id=device_id)
    log.info('Started playing new Track!')

    # Change volume
    sp.volume(100)
    log.info('Increased volume to 100%!')
    sleep(3)
    sp.volume(50)
    log.info('Decreased volume to 50%!')
    sleep(3)
    sp.volume(100)
    log.info('Increased up volume to 100%!')
    sleep(3)

    sp.pause_playback(device_id=device_id)
    log.info('Paused!')

