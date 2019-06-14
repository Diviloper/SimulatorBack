from abc import abstractmethod

import numpy as np

from simulator.truck import Truck


class Event:

    def __init__(self, truck, simulator):
        self.truck = truck
        self.simulator = simulator

    @abstractmethod
    def generate_next(self, current_time):
        pass

    @classmethod
    @abstractmethod
    def generate(cls, current_time, truck, simulator):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        return f'TruckId: {self.truck.id}'


class Arrival(Event):

    def __init__(self, truck, simulator):
        super().__init__(truck, simulator)
        self.alpha = self.simulator.simulation.alpha_A
        self.beta = self.simulator.simulation.beta_A

    def generate_next(self, current_time):
        return [Arrival.generate(current_time, Truck(self.truck.id + 1), self.simulator),
                PreGate.generate(current_time, self.truck, self.simulator)]

    @classmethod
    def generate(cls, current_time, truck, simulator):
        arrival = Arrival(truck, simulator)
        simulator.truck_counter += 1
        return current_time + arrival.beta * np.random.weibull(arrival.alpha), arrival

    def __repr__(self) -> str:
        return 'Arrival Event -> ' + super().__repr__()


class PreGate(Event):

    def __init__(self, truck, simulator):
        super().__init__(truck, simulator)
        self.mean = self.simulator.simulation.mean_PG
        self.sigma = self.simulator.simulation.sigma_PG

    def generate_next(self, current_time):
        return [MainGate.generate(current_time, self.truck, self.simulator)]

    @classmethod
    def generate(cls, current_time, truck, simulator):
        pregate = PreGate(truck, simulator)
        return current_time + np.random.lognormal(pregate.mean, pregate.sigma), pregate

    def __repr__(self) -> str:
        return 'PreGate Event -> ' + super().__repr__()


class MainGate(Event):

    def __init__(self, truck, simulator):
        super().__init__(truck, simulator)
        self.mean = self.simulator.simulation.mean_MG
        self.sigma = self.simulator.simulation.sigma_MG

    def generate_next(self, current_time):
        if self.assign_crane(current_time):
            return [Departure.generate(current_time, self.truck, self.simulator)]
        else:
            return []

    @classmethod
    def generate(cls, current_time, truck, simulator):
        maingate = MainGate(truck, simulator)
        return current_time + np.random.lognormal(maingate.mean, maingate.sigma), maingate

    def __repr__(self) -> str:
        return 'MainGate Event -> ' + super().__repr__()

    def assign_crane(self, current_time):
        self.truck.crane = int(np.random.uniform(0, self.simulator.simulation.n_cranes, 1))
        self.simulator.cranes[self.truck.crane].queue_evolution.append((current_time, True))
        return self.simulator.cranes[self.truck.crane].in_truck(self.truck, current_time)


class Departure(Event):

    def __init__(self, truck, simulator):
        super().__init__(truck, simulator)
        self.mean = self.simulator.simulation.mean_S
        self.sigma = self.simulator.simulation.sigma_S

    def generate_next(self, current_time):
        next_truck = self.simulator.cranes[self.truck.crane].finished(current_time, self.simulator)
        self.simulator.cranes[self.truck.crane].queue_evolution.append((current_time, False))
        if next_truck is not None:
            return [Departure.generate(current_time, next_truck, self.simulator)]
        return []

    @classmethod
    def generate(cls, current_time, truck, simulator):
        departure = Departure(truck, simulator)
        return current_time + np.random.lognormal(departure.mean, departure.sigma), departure

    def __repr__(self) -> str:
        return 'Departure Event -> ' + super().__repr__() + f' Queue size: {self.simulator.cranes[self.truck.crane].queue.qsize()}'
