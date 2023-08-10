import psycopg2
import random
import temp_data


class InteractionToDB(temp_data.TempData):
    def __init__(self):
        self.conn = None
        self.cur = None

    def connecting(self):
        self.conn = psycopg2.connect(host='10.10.20.97', dbname='data_project_db',
                                     user='data_project', password=1111, port=5432)
        self.cur = self.conn.cursor()

    # ---------------------------------------------------------------------------------------------------
    def get_one_location(self):
        self.connecting()
        self.cur.execute(f"SELECT * from TB_SUBWAY", self.conn)
        select_data = self.cur.fetchall()
        count = len(select_data)
        rand_num = random.randint(0, count)
        select_one_data = select_data[rand_num]
        self.conn.commit()
        self.conn.close()
        return select_one_data

    def get_subway_data_about_business_district(self):
        self.connecting()
        self.cur.execute(f"SELECT name, address, latitude, longitude, month_avg_sales_600, day_avg_flow_population_600 from TB_SUBWAY", self.conn)
        total_data = self.cur.fetchall()
        self.conn.commit()
        self.conn.close()
        return total_data

    def get_round_infra_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select TYPE1, TYPE2, TYPE3, TYPE4, LATITUDE, LONGITUDE from TB_INFRA")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        get_satisfied_data_list = list()
        for infra in select_data:
            each_infra_location = (float(infra[4]), float(infra[5]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_infra_location, unit="m")
            if distance <= 600:
                get_satisfied_data_list.append(infra)

        self.conn.commit()
        self.conn.close()
        return get_satisfied_data_list

    def get_total_infra_data(self):
        self.connecting()
        self.cur.execute(f"select type1 from TB_INFRA")
        all_data = self.cur.fetchall()
        self.conn.commit()
        self.conn.close()
        return all_data

    def get_bus_station_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_BUS_STATION")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_bus_station in select_data:
            each_bus_station_location = (float(each_bus_station[0]), float(each_bus_station[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_bus_station_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_subway_stataion_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_SUBWAY_STATION")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_subway_station in select_data:
            each_subway_station_location = (float(each_subway_station[0]), float(each_subway_station[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_subway_station_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_university_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_UNIVERSITY_LOCATION")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_compete_store_ex_b_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_B_EXCEPT_SUBWAY")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_compete_store_ex_sst_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_SST_EXCEPT_SUBWAY")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_stay_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_STAY")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_exercise_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_EXERCISE")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_dessert_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_DESSERT")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_academy_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_ACADEMY")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_hospital_location_data(self, x, y):
        self.connecting()
        self.cur.execute(f"select LATITUDE, LONGITUDE from TB_HOSPITAL")
        select_data = self.cur.fetchall()
        input_location = (float(x), float(y))
        count = 0
        for each_data in select_data:
            each_data_location = (float(each_data[0]), float(each_data[1]))  # 현재 인프라 데이터중에 TYPE1, LATITUDE, LONGITUDE만 가져오도록 했음.
            # 거리 계산(x, y와)
            distance = haversine.haversine(input_location, each_data_location, unit="m")
            if distance <= 600:
                count += 1
        self.conn.commit()
        self.conn.close()
        return count

    def get_district(self):
        self.connecting()
        self.cur.execute(f"select GU_NAME FROM TB_DONG_AVG", self.conn)
        select_gu = self.cur.fetchall()
        select_gu = list(set(select_gu))
        for i in range(len(select_gu)):
            select_gu[i] = ''.join(select_gu[i])
        self.district_list = select_gu
        # for gu in select_gu:
        #     self.cur.execute(f"SELECT DONG_NAME from TB_DONG_AVG where GU_NAME = '{gu}'", self.conn)
        #     select_data = self.cur.fetchall()
        #     for j in range(len(select_data)):
        #         select_data[j] = ''.join(select_data[j])
        #     print(select_data)
        self.conn.commit()
        self.conn.close()
