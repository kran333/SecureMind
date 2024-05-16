ratings_data = LOAD '/user/maria_dev/ml-100k/u.data' AS (user_id: int, movie_id: int, rating:int, rating_ts:int);

meta_data = LOAD '/user/maria_dev/ml-100k/u.item' USING PigStorage('|')
    AS (movie_id:int, movie_title: chararray, release_date: chararray, video_release: chararray, imdb_link: chararray);

name_lookup = FOREACH meta_data GENERATE movie_id, movie_title, ToUnixTime(ToDate(release_date, 'dd-MM-yyyy')) AS release_date;

rating_by_movie = GROUP ratings_data BY movie_id;

avg_ratings = FOREACH rating_by_movie GENERATE GROUP AS movie_id, AVG(ratings_data.rating) AS avg_rating;

five_str_rting = FILTER avg_ratings BY avg_rating > 4.0;

five_str_rting_data = JOIN five_str_rting BY movie_id, name_lookup BY movie_id;

old_five_str_mvie = ORDER five_str_rting_data BY name_lookup::release_date;

DUMP old_five_str_mvie;

