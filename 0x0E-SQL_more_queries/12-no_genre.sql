-- lists all shows contained in hbtn_0d_tvshows without a genre linked

SELECT
	shows.title, genre.genre_id
FROM
	tv_shows shows
		LEFT JOIN
	tv_show_genres genre ON shows.id = genre.show_id
WHERE genre.show_id is NULL
ORDER BY shows.title ASC, genre.genre_id ASC;
