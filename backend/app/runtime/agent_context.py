class AgentContext:

    state = {}

    @classmethod
    def set_state(
        cls,
        state
    ):
        cls.state = state

    @classmethod
    def get_state(
        cls
    ):
        return cls.state