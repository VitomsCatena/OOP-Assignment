# Parent Class demonstrating  general object
class Device:
    """A general electronic device with basic functionality."""
    def __init__(self, brand, model):
        # Public attributes
        self.brand = brand
        self.model = model
        self.is_on = False
        print(f"A new {self.brand} {self.model} device has been created.")

    def turn_on(self):
        """Turns the device on."""
        if not self.is_on:
            self.is_on = True
            print(f"The {self.brand} {self.model} is now on.")
        else:
            print("The device is already on.")

# Child Class inheriting from Device
class Smartphone(Device):
    """A smartphone with specific attributes and methods."""
    def __init__(self, brand, model, os, storage_gb, battery_life_hours):
        # Call the constructor of the parent class
        super().__init__(brand, model)
        
        # Protected attribute 
        self._os = os
        
        # Private attribute (name mangling, two leading underscores)
        self.__battery_life_hours = battery_life_hours
        self.storage_gb = storage_gb
        
    def make_call(self, number):
        """Method to simulate making a phone call."""
        if self.is_on:
            print(f"Calling {number} from your {self.brand} {self.model}.")
        else:
            print(f"Cannot make a call. Your {self.brand} is off.")
            
    def install_app(self, app_name):
        """Method to simulate installing an application."""
        if self.is_on:
            print(f"Installing {app_name} on the {self.brand} {self._os} device.")
        else:
            print(f"Cannot install app. Your {self.brand} is off.")

    def get_battery_life(self):
        """
        Public method to access the private battery attribute.
        This is an example of encapsulation.
        """
        return self.__battery_life_hours

# --- Creating and Using Objects ---
    
# Create  new Smartphone object
my_phone = Smartphone("Google", "Pixel 8", "Android", 128, 48)

print("\n--- Interacting with the Smartphone ---")
my_phone.turn_on()
my_phone.make_call("555-123-4567")
my_phone.install_app("Instagram")

print(f"\nYour phone's OS is {my_phone._os}.") # This is discouraged but possible.
print(f"Your phone's battery life is {my_phone.get_battery_life()} hours.") # Correct way to access private attribute.

# Try to access the private attribute directly (will cause an error)
try:
    print(f"Attempting to access private attribute: {my_phone.__battery_life_hours}")
except AttributeError as e:
    print(f"\nAn error occurred while trying to access a private attribute: {e}")
