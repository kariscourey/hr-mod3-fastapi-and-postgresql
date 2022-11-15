steps = [
    [
        ## Create table (up)
        """
        CREATE TABLE vacations (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(1000) NOT NULL,
            from_date DATE NOT NULL,
            to_date DATE NOT NULL,
            thoughts TEXT
        );
        """,
        ## Drop table (down)
        """
        DROP TABLE vacations;
        """
    ]
]
