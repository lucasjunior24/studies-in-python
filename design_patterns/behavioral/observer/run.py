from abc import ABC, abstractmethod
from typing import Dict, List

class IObserver(ABC):
  @abstractmethod
  def update(self) -> None: pass

class IObservable(ABC):
  @abstractmethod
  def add_abserver(self, observer: IObserver) -> None: pass

  @abstractmethod
  def remove_abserver(self, observer: IObserver) -> None: pass
  
  @abstractmethod
  def notify_abserver(self, observer: IObserver) -> None: pass


class WeatherStation(IObservable):
  "Estação meteorológica"
  def __init__(self):
    self.__observers: List[IObserver] = []
    self.__state: Dict = {}

  @property
  def state(self):
    return self.__state
  
  @state.setter
  def state(self, state_update: Dict) -> None:
    new_state = {**self.__state, **state_update}
    if new_state != self.state:
      self.__state = new_state
      self.notify_abserver()

  def reset_state(self):
    self.__state = {}

  def add_abserver(self, observer: IObserver) -> None:
    self.__observers.append(observer)

  def remove_abserver(self, observer: IObserver) -> None:
    if observer in self.__observers:
      self.__observers.remove(observer)
  
  def notify_abserver(self,) -> None:
    for observer in self.__observers:
      observer.update()
    print()


class Smartphone(IObserver):
  def __init__(self, name: str, observable: WeatherStation):
    self.name = name
    self.observable = observable

  def update(self):
    observable_name = self.observable.__class__.__name__
    print(f'{self.name} o objeto {observable_name} '
          f'acabou de ser atualizado => {self.observable.state}')
          


weather_station = WeatherStation()
smartphone = Smartphone("IPhone", weather_station)
samsung = Smartphone("Sansun", weather_station)
weather_station.add_abserver(smartphone)
weather_station.add_abserver(samsung)

weather_station.state = {'Temperature': "15"}
# weather_station.state = {'Temperature': "30"}
# weather_station.state = {'Humiddity': "90%"}
weather_station.state = {}
weather_station.state = {}
weather_station.state = {}
weather_station.state = {}
weather_station.reset_state()