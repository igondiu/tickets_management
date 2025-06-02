from unittest.mock import MagicMock

from app.main import configure_logging, setup_app


def test_configure_logging(mocker):
    # Arrange
    mock_TimedRotatingFileHandler = mocker.patch("app.main.TimedRotatingFileHandler")
    mock_basicConfig = mocker.patch("app.main.logging.basicConfig")
    mock_debug = mocker.patch("app.main.logging.debug")

    mock_handler = MagicMock()
    mock_TimedRotatingFileHandler.return_value = mock_handler

    # Act
    configure_logging(console_handler=True)

    # Assert
    mock_TimedRotatingFileHandler.assert_called_once()
    mock_basicConfig.assert_called_once()
    mock_debug.assert_called_once_with("Logger successfully configured")


def test_setup_app(mocker):
    # Arrange
    mock_configure_logging = mocker.patch("app.main.configure_logging")
    mock_create_db_and_tables = mocker.patch("app.main.create_db_and_tables")

    # Act
    setup_app()

    # Assert
    mock_configure_logging.assert_called_once_with(True)
    mock_create_db_and_tables.assert_called_once()
