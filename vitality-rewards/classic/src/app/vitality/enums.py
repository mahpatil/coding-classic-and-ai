
class ActivityType():
    RUNNING = "running"
    WALKING = "walking"
    CYCLING = "cycling"
    SWIMMING = "swimming"
    YOGA = "yoga"
    GYM = "gym"
    DANCE = "dance"
    HIIT = "hiit"
    PILATES = "pilates"
    OTHER = "other"

    @classmethod
    def choices(cls):
        return [cls.RUNNING, cls.WALKING, cls.CYCLING, cls.SWIMMING, cls.YOGA, cls.GYM, cls.DANCE, cls.HIIT, cls.PILATES, cls.OTHER]