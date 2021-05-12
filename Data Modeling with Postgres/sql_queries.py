# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id SERIAL primary key, start_time timestamp NOT NULL, user_id varchar NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY, first_name text, last_name text, gender text, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title text, artist_id varchar, year int, duration int);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name text, location text, latitude text, longitude text);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int, weekday varchar);""")

# INSERT RECORDS

songplay_table_insert = ("""  INSERT INTO songplay ( start_time, user_id, level, song_id, artist_id , session_id , location , user_agent )VALUES (%s, %s, %s, %s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET (first_name, last_name, gender, level) =
(EXCLUDED.first_name,  EXCLUDED.last_name, EXCLUDED.gender, EXCLUDED.level)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE SET (title, artist_id, year, duration) =
(EXCLUDED.title, EXCLUDED.artist_id, EXCLUDED.year, EXCLUDED.duration)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO UPDATE SET (name, location, latitude, longitude) =
(EXCLUDED.name, EXCLUDED.location, EXCLUDED.latitude, EXCLUDED.longitude)
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO UPDATE SET (hour, day, week, month, year, weekday) =
(EXCLUDED.hour, EXCLUDED.day, EXCLUDED.week, EXCLUDED.month, EXCLUDED.year, EXCLUDED.weekday)
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id FROM songs JOIN artists  ON songs.artist_id = artists.artist_id WHERE songs.title = %s  AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]