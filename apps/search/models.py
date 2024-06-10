from django.db import models

from apps.user.models import BaseModel


class SearchLog(BaseModel):
    """
    Model to represent logs of user searches.

    This model is designed to capture details of a user's search activity,
    including the search query, the response from ChatGPT, and any additional
    API response. It helps in tracking user queries and understanding user
    behavior, which can be valuable for analytics and future enhancements.

    Attributes:
    - user (ForeignKey): The user who initiated the search.
    - query (TextField): The actual search query string provided by the user.
    - timestamp (DateTimeField): The date and time when the search was executed.
    - chat_gpt_response (JSONField): The response obtained from ChatGPT for the given query.
    - api_response (JSONField): The response from any additional API or service called during the search.

    The `__str__` method provides a readable representation of an instance, which
    includes the user's email, a shortened version of the query, and the timestamp.
    """

    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, related_name='search_logs', verbose_name='User')
    query = models.TextField(verbose_name='Search Query', db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')
    chat_gpt_response = models.JSONField(default=dict, verbose_name='ChatGPT Response')
    api_response = models.JSONField(default=dict, verbose_name='API Response')

    class Meta:
        verbose_name = 'Search Log'
        verbose_name_plural = 'Search Logs'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.email} - {self.query[:50]}... - {self.timestamp}"
