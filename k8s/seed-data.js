// Since seeding in Mongo is done in alphabetical order, it's important to keep
// file names alphabetically ordered, if multiple files are to be run.

db.users.drop();

db.users.insertMany([
    {
        _id: 1,
        username: 'federico',
        firstname: 'Federico',
        lastname: 'Mestrone',
        idealAge: 35
    },
    {
        _id: 2,
        username: 'riccardo',
        firstname: 'Riccardo',
        lastname: 'Mestrone',
        idealAge: 30
    },
]);
