from pathlib import Path
import json

def overwrite_record(count, max_num):
    path = Path('record.json')

    try: 
        contents = path.read_text()
        record = json.loads(contents)
        if not isinstance(record, dict):
            record = {
                'easy': 0,
                'normal': 0,
                'hard': 0,
            }
    except FileNotFoundError:
        record = {
            'easy': 0,
            'normal': 0,
            'hard': 0,
        }

    if max_num == 10:
        record['easy'] = count
    elif max_num == 100:
        record['normal'] = count
    elif max_num == 1000:
        record['hard'] = count

    contents = json.dumps(record)
    path.write_text(contents)
