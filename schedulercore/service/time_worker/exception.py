class TimeValueError(ValueError):
    def __init__(self, value, e):
        self.value = value
        self.e = e


def bug_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except TimeValueError as e:
            raise e
        except Exception as e:
            raise TimeValueError(args, e)

        return result

    return wrapper
