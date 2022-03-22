import concurrent.futures
import time


BAN_API_URL = 'https://api-adresse.data.gouv.fr/search/'

def get_french_addresses(request):
    time.sleep(2)
    print(request)

request_data = [
    {'search_field': '17 rue saint maur'},
    {'search_field': '35 boulevard voltaire'},
    {'search_field': '32 rue rivoli'},
    {'search_field': 'Route de la Croqueterie'},
]

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
    result = executor.map(get_french_addresses, request_data)

end_time = time.time()
print(f'Total time to run multithreads: {end_time - start_time:2f}s')
