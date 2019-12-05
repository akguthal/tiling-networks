# Tiling Networks

## Setup

To run this application, you must setup your database first. To do so, follow the below steps.

1. Create a database called `tiling_networks` under the user `tiling_networks_user`. Set that user's password to `password`. Finally, make sure the user has admin access to the database.
2. Run `python3 dataset/data_importer.py`. This command will generate a network and import that network into the database.

Once that is done, you must run the server. To do so, run the following commands:

```
cd server
python3 server.py
```

Finally, to run the client, run the below commands in a separate terminal window:

```
cd client
yarn install 
yarn start
```

The application will automatically open in your browser, at `localhost:3000`.
