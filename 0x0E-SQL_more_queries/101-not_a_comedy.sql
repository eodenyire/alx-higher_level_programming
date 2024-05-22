-- This query retrieves all shows without the genre Comedy
-- Selecting show titles from the tv_shows table
SELECT title
FROM tv_shows
-- Filtering out shows that have the genre Comedy
WHERE id NOT IN (
    -- Subquery to select show IDs with the genre Comedy
    SELECT show_id
    FROM shows_genres
    -- Finding the genre ID for the genre Comedy
    WHERE genre_id = (
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy'
    )
)
-- Sorting the results in ascending order by show title
ORDER BY title ASC;
