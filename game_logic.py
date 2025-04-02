import abc
import enum

# Typing
Hours = int
Points = int
Image = ...


class Task:
    def __init__(self, name: str, description: str, image: Image,
                 difficulty: Hours, award: Points, penalty: Points,
                 event_on_success: callable, event_on_fail: callable):
        """
        A task that can be given to a player

        :param name: Task name
        :param description: Task description
        :param image: Task image
        :param difficulty: The number of hours required to complete the task
        :param award: The number of points awarded for completing the task
        :param penalty: The number of points taken away if the task is failed
        :param event_on_success: An event that occurs if the task is completed
        :param event_on_fail: An event that occurs if the task is failed
        """
        self.name = name
        self.description = description
        self.image = image
        self.difficulty = difficulty
        self.award = award
        self.penalty = penalty
        self.event_on_success = event_on_success
        self.event_on_fail = event_on_fail


class Card(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name: str, description: str, image: Image):
        """
        Playing card

        :param name: Card name
        :param description: Card description
        :param image: Card image
        """
        self.name = name
        self.description = description
        self.image = image


class ActionCard(Card):
    def __init__(self, name: str, description: str, image: Image, cost: Hours,
                 action: callable, req_args: list[str], check_args: callable):
        """
        Action card - one of the card types

        :param name: Card name
        :param description: Card description
        :param image: Card image
        :param cost: The cost of the card in hours
        :param action: Card action
        :param req_args: A list of parameter names that the `action` function accepts
        :param check_args: A function for verifying the correctness of parameters
            passed to the `action` function
        """
        super().__init__(name, description, image)
        self.cost = cost
        self.action = action
        self.req_args = req_args
        self.check_args = check_args


class TaskTarget(enum.Enum):
    """
    Targets for cards
    """
    ME = 1  # Player
    OPPONENT = 2  # Opponent
    BOTH = 3  # Player or his opponent


class TaskCard(Card):
    def __init__(self, name: str, description: str, image: Image, task: Task, valid_targets: TaskTarget):
        """
        Task card - one of the card types

        :param name: Card name
        :param description: Card description
        :param image: Card image
        :param task: A task that is given when the card is played
        :param valid_targets: Valid targets
        """
        super().__init__(name, description, image)
        self.task = task
        self.valid_targets = valid_targets
