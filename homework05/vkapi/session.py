import typing as tp

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Session:
    """
    Сессия.

    :param base_url: Базовый адрес, на который будут выполняться запросы.
    :param timeout: Максимальное время ожидания ответа от сервера.
    :param max_retries: Максимальное число повторных запросов.
    :param backoff_factor: Коэффициент экспоненциального нарастания задержки.
    """

    # def __init__(
    #         self,
    #         base_url: str,
    #         timeout: float = 5.0,
    #         max_retries: int = 3,
    #         backoff_factor: float = 1.5,
    #         max_timeout: float = 50.0
    # ) -> None:
    #     self.backoff_factor = backoff_factor
    #     self.base_url = base_url
    #     self.timeout = timeout
    #     self.max_retries = max_retries
    #     self.max_timeout = max_timeout
    #     self.session = None
    #
    # def get(self, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
    #     retries = 0
    #     delay = self.timeout
    #     while True:
    #         response = requests.get(self.base_url)
    #         if response.status_code == 200:
    #             return response
    #         time.sleep(delay)
    #         delay = min(delay * self.backoff_factor, self.max_timeout)
    #         delay += random.normalvariate(delay * 0.1)
    #         retries += 1
    #         if retries > self.max_retries or delay > self.max_timeout:
    #             break
    #
    # def post(
    #         self, url: str, params=None, data=None, *args: tp.Any, **kwargs: tp.Any
    # ) -> requests.Response:
    #     session = self.retry_session()
    #     response = session.post(
    #         self.base_url + f"/{url}",
    #         *args,
    #         **kwargs,
    #         timeout=self.timeout,
    #         params=params,
    #         data=data,
    #     )
    #     if response.status_code == 200:
    #         return response
    #     raise requests.exceptions.RetryError
    #
    # def retry_session(self):
    #     if not self.session:
    #         self.session = requests.Session()
    #         retries = Retry(
    #             total=self.max_retries,
    #             backoff_factor=self.backoff_factor,
    #             raise_on_status=False,
    #             status_forcelist=[500, 502, 503, 504],
    #         )
    #         self.session.mount("https://", HTTPAdapter(max_retries=retries))
    #     return self.session
    def __init__(
        self,
        base_url: str,
        timeout: float = 5.0,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
    ) -> None:
        self._session = requests.Session()
        self._session.mount(
            "https://",
            HTTPAdapter(
                max_retries=Retry(
                    total=max_retries,
                    backoff_factor=backoff_factor,
                    status_forcelist=[429, 500, 502, 503, 504],
                )
            ),
        )
        self._base_url = base_url
        self._timeout = timeout

    def get(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
        return self._session.get(self._base_url + "/" + url, params=kwargs, timeout=self._timeout)

    def post(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
        return self._session.post(self._base_url + "/" + url, data=kwargs)
