-- lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT
	genres.name, SUM(ratings.rate) AS rating
FROM
	tv_shows shows
		JOIN
	tv_show_ratings ratings ON ratings.show_id = shows.id
		JOIN
	tv_genres genres ON genres.id = shows.id
GROUP BY genres.name
ORDER BY rating DESC;
