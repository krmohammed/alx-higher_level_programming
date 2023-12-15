-- lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT
    genre.name, SUM(show_rate.rate) AS ratings
FROM
    tv_shows shows
        JOIN
    tv_show_ratings show_rate ON show_rate.show_id = shows.id
        JOIN
    tv_show_genres show_gen ON show_gen.show_id = shows.id
        JOIN
    tv_genres genre ON genre.id = show_gen.genre_id
GROUP BY  genre.name
ORDER BY ratings DESC;
