"""
IP归属地识别
geoip2提供了二进制和csv两种数据库格式
"""
import csv
import geoip2.database


def get_ip_location(ip_address):
    with geoip2.database.Reader('GeoLite2-City.mmdb', ['zh-CN']) as reader:
        response = reader.city(ip_address)
        country = response.country.name
        subdivisions = response.subdivisions[0].name
        city = response.city.name
        return country, subdivisions, city


def convert_mmdb_to_csv():
    with geoip2.database.Reader('GeoLite2-City.mmdb', ['zh-CN']) as reader:
        # 创建 CSV 文件并写入表头
        with open("GeoLite2-City.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['IP', 'Continent', 'Country', 'Subdivisions', 'City', 'Latitude', 'Longitude'])
            print(dir(reader))
            # 遍历 .mmdb 文件中的数据并写入 CSV 文件
            for record in reader:
                ip = record.ip_address
                continent = record.continent.name
                country = record.country.name
                subdivisions = record.subdivisions.name
                city = record.city.name
                latitude = record.location.latitude
                longitude = record.location.longitude

                writer.writerow([ip, continent, country, subdivisions, city, latitude, longitude])


if __name__ == '__main__':
    ip = '110.242.68.66'
    r = get_ip_location(ip)
    print(f"ip {ip} {r}")

    # convert_mmdb_to_csv()
