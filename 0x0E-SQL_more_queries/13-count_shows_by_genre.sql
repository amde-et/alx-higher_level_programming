-- lists all genres from hbnt_0d_shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
