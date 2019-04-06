drop table if exists subscriptions;
drop table if exists sessions;
drop table if exists games;


create table games(
    game_name varchar(255) primary key,
    image_path varchar(255),
    max_players int,
    genre varchar(255)
    );

create table sessions(
    session_id serial primary key,
	server_id int,
	game_name varchar(255),
	date_created date,
	day_of_week varchar(2),
	time_of_day int,
	unique(session_id, day_of_week, time_of_day)
	foreign key(game_name) references games(game_name)
	    on delete cascade
	    on update cascade
	);

create table subscriptions(
    session_id int,
    user_id int,
    primary key(session_id, user_id),
    foreign key(session_id) references sessions(session_id)
	    on delete cascade
	    on update cascade
    );
