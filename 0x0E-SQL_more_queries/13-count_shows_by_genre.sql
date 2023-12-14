-- lists all genres from hbtn_0d_tvshows and displays the
-- number of shows linked to each

SELECT
	genres.name as genre, COUNT(genres.name) as number_of_shows
FROM
	tv_genres genres
		JOIN
	tv_show_genres shows ON genres.id = shows.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
