# TODO: Implement the Seeker class as follows...

# 1) Add the class declaration. Use the following class comment.__doc__
# 2) Create the class constructor. Use the following method comment.__doc__
# 3) Create the get_location(self) method. Use the following method comment.      
# 4) Create the move_location(self, location) method. Use the following method comment.

class Seeker:
  """The person looking for the Hider. The responsibility of a Seeker is to keep track of     its location and distance travelled. Attributes: location (int): The location of the     Seeker (1-1000)."""
  def __init__(self):
    """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
    self.location = 0

  def get_location(self):
    """Gets the current location.
        Returns:
            number: The current location,
        """
    return self.location

  def move_location(self, location):
    """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
    self.location = location 