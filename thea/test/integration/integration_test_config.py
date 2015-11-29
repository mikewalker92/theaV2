from mockito import mock
from thea.lib.config.application_config import ApplicationConfig
from thea.lib.helpers.quickplot_wrapper import QuickplotWrapper
from thea.test.integration.mock_renderer import MockRenderer


class IntegrationTestConfig(ApplicationConfig):
    """
    Overwrites some methods from the main application config so that integration tests can be run.
    """

    # We use a stubbed renderer so that we do not need to draw any windows for the integration tests.
    def get_renderer(self):
        if self._renderer is None:
            self._renderer = MockRenderer()

        return MockRenderer()

    # Mock the quickplot wrapper to speed up the tests and allow better checks.
    def get_quickplot_wrapper(self):
        if self._quickplot_wrapper is None:
            self._quickplot_wrapper = mock(QuickplotWrapper)
