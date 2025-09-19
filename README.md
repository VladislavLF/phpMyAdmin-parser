## Automatic data parsing from phpMyAdmin
This program is designed to automatically log into the phpMyAdmin control panel, navigate to the specified database table, and extract its contents, subsequently outputting them to the console.

## Technologies Used
- The requests library for HTTP requests
- The BeautifulSoup library from BS4 for HTML parsing
- Sessions for maintaining authorization state

## Configuration
Before use, you must set the following parameters at the beginning of the script:
- BASE_URL - the base URL of the phpMyAdmin server
- DB_NAME - the database name
- TABLE_NAME - the name of the table to parse
- USERNAME and PASSWORD - login credentials

## Limitations
- Only works with the classic phpMyAdmin theme (looks for elements with the table_results, column_heading, and data classes)
- Does not handle pagination (if the table is large and paginated)
- Requires direct access to phpMyAdmin without two-factor authentication
