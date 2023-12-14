-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT
	shows.title
FROM
	tv_shows shows
WHERE
	shows.id NOT IN (
		SELECT
		        shows.id
		FROM
        		tv_shows shows
                		JOIN
      			tv_show_genres s_gen ON shows.id = s_gen.show_id
                		JOIN
        		tv_genres genre ON s_gen.genre_id = genre.id
		WHERE
        		genre.name = 'Comedy'
	)
ORDER BY shows.title ASC;
