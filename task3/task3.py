import json

def fill(test_dict:dict,values_dict:dict) -> None:
    '''
    Функция заполнения полей
    :param test_dict: Json Тестов
    :param values_dict: Значения тестов
    :return:
    '''
    qu = list(test_dict)
    while qu:
        example = qu.pop()
        if example["id"] in values_dict:
            example["value"] = values_dict[example["id"]]
        qu.extend(example.get('values',[]))

def main():
    with open('values.json','r',encoding='utf-8') as f:
        results = {item['id']: item['value'] for item in json.load(f)['values']}

    with open('test.json','r',encoding='utf-8') as f:
        report = json.load(f)

    fill(report['tests'],results)

    with open('report.json','w',encoding='utf-8') as f:
        json.dump(report, f ,ensure_ascii = False ,indent=2)

if __name__ == '__main__':
    main()
