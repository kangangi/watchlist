import  os

class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
  MOVIE_API_KEY = '4af1e3754d5f435de8a267191ef1ca85'
  SECRET_KEY = ("Skylar")
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:wamuyu@localhost/watchlist'

  
class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
    Config : The parent configuration class with General configuration settings
  '''
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}