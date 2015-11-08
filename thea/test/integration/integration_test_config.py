from thea.lib.config.application_config import ApplicationConfig
from thea.test.integration.mock_renderer import MockRenderer


class IntegrationTestConfig(ApplicationConfig):
    """
    Overwrites some methods from the main application config so that integration tests can be run.
    """

    def get_renderer(self):
        if self._renderer is None:
            self._renderer = MockRenderer()

        return MockRenderer()
