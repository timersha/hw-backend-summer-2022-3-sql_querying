# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
SELECT flight_no, (scheduled_arrival - scheduled_departure) AS duration
FROM flights
ORDER BY duration ASC
LIMIT 5;
"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
select flight_no, COUNT(flight_no)
from flights
group by flight_no
having COUNT(flight_no) < 50
order by COUNT(flight_no) desc
limit 3;
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
select COUNT(f.flight_no) as count
from flights f
inner join airports_data dep on dep.airport_code = f.departure_airport
inner join airports_data arr on arr.airport_code = f.arrival_airport
where dep.timezone = arr.timezone;
"""
#  count
# --------
#  16824
