-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT
	genre.name AS name
FROM
	tv_genres genre
		JOIN
	tv_show_genres s_gen ON genre.id = s_gen.genre_id
		JOIN
	tv_shows shows ON shows.id = s_gen.show_id
WHERE shows.title = 'Dexter'
ORDER BY name ASC;
