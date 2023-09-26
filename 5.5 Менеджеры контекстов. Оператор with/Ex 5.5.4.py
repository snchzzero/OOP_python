class PrimaryKey:
    def __enter__(self):
        print('вход')

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                print(exc_type)
                raise exc_type
        except Exception as ex:
            return True

with PrimaryKey() as pk:
    raise ValueError
