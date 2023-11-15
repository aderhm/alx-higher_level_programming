-- Lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') as tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ORDER VY tv_shows.title, tv_show_genres.genre_id ASC;
