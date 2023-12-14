-- lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT
	shows.title, SUM(ratings.rate) AS rating
FROM
	tv_shows shows
		JOIN
	tv_show_ratings ratings ON ratings.show_id = shows.id
GROUP BY shows.title
ORDER BY rating DESC;
