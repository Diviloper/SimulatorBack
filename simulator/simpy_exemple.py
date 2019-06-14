import numpy as np


class Simulation:
    def __init__(self):
        self.num_trucks_in_system = 0
        self.clock = 0.0
        self.t_arrival = self.generate_interarrival()
        self.t_depart = float('inf')  # infinito
        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0

    def advance_time(self):
        t_event = min(self.t_arrival, self.t_depart)
        self.total_wait += self.num_trucks_in_system * (t_event - self.clock)
        self.clock = t_event
        if self.t_arrival <= self.t_depart:
            self.handle_arrival_event()
            self.handle_pregate()
            self.handle_maingate()
        else:
            self.handle_depart_event()

    def handle_arrival_event(self):
        self.num_trucks_in_system += 1
        self.num_arrivals += 1
        if self.num_trucks_in_system <= 1:
            self.t_depart = self.clock + self.generate_pregate()
        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_pregate(self):
        if self.num_trucks_in_system <= 1:
            self.t_depart = self.clock + self.generate_maingate()

    def handle_maingate(self):
        if self.num_trucks_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()

    def handle_depart_event(self):
        self.num_trucks_in_system -= 1
        self.num_departs += 1
        if self.num_trucks_in_system > 0:
            self.t_depart = self.clock + self.generate_service()
        else:
            self.t_depart = float('inf')

    def generate_interarrival(self):
        return np.random.lognormal(3.8804, 0.88923)  # TODO: agafar aquest variable de fora

    def generate_pregate(self):
        return np.random.lognormal(6.6019, 1.0388)  # TODO: agafar aquest variable de fora

    def generate_maingate(self):
        return np.random.lognormal(0.54445, 4.176)  # TODO: agafar aquest variable de fora

    def generate_service(self):
        return np.random.lognormal(3.0806, 0.50637)  # TODO: agafar aquest variable de fora


np.random.seed(0)

s = Simulation()

num_steps = 100  # TODO: agafar aquest variable de fora

if __name__ == '__main__':
    print('nitrogeno')
    for i in range(num_steps):
        s.advance_time()
