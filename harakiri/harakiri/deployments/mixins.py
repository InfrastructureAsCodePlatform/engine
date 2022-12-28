from harakiri.core.mixins import BaseAdminMixin


class DeploymentAdminMixin(BaseAdminMixin):
    def histories_url(self, obj):
        from harakiri.deployments.models import History

        return self.get_url(History, singular="history", plural="histories", deployment=obj.id)
