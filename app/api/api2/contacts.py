from aiohttp import web
from app.api.api2.baseview import baseview
routes = web.RouteTableDef()

@routes.view('/api/api2/contacts')
class OperationView(BaseView):
    async def get(self):
        contacts = [dict(name=c.name, description=c.description) for c in self.contact_svc.contacts]
        return dict(contacts=contacts)

app.router.add_routes(routes)
