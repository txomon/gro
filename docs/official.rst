Grooveshark Official API's notes
================================

The main objective of this section is not to document the grooveshark API but
to try to order it in a way that makes me feel confortable with a fantastic
implementation I wonder to have/do.


v3 API methods
--------------

First of all, lets categorize the methods to make them easier to group, with how to use them.

>>> cli = GroClient(id='api-id', key='api-key')

  Connections:

  * registerUser - Create a new user
        >>> cli.user(username='user', password='pass'.....)

  * authenticate - Authenticates user from user and password
        >>> cli.user(username='user', password='pass')

  * authenticateToken - Authenticate user through token
        >>> cli.user(username='user, token='token)

  * authenticateUser - Authenticate user in favor of authenticate
        Not to be used

  * logout - Log out a user
        >>> del cli.user

  * startSession - Start a session
        Implicitly done
 
  
  User Management
   
  * getUserInfo - Get user's info
        >>> cli.user
          
  * getUserIDFromUsername - Gets user's id
        >>> cli.user[<username>]
          
  * getUserSubscriptionDetails - Get user's subscription description
        >>> cli.user.subscription
        
  * getTrialInfo - Get a trial for app and userid combination
        >>> cli.user.trial
          
  * createTrial - Starts a trial for app and userid (difference with before one?)
        >>> cli.user.start_trial()
 
 
  User's stuff management:
  
  * addUserLibrarySongsEx - Add songs to user lib.
        >>> cli.user.library.add(song)
  * addUserLibrarySongs - Add songs to user lib. Is a quite messy method, in 
  favor of the less messy method addUserLibrarySongsEx. 
  * getUserLibrarySongs - Get songs from the user's lib.
  * removeUserLibrarySongs - Remove songs from user lib

  * getUserPlaylists - Get user's playlists
  * undeletePlaylist - Undeletes a playlist
  * deletePlaylist - Deletes a playlist
  * createPlaylist - Creates a playlist
  * renamePlaylist - Renames a playlist

  * getUserPlaylistsSubscribed - Get user's subscribed playlists
  * subscribePlaylist - Subscribe the user to a playlist
  * unsubscribePlaylist - Unsubscribe user from playlist

  * getUserFavoriteSongs - Get user's favorites
  * removeUserFavoriteSongs - Remove song from favorites
  * addUserFavoriteSong - Add a song to user's favorite
  
  Catalog:

  * getPopularSongsToday - Get popular songs of today
  * getPopularSongsMonth - Get popular songs of the month

  * getUserPlaylistsByUserID - Get user playlist for user (no auth)
  * getUserInfoFromUserID - Get user info fos user (no auth)

  * getPlaylistInfo - Get playlist info, no songs, in favor of getPlaylist
  * getPlaylistSongs - Gets playlist's songs, use getPlaylist
  * getPlaylist - Get playlist's info and songs.
  * setPlaylistSongs - Set playlist's songs, overwritting!

  * getArtistsInfo - Get metadata from artists
  * getArtistAlbums - Get artist's album
  * getArtistVerifiedAlbums - Get artist's verified albums
  * getArtistPopularSongs - Get top 100 of artist
  * getAlbumsInfo - Get metadata from albums
  * getAlbumSongs - Get all songs from album
  * getSongsInfo - Get info about songs

  * getDoesAlbumExist - Check if album id exists
  * getDoesSongExist - Check if song id exists
  * getDoesArtistExist - Check if artist id exists

  * getPlaylistSearchResults - Search for a playlist
  * getAlbumSearchResults - Search for an album
  * getSongSearchResults - Search for a song
  * getArtistSearchResults - Search for artist
  * getSimilarArtists - Search similar artists
  * getAutocompleteSearchResults - Autocomplete (search suggestions)

  
  Streaming:
  * getCountry - Get the IP/user's country
  * getStreamKeyStreamServer - Get song streaming
  * getSubscriberStreamKey - Get stream for subscriber? diff to getStreamKeyStreamServer?
  * markStreamKeyOver30Secs - Mark song is been played for 30 secs
  * markSongComplete - Mark song has been completed
  
  Utils:
  * pingService - Ping the service to check if online
        # curl -d '{"method":"pingService"}' http://api.grooveshark.com/ws3.php
        >>> cli.ping_service()
  * getServiceDescription - Get service's method description (Wondering if it works)
  * getSongURLFromTinysongBase62 - Get URL for tinysong
  * getSongURLFromSongID - Get URL for song id
  * getPlaylistURLFromPlaylistID - Get URL for playlist
  * getTinysongURLFromSongID - Get Tinysong for song id
  * getSongIDFromTinysongBase62 - Get song id from tinysong
  
  * getAutoplaySong - Get a song from autoplay
  * getAutoplayTags - Get a list of tags (Stations) ????
  * startAutoplayTag - Start autoplay using a tag ????
  * startAutoplay - Start autoplay ???
  * removeVoteUpAutoplaySong - Remove an autoplay vote up
  * voteUpAutoplaySong - Vote up autoplay song
  * removeSongFromAutoplay - Remove song from autoplay ¿state?
  * addSongToAutoplay - Add a song to autoplay state
  * voteDownAutoplaySong - Vote down autoplay song
  * removeVoteDownAutoplaySong - Remove vote down from autoplay
  
Some notes on the API
---------------------

As you may have noticed, there are several methods that come to be the same. 
Some of them have been deprecated or seem to have been deprecated. I will put
here a use-case on how I plan the API to be used.
>>> cli.catalog.search_song(query='Some song')
>>> song in cli.catalog
>>> 