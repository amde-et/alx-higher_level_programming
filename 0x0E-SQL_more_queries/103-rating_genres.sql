-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
INNER JOIN tv_shows AS ts ON ts.id = tsg.show_id
INNER JOIN tv_show_ratings AS tsr ON tsr.show_id = ts.id
GROUP BY tg.name
ORDER BY rating DESC;
