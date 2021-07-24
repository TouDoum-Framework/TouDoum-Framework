from django.core.cache import cache
from django.db import models

prefix = "token_"


class Token(models.Model):
    token = models.CharField(unique=True, max_length=254)

    def __str__(self):
        return str(self.token)

    def delete(self, *args, **kwargs):
        cache.delete(prefix + self.token)
        super(Token, self).delete(*args, **kwargs)


def check_token(token_str: str) -> bool:
    try:
        token_obj: Token = cache.get(prefix + token_str)
        if not token_obj:
            token_obj = Token.objects.get(token=token_str)
            cache.set(prefix + token_str, token_obj)
        return True
    except Token.DoesNotExist:
        return False
