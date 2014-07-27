Grooveshark Official API's notes
================================

The main objective of this section is not to document the grooveshark API but
to try to order it in a way that makes me feel confortable with a fantastic
implementation I wonder to have/do.


v3 API methods
--------------

First of all, lets categorize the methods to make them easier to group, with how to use them.

>>> conn = Connection(key='api-id', secret='api-key')

  User management:

  * registerUser - Create a new user
        >>> from gro import User
        >>> user = User(username='user', password='pass', connection=conn)
        >>> user.register()

  * authenticate - Authenticates user from user and password
        >>> User(username='user', password='pass', connection=conn)
        >>> user.login()

  * authenticateToken - Authenticate user through token
        >>> User(username='user', token='token', connection=conn)
        >>> user.login()

  * logout - Log out a user
        >>> user = conn.me()
        >>> user.logout() if user

  * startSession - Start a session
        Implicitly done

  * authenticateUser - Authenticate user in favor of authenticate
        Not to be used


  User Management
   
  * getUserInfo - Get user's info
        >>> user.info
          
  * getUserIDFromUsername - Gets user's id
        >>> user.id
          
  * getUserSubscriptionDetails - Get user's subscription description
        >>> user.subscription
        
  * getTrialInfo - Get a trial for app and userid combination
        >>> user.trial_info
          
  * createTrial - Starts a trial for app and userid (difference with before one?)
        >>> user.start_trial()
 
 
  User's stuff management:
  
  * addUserLibrarySongsEx - Add songs to user lib.
        >>> user.library.append(song)

  * getUserLibrarySongs - Get songs from the user's lib.
        >>> user.library

  * removeUserLibrarySongs - Remove songs from user lib
        >>> del user.library[song]

  * addUserLibrarySongs - Add songs to user lib. Is a quite messy method, in
  favor of the less messy method addUserLibrarySongsEx.

  * getUserPlaylists - Get user's playlists
        >>> user.playlists

  * undeletePlaylist - Undeletes a playlist
        >>> recovered_playlist = user.playlists[2]
        >>> recovered_playlist.restore()

  * deletePlaylist - Deletes a playlist
        >>> playlist = user.playlists[2]
        >>> playlist.delete()

  * createPlaylist - Creates a playlist
        >>> user.playlists.new('My playlist')

  * renamePlaylist - Renames a playlist
        >>> playlist = user.playlists[2]
        >>> playlist.name = 'My playlist 2'

  * getUserPlaylistsSubscribed - Get user's subscribed playlists
        >>> user.playlist_subscriptions

  * subscribePlaylist - Subscribe the user to a playlist
        >>> playlist.subscribe()

  * unsubscribePlaylist - Unsubscribe user from playlist
        >>> playlist.unsubscribe()

  * getUserFavoriteSongs - Get user's favorites
        >>> user.favorites

  * removeUserFavoriteSongs - Remove song from favorites
        >>> del user.favorites[song]

  * addUserFavoriteSong - Add a song to user's favorite
        >>> user.favorites.append(new_song)


  Catalog:

  * getPopularSongsToday - Get popular songs of today
        >>> service = conn.get_service()
        >>> service.today_songs

  * getPopularSongsMonth - Get popular songs of the month
        >>> service.month_songs

  * getUserPlaylistsByUserID - Get user playlist for user (no auth)
        >>> user = User(id='user-id', connection=conn)
        >>> user.playlist #TODO: Care on having correct return

  * getUserInfoFromUserID - Get user info fos user (no auth)
        >>> user.info

  * getPlaylistInfo - Get playlist info, no songs, in favor of getPlaylist
        >>> playlist = Playlist(id='playlist-id', connection=conn)
        >>> playlist.info

  * getPlaylistSongs - Gets playlist's songs, use getPlaylist
        >>> playlist

  * getPlaylist - Get playlist's info and songs.
        >>> playlist

  * setPlaylistSongs - Set playlist's songs, overwritting!
        >>> playlist.append()/delete()/pop()

  * getArtistsInfo - Get metadata from artists
        >>> artist = Artist(id='artist-id')
        >>> artist.info

  * getArtistAlbums - Get artist's album
        >>> artist.albums

  * getArtistVerifiedAlbums - Get artist's verified albums
        >>> artist.verified_albums

  * getArtistPopularSongs - Get top 100 of artist
        >>> artist.popular

  * getSimilarArtists - Search similar artists
        >>> artist.similar

  * getAlbumsInfo - Get metadata from albums
        >>> album = artist.albums[0]
        >>> album.info

  * getAlbumSongs - Get all songs from album
        >>> album.songs

  * getSongsInfo - Get info about songs
        >>> song = album.songs[0]
        >>> song.info

  * getDoesAlbumExist - Check if album id exists
        >>> album.check()

  * getDoesSongExist - Check if song id exists
        >>> song.check()

  * getDoesArtistExist - Check if artist id exists
        >>> artist.check()

  * getPlaylistSearchResults - Search for a playlist
        >>> conn.search(obj='playlist', query='alesa')

  * getAlbumSearchResults - Search for an album
        >>> conn.search(obj='album', query='alesa')

  * getSongSearchResults - Search for a song
        >>> conn.search(obj='song', query='alesa')

  * getArtistSearchResults - Search for artist
        >>> conn.search(obj='artist', query='alesa')

  * getAutocompleteSearchResults - Autocomplete (search suggestions)
        >>> conn.search(obj='autocomplete', query='alesa')

  
  Streaming:

  * getCountry - Get the IP/user's country
        >>> service.get_country()

  * getStreamKeyStreamServer - Get song streaming
        >>> song.get_stream()

  * getSubscriberStreamKey - Get stream for subscriber? diff to getStreamKeyStreamServer?
        >>> #TODO: Really need to test this

  * markStreamKeyOver30Secs - Mark song is been played for 30 secs
        >>> song.partial()

  * markSongComplete - Mark song has been completed
        >>> song.complete()

  
  Utils:

  * pingService - Ping the service to check if online
        # curl -d '{"method":"pingService"}' http://api.grooveshark.com/ws3.php
        >>> service.ping()

  * getServiceDescription - Get service's method description (Wondering if it works)
        >>> service.describe('method')

  * getSongURLFromTinysongBase62 - Get URL for tinysong
        >>> song.ts_url

  * getSongURLFromSongID - Get URL for song id
        >>> song.url

  * getPlaylistURLFromPlaylistID - Get URL for playlist
        >>> playlist.url

  * getTinysongURLFromSongID - Get Tinysong for song id
        >>> song.ts_url

  * getSongIDFromTinysongBase62 - Get song id from tinysong
        >>> Song(ts_url='tinysong-url')
  
  * startAutoplayTag - Start autoplay using a tag ????
        >>> autoplay = Autoplay(tags='')

  * getAutoplaySong - Get a song from autoplay
        >>> autoplay.get_song()

  * getAutoplayTags - Get a list of tags (Stations) ????
        >>> autoplay.tags

  * startAutoplay - Start autoplay ???
        >>> autoplay.start()

  * removeSongFromAutoplay - Remove song from autoplay ¿state?
        >>> autoplay.remove(song)

  * addSongToAutoplay - Add a song to autoplay state
        >>> autoplay.add(song)

  * removeVoteUpAutoplaySong - Remove an autoplay vote up
        >>> autoplay.vote = 0

  * voteUpAutoplaySong - Vote up autoplay song
        >>> autoplay.vote = 1

  * voteDownAutoplaySong - Vote down autoplay song
        >>> autoplay.vote = -1

  * removeVoteDownAutoplaySong - Remove vote down from autoplay
        >>> autoplay.vote = 0

Some notes on the API
---------------------

As you may have noticed, there are several methods that come to be the same. 
Some of them have been deprecated or seem to have been deprecated. I will put
here a use-case on how I plan the API to be used.
>>> cli.catalog.search_song(query='Some song')
>>> song in cli.catalog
>>> 