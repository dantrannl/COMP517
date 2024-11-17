import datetime

class Passport:
    # Class variable is used to keep track of number of passports
    passport_count = 0

    def __init__ (self, first_name, last_name, dob, country, exp_date):
            """Initialises a passport object

            Args:
                first_name (str): first name of passport holder.
                last_name (str): last name of passport holder.
                dob (datetime.date obj): DOB of passport holder.
                country (str): passport's country.
                exp_date (datetime.date obj): expiration date of passport.
            """
            self.first_name = first_name
            self.last_name = last_name
            self.country = country
            
            #Convert dob and exp_date to datetime.date objects if they are strings
            if isinstance(dob, str):
                  self.dob = datetime.date.fromisoformat(dob)
            else: 
                  self.dob = dob #dob is already datetime.date object

            if isinstance(exp_date, str):
                  self.exp_date = datetime.date.fromisoformat(exp_date)
            else: 
                  #exp_date is already datetime.date object
                  self.exp_date = exp_date 

            # Initialise dictionary to store country's name and visit counts
            self.visited_countries = {} 

            # Assign the number of the first passport
            self.passport_number = Passport.passport_count
            Passport.passport_count += 1 # Add 1 for the next passport

    def is_valid(self):
            """Checks if expiration date is still valid.

            Returns:
                bool: Return True if the expiration date did not pass yet.
            """
            today = datetime.date.today()
            return self.exp_date >= today
                 
    def summary(self):
          """Returns a summary with human-readable information about the passport

          Returns:
              str: summarised information about the passport
          """
          if self.is_valid() is True:
            return f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}. It is valid"
          
          else: 
            return f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}. It is invalid"
            
    def check_data(self, first_name, last_name, dob, country):
            """Check if data is exactly the same as the passport object and if passport is still valid. 

            Args:
                first_name (str): first name of passport holder.
                last_name (str): last name of passport holder.
                dob (datetime.date obj): DOB of passport holder.
                country (str): passport's country. 

            Returns:
                bool: Only return True if all is correct.
            """
            if isinstance(dob, str):
                  dob = datetime.date.fromisoformat(dob)
            
            if self.is_valid():
                  return (self.first_name == first_name and
                          self.last_name == last_name and
                          self.dob == dob and
                          self.country == country
                          )
            return False
      
    def stamp(self, country_name):
            """
            Record country names and number of visits, unless it is the same as the passport's country.

            Args:
                country_name (str): The name of the country being visited.
            """        
      
            if country_name != self.country:
                if country_name in self.visited_countries:
                  # Increment visit count
                  self.visited_countries[country_name] += 1 

                # First time visit, initialise visit count
                else: self.visited_countries[country_name] = 1
 
    def countries_visited(self):
            """An iterable of the countries that have been stamped.
               
               Returns a dictionary which is iterable.
            """
            return self.visited_countries.keys()
          
    def times_visited(self, country_name):
            """The number of times that country has been stamped. Return 0 if not been stamped.

            Args:
                country_name (str): country name.

            Returns:
                int: The number of times that country has bee visited, 0 if not visited.
            """
            return self.visited_countries.get(country_name, 0)

    def sum_square_visits(self):
          """Sum of squares of the times_visited over each visited country

          Returns:
              int: sum of squares of the times_visited
          """
          return sum(visits **2 for visits in self.visited_countries.values())

    def passport_number(self):
          """The passports id number. The first passport created should have id number 0, the next should be 1, etc.

          Returns:
              int: passport number start from 0
          """
          return self.passport_number
                        
          

