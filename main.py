import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://your_server/phpmyadmin/'
LOGIN_URL = BASE_URL + 'index.php'
DB_NAME = 'your_db_name'
TABLE_NAME = 'your_table_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

def get_login_token(session):
    try:
        response = session.get(LOGIN_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        return None
    token_input = soup.find('input', {'name': 'token'})
    return token_input['value'] if token_input else None

def login(session, token):
    login_data = {
        'pma_username': USERNAME,
        'pma_password': PASSWORD,
        'token': token
    }
    response = session.post(LOGIN_URL, data=login_data)
    return response.status_code

def parse_table(session):
    table_url = f"{LOGIN_URL}?route=/sql&db={DB_NAME}&table={TABLE_NAME}"
    try:
        response = session.get(table_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        return None
    data_table = soup.find('table', {'class': 'table_results'})
    if not data_table:
        return None
    headers = [th.get_text(strip=True).strip("1") for th in data_table.find('thead').find_all('th', class_="column_heading")]
    rows = []
    for tr in data_table.find('tbody').find_all('tr'):
        row = [td.get_text(strip=True) for td in tr.find_all('td', class_="data")]
        rows.append(row)
    return headers, rows

def main():
    session = requests.Session()
    token = get_login_token(session)
    if token == None:
        return False
    status_code = login(session, token)
    if status_code != 200:
        return False
    table = parse_table(session)
    if table == None:
        return False
    print(f"Database '{DB_NAME}' - Table '{TABLE_NAME}'")
    headers, data = table
    print(*headers)
    for row in data:
        print(*row)
    return True

if __name__ == "__main__":
    result = main()
    if result:
        print("Script finished successfully")
    else:
        print("Script finished with error")