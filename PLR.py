import ephem

class SolarSystem:
    def __init__(self, date='2023/06/12 15:00:00', lat='39.9042', lon='116.4074'):
        self.planets = {
            'Mercury': ephem.Mercury(),
            'Venus': ephem.Venus(),
            'Mars': ephem.Mars(),
            'Jupiter': ephem.Jupiter(),
            'Saturn': ephem.Saturn(),
            'Uranus': ephem.Uranus(),
            'Neptune': ephem.Neptune(),
            'Pluto': ephem.Pluto(),
            'Earth': None
            
        }
        self.moons = {
            'Moon': ephem.Moon(),
            'Io': ephem.Io(),
            'Europa': ephem.Europa(),
            'Ganymede': ephem.Ganymede(),
            'Callisto': ephem.Callisto(),
            'Mimas': ephem.Mimas(),
            'Enceladus': ephem.Enceladus(),
            'Tethys': ephem.Tethys(),
            'Dione': ephem.Dione(),
            'Titan': ephem.Titan(),
            'Enceladus': ephem.Enceladus(),
            'Dione': ephem.Dione(),
            'Rhea': ephem.Rhea()
        }
        self.observer = ephem.Observer()
        self.observer.date = date
        self.observer.lat = lat
        self.observer.lon = lon

    def get_positions(self):
        positions = []
        for planet_name, planet in self.planets.items():
            if planet_name == 'Earth':
                ra, dec = self.observer.lat, self.observer.lon
            else:
                planet.compute(self.observer)
                ra, dec = planet.ra, planet.dec
            positions.append(f'{planet_name}_RA: {ra}, {planet_name}_Dec: {dec}')
        for moon_name, moon in self.moons.items():
            moon.compute(self.observer)
            positions.append(f'{moon_name}_RA: {moon.ra}, {moon_name}_Dec: {moon.dec}')
        return positions

solar_system = SolarSystem()
if __name__ == '__main__':
   print(solar_system.get_positions())
