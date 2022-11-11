class Bird:

  valid_range = range(1, 11)

  def __init__(self, name, eggs):
      self.name = name
      self.eggs = eggs

  @property
  def eggs(self):
      return self._eggs

  @eggs.setter
  def eggs(self, eggs):
      if eggs in Bird.valid_range:
          self._eggs = eggs
      else:
          raise ValueError(f"Birds eggs has to be between 1 and 10 (both inclusive). You entered {eggs}")


class Migratory(Bird):

  country_range = range(5, 21)
  month_range = range(1, 13)

  def __init__(self, name, eggs, country, month):
    self.country = country
    self.month = month
    super().__init__(name, eggs)
  
  @property
  def month(self):
    return self._month

  @month.setter
  def month(self, month):
    if month in Migratory.month_range:
      self._month = month
    else:
      raise ValueError(f"Enter a month between 1 and 12 (both inclusive). You entered {month}")


  @property
  def country(self):
    return self._country

  @country.setter
  def country(self, country):
    if country == country.capitalize():
      if len(country) in Migratory.country_range:
        self._country = country
      else:
        raise ValueError(f"Enter a country between 5 and 20 (both inclusive). You entered {country}")
    else:
      raise ValueError(f"Make sure that the first letter of your country is capitalized and the rest lower case. You entered {country}")


def main():
  # falcon = Bird("falcon", 10)
  # print(falcon._eggs)

  falcon = Migratory("falcon", 5, "Spain", 12)


if __name__ == "__main__":
	main()