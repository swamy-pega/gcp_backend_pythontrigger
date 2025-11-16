from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field


#class Config:
#       env_file = ".env"
#       env_file_encoding = "utf-8"

class Settings(BaseSettings):
    # Database configuration
   model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
   db_host: str = Field(..., env='DB_HOST')
   db_port: int = Field(..., env='DB_PORT')
   api_url: str = Field(..., env='API_URL')
   api_quiz_prefix: str = Field(..., env='API_QUIZ_PREFIX')
   ALLOWED_HOSTS: str = Field(..., env='ALLOWED_HOSTS')
   ENV: str = Field(..., env='ENV')


   db_port: int = Field(..., env='DB_PORT')

   db_user: str = Field(..., env='DB_USER')
   db_password: str = Field(..., env='DB_PASSWORD')
   db_name: str = Field(..., env='DB_NAME')
   db_url: str = Field(..., env='DB_URL')
    #db_port: str = Field(..., env='DB_PORT')
    #db_user: str = Field(..., env='DB_USER')
   # db_password: str = Field(..., env='DB_PASSWORD')
    #db_name: str = Field(..., env='DB_NAME')
    #db_url: str = Field(..., env='DB_URL')
   

    #SECRET_KEY: str = Field(..., env='SECRET_KEY')
   SECRET_KEY: str = Field(..., env='SECRET_KEY')
   ALGORITHM: str = Field(..., env='ALGORITHM')
   ACCESS_TOKEN_EXPIRE_MINUTES: str = Field(..., env='ACCESS_TOKEN_EXPIRE_MINUTES')
   GEMINI_API_KEY: str = Field(..., env='GEMINI_API_KEY')


    # Application settings
  #app_name: str = Field('MyApp', env='APP_NAME')
  #app_version: str = Field('1.0.0', env='APP_VERSION')

settings = Settings()

#print("Settings loaded: " + str(settings.dict()))