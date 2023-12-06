import pickle
import datetime

class Alquiler:
    def __init__(self, codigo_alquiler, ubicacion, camas, codigo_persona):
        self.codigo_alquiler = codigo_alquiler
        self.ubicacion = ubicacion
        self.camas = camas
        self.codigo_persona = codigo_persona
        self.fechas_ocupadas = []

    def rent(self, start_date, end_date):
        if self.is_available(start_date, end_date):
            self.fechas_ocupadas.append((start_date, end_date))
            with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/alquileres/alquileres.pickle', 'rb') as f:
                alquileres = pickle.load(f)
                alquileres[self.codigo_alquiler] = self
                with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/alquileres/alquileres.pickle', 'wb') as f:
                    pickle.dump(alquileres, f)
            return True
        return False

    def is_available(self, start_date, end_date):
        for fecha in self.fechas_ocupadas:
            if max(start_date, fecha[0]) < min(end_date, fecha[1]):
                return False
        return True

    @staticmethod
    def check_all_availability(start_date, end_date):
        with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/alquileres/alquileres.pickle', 'rb') as f:
            alquileres = pickle.load(f)
            available_alquileres = []
            for alquiler in alquileres.values():
                if alquiler.is_available(start_date, end_date):
                    available_alquileres.append(alquiler)
            return available_alquileres
