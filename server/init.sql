CREATE TABLE community (
    cid     int,
    sum     int,
    parent  int
);

CREATE TABLE members (
    member      varchar(10),
    value       int,
    community   int
);
