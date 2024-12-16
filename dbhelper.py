import mysql.connector
from streamlit import dataframe


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='flight'
            )
            self.mycursor = self.conn.cursor()
            print('Connection Established.')
        except:
            print('Connection Error.')

    def fetch_city_name(self):
        city = []
        self.mycursor.execute(
            """ 
            select distinct(Source) from flight.flight
            union
            select distinct(Destination) from flight.flight;        
            """
        )
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute(
            f"""
            SELECT Airline, Route, Dep_Time, Duration,Price  FROM flight
            WHERE Source = '{source}' AND Destination ='{destination}'
            """
        )
        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        self.mycursor.execute(
            """
            SELECT Airline, COUNT(*) FROM flight
            GROUP BY Airline
            """
        )
        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return  airline, frequency

    def busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute(
            """
            select Source, count(*) from (select source from flight
							union all
							select Destination from flight) t
            group by t.Source
            order by count(*) desc
            """
        )
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return  city, frequency

    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute(
            """
            select Date_of_Journey, count(*) from flight
            group by Date_of_Journey
            """
        )
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency
