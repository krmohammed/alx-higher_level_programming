-- lists all shows contained in hbtn_0d_tvshows that have
-- at least one genre linked.

SELECT
	shows.title, genre.genre_id
FROM
	tv_shows shows
		JOIN
	tv_show_genres genre ON shows.id = genre.show_id
ORDER BY shows.title ASC, genre.genre_id ASC;
