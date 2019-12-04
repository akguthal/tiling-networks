# Tiling Networks

To run this application, you must setup your database first. To do so, follow the following steps.

1. IF `dataset/community-sql.csv` and `dataset/individual-sql.csv` don't exist yet, run `toy-community.py`
2. Run `createdb tiling_networks`
3. In the database, run `\i server/init.sql`
4. Then, still in the database, run the following two commands (replacing the path as appropriate):
    - `\copy community FROM './dataset/community-sql.csv' WITH CSV;`
    - `\copy members FROM './dataset/individual-sql.csv' WITH CSV;`

Once that is done,
you must run the client and the server. Open up two terminal windows. In one terminal window, run:

`cd server`

`python3 server.py`

In another terminal window, run:

`cd client`

`yarn install` (if this is the first time setting it up)

`yarn start`
