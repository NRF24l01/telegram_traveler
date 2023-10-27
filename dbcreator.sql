CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id int,
                    rang int
                );
CREATE TABLE IF NOT EXISTS Plases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    creator_id text,
                    country text,
                    sity text,
                    dayY text,
                    plase text,
                    textik text,
                    audio_name text
                )