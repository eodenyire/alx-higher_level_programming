-- This query retrieves all genres not linked to the show "Dexter"
-- Selecting genre names from the tv_genres table
SELECT name
FROM tv_genres
-- Filtering out genres that are linked to the show "Dexter"
WHERE id NOT IN (
    -- Subquery to select genre IDs linked to the show "Dexter"
    SELECT genre_id
    FROM shows_genres
    -- Finding the show ID for the show "Dexter"
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
-- Sorting the results in ascending order by genre name
ORDER BY name ASC;
