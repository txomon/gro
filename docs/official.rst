Grooveshark Official API's notes
================================

The main objective of this section is not to document the grooveshark API but
to try to order it in a way that makes me feel confortable with a fantastic
implementation I wonder to have/do.


v3 API methods
--------------

First of all, lets categorize the methods to make them easier to group.


  * addUserLibrarySongs - Add songs to user lib. Is a quite messy method, in 
  favor of the lesser messy method. 
  * getUserLibrarySongs - Get songs from the user's lib.
  * addUserLibrarySongsEx - Add songs to user lib.
  * removeUserLibrarySongs - Remove songs from user lib
  * getUserPlaylistsSubscribed - Get user's subscribed playlists
  * getUserPlaylists - Get user's playlists
  * getUserFavoriteSongs - Get user's favorites
  * removeUserFavoriteSongs - Remove song from favorites
  * logout - Log out a user
  * authenticateToken - Authenticate user through token
  * getUserInfo - Get user's info
  * getUserSubscriptionDetails - Get user's subscription description
  * addUserFavoriteSong - Add a song to user's favorite
  * subscribePlaylist - Subscribe the user to a playlist
  * unsubscribePlaylist - Unsubscribe user from playlist
  * getCountry - Get the IP/user's country
  * getPlaylistInfo - Get playlist info, no songs, in favor of getPlaylist
  * getPopularSongsToday - Get popular songs of today
  * getPopularSongsMonth - Get popular songs of the month
  * pingService - Ping the service to check if online
  * getServiceDescription - Get service's method description (Wondering if it works)
  * undeletePlaylist - Undeletes a playlist
  * deletePlaylist - Deletes a playlist
  * getPlaylistSongs - Gets playlist's songs, use getPlaylist
  * getPlaylist - Get playlist's info and songs.
  * setPlaylistSongs - Set playlist's songs, overwritting!
  * createPlaylist - Creates a playlist
  * renamePlaylist - Renames a playlist
  * authenticate - Authenticates user from user and password
  * getUserIDFromUsername - Gets user's id
  * getAlbumsInfo - Get metadata from albums
  * getAlbumSongs - Get all songs from album
  * getArtistsInfo - Get metadata from artists
  * getSongsInfo - Get info about songs
  * getDoesAlbumExist - Check if album id exists
  * getDoesSongExist - Check if song id exists
  * getDoesArtistExist - Check if artist id exists
  * authenticateUser - Authenticate user in favor of authenticate
  * getArtistVerifiedAlbums - Get artist's verified albums
  * getArtistAlbums - Get artist's album
  * getArtistPopularSongs - Get top 100 of artist
  * getPlaylistSearchResults - Search for a playlist
  * getAlbumSearchResults - Search for an album
  * getSongSearchResults - Search for a song
  * getArtistSearchResults - Search for artist
  * getStreamKeyStreamServer - Get song streaming
  * getSongURLFromTinysongBase62 - Get URL for tinysong
  * getSongURLFromSongID - Get URL for song id
  * getPlaylistURLFromPlaylistID - Get URL for playlist
  * getTinysongURLFromSongID - Get Tinysong for song id
  * getUserPlaylistsByUserID - Get user playlist for user (no auth)
  * getUserInfoFromUserID - Get user info fos user (no auth)
  * getSimilarArtists - Get similar artists
  * startSession - Start a session
  * getTrialInfo - Get a trial for app and userid combination
  * createTrial - Starts a trial for app and userid (difference with before one?)
  * getAutocompleteSearchResults - Autocomplete (search suggestions)
  * getSubscriberStreamKey - Get stream for subscriber? diff to getStreamKeyStreamServer?
  * markStreamKeyOver30Secs - Mark song is been played for 30 secs
  * markSongComplete - Mark song has been completed
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
  * getSongIDFromTinysongBase62 - Get song id from tinysong
  * registerUser - Create a new user