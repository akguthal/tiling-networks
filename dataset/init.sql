DROP TABLE IF EXISTS communities;
DROP TABLE IF EXISTS members;

CREATE TABLE communities (
    cid     int,
    sum     int,
    parent  int,
    leaf    boolean
);

CREATE TABLE members (
    mid         int,
    member      varchar(10),
    value       int,
    community   int
);
