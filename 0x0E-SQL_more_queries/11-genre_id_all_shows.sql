-- lists all shows contained in the database hbtn_0d_tvshows

SELECT
	shows.title, genre.genre_id
FROM
	tv_shows shows
		LEFT JOIN
	tv_show_genres genre ON shows.id = genre.show_id
ORDER BY shows.title ASC, genre.genre_id ASC;
