
from datetime import datetime
import pytz


def current_time():
   """_summary_

   Returns:
       _type_: _description_
   """
   return datetime.now(pytz.timezone('America/Sao_Paulo'))