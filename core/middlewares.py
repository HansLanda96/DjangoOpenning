import time


class TimeProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()
        duration = end - start
        print(f'Processing time for url "{request.path}" is {round(duration, 2)} seconds')
        return response
