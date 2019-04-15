drop table if exists subscriptions;
drop table if exists sessions;
drop table if exists games;


create table games(
    game_name varchar(255),
    server_id bigint,
    image_path varchar(255),
    max_players int,
    genre varchar(255),
    primary key(game_name, server_id)
    );

create table sessions(
    session_id serial primary key,
	server_id bigint,
	game_name varchar(255),
	date_created date,
	date_of_session date,
	time_of_day int,
	unique(server_id, game_name, date_of_session),
	foreign key(game_name, server_id) references games(game_name, server_id)
	    on delete cascade
	    on update cascade,
	check(time_of_day > 0 and time_of_day <= 12)
	);

create table subscriptions(
    session_id int,
    user_id int,
    user_name varchar(255),
    primary key(session_id, user_id),
    foreign key(session_id) references sessions(session_id)
	    on delete cascade
	    on update cascade
    );
