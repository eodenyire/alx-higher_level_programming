<<<<<<< HEAD
 -- Select shows with at least one genre linked
=======
-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
>>>>>>> 09272d6854d0b75b429a7f3041ac9dcee26222ac
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
