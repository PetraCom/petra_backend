dataset = [{'time': '2019-08-01T13:04:00Z',
            'hash': '00069d342b40d274d7b34e080bb8fa77fa3662a387228b59576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 'df096812-afb4-4915-8cb4-a80a62e6939a'},
           {'time': '2019-08-01T13:04:00Z',
           'hash': '00069d342b40d274d7b34e080bb8fa77fa3662a38722zx59576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 1},
           {'time': '2019-08-01T13:04:00Z',
            'hash': '00069d342b40d274d7b34e080bb8fa77fa3662a387228bmn576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 1},
           {'time': '2019-08-01T13:04:00Z',
            'hash': '00069d342b40d274d7b34e080bb8fa77fa3662a3872oub59576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 1},
           {'time': '2019-08-01T13:04:00Z',
           'hash': '00069d342b40d274d7b34e080bb8fa77fa366kj387228b59576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 1},
           {'time': '2019-08-01T13:04:00Z',
            'hash': '00069d342b40d274d7b34e080bb8fa74fa3662a387228b59576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 1},
           {'time': '2019-08-01T13:04:00Z',
            'hash': '00069d342b40d274d7b34e080bb8as77fa3662a387228b59576c63ca',
            'latitude': 60.1538,
            'longitude': 24.95595,
            'serial': '0000000038bf9618',
            'distance': 25.36,
            'pet_id': 1}]


def get_dataset():
    for data in dataset:
        new_latitude = data['latitude'] + 0.001
        new_longitude = data['longitude'] + 0.001
        data.update({'latitude': new_latitude,
                     'longitude': new_longitude})
    return dataset
