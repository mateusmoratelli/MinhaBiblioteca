
from datetime import datetime
import pytz


def current_time():
   return datetime.now(pytz.timezone('America/Sao_Paulo'))