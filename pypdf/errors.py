"""
All errors/exceptions pypdf raises and all of the warnings it uses.

Please note that broken PDF files might cause other Exceptions.
"""


class DeprecationError(Exception):
    """Raised when a deprecated feature is used."""


class DependencyError(Exception):
    """
    Raised when a required dependency (a library or module that pypdf depends on)
    is not available or cannot be imported.
    """


class PyPdfError(Exception):
    """Base class for all exceptions raised by pypdf."""


class PdfReadError(PyPdfError):
    """Raised when there is an issue reading a PDF file."""


class PageSizeNotDefinedError(PyPdfError):
    """Raised when the page size of a PDF document is not defined."""


class PdfReadWarning(UserWarning):
    """Issued when there is a potential issue reading a PDF file, but it can still be read."""


class PdfStreamError(PdfReadError):
    """Raised when there is an issue reading the stream of data in a PDF file."""


class ParseError(PyPdfError):
    """
    Raised when there is an issue parsing (analyzing and understanding the
    structure and meaning of) a PDF file.
    """


class FileNotDecryptedError(PdfReadError):
    """
    Raised when a PDF file that has been encrypted
    (meaning it requires a password to be accessed) has not been successfully
    decrypted.
    """


class WrongPasswordError(FileNotDecryptedError):
    """Raised when the wrong password is used to try to decrypt an encrypted PDF file."""


class EmptyFileError(PdfReadError):
    """Raised when a PDF file is empty or has no content."""


class EmptyImageDataError(PyPdfError):
    """Raised when trying to process an image that has no data."""


STREAM_TRUNCATED_PREMATURELY = "Stream has ended unexpectedly"


class LimitReachedError(PyPdfError):
    """
    Raised when a limit is reached.

    Args:
      message: What was reached.
      setting: The configuration value that sets the limit, if there is one. It is
        appended to the message and kept as the ``setting`` attribute.
      limit: The value of ``setting`` when the error was raised, if known. It is
        appended to the message and kept as the ``limit`` attribute.
    """

    def __init__(self, message: str, *, setting: str | None = None, limit: int | None = None) -> None:
        if setting is not None:
            named = setting if limit is None else f"{setting}={limit}"
            message = f"{message.rstrip('.')} ({named})."
        super().__init__(message)
        self.setting = setting
        self.limit = limit


class XmpDocumentError(PyPdfError, RuntimeError):
    """Raised when the XMP XML document context is invalid or missing."""
