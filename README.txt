1. run the python program

2. make sure the mongo daemon is runnign

3. run this command:
    mongoimport --db fpl --collection players --file mongo_insert_file.json --jsonArray

4. enter mongo and type:
    use fpl
    db.players.find().pretty() // or commands in commands.txt

5. design_doc.txt contains the choices between two different schema designs
and the reason for my choice

