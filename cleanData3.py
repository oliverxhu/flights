import pandas as pd
import datetime
from sqlalchemy import create_engine

try:
    engine = create_engine('mssql+pyodbc://admin:admin123!@flights')
except:
    print('connection to engine failed. check your ODBC connections')


def formatTable(file=r"C:\Users\HF_BI\Documents\Oliver\Flight Output\Output\Parsed\Details.csv"):
    df = pd.read_csv(file, encoding='utf8')
    df['Departure_Time'] = df['time'].apply(lambda x: x.split('\\xe2')[0].strip())
    df['Arrival_Time'] = df['time'].apply(lambda x: x.split('\\x93')[1].strip())
    df['Departure_DateTime'] = pd.to_datetime(df['departureDates'] + ' ' + df['Departure_Time'])
    df['Load_DateTime'] = datetime.datetime.now()
    df_new = df.drop(['airport', 'departureDates', 'Departure_Time', 'time'], axis=1)
    df_new.columns = ['Airline', 'Flight_Duration', 'Source', 'URL', 'Price', 'Stop_Details', 'Stops', 'Destination',
                      'Arrival_Time', 'Departure_DateTime', 'Load_DateTime']
    # cols = df_new.columns.tolist()
    cols = ['Airline', 'Source', 'Destination', 'Departure_DateTime', 'Arrival_Time', 'Flight_Duration',
            'Price', 'Stops', 'Stop_Details', 'URL', 'Load_DateTime']
    df_final = df_new[cols]

    df_final.to_csv(r"C:\Users\HF_BI\Documents\Oliver\Flight Output\Output\Parsed\to_database.csv", index=None)
    # write to table
    # df_final.to_sql('google_flights_dev', con=engine, index=False, if_exists='replace')
