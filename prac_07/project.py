class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    # def __str__(self):
    #     pass

    def __str__(self):
        """Return string representation of project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, "
                f"completion: {self.completion}")

    def __lt__(self, other):
        # Implement comparison for sorting based on priority
        return self.priority < other

    def is_complete(self):
        return self.completion == 100
