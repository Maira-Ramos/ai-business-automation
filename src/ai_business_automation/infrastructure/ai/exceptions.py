class AIException(Exception):
    """Erro base relacionado à inteligência artificial."""


class AIProviderError(AIException):
    """Erro durante comunicação com um provedor de IA."""


class AIResponseParseException(AIException):
    """Erro ao interpretar resposta da IA."""