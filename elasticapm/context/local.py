from elasticapm.context.base import BaseContext


class LocalContext(BaseContext):
    transaction = None
    span = None

    def get_transaction(self, clear=False):
        transaction = self.transaction
        if clear:
            self.transaction = None
        return transaction

    def set_transaction(self, transaction):
        self.transaction = transaction

    def get_span(self):
        return self.span

    def set_span(self, span):
        self.span = span
