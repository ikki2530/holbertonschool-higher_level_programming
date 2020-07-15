-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres ON (tv_genres.id = tv_show_genres.genre_id) JOIN tv_shows ON (tv_show_genres.show_id = 8) GROUP BY tv_genres.name
ORDER BY tv_genres.name;
