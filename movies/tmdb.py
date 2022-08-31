from my_settings import TMDB_API_KEY

class TMDBHelper:
    """API 요청에 필요한 기능들을 제공합니다.
    
    Attributes:
        api_key: API 서비스에서 발급받은 API KEY입니다.
    """
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def get_request_url(self, method, **kargs):
        """API 요청에 필요한 주소를 구성합니다.
        
        Args:
            method: API 서비스에서 제공하는 메서드로써 기본 경로 뒤에 추가됩니다.
            **kargs: 쿼리 스트링 형태로 기본 요청 주소 뒤에 추가됩니다.
            
        Returns:
            base_url, mothod, 쿼리 스트링 형태로 구성된 요청 주소를 반환합니다.
        """
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'
        
        for k, v in kargs.items():
            request_url += f'&{k}={v}'
            
        return request_url

tmdb_helper = TMDBHelper(TMDB_API_KEY)