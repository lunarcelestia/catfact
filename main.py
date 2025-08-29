import requests

def main():
    try:
        print("получаем данные первой страницы...")
        firstpage_url = "https://catfact.ninja/facts"
        response = requests.get( firstpage_url)

        response.raise_for_status()

        data = response.json()

        totalfacts = data['total']
        factsper_page = data['per_page']
        print(f"всего фактов: {totalfacts}, на странице: {factsper_page}")

        last_page = ( totalfacts + factsper_page - 1) // factsper_page
        print(f"номер последней страницы: {last_page}")

        print(f"получаем данные с последней страницы {last_page}...")
        last_page_url = f"{firstpage_url}?page={last_page}"
        last_page_resp = requests.get(last_page_url)
        last_page_resp.raise_for_status()

        last_page_data = last_page_resp.json()
        facts = last_page_data['data']

        if facts:
            shortest = min(facts, key=lambda x: len(x['fact']))
            print("\n" + "="*50)
            print("самый короткий факт с ласт страницы: ")
            print(f"факт: {shortest['fact']}")
           
        else:
            print("на ласт странице нет фактов")

    except requests.exceptions.RequestException as e:
        print(f"ошибка при HTTP-запроса: {e}")
    except KeyError as e:
        print(f"ошибка парсинга, отсутствует ключ {e}")
    except Exception as e:
        print(f"ошибка {e}")

if __name__ == "__main__":
    main()



