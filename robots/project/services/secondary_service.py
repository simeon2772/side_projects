from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    def details(self):
        if self.robots:
            return f"{self.name} Main Service:\n" \
                   f"Robots: {' '.join([r.name for r in self.robots])}"
        else:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"


