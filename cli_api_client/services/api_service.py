import requests

class ApiService:
    def make_request(self, method, url, params=None, data=None, headers=None):
        """
        Make an HTTP request.

        :param method: HTTP method (e.g., "GET", "POST", "PUT", "DELETE", etc.)
        :param url: The URL for the request.
        :param params: Query parameters (dictionary).
        :param data: Request body data.
        :param headers: Request headers.
        :return: Response object.
        """
        try:
            response = requests.request(
                method,
                url,
                params=params,
                data=data,
                headers=headers,
            )

            # Raise an exception for HTTP errors (4xx and 5xx status codes)
            response.raise_for_status()

            return response
        except requests.exceptions.RequestException as e:
            # Handle exceptions (e.g., connection errors, timeouts, etc.)
            print(f"Error making request: {e}")
            return None
