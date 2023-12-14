-- lists all shows, and all genres linked to that show
-- from the database hbtn_0d_tvshows

SELECT
	shows.title AS title, genre.name AS name
FROM
	tv_shows shows
		LEFT JOIN
	tv_show_genres s_genre ON shows.id = s_genre.show_id
		LEFT JOIN
	tv_genres genre ON genre.id = s_genre.genre_id
ORDER BY title ASC, name ASC;
