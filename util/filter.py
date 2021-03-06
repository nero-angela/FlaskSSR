

class Filter:
    """
    Jinja2 Filter
    """

    def __init__(self, app):
        method_list = [f for f in dir(self) if callable(getattr(self, f)) and not f.startswith('__')]
        for method in method_list:
            app.jinja_env.filters[method] = getattr(self, method)

    def comma(self, v):
        """
        숫자에 comma를 찍어줌

        e.g {{ 1000.0 | comma }} -> 1,000
        """
        return '{:,}'.format(int(float(v)))
