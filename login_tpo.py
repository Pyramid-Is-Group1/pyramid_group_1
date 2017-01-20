def main():
    config = Configurator()
    config.add_route('user', '/users/{uid}')
    return config.make_wsgi_app()

@view_config(route_name='user', renderer='user_template.mako')
def user_view(request):
    uid = request.matchdict['uid']
    user = find_user(request, uid)
    if user is None:
        raise HTTPNotFound
    return {'user': user}

def find_user(request, uid):
    return request.db.query(User).filter_by(id=uid).first()

class Test_user_view(unittest.TestCase):
    def test_it(self):
        req = DummyRequest()
        req.db = DummyDB()
        req.matchdict = {'uid': '3'}
        result = user_view(req)
        self.assertEqual(result['user'].id, 3)
