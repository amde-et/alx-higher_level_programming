-- listing show by genre
SELECT ts.title, tg.name
FROM tv_shows AS ts
LEFT OUTER JOIN tv_show_genres AS tsg ON tsg.show_id = ts.id
LEFT OUTER JOIN tv_genres AS tg ON tg.id = tsg.genre_id
ORDER BY ts.title, tg.name ASC;
