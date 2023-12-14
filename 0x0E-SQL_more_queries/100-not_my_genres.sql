--  list all genres not linked to the show Dexter

SELECT
	genre.name
FROM
	tv_genres genre
WHERE
	genre.id NOT IN (
		SELECT
        		genre.id
		FROM
        		tv_genres genre
                		JOIN
        		tv_show_genres s_gen ON genre.id = s_gen.genre_id
                		JOIN
        		tv_shows shows ON shows.id = s_gen.show_id
		WHERE shows.title = 'Dexter'
	)
ORDER BY genre.name ASC;
